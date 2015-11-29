# Eversnap Twitter App
The app is a smart automatic album creator. It run every 20min and fetch the last photos posted on twitter (under the hashtag #carnival) since the last fetching. Every picture is stored in the db and accessible from the rest api and the browser. 

## Installation

* `$ git clone git@github.com:gianlucadonato/eversnap-project.git`
* `$ virtualenv venv`
* `$ source venv/bin/activate`
* `$ pip install -r requirements.txt`
* `$ python manage.py celeryd -B -l info`
* `*** Open an other shell tab ***`
* `$ python manage.py runserver`

## Usage

* `Go to http://localhost:8000/albums/carnival/photos in your browser to shows all the pictures`
* `GET http://localhost:8000/api/albums/carnival/photos to access the data structure of the pictures with the REST api`


*NOTE: The worker job runs every 20min and fetch new tweets. There is a testing route available from 'GET localhost:8000/api/twitter' that let you populate the db with olders tweets*