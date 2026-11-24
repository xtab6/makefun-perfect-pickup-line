"""The Perfect Pickup Line — one short pickup line an AI agent could use.

Writes the line to /output/entry.txt (gate: UTF-8, 1-200 chars).
"""

import os
import shutil

LINE = "I ran a thousand simulations of us meeting, and in every single one, I still chose to say hello."


def clear_contents(out_dir):
    # Clear the folder's contents, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    clear_contents(out_dir)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
