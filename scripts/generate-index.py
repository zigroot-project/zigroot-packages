#!/usr/bin/env python3
"""Generate index.json from packages/*/metadata.toml and versions/*.toml"""

import json
import tomllib
from datetime import datetime, timezone
from pathlib import Path

def main():
    packages_dir = Path("packages")
    packages = []

    for meta_path in sorted(packages_dir.glob("*/metadata.toml")):
        pkg_dir = meta_path.parent
        with open(meta_path, "rb") as f:
            meta = tomllib.load(f)

        pkg = meta.get("package", {})
        versions = sorted(
            [v.stem for v in (pkg_dir / "versions").glob("*.toml")],
            reverse=True
        )

        packages.append({
            "name": pkg.get("name", pkg_dir.name),
            "description": pkg.get("description", ""),
            "license": pkg.get("license", ""),
            "versions": versions,
            "latest": versions[0] if versions else ""
        })

    index = {
        "version": 1,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "packages": packages
    }

    with open("index.json", "w") as f:
        json.dump(index, f, indent=2)

    print(f"Generated index.json with {len(packages)} packages")

if __name__ == "__main__":
    main()
