# Balita Blog


A blog system based on `python3.10` and `Django4`.




## Main Features:
- Articles, Pages, Categories, Tags(Add, Delete, Edit), edc. Articles and pages support `Markdown` and highlighting.
- Articles support full-text search.
- Complete comment feature, include posting reply comment and email notification. `Markdown` supporting.
- Sidebar feature: new articles, most readings, tags, etc.
- OAuth Login supported, including Google, GitHub, Facebook, Weibo, QQ.
- `Memcache` supported, with cache auto refresh.
- Simple SEO Features, notify Google and Baidu when there was a new article or other things.
- Simple picture bed feature integrated.
- `django-compressor` integrated, auto-compressed `css`, `js`.
- Website exception email notification. When there is an unhandle exception, system will send an email notification.
- Wechat official account feature integrated. Now, you can use wechat official account to manage your VPS.

## Installation:
### Linux and MacOS
Create virtual environment(venv):    
```bash
python3 -m venv venv
```

Activate venv:  
```bash
source venv/bin/activate
```

Install requirements for running project via pip: 
```bash
pip3 install -r requirements.txt
```

### Windows

Create virtual environment(venv):   
```bash
python -m venv venv
```

Activate venv:  
```bash
venv\Scripts\activate
```

Install via pip: 
```bash
pip install -r requirements.txt
```
### Create DataBase
```bash
python manage.py makemigrations
python manage.py migrate
```  

### Create super user

Run command in terminal:
```bash
python manage.py createsuperuser
```

[//]: # ()
[//]: # (### Collect static files)

[//]: # (Run command in terminal:)

[//]: # (```bash)

[//]: # (python manage.py collectstatic --noinput)

[//]: # (python manage.py compress --force)

[//]: # (```)




### Getting start to run server
Execute: 
```bash
python manage.py runserver
```

Open up a browser and visit: http://127.0.0.1:8000/ , the you will see the blog.



## About the issues

If you have any *question*, please use Issue or send problem descriptions to my email `odiljonabduvaitov@gmail.com`. I will reponse you as soon as possible. And, we recommend you to use Issue.

