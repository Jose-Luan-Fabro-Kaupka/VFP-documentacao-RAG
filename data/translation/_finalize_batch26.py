#!/usr/bin/env python3
"""Merge all batch26 translations into _write_batch26.py."""
from pathlib import Path
import importlib.util
import re
import json

ROOT = Path(__file__).resolve().parent
STAGING = ROOT / "staging"
OUT_SCRIPT = ROOT / "_write_batch26.py"

text = OUT_SCRIPT.read_text(encoding="utf-8")
pattern = re.compile(r'"([0-9a-f-]+\.md)": """(.*?)""",', re.DOTALL)
translations = {m.group(1): m.group(2) for m in pattern.finditer(text)}

# Load part3
spec = importlib.util.spec_from_file_location("part3", ROOT / "_batch26_part3.py")
part3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(part3)
translations.update(part3.PART3)

# Load staging files (override / add)
staging_ids = [
    "46e99caf-fe50-4d55-aa78-e37cffeca2d1",
    "482f2a40-3ebc-483c-b86b-462cf64c106e",
    "490d957f-926a-4b4c-a265-e3ad5f679f1b",
    "49265836-568c-4121-9aa1-789162d15091",
    "4997e714-635a-4981-b7cc-5f1e7834f39a",
]
for sid in staging_ids:
    p = STAGING / f"{sid}.md"
    translations[f"{sid}.md"] = p.read_text(encoding="utf-8")

lines = [
    '#!/usr/bin/env python3',
    '"""Write remaining batch_0026 translations to data/markdown_pt/."""',
    'from pathlib import Path',
    '',
    'OUT_DIR = Path(__file__).resolve().parents[1] / "markdown_pt"',
    '',
    'TRANSLATIONS = {',
]
for name in sorted(translations.keys()):
    content = translations[name]
    lines.append(f'    {json.dumps(name)}: {json.dumps(content)},')
lines.extend([
    '}',
    '',
    '',
    'def main():',
    '    OUT_DIR.mkdir(parents=True, exist_ok=True)',
    '    written = 0',
    '    failures = []',
    '    for name, content in TRANSLATIONS.items():',
    '        try:',
    '            path = OUT_DIR / name',
    '            path.write_text(content, encoding="utf-8")',
    '            written += 1',
    '        except Exception as e:',
    '            failures.append((name, str(e)))',
    '    print(f"written: {written}")',
    '    if failures:',
    '        print("failures:", failures)',
    '    return written, failures',
    '',
    '',
    'if __name__ == "__main__":',
    '    main()',
    '',
])

OUT_SCRIPT.write_text("\n".join(lines), encoding="utf-8")
print(f"Final script: {len(translations)} entries")
