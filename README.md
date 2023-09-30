# BlogifyAPI
BlogifyAPI is a Django-based web application designed to power a blog platform. This project includes a Dockerized setup for seamless deployment and management. It incorporates essential features to manage blog posts, user accounts, and interactions.

## Dockerized Django Project Setup and Run Guide
#### Setup
1. Clone the repository:
   ```json
   "git clone <repository_url>"
   "cd BlogifyAPI"
3. Set up the Django project:
   python -m venv env
   source env/bin/activate  (On Windows, use: env\Scripts\activate)
   pip install -r requirements.txt
#### Running the Application
1. Build the Docker image:
   ```json
   "docker build ."
3. Run the Docker container:
   ```json
   "docker-compose up -d"
   
## API Documentation
### Authentication

#### Register a User

- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Request Format**:
  ```json
  {
    "username": "example_user",
    "password": "password123",
  }
  
#### Login

- **Endpoint**: `/api/login/`
- **Method**: `POST`
- **Request Format**:
  ```json
  {
    "username": "example_user",
    "password": "password123",
  }
- **Expected Response**:
  ```json
  {
    "token": "<authentication_token>",
    "user_id": "<user_id>",
    "username": "example_user"
  }

#### Logout
- **Endpoint**: `/api/login/`
- **Method**: `POST`
- **Authorization Header** : 'Token <authentication_token>'
- **Expected Response**:
  ```json
  {
    "message": "You are logged out!"
  }
### Blog Posts
#### Get All Blog Posts
- **Endpoint**: /blog/all/
- **Method**: GET
- **Authorization Header** : 'Token <authentication_token>'
- **Expected Response**: List of blog posts
#### Create a Blog Post
- **Endpoint**: /blog/all/
- **Method**: POST
- **Authorization Header** : 'Token <authentication_token>'
- **Request Format**:
  ```json
  {
    "title": "Example Blog Post",
    "content": "This is the content of the blog post."
  }
- **Expected Response**:
  ```json
  {
    "title": "Example Blog Post",
    "content": "This is the content of the blog post.",
    "author": "<author_user_id>",
    "publication_date": "now time"
  }
#### Get Specific Blog Post
- **Endpoint**: /blog/all/<id>
- **Method**: GET
- **Authorization Header** : 'Token <authentication_token>'
- **Expected Response**: Detail of specific Blog post
#### Edit Specific Blog Post
- **Endpoint**: /blog/all/<id>
- **Method**: PUT
- **Authorization Header** : 'Token <authentication_token>'
#### Delete Specific Blog Post
- **Endpoint**: /blog/all/<id>
- **Method**: DELETE
- **Authorization Header** : 'Token <authentication_token>'

## Environment Variables
#### Ensure to set the following environment variables in the docker-compose.yml file:
- **POSTGRES_DB**: The PostgreSQL database name for the project.
- **POSTGRES_USER**: The PostgreSQL database user for the project.
- **POSTGRES_PASSWORD**: The PostgreSQL database password for the project.
- **POSTGRES_HOST**: The PostgreSQL database host IP or URL.
- **POSTGRES_PORT**: The PostgreSQL database port (default is 5432).
