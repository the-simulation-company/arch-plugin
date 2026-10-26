"""Check provider versions against the previous main commit; print the release tag."""

import json
from pathlib import Path
import re
import subprocess
import sys


def version(text: str) -> tuple[int, ...]:
    value = json.loads(text)["version"]
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", value):
        raise ValueError(f"Expected a stable major.minor.patch version, got {value!r}")
    return tuple(map(int, value.split(".")))


base = sys.argv[1]
versions = set()
for provider in ("claude", "codex", "cursor", "devin"):
    path = f".{provider}-plugin/plugin.json"
    current = version(Path(path).read_text())
    previous = version(subprocess.check_output(["git", "show", f"{base}:{path}"], text=True))
    if current <= previous:
        raise ValueError(f"{path}: bump the version above {'.'.join(map(str, previous))}")
    versions.add(current)

if len(versions) != 1:
    raise ValueError("All four provider manifests must have the same version")
print("v" + ".".join(map(str, versions.pop())))
