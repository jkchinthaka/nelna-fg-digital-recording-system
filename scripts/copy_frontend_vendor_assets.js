#!/usr/bin/env node
/**
 * Copy vendored frontend assets from node_modules into static/dist.
 * Do not use public CDNs.
 */
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const htmxSrc = path.join(root, "node_modules", "htmx.org", "dist", "htmx.min.js");
const htmxDest = path.join(root, "static", "dist", "js", "htmx.min.js");
const appJsSrc = path.join(root, "static", "src", "js", "app.js");
const appJsDest = path.join(root, "static", "dist", "js", "app.js");

function mustCopy(src, dest) {
  if (!fs.existsSync(src)) {
    console.error(`Missing vendor asset: ${src}`);
    process.exit(1);
  }
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  fs.copyFileSync(src, dest);
  console.log(`Copied ${path.relative(root, src)} -> ${path.relative(root, dest)}`);
}

mustCopy(htmxSrc, htmxDest);
mustCopy(appJsSrc, appJsDest);
