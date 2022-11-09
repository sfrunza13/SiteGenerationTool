"""Tests for creating paragraphs array"""
# This import is configured in toml
import pytest
from ssj import SSJ  # pylint: disable=import-error


def test_make_paragraphs_md():
    """Test creating paragraphs collection with markdown conversion"""
    input_line = [
        "Silver Blaze\n",
        "\n",
        "\n",
        "*I* *am* **afraid**, *Watson*, **that** I shall have to go,” `said Holmes`, ```as we```\n",
        "__sat__ _down_ *together* *to* **our** __breakfast__ one **morning__.\n",
        "\n",
        "“Go! Where to?”\n",
        "\n",
        "---“To Dartmoor; to King’s Pyland.”",
    ]
    expected = [
        "<h1>Silver Blaze\n</h1>",
        "<p><i>I</i> <i>am</i> <b>afraid</b>, <i>Watson</i>, <b>that</b> I shall have to go,” <code>said Holmes</code>, <code>as we</code>\n</p>",
        "<b>sat</b> <i>down</i> <i>together</i> <i>to</i> <b>our</b> <b>breakfast</b> one **morning__.\n",
        "</p><p>",
        "“Go! Where to?”\n",
        "</p><p>",
        "<hr>“To Dartmoor; to King’s Pyland.”",
    ]

    test = SSJ.line_by_line(SSJ, input_line, "Silver Blaze Test.md")
    assert test[0] == expected


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


def test_make_paragraphs_md_without_header():
    """Test paragraphs without title/header"""

    input_line = ["this is a test.\n", "\n", "this is **paragraph** numero dos."]
    expected = [
        "<p>this is a test.\n</p>",
        "<p>this is <b>paragraph</b> numero dos.</p>",
    ]
    test = SSJ.line_by_line(SSJ, input_line, "testtext2.md")
    assert test[0] == expected
    assert test[1] is False


def test_make_paragraphs_txt_w_h1():
    """Test paragraphs while identifying title/header without md support"""
    input_line = ["this is a test.\n", "\n", "\n", "this is **paragraph** numero dos."]
    expected = [
        "<h1>this is a test.\n</h1>",
        "<p>this is **paragraph** numero dos.</p>",
    ]
    test = SSJ.line_by_line(SSJ, input_line, "testtext.txt")
    assert test[0] == expected
    assert test[1] is True


def test_make_paragraphs_txt_without_header():
    """Test paragraphs without title/header without md support"""
    input_line = ["this is a test.\n", "\n", "this is **paragraph** numero dos."]
    expected = [
        "<p>this is a test.\n</p>",
        "<p>this is **paragraph** numero dos.</p>",
    ]
    test = SSJ.line_by_line(SSJ, input_line, "testtext2.txt")
    assert test[0] == expected
    assert test[1] is False


def test_make_paragraphs_txt_missing_params_self():
    """
    Test paragraphs without a needed parameter
    should throw exception
    """
    with pytest.raises(Exception):
        input_line = ["this is a test.\n", "\n", "this is **paragraph** numero dos."]
        SSJ.line_by_line(input_line, "testtext2.txt")


def test_make_paragraphs_txt_missing_params_input():
    """
    Test paragraphs without a needed parameter
    should throw exception
    """
    with pytest.raises(Exception):
        SSJ.line_by_line(SSJ, "testtext2.txt")


def test_make_paragraphs_txt_empty_input():
    """
    Test paragraphs with empty input
    """
    test = SSJ.line_by_line(SSJ, "", "testtext2.txt")
    assert test[0] == []
