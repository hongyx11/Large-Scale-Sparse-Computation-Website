#!/usr/bin/env python3
"""
Helper script to strip the existing TOC block from myst.yml
so that `myst init --write-toc` can regenerate it.
"""

def main():
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
            # End TOC block if we find a line with less than 4 spaces indent 
            # (which is not a comment or empty line)
            if stripped and not stripped.startswith("#") and indent < 4:
                in_toc = False
        if not in_toc:
            new_lines.append(line)

    with open("myst.yml", "w") as f:
        f.writelines(new_lines)
    print("Stripped existing TOC from myst.yml successfully.")

if __name__ == "__main__":
    main()
