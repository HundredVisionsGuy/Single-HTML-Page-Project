"""
Test CSS.
"""
from file_clerk import clerk
import pytest
from webcode_tk import css_tools as css
from webcode_tk import html_tools as html


project_path = "single_html_page/"

# Get all styles (sheets and tags by file)
css_styles_by_html_files = []
html_files = html.get_all_html_files(project_path)
for file in html_files:
    file_data = []
    # get all link and style tags
    head_tags = html.get_elements("head", file)
    for item in head_tags:
        for tag in item.contents:
            if tag == "\n":
                continue
            if tag.name == 'link':
                href = tag.attrs.get("href")
                if ".css" in href:
                    if "http" not in href[:5]:
                        sheet_path = project_path + href
                        code = clerk.file_to_string(sheet_path)
                        css_sheet = css.Stylesheet(sheet_path, code)
                        file_data.append(css_sheet)
            if tag.name == 'style':
                css_sheet = css.Stylesheet(file, tag.text, "styletag")
                file_data.append(css_sheet)
    css_styles_by_html_files.append({"file": file, "stylesheets": file_data})
print(css_styles_by_html_files)


@pytest.fixture
def html_style_tags():
    html_files = html.get_all_html_files(project_path)
    css_tags = []
    for file in html_files:
        style_tags = html.get_elements('style', file)
        for tag in style_tags:
            stylesheet = css.Stylesheet(file, tag.text, "style_tag")
            css_tags.append(stylesheet)
    return css_tags


@pytest.fixture
def all_stylesheets(html_style_tags):
    stylesheets = html_style_tags
    css_files = clerk.get_all_files_of_type(project_path, "css")
    for file in css_files:
        code = clerk.file_to_string(file)
        sheet = css.Stylesheet(file, code)
        stylesheets.append(sheet)
    return stylesheets


def test_css_for_font_pairing(all_stylesheets):
    font_family_data = []
    for sheet in all_stylesheets:
        # Do something with tag
        sheet_family_data = css.get_font_families(sheet)
        for sheet_data in sheet_family_data:
            selector = sheet_data.get("selector")
            if sheet_family_data and not font_family_data:
                font_family_data += sheet_family_data
            elif sheet_family_data:
                selectors = []
                for item in sheet_family_data:
                    print(item)
                    


    meets = (
        len(font_family_data) == 2 and
        font_family)
    assert len(font_family_data) == 2


# @pytest.fixture
# def global_color_details(css_files):
#     return css_files
