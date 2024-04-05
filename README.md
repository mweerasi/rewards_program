# Rewards Program
Django application for a basic rewards program

## Deployment

### Option 1: Deployment with Docker

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

### Option 2: Set up the conda environment

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

#### Run the Django server

Once you're in the conda environment, or if you already have all the dependencies in the `environment.yml` file installed locally, you can run the server.

Run the server locally with the command below.
```
python manage.py runserver
```

### Option 3: Use pip and run locally

Install the required dependencies using:
```
pip install -r requirements.txt`
```

Run the server with:
```python manage.py runeserver
```


## Project Information
This is a Django REST Framework project that provides an API for managing rewards programs, members, and rewards.
Models

### The project includes the following models:

- Member: Represents a rewards member with fields such as name and alias.
- Program: Represents a rewards program with a name field.
- Reward: Represents a reward that can be associated with a program. It has a name field.
- ProgramMembership: Represents a member's association with a specific rewards program, including their current points balance.
- ProgramReward: Represents a reward's association with a specific program, including the cost and maximum claim limit.
- History: Represents the history of a member redeeming a reward within a program. It includes a foreign key to the member, a foreign key to the reward, the point value associated with the redemption, and the creation timestamp.

### API Endpoints

The API provides the following endpoints:

- /members/: CRUD operations for managing members.
- /programs/: CRUD operations for managing reward programs.
- /rewards/: CRUD operations for managing rewards.
- /programs/{program_pk}/members/: CRUD operations for managing program memberships.
- /programs/{program_pk}/rewards/: CRUD operations for managing program rewards.
- /programs/{program_pk}/members/{member_pk}/history/: CRUD operations for managing reward redemption history.

### Serializers

The project uses the following serializers:

- MemberSerializer: Serializes the Member model.
- ProgramSerializer: Serializes the Program model.
- RewardSerializer: Serializes the Reward model.
- ProgramMemberSerializer: Serializes the ProgramMembership model and includes the member name.
- ProgramRewardSerializer: Serializes the ProgramReward model and includes the reward name.
- HistorySerializer: Serializes the History model and includes the member name and reward name.

### Views

The project defines the following views:

- MemberView: Provides CRUD operations for the Member model.
- ProgramView: Provides CRUD operations for the Program model.
- RewardView: Provides CRUD operations for the Reward model.
- ProgramMembersView: Provides CRUD operations for the ProgramMembership model within a specific program.
- ProgramRewardsView: Provides CRUD operations for the ProgramReward model within a specific program.
- HistoryView: Provides CRUD operations for the History model, linking a member and a reward within a specific program.

### URLs

The project defines the following URL patterns:

- /members/: Routes to the MemberView.
- /programs/: Routes to the ProgramView.
- /rewards/: Routes to the RewardView.
- /programs/{program_pk}/members/: Routes to the ProgramMembersView.
- /programs/{program_pk}/rewards/: Routes to the ProgramRewardsView.
- /programs/{program_pk}/members/{member_pk}/history/: Routes to the HistoryView.
