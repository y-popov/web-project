sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask.conf /etc/gunicorn.d/
sudo /etc/init.d/gunicorn restart
sudo gunicorn --bind 0.0.0.0:8080 hello &
sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask_db"
sudo chmod 777 ask/db.sqlite3
python ask/manage.py syncdb
