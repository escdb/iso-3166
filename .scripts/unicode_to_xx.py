# Simple script to get a mapping of all Twemoji image files to ISO 3166-1 codes.
import os

# EMOJI_A = 0X1F1E6
# EMOJI_Z = 0X1F1FF
EMOJI_OFFSET = 0x1F1A5

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_ROOT = os.path.join(CURRENT_DIR, "..")

TWEMOJI_DIR = os.path.join(REPO_ROOT, "emoji", "svg", "twemoji")
# Used for the path string in the "{svg, png}_emoji.json" file.
OUTPUT_DIR_PREFIX = os.path.join(".", "svg", "twemoji")


def indicator_to_chr(indicator_string: str) -> str:
    """Convert an indicator Unicode endpoint to a letter"""
    unicode_ord = int(indicator_string, 16)
    letter_ord = unicode_ord - EMOJI_OFFSET
    return chr(letter_ord)


def filename_to_code(filename_in: str) -> str:
    """Convert a filename to an ISO code"""
    # e.g. 1f1ec-1f1fc.svg to "1f1ec-1f1fc" and ".svg"
    name, ext = os.path.splitext(filename_in)
    # "1f1ec-1f1fc" to "1f1ec" and "1f1fc".
    a, b = name.split("-")
    return indicator_to_chr(a) + indicator_to_chr(b)


def get_filename_mapping():
    assert os.path.exists(TWEMOJI_DIR), "Twemoji directory does not exist!"
    result_dict = {}
    with os.scandir(TWEMOJI_DIR) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith(".svg"):
                f_name = entry.name
                xx = filename_to_code(entry.name)
                result_dict[xx] = str(os.path.join(OUTPUT_DIR_PREFIX, f_name))
    return result_dict

if __name__ == "__main__":
    import json
    res_dict = get_filename_mapping()
    print("Ok")
    # There are emoji in the .json file, so ensure_ascii should be False.
    print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False))
