# Python version: 3.12.4

---

## > Prepare environment:

### 1. Activate environment:
**in the root of the project type:**
####
- **Windows: (testing with git bash)**
> source .venv/Scripts/activate

- **macos/Linux:** 
> source .venv/bin/activate

### 2. Install pip dependencies:
####
> pip install -r requirements.txt

### pip packages:
 - Selenium 4.23.1 
 - Flask    3.0.3
 - easyocr  1.7.1

---

**If you need another package:**

install with pip and delete requirements.txt
- rebuild requirements.txt with:
####
> pip freeze > requirements.txt

- To run:
> python main.py

**Link to test with postamn or another form:**
> **GET** http://127.0.0.1:5300/placa/AUH628
