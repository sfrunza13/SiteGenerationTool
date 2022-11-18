"""Tests for editing template"""
# This import is configured in toml
import pytest
from ssj import SSJ  # pylint: disable=import-error

def test_edit_template():
    """
    Test adding titles and paragraphs to template
    """
    input_paragraphs = [
        "<h1>This is the title</h1>",
        "<p>this is the first test paragraph</p>",
        "<p>this is the second test paragraph</p>",
        "<p>this is the third test paragraph</p>"
    ]

    SSJ.edit_template(SSJ, input_paragraphs, True)
    assert SSJ.template.find("<title>This is the title</title>")
    assert SSJ.template.find("<body><h1>This is the title</h1><p>this is the first test paragraph</p><p>this is the second test paragraph</p><p>this is the third test paragraph</p></body>")
