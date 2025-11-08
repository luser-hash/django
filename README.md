📝 Django To-Do App
------------------------
A simple To-Do web application built with Django.
This project was created as a learning exercise to understand Django’s MVC (Model-View-Template) structure and perform basic CRUD operations — Create, Read, Update, and Delete.

🚀 Features
------------------------
✏️ Create new tasks with title, description, and optional due date
👀 Read and view all tasks in a clean, minimal UI
🔄 Update task details or mark tasks as done
❌ Delete tasks safely
⏰ Track due dates and creation times
⚡ Instant status toggle for marking tasks as completed
🎨 Responsive and modern design built with pure HTML & CSS

🧰 Technologies Used
-------------------------
Python 3.13
Django 5.2
SQLite3 (default Django database)
HTML5, CSS3

🖥️ How to Run Locally
-------------------------
1. Clone the repository

git clone https://github.com/luser-hash/django.git
cd django-todo-app

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate       # On Mac/Linux
venv\Scripts\activate          # On Windows

3. Install dependencies

pip install django


4. Run migrations

python manage.py makemigrations
python manage.py migrate

5. Start the development server

python manage.py runserver

6. Open in browser

http://127.0.0.1:8000/

🌟 Future Improvements
----------------------------
User authentication (login/signup)
Priority levels or categories
Ajax-based toggling (no page reload)
Dark mode

