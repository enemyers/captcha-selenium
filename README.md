# Python version: 3.12.+

---

## > Prepare environment:

### 1. Activate environment:
**In the root of the project type:**
####
- **Windows: (testing with git bash)**


> python3 -m venv .venv

> source .venv/Scripts/activate

- **Linux:**
> sudo apt install python3.12-venv xvfb ffmpeg **(Ubuntu)**

> python3 -m venv .venv

> source .venv/bin/activate

### 2. Install pip dependencies:
####
> python3 -m pip freeze > requirements.txt

### pip packages:
 - Selenium 4.23.1 
 - Flask    3.0.3
 - easyocr  1.7.1 (https://github.com/JaidedAI/EasyOCR)
 - PyVirtualDisplay 3.0
 - PyPasser 0.0.5 (recaptchav2) (https://pypi.org/project/PyPasser/)

---

**If you need another package:**

**Install with pip and delete requirements.txt**
- rebuild requirements.txt with:
####
> pip freeze > requirements.txt

- To run:
> python main.py

**Link to test endpoints:**

> **GET:** http://127.0.0.1:5300/placa/{patente} EXAMPLE: AUH628

> **GET:** http://127.0.0.1:5300/papeleta/{patente} EXAMPLE: AUH628
