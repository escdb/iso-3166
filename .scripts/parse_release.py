# This scripts combines the contents of the /data/ directory and the /amendments/ directory,
# such that there is one output `.json` that can be used by applications.
# ---

# Standard library.
import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Literal


# Types.
STANDARD = Literal["3166-1", "3166-2", "3166-3"]
AMEND_TYPE = Literal["add", "edit", "reserve"]


class IsoParser:
    """Parser for the iso-3166_data.json file (release)"""

    def __init__(self, repo_root: str | None = None):

        self.repo_root: Path = self.set_repo_root(repo_root)
        # Only used in __init__.
        _data_dir =  self.repo_root / "regions" / "iso"
        _amendment_dir = self.repo_root / "regions" / "extra"
        # Set class constants.
        self.OFFICIAL_DATA_PATHS: dict[STANDARD, Path] = {
            "3166-1": _data_dir / "iso_3166-1.json",
            "3166-2": _data_dir / "iso_3166-2.json",
            "3166-3": _data_dir / "iso_3166-3.json",
        }
        # Amendment files.
        self.AMENDMENT_FILES: dict[STANDARD, dict[AMEND_TYPE, Path]] = {
            "3166-1": {
                "add": _amendment_dir / "iso_3166-1-additions.json",
                "edit": _amendment_dir / "iso_3166-1-edits.json",
            },
            "3166-2": {
                "add": _amendment_dir / "iso_3166-2-additions.json",
                "edit": _amendment_dir / "iso_3166-2-edits.json",
            },
            "3166-3": {
                "add": _amendment_dir / "iso_3166-3-additions.json",
                "edit": _amendment_dir / "iso_3166-3-edits.json",
            },
        }

    @staticmethod
    def set_repo_root(custom: str | None = None) -> Path:
        """Return the root directory of the git repository"""
        if custom:
            return Path(custom)
        else:
            try:
                root = subprocess.check_output(
                    ['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.STDOUT
                )
                # Decode and strip any extra whitespace.
                return Path(root.decode('utf-8').strip())
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
        if append_amendments:  # May thus also override stuff from the "main" ISO file.
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

    OUTPUT_PATH = Path(__file__).resolve().parents[1] / "iso_3166_data.json"

    print("Create IsoParser...")
    parser = IsoParser()
    print("Parse files into ISO dict...")
    parsed_dict = parser.create_iso_dict(APPEND_AMENDMENTS)
    print("Write ISO dict to file...")
    with open(OUTPUT_PATH, "w") as json_f:
        # There are emoji in the .json file, so ensure_ascii should be False.
        json.dump(parsed_dict, json_f, indent=2, sort_keys=True, ensure_ascii=False)
    print(f"OK: Output file '{OUTPUT_PATH}' created.")
