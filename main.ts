// news-image-20261124 entry runner.
// Reads entry.png from this repo, validates it, and writes it to the
// output directory required by make.fun. Node 22, standard library only.
import { readFileSync, writeFileSync, mkdirSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1024 * 1024;
const MAX_SIDE = 1024;

function fail(message) {
  console.error("entry error: " + message);
  process.exit(1);
}

const here = dirname(fileURLToPath(import.meta.url));
const sourcePath = join(here, "entry.png");
let png;
try {
  png = readFileSync(sourcePath);
} catch {
  fail("cannot read entry.png next to main.ts");
}

if (png.length < 33 || !png.subarray(0, 8).equals(PNG_MAGIC)) {
  fail("entry.png is not a PNG file");
}
if (png.length > MAX_BYTES) {
  fail("entry.png is " + png.length + " bytes, over the 1 MiB limit");
}
const width = png.readUInt32BE(16);
const height = png.readUInt32BE(20);
if (png.readUInt32BE(8) !== 13 || png.toString("ascii", 12, 16) !== "IHDR") {
  fail("entry.png has no IHDR chunk where expected");
}
if (width > MAX_SIDE || height > MAX_SIDE) {
  fail("entry.png is " + width + "x" + height + ", over the 1024x1024 limit");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "entry.png");
writeFileSync(outPath, png);
const written = statSync(outPath).size;
console.log(
  "wrote " + outPath + " (" + width + "x" + height + ", " + written + " bytes)"
);
