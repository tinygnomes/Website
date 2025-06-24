# How-To: Deploy the Project

This guide provides instructions on how to deploy the TinyGnomes project. We use two distinct processes: one for continuous deployment during development and another for final production deployment.

## Development Deployment to GitHub Pages

For development and review purposes, the project is automatically deployed to GitHub Pages. This allows team members and stakeholders to track progress and provide feedback on the live site.

### Process

-   **Trigger**: A push to the `main` branch automatically triggers the deployment process.
-   **Mechanism**: The deployment is handled by a GitHub Actions workflow defined in the [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) file.
-   **Environment**: This is considered a staging or development environment. The content reflects the latest changes merged into the `main` branch.

No manual steps are required for this deployment.

## Production Deployment

The final, official version of the website is deployed manually to our production web server.

### Process

This process will be performed by an authorized team member when the website is ready for a public release.

1.  **Build the Site**: Generate the static site files using the required build commands (e.g., `npm run build`).
2.  **Transfer Files**: Copy the generated static files to the web server using a secure method (e.g., SCP, SFTP, or rsync).
3.  **Verify**: Check the live site to ensure the deployment was successful.

This document will be updated with more specific server details and commands once the project is closer to its first production release.