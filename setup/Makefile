DB = magic_diary
DB_USER = postgres
PROJECT_DIR = /media/planet/LABS/Occult/innovations/magical_diary/diary/
PYTHON = /usr/bin/python
PROJECT_APACHE_CONF = diary/diary_apache.conf

#This values is based on what is set in PROJECT_DIR/PROJECT_APACHE_CONF
PROJECT = diary
PRODUCTION_ROOT = /var/opt/

#Where should the apache conf of the project be deployed?
#Personally, I prefer that one have a special "extras" conf dir (specified via APACHE_CONF_INCLUDE_DIRS in /etc/sysconfig/apache2)
APACHE_CONF_DIR = /media/planet/LABS/apache_confs/
APACHE_USER = wwwrun


db:
	@echo "Creating the database [" $(DB) "]"
	createdb -U $(DB_USER) $(DB)

drop-db:
	@echo "Deleting the database [" $(DB) "]"
	dropdb -U $(DB_USER) $(DB)

init-db:db
	@echo "Initializing the database..."
	${PYTHON} $(PROJECT_DIR)/manage.py syncdb
	
apache-deploy:
	@echo "Deploying WSGI app in Apache..."
	mkdir -p $(PRODUCTION_ROOT)
	ln -fs $(PROJECT_DIR) $(PRODUCTION_ROOT)
	cp $(PROJECT_DIR)/$(PROJECT_APACHE_CONF) $(APACHE_CONF_DIR)

apache-undeploy:
	@echo "Un-Deploying WSGI app from Apache..."
	rm -f $(PRODUCTION_ROOT)$(PROJECT)
	rm -f $(APACHE_CONF_DIR)/$(PROJECT_APACHE_CONF)
	rcapache2 reload

apache-reload:apache-deploy
	rcapache2 reload

apache-install:apache-reload

#best this is run as root...
install:init-db apache-install
	@echo "Also init media directory..."
	mkdir $(PROJECT_DIR)/media
	chown $(APACHE_USER) $(PROJECT_DIR)/media

#best this is run as root...
all:install
	

uninstall:drop-db apache-undeploy
	@echo "Removed the magical diary from this server..."
