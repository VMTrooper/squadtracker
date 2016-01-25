Provisioning a new site
=======================
## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

#### /etc/nginx/sites-available/staging.squadtracker.io
    server {
        listen 80;
        server_name staging.squadtracker.io;
    
    * gunicorn will serve static content from the following directory.
    * run python3 manage.py collectstatic --noinput after configuring settings.py   accordingly for STATIC setting
        location /static {
            alias /home/elspeth/sites/staging.squadtracker.io/static;
        }
    
        location / {
    * proxy_set_header setting for ALLOWED_HOSTS to work.
    * Otherwise, need DEBUG=True or localhost added to ALLOWED_HOSTS
            proxy_set_header Host $host;
            proxy_pass http://unix:/tmp/staging.squadtracker.io.socket;
        }
    }

### Upstart Job

* see gunicorn-upstart.template.bak
* replace SITENAME with, e.g., staging.my-domain.com

### Folder structure:
Assume we have a user account at /home/username
```
/home/username
|__ sites
    |__ SITENAME
         |__ database
         |__ source
         |__ static
         |__ virtualenv
```

### Pip Packages for Test Server
pip3
* pymongo
* django==1.8.4
* django-jenkins
* selenium --upgrade
* coverage
* jinja2

### Selenium Chrome Driver
* chromedriver (https://sites.google.com/a/chromium.org/chromedriver/)
* http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip
* http://chromedriver.storage.googleapis.com/2.20/chromedriver_mac32.zip

### Jenkins Server
* firefox (Debian iceweasel)
* chrome
* python3
* jenkins plugin: Violations
* jenkins plugin: Cobertura

### Project Page
http://vmtrooper.github.io/squadtracker/
