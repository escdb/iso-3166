# Amendments
Any amendments to the data in the `../data/` directory are to be put in this directory.


## General file format

```json
{
  "3166-x": {
    "xxxx": {
        "_comment": "edits here."
    }
  }
}
```

Where `3166-x` is any of (`3166-1`, `3166-2`, or `3166-3`, i.e. the standard being amended to), and `xxxx` is the shortest unambiguous code to either make edits on or additions to. This is:
- `3166-1`: The alpha-2 code.
- `3166-2`: The "code".
- `3166-3`: The alpha-4 code.



## Additional defined rows
### ISO 3166-1
- `aliases`: An array of strings defining the previous names under which a country participated at Eurovision, if and only if these names are not already used as a `common_name`, `name`, or `official_name` in the official ISO files. In the future, aliases may get a more general purpose.
- `alt_alpha_2`: An alternative alpha-2 code to refer to the country/region/territory. This is a "soft reservation"; the code shall not be used for anything but an alias for the respective territory.
- `alt_alpha_3`: An alternative alpha-3 code to refer to the country/region/territory. This is a "soft reservation"; the code shall not be used for anything but an alias for the respective territory.
- `esc_name`: The name under which the country took part in Eurovision. In case there are several names, the name of the most recent participation is used, if and only if this name not already the next precedence name (i.e. `common_name` if defined, else `name`).
- `_comment`: A repository-specific remark on any amendments made to the official ISO list. This is purely meant as documentation and should not be used for any end applications.
- `in_esc`: A boolean indicating if the country has ever participated in Eurovision.
- `in_jesc`: A boolean indicating if country has ever participated in Junior Eurovision.

### ISO 3166-2
- `_comment`: A repository-specific remark on any amendments made to the official ISO list. This is purely meant as documentation and should not be used for any end applications.

### ISO 3166-3
- `esc_name`: The name under which the country took part in Eurovision. In case there are several names, the name of the most recent participation is used, if and only if this name not already the next precedence name (i.e. `common_name` if defined, else `name`).
- `in_esc`: A boolean indicating if the country has ever participated in Eurovision.
- `in_jesc`: A boolean indicating if country has ever participated in Junior Eurovision.

## Resources
- [Unicode CLDR: Country/Region (Territory) Names](https://cldr.unicode.org/translation/displaynames/countryregion-territory-names): Contains a few examples of "sensitive" names, or territories that may have an alternative name.
- [Wikipedia page on Regional indicator symbols](https://en.wikipedia.org/wiki/Regional_indicator_symbol): Used to ensure that all Unicode flag emoji have their alpha_2 code reserved.
- [Unicode emoji sequences](https://unicode.org/Public/emoji/latest/emoji-sequences.txt): A more official reference for Unicode emoji.
