DJANGO BOOTSTRAP SITE

A multi-page website built by converting the "Personal" Bootstrap 5 template by Start Bootstrap into a fully working Django project. It uses Django's static files system, named URL routes and view functions to serve each page.

Peer Group Assignment
Submission deadline: Monday, 9 November 2026


TEMPLATE USED

Name: Personal
Author: Start Bootstrap (https://startbootstrap.com/template/personal)
License: MIT (the original copyright notice is kept in the template files)


PAGES

Home      /           templates/index.html
Resume    /resume/    templates/resume.html
Projects  /projects/  templates/projects.html
Contact   /contact/   templates/contact.html


WHAT WAS DONE

- Created the Django project (django_bootstrap_site) and the pages app
- Moved the template's CSS, JavaScript and images into the static folder
- Configured STATICFILES_DIRS and TEMPLATES in settings.py
- Replaced hardcoded asset paths with the {% static %} tag
- Replaced page links with the {% url %} tag
- Added a view and a URL route for each page
- [Add more as you build: base.html layout, contact form saved to the database, admin setup, customised content]


TECH STACK

- Python 3
- Django 6.1
- Bootstrap 5 (via the Start Bootstrap template)
- SQLite (default Django database)


PROJECT STRUCTURE

django-bootstrap-site/
  django_bootstrap_site/   Project settings and main URL config
  pages/                   App with views and URL routes
  static/                  CSS, JS and images (assets, css, js)
  templates/               HTML templates
  manage.py
  requirements.txt
  README.md


HOW TO RUN THE PROJECT

1. Clone the repository
   git clone https://github.com/noahchep/django-bootstrap-site.git
   cd django-bootstrap-site

2. Create and activate a virtual environment
   Windows:
   python -m venv .venv
   .venv\Scripts\activate

   macOS / Linux:
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Apply migrations
   python manage.py migrate

5. Start the development server
   python manage.py runserver

6. Open http://127.0.0.1:8000/ in your browser

7. Optional: create an admin user
   python manage.py createsuperuser
   Then visit http://127.0.0.1:8000/admin/


TEAM MEMBERS

1. [Your name] - GitHub: noahchep - Project setup, repository, static files, views and URLs
2. [Member 2] - GitHub: [username] - [Contribution]
3. [Member 3] - GitHub: [username] - [Contribution]
4. [Member 4] - GitHub: [username] - [Contribution]


GIT WORKFLOW

1. Pull the latest changes: git pull origin main
2. Create your own branch: git checkout -b feature/your-feature
3. Commit your work with clear messages
4. Push your branch and open a Pull Request on GitHub
5. The group lead reviews and merges


CREDITS

- Template: Personal by Start Bootstrap (https://startbootstrap.com), MIT License
- Built with Django (https://www.djangoproject.com/) and Bootstrap (https://getbootstrap.com/)
