# SiteGenerationTool
Author: Stefan Frunza


<p>A tool that will take a text file as an option and create HTML markup based upon it.<br>
To use simply open a console to the script's location and write <strong>python Sitegen.py</strong> along with the options you wish to specify, among which you must have a plain text file to convert to mark up.</p>


<p>The tool will automatically create a <strong>./dist</strong> directory and insert the created HTML there. Everytime the program runs it will delete the target <strong>./dist</strong> directory and recreate it.</p>


<p>A user may specify an input directory instead of an input file and the program will go through every file within the directory and attempt to convert .txt to .html while ignoring further directories.</p>


<h2>Possile Options:</h2>


| ShortCut | LongOption | Result |
| -------- | -------- | ------ |
| -v | --version | Displays name and version of program |
| -h | --help | Displays a help message with useful information about program and possible options |
| -i | --input | Specify an Input file please add .txt suffix (requires argument) |
| -o | --ouput | Specify a name for existing output directory (requires argument, must be existing directory) *IN PROGRESS|

