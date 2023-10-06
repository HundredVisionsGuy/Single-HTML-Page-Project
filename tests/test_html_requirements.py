"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_elements = [("doctype", 1),
                     ("html", 1),
                     ("head", 1),
                     ("title", 1),
                     ("h1", 1),
                     ("p", 2)]


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("single_html_page/", "html")
    return files


@pytest.mark.parametrize("element,num", required_elements)
def test_files_for_required_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        actual = html.get_num_elements_in_file(element, file)
        assert actual >= num


def test_for_presence_of_html_files(files):
    assert len(files) > 0
