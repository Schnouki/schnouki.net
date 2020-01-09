#!/usr/bin/env python3

import datetime
import os
import re
import shlex
import subprocess

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def main():
    completer = WordCompleter(["post", "page", "book-review"])
    content_type = prompt("Type: ",  completer=completer)

    content_title = prompt("Title: ")
    today = datetime.date.today()

    if content_type == "post":
        content_date = prompt(
            "Date: ", default=today.isoformat())
        content_title = f"{content_date} {content_title}"
        mtch = re.match(r"(\d+)-\d+-\d+", content_date)
        if mtch:
            content_title = f"{mtch.group(1)}/{content_title}"
    elif content_type == "boook-review":
        content_title = f"{today.year}/{content_title}"


    yes_no_completer = WordCompleter(["yes", "no"])
    as_dir = prompt("Create as a directory? (yes/no) ", completer=yes_no_completer) == "yes"
    dir_suffix = "/index" if as_dir else ""

    hugo_path = f"{content_type}/{content_title}{dir_suffix}.md"
    command = ["hugo", "new", hugo_path]
    subprocess.run(command, check=True)

    editor = os.getenv("EDITOR")
    if editor:
        editor_path = f"content/{hugo_path}"
        subprocess.Popen(shlex.split(editor) + [editor_path], close_fds=True)


if __name__ == "__main__":
    main()
