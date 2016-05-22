if (( $# != 1 ))
then
  echo "Usage: sh start.sh {project name}"
  echo "Where project name is something like UserService, TodoService, etc"
  exit 1
fi

wget https://github.com/TangentSolutions/DRF-seed/archive/master.zip
unzip master.zip
mv DRF-seed-master $1
cd $1 && git init
docker-compose run --rm ci ansible-playbook ansibles/bootstrap.yml


echo "******************"
echo "Success!" 
echo "******************"
echo "To run your app try: docker-compose up"
echo "you might want to quickly create a superuser: docker-compose rum --rm web python manage.py createsuperuser"
echo "To run the tests: docker-compose run --rm web python manage.py test"
echo "To continuosly run the tests: docker-compose run --rm web python sniffer" 
echo "NBNBNBNBNBNB: ALWAYS RUN ALL COMMANDS THROUGH DOCKER. E.G.: docker-compose run --rm ...."
echo "... have fun ..."
