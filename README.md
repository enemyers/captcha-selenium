# Python version: 3.12.+

## Prepare environment:

### 1. Activate environment:
**In the root of the project type:**
####
- **Windows: (testing with git bash)**

> python -m venv .venv

> source .venv/Scripts/activate

 **Install via terminal:** 

> winget install "FFmpeg (Essentials Build)"

**Install DLL on /Windows/System32/**

https://www.dllme.com/dll/files/libomp140_x86_64/00637fe34a6043031c9ae4c6cf0a891d

---

- **Linux:**

 **Install via terminal:** 

> sudo apt install python3.12-venv xvfb ffmpeg **(Ubuntu 22.04+)**

> python3 -m venv .venv

> source .venv/bin/activate

---

- **macOS (homebrew)**

 **Install via terminal:** 

> brew install ffmpeg

> python3 -m venv .venv

> source .venv/bin/activate

### 2. Install pip dependencies:
####
> pip install -r requirements.txt

**if error with modules reinstall these packages:**

> pip install -r selenium Flask easyocr PocketSphinx pypasser

### pip packages:
 - Selenium 4.23.1 
 - Flask    3.0.3
 - easyocr  1.7.1 (https://github.com/JaidedAI/EasyOCR)
 - PyVirtualDisplay 3.0
 - PyPasser 0.0.5 (recaptchav2) (https://pypi.org/project/PyPasser/)

---

### To run project:
> python main.py


**NOTE:**

**ON WINDOWS AND MACOS NOT WORK BACKGROUND DISPLAY, SO YOU NEED COMMENT THIS:**

> #from pyvirtualdisplay import Display --> (/modules/papeleta.py) and (/modules/papeleta.py)

> #display = Display(visible=0, size=(800, 600)) --> (/modules/papeleta.py) and (/modules/papeleta.py)

> #display.start() (/modules/papeleta.py) and --> (/modules/papeleta.py)

> #display.stop() (/modules/papeleta.py) and --> (/modules/papeleta.py)

---

**Links to test the endpoints:**

> **GET:** http://localhost:5300/placa/{patente} EXAMPLE: AUH628

> **GET:** http://localhost:5300/papeleta/{patente} EXAMPLE: AUH628
