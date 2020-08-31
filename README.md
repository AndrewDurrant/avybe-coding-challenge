**AVYBE CODING CHALLENGE**

__Instructions:__
For the coding challenge, please make a website using Django, where the user can showcase her profile. So the user will be able to add and edit:
- a profile picture
- a nickname

You don't need to worry about aesthetics, just try to get the functionality done. You will most likely have to use Django forms, which will update the database automatically. Feel free to ask for any clarification or guidance if you're stuck – I can help with that. You can also use google, stack overflow, and the Django documentation for help.


**Initial Setup for Django Project**
1. Create a new virtual environment - `python3 -m venv ~/.virtualenvs/<virtual_env_name>`
   - it's a good idea to keep all virtual environments in one place, ex. ./virtualenvs/ in home directory. The path is where the new environment will be saved
2. Activate your virtual environment - `source ~/.virtualenvs/<virtual_env_name>/bin/activate`
   - if source doesn't work, try using a dot instead `. ~/.virtualenvs/djangodev/bin/activate`
3. After you've created and activated a virtual environment, install Django `python -m pip install Django`
4. cd into a directory where you'd like to store your code, run command `django-admin startproject <project_name>`
   - this creates a <project_name> directory in your current directory
5. `git init`
6. Start the server `python manage.py runserver`
7. Create `.env` file and move SECRET_KEY from `settings.py`
8. Install package to handle .env file `pip install -U python-dotenv`; import to manage.py, wsgi.py and settings.py
9. Creating a new app: 
  `django-admin startapp <app_name>`
  - Make sure to add it to settings!

10. Setting Up PostgreSQL:  
  `pip install psycopg2 and/or psycopg2-binary`
  - Update databases in settings.py
  - Only psycopg2-binary works for me and it has not been an issue as of yet...

11. Create database

__migrate table data__  
`python manage.py migrate`