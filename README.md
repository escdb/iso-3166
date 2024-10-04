# iso-3166
Codes and other data of the ISO 3166 standard, adapted for ESCDB usage.

This repository has several purposes:
- To provide the other data repositories an overview with the correct country/region codes to use.
- To provide any source using the other data repositories with a "ground truth" of codes that can be expected to potentially be used in any consumed data.
- To make validation of user input concerning any of the respective countries/regions/territories convenient.


## About the data
The data is derived from [the Debian repository for ISO codes](https://salsa.debian.org/iso-codes-team/iso-codes), which in turn is based on several ISO standards including ISO 3166.

To make it easy to udpate the repository with the "upstream" data (i.e. the Debian repository), any files in the `/data/` repository should not be modified by any user. For consistency **only** updates allowed to those files are when the Debian repository updates those files.

Instead, any necessary changes to the ISO 3166 standard in the scope of this project should be made in a separate `amendments` directory.
This repository nevertheless strives to be as consistent with international standards as possible, and only deviates when this is necessary for any features (such as support for specific contests which can otherwise not be supported).


## Contributions
Since the accuracy and consistency of the data in this repository is of utmost importance for the proper functioning of other aspects of the project, any Pull Requests will be thoroughly reviewed. It is recommended to textually discuss any proposed changes to the admendments (or new amendments) with the project owners before creating pull requests, as the chance of them being accepted otherwise is relatively low.\


## Licensing
To stay consistent with the Debian repository, this repository shares the same license (GNU LGPLv2.1).
