# 🌐 Django Website Setup Guide

This guide explains step-by-step how to design and run a simple website using **Django**.  
Follow the commands carefully to set up your project.  

---

## 📂 1. Create Project Folder
```bash
mkdir myproject
cd myproject
```

---

## 🛠️ 2. Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

---

## 📦 3. Install Django
```bash
pip install django
```

Check installation:
```bash
django-admin --version
```

---

## 🚀 4. Create Django Project
```bash
django-admin startproject mysite
cd mysite
```

Project structure:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

---

## 🧩 5. Create Django App
```bash
python manage.py startapp home
```

App structure:
```
home/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

---

## 🎨 6. Add Templates
Inside your app (`home/`), create:
```
home/templates/home/index.html
```

Example `index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Website</title>
</head>
<body>
    <h1>Welcome to My Django Website 🚀</h1>
</body>
</html>
```

---

## 🖼️ 7. Add Static Files
Inside your app (`home/`), create:
```
home/static/home/style.css
```

Example `style.css`:
```css
body {
    background-color: #f4f4f4;
    text-align: center;
    font-family: Arial, sans-serif;
}
```

Update `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "home" / "static"]
```

---

## 📁 8. Add Media Files (For User Uploads)
In project root (`mysite/settings.py`):
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"
```

Update `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🔗 9. Connect App in `settings.py`
Add app name inside `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'home',
]
```

---

## 📝 10. Create `urls.py` in App
Inside `home/` create a new file `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Update `views.py`:
```python
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')
```

---

## ▶️ 11. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🏃 12. Run Development Server
```bash
python manage.py runserver
```

Open browser:  
👉 http://127.0.0.1:8000

---

## 🌳 13. Final Folder Structure
```
myproject/
│── venv/
│── mysite/
│   │── mysite/
│   │   │── settings.py
│   │   │── urls.py
│   │   │── asgi.py
│   │   │── wsgi.py
│   │   │── __init__.py
│   │── home/
│   │   │── templates/
│   │   │   │── home/
│   │   │   │   │── index.html
│   │   │── static/
│   │   │   │── home/
│   │   │   │   │── style.css
│   │   │── views.py
│   │   │── urls.py
│   │   │── models.py
│   │   │── admin.py
│   │   │── apps.py
│   │   │── tests.py
│   │── manage.py
│── media/
```

---

## 📸 14. Add Image in README
To show project screenshot in README:

```markdown
![Demo Screenshot](static/Screenshot%202025-09-09%20160638.png)
```

> Save your screenshot as `static/demo.png` inside the project and GitHub will display it.

---

## ✅ Summary
You have successfully:
1. Created Django project & app  
2. Added templates, static & media files  
3. Connected URLs & views  
4. Ran the Django server  

Now your **Django Website is Live** 🚀
