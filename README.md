# SiteGenerationTool
Author: Stefan Frunza

<H1>Requirements</H1>
<p>To use this program, Python is all you require. To contribute the dependencies in requirements-dev.txt would be helpful.</p>

<H1>Warning</H1>
<p><strong>THIS PROGRAM DELETES THE TARGET DIRECTORY SPECIFIED WITH THE -o OPTION.</strong> it then recreates it and populates it with the new HTML, but remember <strong>THIS PROGRAM DELETES THE TARGET DIRECTORY SPECIFIED WITH THE -o OPTION.</strong></p>

<H1>What it is</H1>
<p>A tool that will take a text (.txt) or markdown (.md) file as an option and create HTML markup based upon it.<br>
To use simply open a console to the script's location and write <code>py src/super_site_generator_package/main.py</code> along with the options you wish to specify, among which you must have a plain text file to convert to mark up. Alternatively you can obviously cd into the package and make it a shorter command: <code>py main.py</code>.</p>


<p>Optionally, if you leave 2 empty lines below the first line in the .txt file the program will make the first line of your text file the title of the HTML page that will be generated along with having it be bolded as an H1 at the top of the page.</p>


<p>The tool will automatically create a <strong>./dist</strong> directory and insert the created HTML there. Everytime the program runs it will delete the target <strong>./dist</strong> directory and recreate it.</p>


<p>A user may specify an input directory instead of an input file and the program will go through every file within the directory and attempt to convert .txt to .html while ignoring further directories. When a directory is specified as input the program will also attempt to create an index.html with anchor tags to all of the HTML files generated based on the input directory's contents.</p>


<h2>Possible Options:</h2>


| ShortCut | LongOption | Result |
| -------- | -------- | ------ |
| -v | --version | Displays name and version of program |
| -h | --help | Displays a help message with useful information about program and possible options |
| -i | --input | Specify an Input directory or file only .txt suffix will be correctly parsed (requires argument) |
| -o | --ouput | Specify a name for existing directory (optional argument)|
| -c | --config | Specify a json file with all other options within it|

<h2>Markdown Support:</h2>

| Type | Or | Result |
| -------- | -------- | ------ |
| \*Italic\* | \_Italic\_ | <i>Italic</i>  |
| \*\*Bold\*\* | \_\_Bold\_\_ | <b>Bold</b>  |
| --- | |<hr>H R |


<h1>You can use my new PIP package</h1>
<p>My site generator is now a stand alone pip package that you can run from the cli with the command <code>ssgen</code>. Originaly the site generators name was going to be something like supersaiyagen in reference to the golden haired super forms in the dragon ball series of anime, in fact that is why the class that does most of the work is called SSJ. I decided to harken back to this namesake with the entrypoint command of <code>ssgen</code>.</p>


<p>The pip package is currently located here: <i>https://test.pypi.org/project/super-site-generator-package/1.0.7/</i> and can be installed using: <code>pip install -i https://test.pypi.org/simple/ super-site-generator-package==1.0.7</code></p>


<p>If you so choose you can test it out in a python virtual environement by running <code>py -m venv</code> and then <code>Scripts\activate</code>(on Windows) or <code>/bin/activate</code>(on basically everything else). You could also just install it straight into the CLI without any of this as well following the next step.</p>

<p>Ensure you have pip and that it is updated and try installing using <code>pip install -i https://test.pypi.org/simple/ super-site-generator-package==1.0.7</code></p>

<p>Just like when you work with the main module directly you can specify all of the arguments right after <code>ssgen</code> like <code>ssgen -vh</code> for example to see version and help. Everything should work the same as was outlined in the table of options in the previous section just replace <code>main.py</code> for <code>ssgen</code>.</p>
