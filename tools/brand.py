#!/usr/bin/env python3
"""Brand visible Pterodactyl Panel v1 source without changing daemon/API names."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parent.parent
TARGETS = [ROOT / "resources" / "views", ROOT / "resources" / "scripts"]
EXTS = {".tsx", ".ts", ".jsx", ".js", ".blade.php", ".php"}
changed = []
for folder in TARGETS:
    if not folder.is_dir():
        continue
    for file in folder.rglob("*"):
        if not file.is_file() or not (file.suffix in EXTS or file.name.endswith(".blade.php")):
            continue
        original = file.read_text(encoding="utf-8")
        # Change only exact display text, not technical identifiers or attribution.
        modified = re.sub(r'(?<=>)Pterodactyl(?=<)', 'INSANE_PANEL', original)
        modified = modified.replace('>Pterodactyl Panel<', '>INSANE_PANEL<')
        if modified != original:
            file.write_text(modified, encoding="utf-8")
            changed.append(str(file.relative_to(ROOT)))
print("Updated", len(changed), "frontend files:")
print("\n".join(changed))
print("Review remaining visible labels manually before building.")
