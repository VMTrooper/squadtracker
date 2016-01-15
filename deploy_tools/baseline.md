Baseline the Web Server
=======================
## Create Ubuntu instance in gCloud

gcloud compute instances create squad01 \
--image-project ubuntu-os-cloud \
--image ubuntu-1404-trusty-v20151113 \
--machine-type f1-micro

## Configure user

root@server:$ useradd -m -s /bin/bash elspeth # add user named elspeth
# -m creates a home folder, -s sets elspeth to use bash by default

root@server:$ usermod -a -G sudo elspeth # add elspeth to the sudoers group 
root@server:$ su - elspeth # switch-user to being elspeth!

# Modify sudoers to let elspeth not user password.

## Prepare Python3 on the server
sudo apt-get -qqy install nginx git python3 python3-pip
sudo pip3 install django==1.8.4
sudo pip3 install virtualenv gunicorn

# Need to debug fabric for following:
- sites-available and sites-enabled ln not created
- default site not removed