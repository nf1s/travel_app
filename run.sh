#!/bin/bash


function firstTime (){
	echo "First time"
	
	echo "activate virtual environment"
	source ../venv/bin/activate
	
	cd travel
	echo "Model migrations"
	python manage.py makemigrations
	python manage.py migrate
	
	echo "create super user"
	python manage.py loaddata booking/fixtures/users.json
		
	echo "load database"
	python manage.py loaddata booking/fixtures/initial_data.json
	
	#echo "run tests"
	#python manage.py test
	
	echo "run server"
	python manage.py runserver
}


function normalRun (){
	echo "normal run"
	echo "activate virtual environment"
	source ../venv/bin/activate

	cd travel
	echo "runserver"
	python manage.py runserver
}

while true; do
	read -p "Is it your first time to run the app? " yn
	case $yn in
		[Yy]* ) firstTime ; break;;
		[Nn]* ) normalRun ; break;;
		* ) echo "Please answer yes or no.";;
	esac
done
