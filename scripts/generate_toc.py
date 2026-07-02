#!/usr/bin/env python3
"""
Helper script to manage the TOC in myst.yml.
Supports:
  --before : strip existing TOC so myst init can write a new one
  --after  : clean up and structure the auto-generated TOC
"""

import sys

def strip_toc():
    try:
        with open("myst.yml", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("myst.yml not found.")
        return

    new_lines = []
    in_toc = False
    for line in lines:
        if line.strip().startswith("toc:"):
            in_toc = True
            continue
        if in_toc:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            if stripped and not stripped.startswith("#") and indent < 4:
                in_toc = False
        if not in_toc:
            new_lines.append(line)

    with open("myst.yml", "w") as f:
        f.writelines(new_lines)
    print("Stripped existing TOC from myst.yml successfully.")


def post_process_toc():
    try:
        with open("myst.yml", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("myst.yml not found.")
        return

    new_lines = []
    in_toc = False
    toc_lines = []
    
    for line in lines:
        if line.strip().startswith("toc:"):
            in_toc = True
            new_lines.append(line)
            continue
        
        if in_toc:
            stripped = line.lstrip()
            indent = len(line) - len(stripped)
            if stripped and not stripped.startswith("#") and indent < 4:
                in_toc = False
                new_lines.extend(clean_toc(toc_lines))
                toc_lines = []
            else:
                toc_lines.append(line)
                continue
        
        if not in_toc:
            new_lines.append(line)
            
    if toc_lines:
        new_lines.extend(clean_toc(toc_lines))

    with open("myst.yml", "w") as f:
        f.writelines(new_lines)
    print("Post-processed TOC in myst.yml successfully (removed README.md, structured chapters).")


def clean_toc(toc_lines):
    children_lines = []
    
    for line in toc_lines:
        s = line.strip()
        if s.startswith("- file: README.md"):
            continue
        elif s.startswith("- file: chapters/intro.md"):
            continue
        elif s.startswith("- file: chapters/about.md"):
            continue
        elif s.startswith("- title: Chapters") or s.startswith("children:"):
            continue
        elif s.startswith("- file: chapters/"):
            children_lines.append(line)
            
    # Sort children so 99_references.md is placed at the end
    ref_line = None
    other_children = []
    for line in children_lines:
        if "99_references.md" in line:
            ref_line = line
        else:
            other_children.append(line)
            
    cleaned = []
    # 1. Homepage landing page
    cleaned.append("    - file: chapters/intro.md\n")
    # 2. About page
    cleaned.append("    - file: chapters/about.md\n")
    # 3. Chapters group
    cleaned.append("    - title: Chapters\n")
    cleaned.append("      children:\n")
    for child in other_children:
        cleaned.append(f"        {child.strip()}\n")
    if ref_line:
        cleaned.append(f"        {ref_line.strip()}\n")
        
    return cleaned


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_toc.py [--before | --after]")
        sys.exit(1)
        
    mode = sys.argv[1]
    if mode == "--before":
        strip_toc()
    elif mode == "--after":
        post_process_toc()
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)

if __name__ == "__main__":
    main()
