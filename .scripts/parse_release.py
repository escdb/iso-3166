# This scripts combines the contents of the /data/ directory and the /amendments/ directory,
# such that there is one output `.json` that can be used by applications.
# ---

# Standard library.
import json
import os
import subprocess
from collections import defaultdict
from typing import Literal


# Types.
STANDARD = Literal["3166-1", "3166-2", "3166-3"]
AMEND_TYPE = Literal["add", "edit", "reserve"]


class IsoParser:
    """Very descriptive description"""

    def __init__(self, repo_root: str | None = None):
        self.repo_root = self.set_repo_root(repo_root)
        # Only used in __init__.
        _data_dir = os.path.join(self.repo_root, "data")
        _amendment_dir = os.path.join(self.repo_root, "amendments")
        # Set class constants.
        self.OFFICIAL_DATA_PATHS: dict[STANDARD, str] = {
            "3166-1": os.path.join(_data_dir, "iso_3166-1.json"),
            "3166-2": os.path.join(_data_dir, "iso_3166-2.json"),
            "3166-3": os.path.join(_data_dir, "iso_3166-3.json"),
        }
        # Amendment files.
        self.AMENDMENT_FILES: dict[STANDARD, dict[AMEND_TYPE, str]] = {
            "3166-1": {
                "add": os.path.join(_amendment_dir, "iso_3166-1-additions.json"),
                "edit": os.path.join(_amendment_dir, "iso_3166-1-edits.json"),
            },
            "3166-2": {
                "add": os.path.join(_amendment_dir, "iso_3166-2-additions.json"),
                "edit": os.path.join(_amendment_dir, "iso_3166-2-edits.json"),
            },
            "3166-3": {
                "add": os.path.join(_amendment_dir, "iso_3166-3-additions.json"),
                "edit": os.path.join(_amendment_dir, "iso_3166-3-edits.json"),
            },
        }

    @staticmethod
    def set_repo_root(custom: str | None = None) -> str:
        """Return the root directory of the git repository"""
        if custom:
            return custom
        else:
            try:
                root = subprocess.check_output(
                    ['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.STDOUT
                )
                return root.decode('utf-8').strip()  # Decode and strip any extra whitespace.
            except subprocess.CalledProcessError as e:
                print(f"Error getting repo root: {e.output.decode('utf-8')}")
                raise

    # Start of data loading!
    # Create ISO dict.
    def create_iso_dict(self, append_amendments: bool = True) -> dict:
        iso_dict = {}
        for standard, fp in self.OFFICIAL_DATA_PATHS.items():
            with open(fp, "r") as file:
                """
                Example format after unpacking:
                "AW": {
                  "alpha_2": "AW",
                  "alpha_3": "ABW",
                  "flag": "🇦🇼",
                  "name": "Aruba",
                  "numeric": "533"
                }, ...
                """
                match standard:
                    case "3166-1":
                        iso_dict[standard] = {i["alpha_2"]: i for i in json.load(file)[standard]}
                    case "3166-2":
                        # Dict comprehension not possible because of default dict.
                        temp_iso = json.load(file)
                        temp_dict = defaultdict(dict)
                        for i in temp_iso[standard]:
                            code = i["code"]
                            temp_dict[code[:2]][code] = i
                        iso_dict[standard] = temp_dict
                    case "3166-3":
                        iso_dict[standard] = {i["alpha_4"]: i for i in json.load(file)[standard]}
        if append_amendments:
            for standard, amend_dict in self.AMENDMENT_FILES.items():
                for amend_type, fp in amend_dict.items():
                    with open(fp, "r") as file:
                        i_dict = json.load(file)
                        match amend_type:
                            case "add":
                                for k, v in i_dict[standard].items():
                                    iso_dict[standard][k] = v
                            case "edit":
                                # e.g. "GB": {"alt_alpha_2": "UK"}
                                for outer_k, _outer_v in i_dict[standard].items():
                                    # e.g. "alt_alpha_2", "UK".
                                    for k, v in _outer_v.items():
                                        iso_dict[standard][outer_k][k] = v
                            case "reserve":
                                pass
        return iso_dict


if __name__ == "__main__":
    APPEND_AMENDMENTS = True  # Whether to append the amendments.
    OUTPUT_PATH = "iso_3166_data.json"
    # CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    # REPO_ROOT = os.path.join(CURRENT_DIR, "..")

    print("Create IsoParser...")
    parser = IsoParser()
    print("Parse files into ISO dict...")
    parsed_dict = parser.create_iso_dict(APPEND_AMENDMENTS)
    print("Write ISO dict to file...")
    with open(OUTPUT_PATH, "w") as json_f:
        json.dump(parsed_dict, json_f, indent=2, sort_keys=True)
    print(f"OK: Output file '{OUTPUT_PATH}' created.")
