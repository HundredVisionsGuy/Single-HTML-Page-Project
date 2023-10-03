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


@pytest.mark.parametrize("file,rule,goal,expected",
                         global_color_contrast_tests)
def test_files_for_global_color_contrast(file, rule, goal, expected):
    bg_color = rule.get("background-color")
    bg_color = color_tools.get_hex(bg_color)
    color = rule.get("color")
    color = color_tools.get_hex(color)
    result = color_tools.passes_color_contrast(goal, bg_color, color)
    assert result == expected
