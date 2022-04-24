# Chicago Taxi Trips Analytics

Chicago taxi trips anlytics is web service that provides basic analytics over Chicago Taxi Trips dataset


## Prerequisites
Before you start consuming this APIs supported by Chicago Taxi Trips Analytics web service make sure your system meets the following prerequisities:

- A MacOS or Linux system
- Docker installed on your system

## Usage

- To download the Chicago Taxi Trips dataset and build the service run below command from the root of the project:

```shell
    $ bin/setup
```

- To run the server on local machine run below command from the root of the project:

```shell
    $ bin/run [<port_num>]
```
This command will build the docker image and run the service in docker container on the given port, if port number is not provided it will run on port
`8080` by default.

## Documentation
Currently documentation is provided as swagger only. swagger can be access after running the server:

```
    http://0.0.0.0:8080/docs
```


## Development

To run this service on your local machine instead of using docker run below commands:

```shell
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    $ pip install -r requirements_dev.txt
    $ uvicorn app.main:app --reload  # run the server
```
