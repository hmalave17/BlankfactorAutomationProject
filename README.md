# BlankfactorAutomation

## Project
The **BlankfactorAutomation** project was created to demonstrate the automation testing skills of **Hernan Jose Malave Montero**, who is interested in joining Blankfactor as a QA Automation Engineer.  

## Characteristics
This project has the following key features:  
- **Programming Language:** Python  
- **Automation Frameworks:** Behave (BDD) + Playwright  
- **Design Pattern:** Page Object Model (POM)  
- **Reporting:** HTML report generated with `behave-html-formatter`  
- **Cross-Browser Support:** Chromium, Firefox, WebKit, Edge  
- **Execution:** Compatible with Windows and macOS

## Project Structure

blankfactorautomation/<br> 
│── config/ <br> 
│── features/ <br> 
│      │── steps/ <br> 
│── pages/ <br> 
│── reports/ <br> 
│── venv/ <br> 
│── .env <br> 
│── behave.ini <br>  
Manual_Test/<br>
.gitignore<br>
requirements.txt


---

## File List
- **retirement_and_wealth_section.feature** → Contains the BDD (Behavior-Driven Development) scenarios written in Gherkin.  
- **contact_page.py, home_page.py, retirement_and_wealth_page.py** → Page Object Model classes where locators and methods are defined.  
- **retirement_and_wealth_steps.py** → Step definitions mapping Gherkin steps to executable Playwright code.  
- **environment.py** → Global hooks (before/after execution). Handles browser setup and teardown.  
- **constants.py** → Centralized constants such as `BASE_URL`, expected texts, and supported browsers.  
- **behave.ini** → Behave configuration file, including formatter setup for HTML reports.  
- **.env** → Stores environment variables such as `BROWSER`, `HEADLESS`, and `BASE_URL`.  

---

## Execution

### 1. Clone the repository
```bash
git clone https://github.com/hmalave17/BlankfactorAutomation.git <br>

### 2. Navigate to project root
cd BlankfactorAutomation/BlankfactorAutomationPy (**make sure you are located in the root of the automation project**) <br>

### 3. Setup environment
python -m venv venv
source venv/bin/activate   (**this options is to macOS/Linux**)
venv\Scripts\activate   (**this options is toWindows PowerShell**)   
pip install -r requirements.txt

### 4. Run the tests
Using .env configuration (default browser defined in .env file): <br>

- **Git Bash:**behave
- **PowerShell (Windows):** $env:BROWSER="firefox"; $env:HEADLESS="true"; behave


**Browser options**<br>
- **chrome** runs with Chromium/Chrome (default)<br>
- **edge** runs with Chromium/Edge<br>
- **firefox** runs with Firefox<br>
- **webkit** runs with WebKit (Safari engine)<br>

**Reports:**
- **After execution, HTML reports are generated under:<br>
- **blankfactorautomation/reports/report.html

**Note:**
- **HEADLESS=false** browser visible<br>
- **HEADLESS=true** browser no visible



