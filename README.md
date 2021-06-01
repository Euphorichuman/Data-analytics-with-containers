# DATA ANALYTICS WITH CONTAINERS

Container-based data analytics development solution: Visualizations of a database with a data source (The 100 richest people in the year 2019) using Jupyter notebook and Dash application.

### Built with

Container:
- [Docker](https://www.docker.com/)
- [Docker compose](https://docs.docker.com/compose/)

Database:
- [MySql](https://www.mysql.com/)
- [SQLalchemy](https://www.sqlalchemy.org/) was used as a driver for the connection.

Notebook:
- [Jupyter Notebook](https://jupyter.org/)

App web:
- [Dash](https://dash.plotly.com/deployment)

## Project creation

You can configure this project locally by cloning this repository.

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker compose](https://docs.docker.com/compose/)

### Installation

1. Download and configure [Docker](https://www.docker.com/) for container creation.

2. Clone the repo:
   ```
   git clone https://github.com/fuentesDeveloper/Data-analytics-with-containers.git
   ```
3. Create and start containers:
   ```
   docker-compose up -d
   ```

## Features

With this project you can perform and observe the following functionalities:

- It has a database with a data source (The 100 richest people in the year 2019).

- From a jupyter notebook you can connect to the database and view the data.

- Show those same visualizations using the Dash server.

## Contributions
All **Pull Requests** are welcome. For major changes, please open an issue first to discuss what you would like to change.

Be sure to update the tests accordingly.

## Authors
This container-based data analytics development solution was created by:

- [Martin Fuentes](https://github.com/Euphorichuman)
- [Sergio Mancilla](https://github.com/sdmancilla)
- Daniel Meza
- Randy Romero
