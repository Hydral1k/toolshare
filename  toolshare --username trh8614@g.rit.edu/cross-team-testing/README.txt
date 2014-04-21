toolShare R2 (4/20/2014)

Team 1 'The D is Silent'


A simple Django web based service that runs on Python and HTML/CSS.
This tool centralizes tool use which users can register and share tool items
as well as check them out. Tool Share is meant to enable neighbors in a community to be able to share items of common use. 
The successful implementation should make it easy for anyone wanting to participate to register and be able to share or borrow items.

Test Liason: Tom Heissenberger - trh8614@rit.edu - 1(585)-764-8025

Contents of R2 Documents folder:
- README.txt
- TetsPlanTracker.xlsx
- R2 Requirements.docx
- R2 Test Plan Document.docx


Requirements:
- Django 1.6+
- Python 3.3+
- A brain and an IQ of above 80.
- Chrome, Firefox
- Open ports, internet connection.

Installation: 
- Extract SVN Repository to respective location on computer. 
- Navigate to directory through console and locate manage.py
- Run command: py manage.py runserver (Windows) python3 manage.py runserver (Linux, depending on enviroment variable names)
- TEST CASES (Fully Implemented): py manage.py test (Windows) python3 manage.py test
- Navigate to website using supported browser @ address http://localhost:8000/


Known Bugs:
None currently found after light debugging.
TBA


Missing Features:
- GUI not finalized
- Not actually 'hosted'. Only run 'virtually'. (R2 FINAL)
- Tool info not fully available (R2 FINAL)


How To:
Admin login page is located at http://localhost:8000/admin
You can change user settings here
Username: test
Password: test
(This will give you global access and power to make and modify changes.)