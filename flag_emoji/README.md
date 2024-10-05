# Custom flag emoji

## About this direcctory
Each subdirectory contains flag emoji of the given category.

Besides the file you are currently reading, this directory also contains a `.json` file that should make it convenient to import the custom emoji images into your application. The file has the following structure:

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

This means that the file is first grouped by the ISO standard, and then each code is mapped to the path its image can be found.
