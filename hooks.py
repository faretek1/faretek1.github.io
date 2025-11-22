# These are run when the docs are built and after building. See plugins/mkdocs-simple-hooks in mkdocs.yml

import shutil
from pathlib import Path


def on_pre_build(*args, **kwargs):
    print("RUNNING ON_PRE_BUILD")
    # shutil.copy("README.md", "docs/gh-readme.md")


def on_post_build(config: dict, *args, **kwargs):
    print("RUNNING ON_POST_BUILD")

    site_dir = Path(config['site_dir'])

    def cpy(origin: Path, dest: Path):
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(origin, dest)

    cpy(
        Path(".well-known", "atproto-did"),
        site_dir / ".well-known" / "atproto-did"
    )
    cpy(
        Path(".well-known", "discord"),
        site_dir / ".well-known" / "discord"
    )
