#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_test.py — attsis-learn pre-push validation. All checks must pass."""
import sys
import os
import io
import html.parser

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASS = []
FAIL = []


def check(name, condition, detail=""):
    if condition:
        PASS.append(name)
        print(f"  PASS  {name}")
    else:
        FAIL.append(name)
        print(f"  FAIL  {name}{(' — ' + detail) if detail else ''}")


def file_exists(rel):
    return os.path.isfile(os.path.join(ROOT, rel))


def file_contains(rel, text):
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path):
        return False
    with open(path, encoding="utf-8") as f:
        return text in f.read()


class HTMLValidator(html.parser.HTMLParser):
    pass


def validate_html(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path):
        return False
    try:
        with open(path, encoding="utf-8") as f:
            HTMLValidator().feed(f.read())
        return True
    except html.parser.HTMLParseError:
        return False


print("\n── attsis-learn smoke test ──\n")

# Required files
check("site/index.html exists",       file_exists("site/index.html"))
check("site/css/style.css exists",    file_exists("site/css/style.css"))
check("site/js/main.js exists",       file_exists("site/js/main.js"))
check("CLAUDE.md exists",             file_exists("CLAUDE.md"))
check("PENDING_TASKS.md exists",      file_exists("PENDING_TASKS.md"))
check("docs/product/PRODUCT.md",      file_exists("docs/product/PRODUCT.md"))
check("pages.yml exists",             file_exists(".github/workflows/pages.yml"))
check("ci.yml exists",                file_exists(".github/workflows/ci.yml"))

# HTML validity
check("site/index.html is valid HTML", validate_html("site/index.html"))

# Required content
check("index.html has charset UTF-8",
      file_contains("site/index.html", 'charset="UTF-8"'))
check("index.html has viewport meta",
      file_contains("site/index.html", "viewport"))
check("index.html has og:title",
      file_contains("site/index.html", "og:title"))
check("index.html has WhatsApp CTA",
      file_contains("site/index.html", "wa.me/"))
check("index.html has trust bar",
      file_contains("site/index.html", "trust-bar"))
check("index.html has P.Eng",
      file_contains("site/index.html", "P.Eng"))

# Content sessions
for lvl in (1, 2):
    for s in range(1, 9):
        rel = f"content/level{lvl}/session-{s:02d}.md"
        check(f"{rel} exists", file_exists(rel))

# No secrets
check("No hardcoded secrets in index.html",
      not file_contains("site/index.html", "sk-") and
      not file_contains("site/index.html", "API_KEY"))

print(f"\n── {len(PASS)} passed · {len(FAIL)} failed ──\n")

if FAIL:
    print("Fix failures before pushing.\n")
    sys.exit(1)

print("All checks passed. Safe to push.\n")
