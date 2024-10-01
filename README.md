<h1>Project Architecture</h1>

Setting Up Your Machine
-------------------------
Required installations:
-----------------------

*	Selenium: is a popular automation tool that allows developers to programmatically interact with and test web applications by controlling web browsers. It provides a powerful framework to simulate user actions, such as clicks and form submissions, across different browsers like Chrome, Firefox, and Edge.
*	Python 3: The programming language used in the tests.
*   Allure Report: is a flexible, lightweight tool for generating visual, informative reports from test results. It integrates with popular testing frameworks to provide detailed insights, including step-by-step execution logs, screenshots, and metadata, making it easier to analyze and improve software testing outcomes

Setting Up the Test Automation Environment
------------------------------------------------------------

To perform your automation, it is necessary to install some resources, as described below:

Windows
--------

<h3>1. Installing the Python 3</h3>

*	Download from: <https://www.python.org/downloads/>.
*	Run the downloaded file and follow the instructions by clicking ‘next’.
* 	Select the 3 displayed checkboxes and continue clicking ‘next’ until ‘finish’.
*	In the prompt Console, type the command `python --version`; if the installation is correct, the installed version will appear.

<h3>2. Installing the dependencies</h3>

*	After installing Python, within terminal type: 
`bash
pip install selenium pytest allure-pytest webdriver-manager
`

<h3>3. Installing the Allure Report</h3>

*	Open the Windows PowerShell and type: 
`bash
irm get.scoop.sh | iex
`
*	In the prompt Console, type the command `allure --version`; if the installation is correct, the installed version will appear.
If you had any problem during installation, follow this documentation: <https://github.com/ScoopInstaller/Install#readme>

And that's it, your environment is set up.

Executing Automated Tests
-----------------------------------

To execute the automated tests, we will use some commands from the root folder of our project.

*	To execute all implemented scenarios, we use the following code:
`bash
pytest test_google.py --alluredir=allure-results
`

*	To generate and serve the Allure report, you can go to the project folder and execute:
`bash
allure serve allure-results
`

Just open it in your browser to view the results.