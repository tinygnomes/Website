import os
import re
import requests
from bs4 import BeautifulSoup

def main():
    """
    Main function to run the website migration script.
    """
    WEBSITE_DIR = "website.tinygnomes.com"
    ASSETS_DIR = os.path.join(WEBSITE_DIR, "local_assets")

    # Create assets directory in the root, not inside the website folder
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)
    
    print("Starting website migration...")

    # Fix file names before processing
    rename_security_file(WEBSITE_DIR)
    
    html_files = find_html_files(WEBSITE_DIR)
    
    for file_path in html_files:
        process_html_file(file_path, ASSETS_DIR)

    # Post-processing tasks
    list_placeholder_pages(html_files)

    print("\nMigration script finished.")
    print(f"Please review the '{ASSETS_DIR}' directory and the modified HTML files.")
    print("Manual tasks remaining:")
    print("- Review and implement placeholder pages.")
    print("- Review and rewrite CSS for maintainability.")
    print("- Review robots.txt.")
    print("- Perform general improvements (responsiveness, performance, accessibility, SEO).")

def find_html_files(directory):
    """
    Finds all HTML files in a given directory and its subdirectories.
    """
    html_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def process_html_file(file_path, assets_dir):
    """
    Processes a single HTML file to apply migration changes.
    """
    print(f"Processing {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # High Priority Tasks
        fix_cookie_dialog(soup)
        fix_login_button(soup)

        # Migration & Cleanup Tasks
        remove_framer_code(soup, assets_dir)
        remove_inline_font_faces(soup)
        add_google_fonts(soup)
        localize_resources(soup, assets_dir, file_path)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
            
        print(f"Finished processing {file_path}.")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def fix_cookie_dialog(soup):
    """
    Replaces the cookie dialog with a static notice.
    """
    policy_div = soup.find('div', attrs={'data-framer-name': 'Policy'})
    if policy_div:
        policy_div.clear()
        policy_div.string = "This website uses only technical cookies for logged-in users."
        # Remove unnecessary attributes
        for attr in list(policy_div.attrs.keys()):
            if attr != 'class': # Keep class for styling if needed
                del policy_div[attr]
        print("  - Cookie dialog replaced with a static notice.")

def fix_login_button(soup):
    """
    Updates the login button to link to the correct URL.
    """
    login_button = soup.find('a', attrs={'data-framer-name': 'Log in'})
    if login_button:
        login_button['href'] = 'https://www.tinygnomes.com/quilt.fcgi'
        print("  - Login button link updated.")

def remove_framer_code(soup, assets_dir):
    """
    Removes Framer-specific code from the HTML.
    """
    # Remove Framer comments
    framer_comment = soup.find(string=lambda text: "Built with Framer" in text)
    if framer_comment:
        framer_comment.extract()
        print("  - Removed Framer comment.")

    # Remove Framer meta tags and download og:image
    meta_tags_to_remove = soup.find_all('meta', attrs={'name': ['generator', 'framer-search-index']})
    og_image_meta = soup.find('meta', property='og:image')
    if og_image_meta and og_image_meta.get('content', '').startswith('https://framerusercontent.com'):
        img_url = og_image_meta['content']
        filename = os.path.basename(img_url.split('?')[0])
        local_img_path = os.path.join(assets_dir, filename)
        if download_file(img_url, local_img_path):
            print(f"  - Downloaded og:image to {local_img_path}")
        og_image_meta.decompose()
        print("  - Removed og:image meta tag.")

    for tag in meta_tags_to_remove:
        tag.decompose()
    if meta_tags_to_remove:
        print(f"  - Removed {len(meta_tags_to_remove)} Framer meta tags.")

    # Remove Framer scripts and module preloads
    framer_scripts = soup.find_all('script', src=re.compile(r'events\.framer\.com|framerusercontent\.com'))
    framer_bundle_script = soup.find('script', attrs={'data-framer-bundle': True})
    if framer_bundle_script:
        framer_scripts.append(framer_bundle_script)
    
    for script in framer_scripts:
        script.decompose()
    if framer_scripts:
        print(f"  - Removed {len(framer_scripts)} Framer scripts.")
        
    module_preloads = soup.find_all('link', rel='modulepreload', href=re.compile(r'framerusercontent\.com'))
    for link in module_preloads:
        link.decompose()
    if module_preloads:
        print(f"  - Removed {len(module_preloads)} Framer module preloads.")

    # Remove Framer-specific attributes
    attributes_to_remove = [
        'data-framer-hydrate-v2', 'data-framer-ssr-released-at',
        'data-framer-page-optimized-at', 'data-framer-component-type',
        'data-framer-name', 'data-framer-page-link-current',
        'data-framer-background-image-wrapper', 'data-framer-original-sizes',
        'data-styles-preset', 'data-highlight', 'data-border'
    ]
    count = 0
    for tag in soup.find_all(True):
        for attr in list(tag.attrs):
            if attr in attributes_to_remove or attr.startswith('data-framer-'):
                del tag[attr]
                count += 1
    if count > 0:
        print(f"  - Removed {count} Framer-specific attributes.")

def download_file(url, local_path):
    """
    Downloads a file from a URL to a local path.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except requests.exceptions.RequestException as e:
        print(f"    - Error downloading {url}: {e}")
        return False

def localize_resources(soup, assets_dir, html_file_path):
    """
    Downloads and localizes external resources.
    """
    html_dir = os.path.dirname(html_file_path)

    # Localize Favicon
    favicon_link = soup.find('link', rel='icon')
    if favicon_link and favicon_link['href'].startswith('https://framerusercontent.com'):
        favicon_url = favicon_link['href']
        filename = os.path.basename(favicon_url.split('?')[0])
        local_favicon_path = os.path.join(assets_dir, filename)
        if download_file(favicon_url, local_favicon_path):
            relative_path = os.path.relpath(local_favicon_path, html_dir)
            favicon_link['href'] = relative_path
            print(f"  - Localized favicon to {local_favicon_path}")

    # Localize Images
    images = soup.find_all('img')
    for img in images:
        if img.get('src', '').startswith('https://framerusercontent.com/images/'):
            img_url = img['src']
            filename = os.path.basename(img_url.split('?')[0])
            local_img_path = os.path.join(assets_dir, filename)
            if download_file(img_url, local_img_path):
                relative_path = os.path.relpath(local_img_path, html_dir)
                img['src'] = relative_path
                print(f"  - Localized image to {local_img_path}")
        if img.get('srcset'):
            # For simplicity, we'll just remove srcset and rely on src.
            # A more robust solution would parse and download all srcset images.
            del img['srcset']
            print("  - Removed srcset from an image. Please review manually.")

def remove_inline_font_faces(soup):
    """
    Removes @font-face declarations from inline <style> tags.
    """
    style_tags = soup.find_all('style')
    count = 0
    for style_tag in style_tags:
        if style_tag.string:
            original_css = style_tag.string
            # This regex is a simpler, Python-compatible version to remove @font-face rules.
            cleaned_css, num_subs = re.subn(r'@font-face\s*\{.*?\}', '', original_css, flags=re.IGNORECASE | re.DOTALL)
            if num_subs > 0:
                style_tag.string.replace_with(cleaned_css)
                count += num_subs
    if count > 0:
        print(f"  - Removed {count} @font-face declarations from inline styles.")

def add_google_fonts(soup):
    """
    Adds Google Fonts link to the HTML head.
    """
    head = soup.find('head')
    if head:
        # Remove any existing Google Fonts links to avoid duplicates
        for link in head.find_all('link', href=re.compile(r'fonts\.googleapis\.com')):
            link.decompose()
        
        font_links = [
            '<link rel="preconnect" href="https://fonts.googleapis.com">',
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Raleway:wght@400;700&family=Fragment+Mono:wght@400;700&display=swap" rel="stylesheet">'
        ]
        for link_str in font_links:
            head.append(BeautifulSoup(link_str, 'html.parser'))
        print("  - Added Google Fonts links to <head>.")

def rename_security_file(website_dir):
    """
    Renames security..html to security.html.
    """
    old_path = os.path.join(website_dir, 'security..html')
    new_path = os.path.join(website_dir, 'security.html')
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_path} to {new_path}")

def list_placeholder_pages(html_files):
    """
    Lists placeholder pages that need review.
    """
    placeholder_keywords = ['about', 'api', 'contact', 'faq', 'integration', 'pricing', 'security', 'terms', 'testimonials', 'white-label', 'features/', 'new-misc/']
    
    print("\n--- Placeholder Pages for Review ---")
    for file_path in html_files:
        for keyword in placeholder_keywords:
            if keyword in file_path:
                print(file_path)
                break

if __name__ == "__main__":
    main()