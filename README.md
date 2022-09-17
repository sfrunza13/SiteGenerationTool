# SiteGenerationTool
Author: Stefan Frunza

<H1>Requirements</H1>
<p>To work with this program, Python is all you require</p>

<H1>Warning</H1>
<p><strong>THIS PROGRAM DELETES THE TARGET DIRECTORY SPECIFIED WITH THE -o OPTION.</strong> it then recreates it and populates it with the new HTML, but remember <strong>THIS PROGRAM DELETES THE TARGET DIRECTORY SPECIFIED WITH THE -o OPTION.</strong></p>

<H1>What it is</H1>
<p>A tool that will take a text file as an option and create HTML markup based upon it.<br>
To use simply open a console to the script's location and write <strong>python Sitegen.py</strong> along with the options you wish to specify, among which you must have a plain text file to convert to mark up.</p>


<p>Optionally, if you leave 2 empty lines below the first line in the .txt file the program will make the first line of your text file the title of the HTML page that will be generated along with having it be bolded as an H1 at the top of the page.</p>


<p>The tool will automatically create a <strong>./dist</strong> directory and insert the created HTML there. Everytime the program runs it will delete the target <strong>./dist</strong> directory and recreate it.</p>


<p>A user may specify an input directory instead of an input file and the program will go through every file within the directory and attempt to convert .txt to .html while ignoring further directories. When a directory is specified as input the program will also attempt to create an index.html with anchor tags to all of the HTML files generated based on the input directory's contents.</p>


<h2>Possile Options:</h2>


| ShortCut | LongOption | Result |
| -------- | -------- | ------ |
| -v | --version | Displays name and version of program |
| -h | --help | Displays a help message with useful information about program and possible options |
| -i | --input | Specify an Input file please add .txt suffix (requires argument) |
| -o | --ouput | Specify a name for existing output directory (requires argument, must be existing directory)|

