"""
Test CSS.
"""
import pytest
from webcode_tk import css_tools as css
from webcode_tk import color_tools
from webcode_tk import html_tools as html


project_path = "single_html_page/"
html_files = html.get_all_html_files(project_path)
styles_by_html_files = css.get_styles_by_html_files(project_path)
global_color_rules = css.get_global_colors(project_path)

global_color_contrast_tests = []
for file in html_files:
    goal = "Normal AAA"
    rule = global_color_rules.get(file)
    global_color_contrast_tests.append((file, rule, goal, True))


def get_unique_font_families(project_folder):
    font_rules = css.get_unique_font_rules(project_folder)
    font_families_tests = []
    for file in font_rules:
        # apply the file, unique rules, unique selectors, and unique values
        filename = file.get("file")
        unique_rules = file.get("rules")
        passes_rules = len(unique_rules) >= 2
        passes_selectors = passes_rules
        unique_values = []
        for rule in unique_rules:
            value = rule.get("family")
            if value not in unique_values:
                unique_values.append(value)
        passes_values = len(unique_values) == 2
        font_families_tests.append((filename, passes_rules, passes_selectors,
                                    passes_values))
    return font_families_tests


def get_font_rules_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append(test[:2])
    return rules_data


def get_font_selector_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append((test[0],test[2]))
    return rules_data


def get_font_family_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append((test[0],test[3]))
    return rules_data


font_families_tests = get_unique_font_families(project_path)
font_rules_results = get_font_rules_data(font_families_tests)
font_selector_results = get_font_selector_data(font_families_tests)
font_family_results = get_font_family_data(font_families_tests)


@pytest.mark.parametrize("file,rule,goal,expected",
                         global_color_contrast_tests)
def test_files_for_global_color_contrast(file, rule, goal, expected):
    bg_color = rule.get("background-color")
    bg_color = color_tools.get_hex(bg_color)
    color = rule.get("color")
    color = color_tools.get_hex(color)
    result = color_tools.passes_color_contrast(goal, bg_color, color)
    assert result == expected


@pytest.mark.parametrize("file,passes_rules", font_selector_results)
def test_files_for_enough_font_rules(file, passes_rules):
    assert passes_rules


@pytest.mark.parametrize("file,passes_selector", font_selector_results)
def test_files_for_for_enough_font_selectors(file, passes_selector):
    assert passes_selector


@pytest.mark.parametrize("file,passes_font_families", font_selector_results)
def test_files_for_2_font_families_max(file, passes_font_families):
    assert passes_font_families
