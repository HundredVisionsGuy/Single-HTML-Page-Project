"""
Test for HTML and CSS validity
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html
from webcode_tk import validator_tools as validator


html_results = []
html_files = clerk.get_all_files_of_type("single_html_page/", "html")
for file in html_files:
    report = validator.get_markup_validity(file)
    expected = f"{file}: No Errors Found."
    if not report:
        result = expected
        html_results.append((result, expected))
    else:
        for error in report:
            error_message = error.get("message")
            result = f"{file}: {error_message}"
            html_results.append((result, expected))


css_results = []
# css_files = clerk.get_all_files_of_type("single_html_page/", "css")
for file in html_files:
    validator_results = validator.get_markup_validity(file)
    expected = f"{file}: No Errors Found."
    for error in validator_results:
        error_message = error.get("message")
        if "CSS" in error_message:
            result = f"{file}: {error_message}"
            css_results.append((result, expected))
        else:
            continue


@pytest.mark.parametrize("result,expected", html_results)
def test_html_validity(result, expected):
    assert result == expected


@pytest.mark.parametrize("result,expected", css_results)
def test_css_validity(result, expected):
    assert result == expected
