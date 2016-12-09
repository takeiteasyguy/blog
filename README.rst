**Blog Project**


What should be implemented
==========================

Please, create a test python application.

The application should be a blog which allows user to create\edit\list and delete posts.

There should be three roles - anonymous, simple users and admin.

Requirements:

1. As an anon. user I want to see all published posts.

2. As an authorized user (logged in) I want to CRUD my posts.

3. As an admin I want to CRUD all posts.

Tech reqs:

- UI must be done using Twitter Bootstrap;

- Publish project to github and also provide an amount of spent time.

Used environment
================

- Windows 7
- Python 2.7
- PyCharm 2016.2.2

Deployment
==========

1. Download the project app from git repository

2. Create necessary virtualenv

3. Install project requirements using pip: pip install -r requirements.txt

4. Apply migrations using manage.py command: manage.py migrate

5. Collect staticfiles using manage.py command: manage.py collectstatic

6. Run server using manage.py command: manage.py runserver (I prefer to use PyCharm built-in debug mode to run server)

7. Enjoy =)

Some additional notes
=====================

- Database will be already filled with necessary users (applied in migrations) with credentials:

1. type: simple user; username: 'simple_user', password: '1234'
2. type: admin; username: 'admin'; password: '1234'

- It was decided not to use AJAX-based interface as it is more comprehensive than default Django forms behaviour

- There are no any permissions in backend views as it is protected by CSRF tokens, so in case if simple user doesn't have Edit permission on some post he will not see this in rendered template and won't be able to Edit this post. Anyway this could be replaced with Django REST framework and AJAX-requests, which is better scalable

- Time spent: development - 4h; project description and other appropriate updates - 2h

Please feel free to contact me via email (journalbeast@gmail.com) or via skype (aleksandr.adasenka)