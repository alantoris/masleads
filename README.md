# masleads


## Instructions 

To execute this test it is enough to simply build the docker images generated using the docker compose file

`docker-compose build`

After its completion we will simply launch the django backend containers and the database with the initial data loaded

`docker-compose up`

After these steps we will have the backend available in our local environment on port 8000

## Documentation

We can directly access the API documentation provided by Django rest framework through the browser http://localhost:8000
We will open the root of the API and we will be able to navigate between the links, list, filter and create elements.