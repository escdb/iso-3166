# Custom flag emoji

## About this directory
Each subdirectory contains flag emoji of the given category.

Besides the file you are currently reading, this directory also contains a `png_emoji.json` and `svg_emoji.json` file that should make it convenient to import the custom emoji images into your application. The files have the following structure:

```json
{
  "3166-1": {
    "XA": "./path/to/filename_a.png"
  },
  "3166-2": {
    "XX-XB": "./path/to/filename_b.png",
    "XX-XC": "./path/to/filename_c.png"
  },
  "3166-3": {
    "XXXD" : "./path/to/filename_d.png"
  }
}
```
*The `.svg` file is identically structured, but obviously with `.svg` as file extension :)*

This means that the file is first grouped by the ISO standard, and then each code is mapped to the path its image can be found.

## Licensing
All graphics (PNG/SVG) in the subdirectories of this directory fall under the CC-BY-4.0 license (as found in `LICENSE-EMOJI`).
The `twemoji` directories fall under the CC-BY-4.0 license of [`@jdecked`'s Twemoji repository](https://github.com/jdecked/twemoji).
