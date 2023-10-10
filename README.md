# Single-HTML-Page-Project
Students will design a single web page project that matches their project plan that they submitted in class.

## Project Requirements
Are listed in the README file in the `single_html_page` folder.
You must meet all requirements in the following areas:
* HTML - meet specific elements
* Validity - passes the W3C Validator (HTML and CSS)
* CSS - meet specific CSS requirements (colors & fonts)
* UX - Meet readability requirements.

## Instructions
1. Place all of your project files (HTML, CSS, images, etc.) into the simple_html_page folder.
2. Clone this project: `git clone `.
3. Open the projec tin VS Code (double click on `simple-html-page-test.code-workspace`)
4. Open the terminal (View > New Terminal).
5. Install the Python extension: ***Python extension for Visual Studio Code***
6. In the terminal, type `poetry shell`.
    - You should see a line saying something like `Spawning shell within C:\Users\my_username\AppData\Local\pypoetry\Cache\virtualenvs\simple-html-page-IMtvp_MA-py3.9`
7. Note the name of your virtual environment file, which will look something like `simple-html-page-IMtvp_MA-py3.9`
8. Open the Command Palette 
    - in the menu it's: View > Command Palette
    - you could also type `Ctrl + Shift + P`
9. Type Python: Select Interpreter
    - if you see the virtual environment file, click it.
    - if you don't see it, click `Select at Workspace level`
10. Select the virtual environment file from above (it should show the word Poetry in blue on the right)
    - if you don't see it, close VS Code and re-open it and repeat steps 8 and 9.
11. Type `poetry update` and wait for everything to install.
12. In the terminal, once everything is done installing, type `pytest`
13. If that doesn't work, click the Testing icon (looks like a beaker), then click the blue `Configure Python Tests` button, then select `pytest pytest framework` and choose the `tests` folder
