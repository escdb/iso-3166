# iso-3166
Codes and other data of the ISO 3166 standard, adapted for ESCDB usage.

This repository has several purposes:
- To provide the other data repositories an overview with the correct country/region codes to use.
- To provide any source using the other data repositories with a "ground truth" of codes that can be expected to potentially be used in any consumed data.
- To make validation of user input concerning any of the respective countries/regions/territories convenient.
- To enrich the data by ISO and Unicode with custom emoji for specific territories and subdivisions.


## About the data
### ISO data
The data is derived from [the Debian repository for ISO codes](https://salsa.debian.org/iso-codes-team/iso-codes), which in turn is based on several ISO standards including ISO 3166.

To make it easy to update the repository with the "upstream" data (i.e. the Debian repository), any files in the `/regions/iso/` repository should not be modified by any user. For consistency, updates to those files are allowed **only** when the Debian repository updates those files.

Instead, any necessary changes to the ISO 3166 standard in the scope of this project should be made in a separate `/regions/extra/` directory.
This repository nevertheless strives to be as consistent with international standards as possible, and only deviates when this is necessary for any features (such as support for specific contests which can otherwise not be supported).

### Flag emoji
The `/emoji/` directory contains all emoji for ISO-3166 territories inside the CLDR, as well as some custom emoji representing other ISO-3166 codes specifically made for this repository. All emoji are stored in both the `.png` and `.svg` file formats, each with their dedicated directory (`/emoji/png/` and `/emoji/svg/`).

Each filetype has the following subdirectories:
- `extra` -> Extends the set of flag emoji that is already assigned to territories in CLDR with custom-made, emoji-like images. 
- `twemoji` -> For convenience, the Twemoji for all CLDR flags. These are taken from [`@jdecked`'s Twemoji repository](https://github.com/jdecked/twemoji) (under CC-BY-4.0). 

To use the files in code, the files are accompanied by a `.json` file that link the ISO 3166 codes of the respective territories/subdivisions to the image. This can be useful when wanting to render a flag alongside content concerning regions without Unicode supporting them.

The `.png` version of the provided Twemoji are 72×72 px, and for all other emoji 300×300 px.




### Other
Finally, the `misc` file contains some helper files that do not necessarily contribute to the data set itself.


## Contributions
Since the accuracy and consistency of the data in this repository is of utmost importance for the proper functioning of other aspects of the project, any Pull Requests will be thoroughly reviewed. It is recommended to textually discuss any proposed changes to the admendments (or new amendments) with the project owners before creating pull requests, as the chance of them being accepted otherwise is relatively low.


## Licensing
To stay consistent with the Debian repository, this repository shares the same license (GNU LGPLv2.1). 
Some specific files, notably emoji graphics, may use additional or different licenses (such as CC-BY-4.0).

If different licenses apply, these will be mentioned in the specific directory.