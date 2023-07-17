# Student Management Flask App

This is a simple Flask application that allows users to submit a form with their name and college, and saves the form data to a PostgreSQL database. The application then displays the data from the database on a webpage.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.7 or later to run this app. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems. 

In Ubuntu, Mint and Debian you can install Python 3 like this:

```
sudo apt-get install python3 python3-pip
```

For other Linux flavors, macOS and Windows, packages are available at

http://www.python.org/getit/

### Installation

Clone this repository:

```
git clone https://github.com/tgoyal63/Student_Crud_Flask.git
```

Then, navigate to the project folder:

```
cd Student_Crud_Flask
```

We recommend creating and activating a virtual environment before proceeding:

```
python3 -m venv venv
source venv/bin/activate  # for Linux or macOS
venv\Scripts\activate     # for Windows
```

Install the project dependencies:

```
pip install -r requirements.txt
```

### Configuration

You need to rename `demo.env` file as `.env` file in the root directory and set the `SQLALCHEMY_DATABASE_URI` variable:

```
SQLALCHEMY_DATABASE_URI=your_postgresql_uri_here
```

### Running the Application

To run the application:

```
python app.py
```

Open a web browser and navigate to `http://127.0.0.1:5000` to see the application running.
