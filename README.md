# Kegerator


The hardware integration project for the Kegerator project

Disclaimer: I used `nc` as the name of my virtual environment to set up Python packages, but you can use whatever name you choose.

Install pip with:

    sudo apt-get install python-pip
    sudo apt-get install python-dev

Install mysql with:

    sudo apt-get install mysql-server mysql-client libmysqlclient-dev

    sudo pip install virtualenv && sudo pip install virtualenvwrapper

In your ~/.bash_profile, add:
    source "/usr/local/bin/virtualenvwrapper.sh"

Then,

    source ~/.bash_profile
    mkvirtualenv nc
    workon nc

    pip install -r requirements.txt

In mysql,

    CREATE DATABASE kegerator;
    CREATE USER 'nc'@'localhost' IDENTIFIED BY 'kegerator1234';
    GRANT ALL PRIVILEGES ON kegerator . * TO 'nc'@'localhost';

    python main.py

Note: Every time you work on this project, you need to enter the `nc` environment by running `workon nc`.
