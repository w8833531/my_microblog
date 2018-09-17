## Welcome to my microblog
  This is my flask practice according to [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
## How to start it use docker-compose(need a docker-ce enviroment on your system)
### 1.  git clone my_microblog, run "git clone https://github.com/w8833531/my_microblog && cd my_microblog" command.
### 2.  config your setting in example.env_online file
### 3.  rename this file from example.env_online to .env_online run   "mv example.env_online  .env_online" command
### 4.  run   "docker-compose up"  command to start your microblog app
### 5.  Access URL: http://127.0.0.1:5000
### 6.  Stop & remove  run "docker-compose stop" to stop all docker containers, run "docker-compose rm" to rm all docker containers, run ", run "docker volume rm microblog_mysqldata" to remove mysqldata volume"