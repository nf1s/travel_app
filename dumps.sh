#!/bin/bash
echo "Activating virtual environment .."
source ../venv/bin/activate

cd travel
echo "dump database users fixtures to travel/booking/fixtures/users.json"
python manage.py dumpdata auth.User --indent 4 > booking/fixtures/users.json

echo "dump database fixtures to travel/booking/fixtures/initial_data.json"
python manage.py dumpdata --format=json booking > booking/fixtures/initial_data.json

echo "Done."