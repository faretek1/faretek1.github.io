import shutil
from pathlib import Path

def on_pre_build(*args, **kwargs):
    print("RUNNING ON_PRE_BUILD")
    shutil.copy("README.md", "docs/README.md")

def on_post_build(config: dict, *args, **kwargs):
    print("RUNNING ON_POST_BUILD")

    site_dir = config['site_dir']

    origin = Path(site_dir, ".well-known", "atproto-did")
    dest = Path(".well-known", "atproto-did")
    dest.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy(origin, dest)
