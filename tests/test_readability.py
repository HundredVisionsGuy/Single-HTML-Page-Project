"""
Test UX (User eXperience) for readability metrics.
"""
from file_clerk import clerk
import pytest
from webcode_tk import ux_tools

@pytest.fixture
def reading_level_goals():
    goals = [("Min", 7),
             ("Max", 11)]
    return goals


@pytest.fixture
def html_files():
    files = clerk.get_all_files_of_type("single_html_page/", "html")
    return files


@pytest.mark.parametrize("files",html_files)
def test_files_for_readability_grade_level(reading_level_goals):
    for file in html_files:
        print("Nothing to see here...yet.")
