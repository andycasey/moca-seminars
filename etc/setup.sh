# Initialisation commands for Nectar cloud instance
sudo apt-get update
sudo apt-get install git apache2 libapache2-mod-wsgi python-dev python-pip -y
sudo a2enmod wsgi

# Set up repository
cd /var/www/
sudo git clone https://github.com/andycasey/moca-seminars.git seminars
cd seminars/seminars/

# Set up python and dependencies
pip install --upgrade pip
sudo pip install virtualenv
sudo virtualenv venv
source venv/bin/activate
sudo pip install -r ../requirements.txt --target=venv/lib/python2.7/site-packages/
deactivate

# Get apache config file
sudo cp ../etc/seminars.conf /etc/apache2/sites-available/

# Enable site and DISABLE all others
sudo a2dissite 000-default
sudo a2ensite seminars
sudo service apache2 reload

sudo seminars/venv/bin/python db_create.py

