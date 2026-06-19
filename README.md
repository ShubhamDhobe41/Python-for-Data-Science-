# Python for Data Science — Learning Roadmap

A structured, self-paced guide to learning Python for data science, from fundamentals to deployment-ready skills.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Learning Path](#learning-path)

---

## Prerequisites

- Basic computer literacy (file systems, installing software)
- No prior programming experience required — this path starts from zero
- High school level math (algebra, basic statistics) — refreshed along the way

---

## Environment Setup

1. **Install Python** — Get the latest stable version from [python.org](https://www.python.org/downloads/)
2. **Install a code editor** — [VS Code](https://code.visualstudio.com/) (recommended) or [PyCharm](https://www.jetbrains.com/pycharm/)
3. **Install Jupyter Notebook / JupyterLab** — for interactive data exploration
   ```bash
   pip install jupyterlab
   ```
4. **Set up a virtual environment** — keeps project dependencies isolated
   ```bash
   python -m venv ds-env
   # Windows
   ds-env\Scripts\activate
   # Mac/Linux
   source ds-env/bin/activate
   ```
5. **Install core data science libraries**
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn jupyterlab
   ```

> 💡 Alternative: Use [Anaconda](https://www.anaconda.com/download) — bundles Python + most data science libraries + Jupyter in one installer. Great for beginners who want fewer setup steps.

---

## Learning Path

### Stage 1: Python Fundamentals (1–3 weeks)
- Day 1:  Variables, data types, type conversion
- Day 2:  Operators and expressions
- Day 3:  Conditionals (`if`, `elif`, `else`)
          Loops (`for`, `while`)
          String manipulation and formatting (f-strings)
- Day 4 : List and List Operations
- Day 5 : tuples, dictionaries, sets
- [ ] Functions, arguments, return values
- [ ] Error handling (`try`/`except`)
- [ ] File I/O (reading/writing `.txt`, `.csv`)
- [ ] List/dict comprehensions

### Stage 2: Intermediate Python (1–2 weeks)
- [ ] Object-Oriented Programming (classes, objects, inheritance)
- [ ] Modules and packages
- [ ] Lambda functions, `map()`, `filter()`, `reduce()`
- [ ] Working with `datetime`
- [ ] Regular expressions (`re` module)
- [ ] Virtual environments and `pip`
- [ ] Reading documentation effectively
---

## Recommended Resources

**Free**
- [Python Official Docs](https://docs.python.org/3/)
- [freeCodeCamp – Data Analysis with Python](https://www.freecodecamp.org/)
- [campusx - Python with Data Science](https://learnwith.campusx.in/)

## Progress Tracker

| Stage | Topic | Status |
|-------|-------|--------|
| 1 | Python Fundamentals | ⬜ Started |
| 2 | Intermediate Python | ⬜ Not Started |
| 3 | NumPy | ⬜ Not Started |
| 4 | Pandas | ⬜ Not Started |
| 5 | Data Visualization | ⬜ Not Started |
| 6 | Statistics & Probability | ⬜ Not Started |
| 7 | Data Cleaning & EDA | ⬜ Not Started |
| 8 | Machine Learning (scikit-learn) | ⬜ Not Started |
| 9 | Portfolio & Projects | ⬜ Not Started |

> Update this table as you go: ⬜ Not Started → 🟨 In Progress → ✅ Complete

*Happy learning! Consistency beats intensity — even 30 focused minutes a day will get you there.*
