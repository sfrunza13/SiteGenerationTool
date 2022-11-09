## Black and PyLint
For source formatting insure you download Black for python by running the following:

`pip install black`


and making sure the settings.json under .vscode looks as follows:

```
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
}
```


and then every time you save a file Black will automatically format it, if you want to format multiple files at the same time you can run the following from the command line:


`python -m black {directory/file}`


When it comes to linting install pylint using `pip install pylint`

then use `pylint src` or `pylint {targetfile}`

To add this linter to the VSCode IDE follow the following links instructions: https://code.visualstudio.com/docs/python/linting

It amounts to Ctrl+Shift+P -> python select linter -> select pylint -> install

Then whenever you want to use it Ctrl+Shift+P and select Python: Run Linting


## Requirements and Testing
For ease of installation I have now commited a requirements-dev.txt that you can install all the dependencies this project currently uses including the testing dependencies I have recently added.

For the primary testing framework and for ease of use we are using **pytest**.

The naming convention for these tests is **test_module_name_method_name**, I suggest you follow this convention, in any case the test files must be prepended with the word *test*.

To write pytest tests is relatively intuitive compared to the other methods I have taken a look at.

To start set up a pyproject.toml to configure pytest and coverage with the following properties:

```
[tool.pytest.ini_options] 
addopts = "-ra --cov"
testpaths = ["tests"] 
pythonpath = ['src']
```

-ra for extra test summary when running pytest, and --cov for running coverage when running pytest.

After this is set up to run the tests just run `pytest` from the command line.


if you want to see report after from captured data:

`coverage report`

if you want to see missing lines as well

`coverage report -m`

If you want more information from the test runs you can append the `-v` option or `-vv` depending on how verbose you would like it

With the above settings to write a test first import the module you want to test relative to src, ignoring the pylint error since the pythonpath to src is already specified in our config toml.

Then all you must do is ensure that the test method begins with the prefix `test` and to assert just use the keyword `assert`.

Example code:

```
def test_make_paragraphs_md_w_h1():
    """Test paragraphs while identifying title/header"""
    is_title = True
    input_line = ["this is a test.\n", "\n", "\n", "this is **paragraph** numero dos."]
    expected = [
        "<h1>this is a test.\n</h1>",
        "<p>this is <b>paragraph</b> numero dos.</p>",
    ]
    test = SSJ.line_by_line(SSJ, input_line, "testtext.md")
    assert test[0] == expected
    assert is_title is True
```

if you expect the test to raise an exception you should specify that as follows:

```
def test_make_paragraphs_txt_missing_params_self():
    """
    Test paragraphs without a needed parameter
    should throw exception
    """
    with pytest.raises(Exception):
        {Test goes here}
```