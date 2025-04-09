import sys
from typing import Dict

# NOT SUPPORTED:
# - figures
# - comments
# - table
# - enumerate
# - alertblock, exampleblock


def remove_textbf(line: str, flags: Dict[str, bool]) -> str:
    while line.find("\\textbf") != -1:
        start = line.find("\\textbf{")
        end = line.find("}", start)
        textbf = line[start : end + 1]
        textbf_without_braces = textbf.replace("\\textbf{", "**").replace("}", "**")
        line = line.replace(textbf, textbf_without_braces)
    return line


def remove_textit(line: str, flags: Dict[str, bool]) -> str:
    while line.find("\\textit") != -1:
        start = line.find("\\textit{")
        end = line.find("}", start)
        textit = line[start : end + 1]
        textit_without_braces = textit.replace("\\textit{", "*").replace("}", "*")
        line = line.replace(textit, textit_without_braces)
    return line


def remove_frame(line: str, flags: Dict[str, bool]) -> str:
    line = line.replace("\\end{frame}", "")
    while line.find("\\begin{frame}") != -1:
        line = line.replace("\\begin{frame}", "")
        start = line.find("{")
        if start == -1:
            break
        end = line.find("}", start)
        frame_name = line[start : end + 1]
        frame_name_clean = "#### " + frame_name.replace("{", "").replace("}", "")
        line = line.replace(frame_name, frame_name_clean)
    return line

def remove_itemize(line: str, flags: Dict[str, bool]) -> str:
    line = line.replace("\\begin{itemize}", "")
    line = line.replace("\\end{itemize}", "")
    line = line.replace("\\item", "- ")
    return line

def remove_section(line: str, flags: Dict[str, bool]) -> str:
    if line.find("\\section") != -1:
        start = line.find("{")
        if start != -1:
            end = line.find("}", start)
            section_name = line[start : end + 1]
            section_name_clean = section_name.replace("{", "").replace("}", "")
            line = line.replace(section_name, "### " + section_name_clean)
        line = line.replace("\\section", "")
    return line

def remove_whitespace_start(line: str, flags: Dict[str, bool]) -> str:
    return line.lstrip()

def fix_equations(line: str, flags: Dict[str, bool]) -> str:
    line = line.replace("\\[", "$$").replace("\\]", "$$")
    line = line.replace("\\(", "$").replace("\\)", "$")
    line = line.replace("\\begin{equation}", "$$").replace("\\end{equation}", "$$")
    return line

def remove_blocks(line: str, flags: Dict[str, bool]) -> str:
    if line.find("\\begin{block}") != -1:
        flags["block"] = True
        line = line.replace("\\begin{block}", "")
        start = line.find("{")
        if start != -1:
            end = line.find("}", start)
            block_name = line[start : end + 1]
            block_name_clean = block_name.replace("{", "").replace("}", "")
            line = line.replace(block_name, block_name_clean)
    
    if flags["block"]:
        if line.find("\\end{block}") != -1:
            flags["block"] = False
            line = line.replace("\\end{block}", "")
        else:
            line = "> " + line
    return line

def remove_comments(line: str, flags: Dict[str, bool]) -> str:
    if line.find("%") != -1:
        start = line.find("%")
        line = line[:start]
    return line


# create main with command line argument
def main():
    args = sys.argv[1:]

    print(args)
    filename = args[1]
    updated_filename = filename.replace(".md", "_updated.md")

    with open(filename, "r") as f:
        lines = f.readlines()

    cleaning_steps = [
        #remove_whitespace_start,
        remove_section,
        remove_textbf,
        remove_textit,
        remove_frame,
        remove_itemize,
        fix_equations,
        remove_blocks,
    ]

    flags = {
        "block" : False
    }

    # first pass to remove comments section and whitespace at the state
    for i, line in enumerate(lines):
        line = line.lstrip()
        line = remove_comments(line, flags)
        lines[i] = line

    for i, line in enumerate(lines):
        for step in cleaning_steps:
            line = step(line, flags)
        lines[i] = line

    with open(updated_filename, "w") as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    main()
