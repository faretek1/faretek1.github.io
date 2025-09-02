import argparse
from datetime import datetime
import os
import json
import sys
from pathlib import Path
from typing import Final


def _gen_appdata_folder() -> Path:
    un = "faretek"
    match sys.platform:
        case "win32":
            return Path(os.getenv('APPDATA')) / un
        case "linux":
            return Path.home() / f".{un}"
        case plat:
            raise NotImplementedError(f"No 'appdata' folder implemented for {plat}")

APPDATA_FARETEK: Final[Path] = _gen_appdata_folder()
APPDATA_FARETEK_MKBLOG: Final[Path] = APPDATA_FARETEK / "mkblog"

class DataBase:
    def __init__(self):
        self.location = APPDATA_FARETEK_MKBLOG / "data.json"

    @property
    def data(self) -> dict:
        if not self.location.exists():
            return {}

        return json.load(self.location.open())

    @data.setter
    def data(self, data: dict):
        APPDATA_FARETEK_MKBLOG.mkdir(parents=True, exist_ok=True)
        json.dump(data, self.location.open("w"))

    def get(self, __key, __default=None):
        return self.data.get(__key, __default)

    def __setitem__(self, key, value):
        _data = self.data
        _data[key] = value
        self.data = _data

    def __getitem__(self, item):
        return self.data[item]



DB: Final[DataBase] = DataBase()

class Args(argparse.Namespace):
    name: str
    authors: str
    is_draft: bool
    categories: str
    markdown: str

def main():
    parser = argparse.ArgumentParser(
        prog="mkblog",
        description="Make a blog entry and set default params",
        epilog="Docs are in retek's page",
    )

    parser.add_argument("-n", "--name", action="store", dest="name", default=None,
                        help="Name of the blog entry")
    parser.add_argument("-a", "--authors", action="store", dest="authors", default=None,
                        help="Space-delimited list of authors")
    parser.add_argument("-d", "--draft", action="store_true", dest="is_draft", default=False,
                        help="Whether the blog entry is draft")
    parser.add_argument("-c", "--categories", action="store", dest="categories", default="")
    parser.add_argument("-M", "--markdown", action="store", dest="markdown", default="")

    ### Parse args and set 'dynamic' defaults

    args = parser.parse_args(namespace=Args())
    dt_created = datetime.now()

    if args.authors is None:
        args.authors = DB.get("authors", "unknown-author")
    else:
        DB["authors"] = args.authors

    if args.name is None:
        args.name = "untitled"
        name = f"{args.authors}-{dt_created}"
    else:
        name = f"{args.authors}-{args.name}"

    authors = args.authors.split(" ")
    categories = args.categories.split(" ")  # explicit is better than implicit
    if categories == ['']:
        categories = []
    ### Actual action

    writepath = (Path.cwd() / f"{name}.md").resolve()
    print(f"Making a blog at {str(writepath)!r}")

    writepath.write_text("""\
---
date: {dt_created}
draft: {draft}
authors:
{authors_items}{cats_tag}{categories_items}---

# {name}

{markdown}

""".format(
        dt_created=dt_created.isoformat(),
        authors_items=''.join(
            f"- {author}\n" for author in authors
        ),
        categories_items=''.join(
            f"- {cat}\n" for cat in categories
        ),
        name=args.name,
        cats_tag="categories:\n" if categories else "",
        markdown=f"<!-- {', '.join(authors)}, write some stuff! -->" if not args.markdown else args.markdown,
        draft=json.dumps(args.is_draft)
    ))
