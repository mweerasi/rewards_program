# Rewards Program
Django application for a basic rewards program

## Deployment locally

### Set up the conda environment

First, you need to [install Anaconda](https://docs.anaconda.com/anaconda/install/index.html) on your system. Optionally, you can [install Mamba](https://github.com/mamba-org/mamba) as well, and substitute `conda` with `mamba` in all following commands.

Make sure to update Anaconda by running
```
conda update -n base conda
```
For convenience, we use a single conda environment throughout the entire API, frontend, and submodules. It includes all the necessary libraries, packages, and binaries needed. To download the dependencies and create the conda environment, inside the platformAPI directory, run:
```
conda env create --file environment.yml
```
This process will take some time, as conda has to find appropriate, non-conflicting versions for all necessary depedencies. After it is complete, you can activate the new environment with:
```
conda activate rewards-server
```

### Run the Django server

Once you're in the conda environment, or if you already have all the dependencies in the `environment.yml` file installed locally, you can run the server.

Run the server locally with the command below.
```
python manage.py runserver
```


## Deployment with Docker

If you're deploying with Docker, the changes you make to the database will not persist.

You can use [Docker](https://docs.docker.com/get-docker/) to locally deploy the backend API server.

The entire process is fully automated though the `docker-compose.yaml` and `Dockerfile` files. To download, setup and run everything you can simply do:
```
docker compose up
```

If there are any changes in the API code, you can make sure the image is rebuilt and not run from cache with:
```
docker compose up --build
```
