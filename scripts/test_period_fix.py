#!/usr/bin/env python3
"""Valida a regra estreita de espaço após ponto contra a sintaxe FoxPro."""

from __future__ import annotations

import re

from html_utils import MISSING_SPACE_AFTER_PERIOD_RE, _apply_outside_code

MUST_NOT_CHANGE = [
    "Set the value to .T. or .F. as needed.",
    "The property returns .NULL. when empty.",
    "Use This.Caption to read the text.",
    "ThisForm.Show()",
    "frmTest.Show",
    "CursorAdapter.AfterCursorFill fires next.",
    "XMLAdapter.XMLNameIsXPath property is True (.T.).",
    "_SCREEN.Themes is set to True.",
    "Run MYAPP.APP from the prompt.",
    "Memo File Structure (.FPT)",
    "TRY...CATCH...FINALLY in procedural code.",
    "The file TEMP.TXT was created.",
    "oRep.Theme = 1",
    "```foxpro\nfrmMyForm.Show\nx = .T.\n```",
    "Value is .T.There",  # uppercase literal context, prev char uppercase -> untouched
]

MUST_CHANGE = [
    ("end of the program file.You cannot include", "end of the program file. You cannot include"),
    ("Windows Control Panel.This setting is available", "Windows Control Panel. This setting is available"),
    ("user cannot edit the control.The table or view", "user cannot edit the control. The table or view"),
    ("creates a dotted line.The 100 pen type", "creates a dotted line. The 100 pen type"),
    ("specific to the OLE object.In this case", "specific to the OLE object.In this case"),  # 'In' not in list
]


def fix(text: str) -> str:
    return _apply_outside_code(
        text, lambda part: MISSING_SPACE_AFTER_PERIOD_RE.sub(r". \1", part)
    )


print("=== MUST NOT CHANGE ===")
fails = 0
for s in MUST_NOT_CHANGE:
    got = fix(s)
    ok = got == s
    if not ok:
        fails += 1
    print(f"{'ok  ' if ok else 'FAIL'} {s!r}")
    if not ok:
        print(f"      -> {got!r}")

print("\n=== MUST CHANGE ===")
for src, expected in MUST_CHANGE:
    got = fix(src)
    ok = got == expected
    if not ok:
        fails += 1
    print(f"{'ok  ' if ok else 'FAIL'} {src!r}")
    print(f"      -> {got!r}")

print(f"\nfailures: {fails}")
