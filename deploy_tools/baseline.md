Baseline the Web Server
=======================
## Create Ubuntu instance in gCloud

	gcloud compute instances create squad01 \
	--image-project ubuntu-os-cloud \
	--image ubuntu-1404-trusty-v20151113 \
	--machine-type f1-micro

## Configure user

	root@server:$ useradd -m -s /bin/bash elspeth # add user named elspeth
NOTE: -m creates a home folder, -s sets elspeth to use bash by default

	root@server:$ usermod -a -G sudo elspeth # add elspeth to the sudoers group 

## Modify sudoers to let elspeth not use password.
	elspeth ALL=NOPASSWD: ALL

## Switch to elspeth
	root@server:$ su - elspeth # switch-user to being elspeth!

## Prepare Python3 on the server
	sudo apt-get -qqy install nginx git python3 python3-pip
	sudo pip3 install django==1.8.4
	sudo pip3 install virtualenv gunicorn django-jenkins

# Need to debug fabric for following:
- should check for and delete the default site not removed
```
sudo rm /etc/nginx/sites-enabled/default
```

# In the source directory, run the following commands...
```
# source the nginx site template and replace with the site name
$ sed "s/SITENAME/prod.squadtracker.io/g" \
deploy_tools/nginx.template.conf | sudo tee \
/etc/nginx/sites-available/prod.squadtracker.io

# create the ln for the sites-available directory under sites-enabled
$ sudo ln -s /etc/nginx/sites-available/prod.squadtracker.io \
/etc/nginx/sites-enabled/prod.squadtracker.io

# source the gunicorn upstart config template and replace with the site name
$ sed "s/SITENAME/prod.squadtracker.io/g" \
deploy_tools/gunicorn-upstart.template.conf | sudo tee \
/etc/init/gunicorn-prod.squadtracker.io.conf

# Reload nginx and start the web site service
$ sudo service nginx reload
$ sudo start gunicorn-prod.squadtracker.io
```