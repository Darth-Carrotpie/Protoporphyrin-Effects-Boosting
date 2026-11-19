"""Check the wiki's source integrity and local navigation using only Python."""

import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def check(root):
    errors = []
    manifest = json.loads((root / "raw/manifest.json").read_text(encoding="utf-8"))
    for name, digest in manifest.items():
        path = (root / name).resolve()
        if not path.is_relative_to((root / "raw").resolve()):
            errors.append(f"Source escapes raw/: {name}")
        elif not path.is_file():
            errors.append(f"Missing source: {name}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            errors.append(f"Source changed: {name}")
    actual = {p.relative_to(root).as_posix() for p in (root / "raw").rglob("*")
              if p.is_file() and p.name not in {"manifest.json", ".gitkeep"}}
    errors.extend(f"Unpinned source: {name}" for name in sorted(actual - manifest.keys()))

    articles = [p for p in (root / "wiki").glob("*/*.md")
                if p.name not in {"index.md", "log.md"}]
    index = (root / "wiki/index.md").read_text(encoding="utf-8")
    for path in [root / "README.md", *(root / "wiki").rglob("*.md")]:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.strip("<>")
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            local = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            if not local.is_relative_to(root.resolve()) or not local.exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
        if path in articles:
            for field in ["Sources", "Raw", "Updated"]:
                if not re.search(rf"^> {field}: .+", text, re.M):
                    errors.append(f"Missing {field}: {path.relative_to(root)}")
            raw_line = re.search(r"^> Raw: (.+)", text, re.M)
            raw_links = re.findall(r"\]\(([^)]+)\)", raw_line[1]) if raw_line else []
            if not raw_links or any(not (path.parent / unquote(link)).resolve().is_relative_to(
                    (root / "raw").resolve()) for link in raw_links):
                errors.append(f"Invalid raw references: {path.relative_to(root)}")
            if f"]({path.relative_to(root / 'wiki').as_posix()})" not in index:
                errors.append(f"Article missing from index: {path.relative_to(root)}")
    return errors, len(manifest), len(articles)


if __name__ == "__main__":
    errors, sources, articles = check(ROOT)
    for error in errors:
        print(error)
    if errors:
        raise SystemExit(1)
    print(f"PASS: {sources} source hashes; local links; {articles} indexed articles and metadata")
