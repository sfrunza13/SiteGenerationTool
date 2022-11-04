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