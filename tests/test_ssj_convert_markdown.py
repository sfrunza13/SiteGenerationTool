"""SSJ module tests for convert markdown"""
# This import is configured in toml
import pytest
from ssj import SSJ  # pylint: disable=import-error

## All tests that have to do with markdown conversion method
def test_convert_markdown():
    """
    Check to see markdown conversion works
    Currently tests hr, b, i, and code using
    ---, ** or __ , * or _ and ``` or ` respectively
    """
    test = SSJ.convert_markdown(
        SSJ,
        """---Lovely night we have here. **This sho
                                uld be bold** *I will italicize this*""",
    )
    test2 = SSJ.convert_markdown(
        SSJ,
        """```Lovely night``` we `have` here. __This sho
                                uld be bold__ _I will italicize this_""",
    )
    assert (
        test
        == """<hr>Lovely night we have here. <b>This sho
                                uld be bold</b> <i>I will italicize this</i>"""
    )
    assert (
        test2
        == """<code>Lovely night</code> we <code>have</code> here. <b>This sho
                                uld be bold</b> <i>I will italicize this</i>"""
    )


def test_convert_markdown_empty():
    """
    Check to see what happens with empty string
    """
    test = SSJ.convert_markdown(
        SSJ,
        """""",
    )
    assert test == ""


def test_convert_markdown_number():
    """
    Check to see what happens with number
    """
    with pytest.raises(Exception):
        test = SSJ.convert_markdown(
            SSJ,
            3,
        )


def test_convert_markdown_null():
    """
    Check to see what happens with null
    """
    with pytest.raises(Exception):
        test = SSJ.convert_markdown(
            SSJ,
            None,
        )
