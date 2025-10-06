import shutil
from pathlib import Path


def on_pre_build(*args, **kwargs):
    print("RUNNING ON_PRE_BUILD")
    shutil.copy("README.md", "docs/gh-readme.md")


def on_post_build(config: dict, *args, **kwargs):
    print("RUNNING ON_POST_BUILD")

    site_dir = Path(config['site_dir'])

    origin = Path(".well-known", "atproto-did")
    dest = site_dir / ".well-known" / "atproto-did"
    dest.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy(origin, dest)
