"""This is the main module that parses the arguments passed to the program and passes
them to the SSJ module to parse into HTML"""
import sys
import getopt
import os
import shutil
from os.path import isdir
from ssj import SSJ


def main(argv):
    """Main method, takes arguments, checks they're valid and sends them on to SSJ"""

    try:

        opts, args = getopt.getopt(
            argv, "vhi:o:c:", ["version", "help", "input=", "output=", "config="]
        )
    except getopt.GetoptError:
        print("Error with GetOpt")
        sys.exit(2)

    config_exists = 0

    for opt, arg in opts:
        if opt in ("-c", "--config"):
            config = arg
            config_exists = 1
            break

    if config_exists == 1:
        if os.path.exists(config) and config.endswith(".json"):
            config_opts = SSJ.parse_config(SSJ, config)
            super_site_jen = parse_config_args(config_opts)
    elif config_exists == 0:
        super_site_jen = parse_arg(opts)

    try:
        shutil.rmtree(super_site_jen.output)
    except OSError as error:
        print(error)

    os.mkdir(super_site_jen.output)

    if super_site_jen.input_name.endswith(".txt") or super_site_jen.input_name.endswith(
        ".md"
    ):
        super_site_jen.parse_file(super_site_jen.input_name)
    elif isdir(super_site_jen.input_name):
        super_site_jen.parse_dir(super_site_jen.input_name)


def parse_config_args(config_opts):
    """
    Checks what to do with arguments
    in config json
    """
    if config_opts[0] != "":
        input_name = config_opts[0]
    if config_opts[1] != "":
        output = config_opts[1]
        if "output" in locals():
            super_site_jen = SSJ(input_name, output)
        elif "input_name" in locals():
            super_site_jen = SSJ(input_name)
    return super_site_jen


def parse_arg(opts):
    """
    Make sense of the passed argument
    """
    name = "SSJ SSG the Super Saiyan Site Tool"
    version = "0.0.1"
    for opt, arg in opts:
        if opt in ("-v", "--version"):
            print("Name: " + name, "\nVersion: " + version)
        if opt in ("-h", "--help"):
            print(
                """This tool is designed to take a plain text file and generate a HTML markup
                file based upon it.\nPossible options:\n -i or --input to specify an input
                file\n -o or --output to specify the name of a specific directory you would
                like to output to (it must be an existing valid directory).\n -v or
                --version to see the name and version of the tool\n"""
            )
        if opt in ("-i", "--input"):
            input_name = arg

        if opt in ("-o", "--output"):
            output = arg

    if "output" in locals():
        super_site_jen = SSJ(input_name, output)
    elif "input_name" in locals():
        super_site_jen = SSJ(input_name)
    else:
        print("There must be at least a valid .txt, .md, or directory input specified")
        sys.exit(1)

    return super_site_jen


if __name__ == "__main__":
    main(sys.argv[1:])
