# BlankfactorAutomation

## Project
The **BlankfactorAutomation** project was created to demonstrate the automation testing skills of Hernan Jose Malave Montero, who is interested in joining Blankfactor as a QA Automation Engineer.  

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
git clone https://github.com/hmalave17/BlankfactorAutomationProject.git

### 2. Navigate to project root
cd BlankfactorAutomation/BlankfactorAutomationPy (make sure you are located in the root of the BlankfactorAutomationPy folder)

### 3. Setup environment
python -m venv venv

### 4. Activate the environment
Git Bash (Windows): source venv/Scripts/activate <br>
Git Bash (macOS/Linux): source venv/bin/activate <br>
powershell: venv\Scripts\activate <br>

### 5. run dependencies
cd .. (make sure you are located in the root of the automation project)

### 6. run dependencies
pip install -r requirements.txt

### 7. Navigate to project root
cd BlankfactorAutomationPy (make sure you are located in the root of the BlankfactorAutomationPy folder)

### 8. Run the tests
-Git Bash:behave (run browser chromium by default) <br>
-PowerShell (Windows): $env:BROWSER="firefox"; $env:HEADLESS="true"; behave <br>

**Browser options**
-chrome runs with Chromium/Chrome (default)
-edge runs with Chromium/Edge
-firefox runs with Firefox
-webkit runs with WebKit (Safari engine)

**Reports:**
-After execution, HTML reports are generated under:
-blankfactorautomation/reports/report.html

**Note**:
-HEADLESS=false browser visible
-HEADLESS=true browser no visible



