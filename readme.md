project path /opt/

open port 80 , 22
sudo iptables -A INPUT -p tcp --dport 8000 -j ACCEPT (make sure add ipv4 and ipv6 both)
https://www.cyberciti.biz/faq/how-to-open-firewall-port-on-ubuntu-linux-12-04-14-04-lts/
https://www.digitalocean.com/community/questions/sudo-ufw-status-return-inactive

make sure add 22 before restart

or network interface>>securtiy group .. edit inbound rules.


sudo apt-get update
sudo apt-get install nginx

verfiy open browser and your instance ip in url bar.


sudo python3.8 -m venv envp
source envp/bin/activate

sudo chown -R $USER /opt/testapp/
chown  $USER:www-data *
chown www-data:www-data db.sqlite3 
chown -R www-data:www-data /var/www/html
must be ubuntu user and www-data group


pip install -r requirements.txt
sudo apt-get install gcc
sudo apt-get install python3-dev
pip install uwsgi


uwsgi --socket projectalfa.sock --module testapp.wsgi --chmod-socket=666

rest follow this : https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html

