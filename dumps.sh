#!/bin/bash
echo "Activating virtual environment .."
source ../venv/bin/activate

echo "dump database users fixtures to travel/booking/fixtures/users.json"
python travel/manage.py dumpdata auth.User --indent 4 > travel/booking/fixtures/users.json

echo "dump database fixtures to travel/booking/fixtures/initial_data.json"
python travel/manage.py dumpdata --format=json booking > travel/booking/fixtures/initial_data.json

echo "Done."