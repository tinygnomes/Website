const liveServer = require("live-server");
const path = require("path");
const fs = require("fs");

const params = {
    port: 8080,
    root: path.join(__dirname, "website"),
    open: false,
    // Middleware function to handle clean URLs
    middleware: [function(req, res, next) {
        const filePath = path.join(params.root, req.url);
        // If it's not a file and has no extension, try adding .html
        if (!path.extname(req.url) && req.url.slice(-1) !== '/') {
            const htmlFilePath = `${filePath}.html`;
            if (fs.existsSync(htmlFilePath)) {
                req.url += ".html";
            }
        }
        next();
    }]
};

liveServer.start(params);
