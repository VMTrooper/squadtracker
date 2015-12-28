Provisioning a new site
=======================
## Required packages:
* nginx
* Python 3
* Git
* pip
* virtualenv
e.g.,, on Ubuntu:
deploy_tools/provisioning_notes.md.
        sudo apt-get install nginx git python3 python3-pip
        sudo pip3 install virtualenv
    ## Nginx Virtual Host config
    * see nginx.template.conf
    * replace SITENAME with, e.g., staging.my-domain.com
    ## Upstart Job
    * see gunicorn-upstart.template.conf
    * replace SITENAME with, e.g., staging.my-domain.com
    ## Folder structure:
    Assume we have a user account at /home/username
    /home/username
    └── sites
        └── SITENAME
             ├── database
             ├── source
             ├── static
             └── virtualenv



pip3
pymongo
django==1.8.4
django-jenkins
selenium --upgrade
coverage
jinja2

test machine binary
chromedriver (https://sites.google.com/a/chromium.org/chromedriver/)
http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/2.20/chromedriver_mac32.zip

Jenkins Server
firefox (Debian iceweasel)
chrome
python3
jenkinsplugin-Violations
jenkinsplugin-Cobertura

Google Cloud instance
gcloud compute instances create squad01 \
--image-project ubuntu-os-cloud \
--image ubuntu-1404-trusty-v20151113 \
--machine-type f1-micro

http://vmtrooper.github.io/squadtracker/
