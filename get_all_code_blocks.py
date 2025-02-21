# This file contains a regular expression pattern adapted from the llm project:
# https://github.com/simonw/llm/blob/main/llm/utils.py
# Original work under Apache 2.0 license

import argparse
import re
import sys

# TODO: make it so that it does a check between input and attempted output; if they're the same, fail/don't write anything, not this code's job to write arbitrary streams for the user


def get_all_code_blocks(text: str) -> str | list[str]:
    pattern = re.compile(
        r"""(?m)^(?P<fence>`{3,})(?P<lang>\w+)?\n(?P<code>.*?)^(?P=fence)[ ]*(?=\n|$)""",
        re.DOTALL,
    )
    matches = list(pattern.finditer(text))
    blocks = [match.group("code") for match in matches]
    return blocks if blocks else text


def main():
    parser = argparse.ArgumentParser(
        prog="CodeBlockExtractor",
        description="Gets all code fences inside an output, and writes it to a markdown file. Useful for working with LLMs."
    )
    parser.add_argument('filename')
    parser.add_argument('-m', '--multi-file', action='store_true',
                        help='Write each code block to a separate file.')
    # this is the single file way (default)
    with open(y, "r") as f:
        text = f.read()
        code_blocks = get_all_code_blocks(text)
        with open(f"{f.name}_all_blocks.md")
        # this is the multifile way
    with open(x, "r") as f:
        text = f.read()
        code_blocks = get_all_code_blocks(text)
        for i, block in enumerate(code_blocks, start=1):
            with open(f"{f.name}_block_{i}.md") as block_file:
                block_file.write(block)


if __name__ == "__main__":
    main()
