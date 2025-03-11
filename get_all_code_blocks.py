# This file contains a regular expression pattern adapted from the llm project:
# https://github.com/simonw/llm/blob/main/llm/utils.py
# Original work under Apache 2.0 license

import argparse
import re
from pathlib import Path

# import pyjq


def load_provider_response(json_response: str):
    import json
    resp = json.loads(json_response)


def get_all_code_blocks(text: str) -> list[str]:
    pattern = re.compile(
        r"""(?m)^(?P<fence>`{3,})(?P<lang>\w+)?\n(?P<code>.*?)^(?P=fence)[ ]*(?=\n|$)""",
        re.DOTALL,
    )
    matches = list(pattern.finditer(text))
    blocks = [match.group("code") for match in matches]
    if blocks:
        return blocks
    raise ValueError("No code blocks found in input.")


def single_file(filename):
    # this is the single file way (default)
    with open(filename, "r") as f:
        text = f.read()
        # gets all extensions: not entirely sure why useful but still
        # src: https://stackoverflow.com/a/66335484
        p = Path(filename)
        name = p.with_name(p.name.split('.')[0]).with_suffix('')
        code_blocks = get_all_code_blocks(text)
        with open(f"{name}_all_blocks.md", "w") as blocks_file:
            for i, block in enumerate(code_blocks, start=1):
                blocks_file.write(f"{name} Code Block #{i}\n")
                blocks_file.write(("-" * 80) + "\n")
                blocks_file.write(block)
                blocks_file.write(("-" * 80) + "\n")


def multi_file(filename):
    # this is the multifile way
    with open(filename, "r") as f:
        text = f.read()
        p = Path(filename)
        name = p.with_name(p.name.split('.')[0]).with_suffix('')
        code_blocks = get_all_code_blocks(text)
        for i, block in enumerate(code_blocks, start=1):
            with open(f"{name}_block_{i}.md", "w") as block_file:
                block_file.write(f"{name} Code Block #{i}\n")
                block_file.write(("-" * 80) + "\n")
                block_file.write(block)
                block_file.write("-" * 80)


def stream(): pass


def main():
    # instantiate parser object
    parser = argparse.ArgumentParser(
        prog="CodeBlockExtractor",
        description="Gets all code fences inside an output, and writes it to a markdown file. Useful for working with LLMs."
    )
    parser.add_argument('filename')
    parser.add_argument('-m', '--multi-file', action='store_true',
                        help='Write each code block to a separate file.')
    # get arguments
    args = parser.parse_args()
    try:
        if args.multi_file:
            multi_file(args.filename)
        else:
            single_file(args.filename)
    except ValueError as e:
        print(f"Here's the issue: {e}")


if __name__ == "__main__":
    main()
