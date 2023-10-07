"""
Test UX (User eXperience) for readability metrics.
"""
from file_clerk import clerk
import pytest
from webcode_tk import ux_tools

# goals
min_reading_level = 7
max_reading_level = 11
max_words_per_sentence = 20
max_sentences_per_paragraph = 5
html_files = clerk.get_all_files_of_type("single_html_page/", "html")
grade_level_expectations = []
file_stats = []
for file in html_files:
    level = ux_tools.get_flesch_kincaid_grade_level(file)
    grade_level_expectations.append((file, level, min_reading_level,
                                     max_reading_level))
    stats = ux_tools.get_readability_stats(file, ["p", "div"])
    stats["file"] = file
    file_stats.append(stats)


@pytest.mark.parametrize("file,actual,min,max", grade_level_expectations)
def test_files_for_readability_grade_level(file, actual, min, max):
    assert actual > min and actual < max
