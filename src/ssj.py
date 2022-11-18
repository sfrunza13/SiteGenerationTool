"""ssj module where the input directory or file is parsed into an HTML with some MarkDown Support"""
from os import listdir
from os.path import isfile, join
from pathlib import Path
import re
import json


class SSJ:
    """SSJ class the Site Generator object that does all the work"""

    defaultOutputFolder = Path("./dist")
    token = "<body>"
    template = r"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Filename</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="..\static\style.css">
</head>
<div class="navbar">
</div>
<body></body>
</html>"""

    def __init__(self, input_name=None, output=None):
        self.input_name = input_name
        if input_name is None:
            print("No input has been specified at time of initialization.")
        if output is None:
            self.output = SSJ.defaultOutputFolder
        else:
            self.output = Path(output)

    def parse_file(self, input_file, input_folder=None):
        """looks through text file and parses header, body paragraphs, etc...
        first line is header if it's given a few empty newlines underneath, new
        paragraphs are denoted by newlines, convert markdown is done at every
        point to see if there are special characters in the text to translate to
        supported mark up tags."""
        paragraphs = []

        try:
            if input_folder is None:
                with open(input_file, "r", encoding="utf8") as file:
                    lines = file.readlines()
            else:
                input_folder = Path(input_folder)
                source = input_folder / input_file
                with open(source, "r", encoding="utf8") as file:

                    lines = file.readlines()

            paragraphs, title_question_mark = SSJ.line_by_line(SSJ, lines, input_file)

            output_name = input_file[: input_file.find(".")] + ".html"

            temp_temp = SSJ.template

            self.edit_template(paragraphs, title_question_mark)

            self.write_out(output_name)

            SSJ.template = temp_temp

        except OSError as err:
            print("Error: " + str(err))

    def edit_template(self, paragraphs, title):
        """
        Replace the template HTML with the newly aquired
        specifics to the most currently opened file
        """
        if title:
            # title_pos = SSJ.template.find("<title>") + len("<title>")

            # SSJ.template = (
            #     SSJ.template[:title_pos]
            #     + paragraphs[0][4:-5]
            #     + SSJ.template[title_pos:]
            # )
            SSJ.template = SSJ.template.replace("Filename", paragraphs[0][4:-5])

        pos = SSJ.template.find(SSJ.token) + len(SSJ.token)

        for paragraph in reversed(paragraphs):
            SSJ.template = SSJ.template[:pos] + paragraph + SSJ.template[pos:]

    def write_out(self, output):
        """writes edited template to output file"""
        try:
            if self.output:
                with open(self.output / output, "w", encoding="utf-8") as file_out:

                    file_out.write(SSJ.template)

        except OSError as err:
            print("Error: " + str(err))

    def parse_dir(self, input_name):
        """Looks through directory, adds valid files to navbar then sends them to be converted"""
        input_folder = input_name

        # retrieve every txt file in dir omitting other dirs
        onlyfiles = [f for f in listdir(input_name) if isfile(join(input_name, f))]

        SSJ.template = SSJ.template.replace("Filename", "Index Page")

        # go through files and make the navbar
        for file in onlyfiles:
            if file.endswith(".txt") or file.endswith(".md"):
                output_name = file[: file.find(".")] + ".html"
                href_name = output_name.replace(" ", "%20")
                pos = SSJ.template.find('<div class="navbar">') + len(
                    '<div class="navbar">'
                )
                SSJ.template = f"""{SSJ.template[:pos]}<button><a href={href_name}>{output_name}</a>
                    </button>{SSJ.template[pos:]}"""

        # parse files one by one
        for file in onlyfiles:
            self.parse_file(file, input_folder)

        try:
            if self.output:
                with open(
                    self.output / "Index.html", "w", encoding="utf-8"
                ) as file_out:
                    file_out.write(SSJ.template)
        except OSError as err:
            print("Error: " + str(err))

        # SSJ.template = temp

    def markdown_search(self, regex, ind_chars, tag, line):
        """Searches for what could be considered markdown in the txt file"""
        new_line = line
        match = re.search(regex, new_line)
        while match is not None:
            if tag == "hr":
                new_line = (
                    new_line[: match.span()[0]]
                    + "<"
                    + tag
                    + ">"
                    + new_line[match.span()[0] + ind_chars :]
                )
            else:
                new_line = (
                    new_line[: match.span()[0]]
                    + "<"
                    + tag
                    + ">"
                    + new_line[
                        match.span()[0] + ind_chars : match.span()[1] - ind_chars
                    ]
                    + "</"
                    + tag
                    + ">"
                    + new_line[match.span()[1] :]
                )
            match = re.search(regex, new_line)
        return new_line

    def convert_markdown(self, line):
        """uses markdown_search to go through the different
        special characters we would like to check and convert"""
        new_line = line
        # bold
        new_line = SSJ.markdown_search(SSJ, r"\*\*[^*]+\*\*", 2, "b", new_line)
        new_line = SSJ.markdown_search(SSJ, r"__[^*]+__", 2, "b", new_line)
        # italics
        new_line = SSJ.markdown_search(SSJ, r"\*[^*]+\*", 1, "i", new_line)
        new_line = SSJ.markdown_search(SSJ, r"_[^*]+_", 1, "i", new_line)
        # code
        new_line = SSJ.markdown_search(SSJ, r"\`\`\`[^*]+\`\`\`", 3, "code", new_line)
        new_line = SSJ.markdown_search(SSJ, r"\`[^*]+\`", 1, "code", new_line)
        # hr
        new_line = SSJ.markdown_search(SSJ, r"\-\-\-[^*]", 3, "hr", new_line)

        return new_line

    def parse_config(self, config_file):
        """parses config json"""
        with open(config_file, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
            print("Read successful")

        arr_of_str = [""] * 2

        if data["input"]:
            arr_of_str[0] = data["input"]
        else:
            arr_of_str[0] = SSJ.defaultOutputFolder

        if data["output"]:
            arr_of_str[1] = data["output"]
        else:
            arr_of_str[0] = Path("./output")

        return arr_of_str

    def line_by_line(self, lines, input_file):
        """
        Convert line by line and
        seperate them into paragraphs
        Returns Tuple consisting of
        List of Paragraphs
        Bool whether title is found
        """
        paragraphs = []
        title_question_mark = True
        for i, line in enumerate(lines):
            if i == 0:
                title_storage = line
            elif i == 1:
                if line != "\n":
                    title_question_mark = False
                    new_line = "<p>" + title_storage + "</p>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
                    new_line = "<p>" + line + "</p>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
            elif i == 2:
                if line != "\n":
                    title_question_mark = False
                    new_line = "<p>" + title_storage + "</p>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
                    new_line = "<p>" + line + "</p>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
            elif i == 3:
                if title_question_mark is True:
                    new_line = "<h1>" + title_storage + "</h1>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
                    new_line = "<p>" + line + "</p>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
            else:
                if line == "\n":
                    new_line = "</p>" + "<p>"
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )
                else:
                    new_line = line
                    paragraphs.append(
                        SSJ.convert_markdown(SSJ, new_line)
                        if input_file.endswith(".md")
                        else new_line
                    )

        return paragraphs, title_question_mark
