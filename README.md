# FinalRound2

Clone this repository.

I will guide you through some series of sequential installations, if they are already installed skip them.

0 - sudo apt-get update

1 - sudo apt-get install python3-pip<br>
2 - pip3 install django

In the cloned ClashRound2 folder go to the sandbox folder you will find a script install.sh
we will install sandbox

3 - chmod +x install.sh<br>
4 - ./install.sh

Now we will install mysql

5 - sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev<br>
6 - mysqld --initialize<br>
7 - sudo mysql_secure_installation<br>


No we will create the database

7 - mysql -u root -p<br>

Enter the password of root mysql

The name of the database should specificly be git and user should be gituser and password should be 'password'

8 - CREATE DATABASE git CHARACTER SET UTF8;<br>
9 - CREATE USER gituser@localhost IDENTIFIED BY 'password';<br>
10 - GRANT ALL PRIVILEGES ON git.* TO gituser@localhost;<br>
11 - FLUSH PRIVILEGES;<br>
12 - exit<br>

12.5 pip3 install mysqlclient<br>

Now run

13 - python3 manage.py runserver <br>
 
In the ClashRound2 folder to check if any errors.
if any errors in uninstall above things and follow again correctly

Now we will have to make migrations

14 - python3 manage.py makemigrations<br>
15 - python3 manage.py migrate<br>
16 - python3 manage.py createsuperuser<br>

set the password to 1 
make username and email whatever you want

No go to the server that you are running the go to admin url

17 - http://localhost/admin<br>

login

and add 6 question in admin section with whatever title and text of the question.

If you want the actual questions and solutions they are in quesDescrip folder.
Logout the admin

run sever and enter this url to start timer

18 - http://localhost/timer   <br>  Enter admin password 1

Wait 1 min and regiter page will appear.

All set.

To test solutions .cpps of the questions are present in queDescrip folder

