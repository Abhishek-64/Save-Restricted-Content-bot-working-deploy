To run python3 -m main permanently using Supervisor, follow these steps:

Install Supervisor (if not already installed):

sh
Copy code
sudo apt-get update
sudo apt-get install supervisor
Create a Supervisor configuration file for your script:

sh
Copy code
sudo nano /etc/supervisor/conf.d/save_restricted_content_bot.conf
Add the following content to the configuration file:

ini
Copy code
[program:save_restricted_content_bot]
command=/usr/bin/python3 -m main
directory=/home/ubuntu/Save-Restricted-Content-bot-working-deploy
autostart=true
autorestart=true
stderr_logfile=/var/log/save_restricted_content_bot.err.log
stdout_logfile=/var/log/save_restricted_content_bot.out.log
user=ubuntu
Make sure to replace /usr/bin/python3 with the path to your Python 3 interpreter if it's different, and adjust the directory to the correct path of your project directory.

Update Supervisor to read the new configuration:

sh
Copy code
sudo supervisorctl reread
sudo supervisorctl update
Start the new Supervisor program:

sh
Copy code
sudo supervisorctl start save_restricted_content_bot
Check the status of your program to ensure it's running:

sh
Copy code
sudo supervisorctl status save_restricted_content_bot
Your script should now be running under Supervisor, and it will automatically restart if it crashes. The logs for the script can be found at /var/log/save_restricted_content_bot.err.log and /var/log/save_restricted_content_bot.out.log.