# Math Generators
Math worksheets generators for addition and subtraction. Limited to 64 questions. 

Answers to subtraction questions and components to addition questions are single digit numbers 2 and above.

## Getting Started

### Prerequisites
os version: Windows 10 and above

Python 3.11.9 (April 2, 2024) - Should work with earlier/later versions too

### Downloading
Downloading [python](https://www.python.org/downloads/)

Downloading [pip](https://pip.pypa.io/en/stable/installation/)

```bash
py -m ensurepip --upgrade
```

Downloading [python-docx](https://python-docx.readthedocs.io/en/latest/user/install.html#install)

```bash
pip install python-docx
```

### Running Instructions
Run in terminal

```bash
python main.py
```

If python not found, try the following:

```bash
python3 main.py
```

or

Click "run python file" in main.py in VSCode

## Example
```python
import mathGenerators

#this modifies 2 seperate documents
mathGenerators.additionGenerator50(False, True)
mathGenerators.subtractionGenerator50(False, True)

#this modifies a single document
mathGenerators.subtractionGenerator20(True, True, 2)
mathGenerators.subtractionGenerator20(False, False)
```

## Author
Nut15

## Version History
0.1 - 7/07/2024

Initial Release

0.2 - 10/07

Improved generators

Write inside .docx instead of .txt

0.3 - 12/08

Placed all generators in mathGenerators, a single module

moved all .docx files to be changed to a single folder - printing documents

completed descriptions for functions and modules

added Example secion in README