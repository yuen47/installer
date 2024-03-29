#!/bin/sh

# regular updates
echo 'updating system...'
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt install python python-dev python3 python3-dev -y

# python pip
echo 'installing python pip and packages...'
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo apt-get install mysql-client -y
sudo apt-get install mysql-server -y
sudo apt-get install python-mysqldb -y

# install the iems_newsbot SQL database and table
cat <<EOF > install.sql
/* SQL database setup - can be done through the mysql client in shell */
DROP DATABASE IF EXISTS database1;
CREATE DATABASE database1;
EOF
sudo mysql -u root -p < install.sql

# pip packages
sudo pip install SQLAlchemy
sudo apt-get install python-pandas -y
sudo pip install numpy

# clean up mess on hard disk (removes everything sitting on the hard disk)
cd
echo 'cleaning up disk...'
rm -r -f *

sudo apt autoremove -y
