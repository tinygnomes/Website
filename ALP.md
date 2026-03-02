- [Table of Contents](README.md)
- [Previous Chapter](Overview.md)

# Introduction to AI-assisted Literate Programming

> I will not repeat a general introduction to ALP here. You can find it [here](https://github.com/tinygnomes/TGDocumentExtractor/blob/master/ALP.md)

My ALP experiment has been a great success for backend programming. Admittedly, it is not clear how it would work for a static website (or even just UI / frontend programming). Clearly, describing something almost purely visual with words is a terrible idea. (There's still much that can be described of course, from the JS code to the design decisions to many aspects of the HTML and CSS coding.) Therefore the goal is to start from a *visual* source of truth; we are doing this by having a reference Figma design. Initially, we attempted to use Locofy to generate HTML/CSS, but the code produced was of low quality (non-semantic `div` bloat) and required significant manual cleanup, conflicting with our goal of maintaining a clean, hand-crafted static site.

Instead, we are pivoting to a direct **Figma API Integration** workflow. The AI agent will directly interrogate the Figma file via a customized locally-run MCP Server to intelligently extract Design Tokens (colors, fonts), exact layout coordinates, and SVG image assets. The AI will then generate or edit the final semantic HTML, CSS, and JS starting from the MarkDown specifications and the precise measurements fetched directly from Figma.

I'm not as confident about this approach as much as I was about using ALP for backend programming, but I am cautiously optimistic.

- [Next Chapter](GEMINI.md)