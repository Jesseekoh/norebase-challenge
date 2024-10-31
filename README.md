# Norebase Challenge

## Overview
This is a simple implementation of a Like Button feature


## Setup

### Prerequisites
- Python 3.x
- PostgreSQL
- Redis

### Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables
    ```env
    SECRET_KEY=<your_secret_key>
    SQLALCHEMY_DATABASE_URI=<your_database_uri>
    ```



5. Run the application:
    ```sh
    flask run
    ```

## Configuration
Key configurations include:
- `SECRET_KEY`: this should be provided in the .env file
- `SQLALCHEMY_DATABASE_URI`: Database connection URI (default: `sqlite:///default.db`)
- `SESSION_TYPE`: Session type (default: `filesystem`)
- `SESSION_COOKIE_HTTPONLY`: HTTPOnly flag for session cookies (default: `True`)
- `SESSION_COOKIE_SECURE`: Secure flag for session cookies (default: `False`)
- `SESSION_PERMANENT`: Permanent session flag (default: `False`)


## Usage
The application provides the following endpoints:

### User Registration
- **URL:** `/register`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "your_username",
        "email": "your_email",
        "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
      "message": "You've logged in successfully"
    }
    ```

### User Login
- **URL:** `/login`
- **Method:** `POST`
- **Payload:**
    ```json
    {
      "email": "your_email",
      "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
      "message": "You've logged in successfully"
    }
    ```

### Create Post
- **URL:** `/post/new`
- **Method:** `POST`
- **Payload:**
    ```json
    {
      "title": "Post Title",
      "content": "Post Content"
    }
    ```
- **Response:**
    ```json
    {
      "message": "Article created successfully"
    }
    ```

### Like Post
- **URL:** `/like`
- **Method:** `POST`
- **Payload:**
    ```json
    {
      "articleID": "article_id"
    }
    ```
- **Response:**
    ```json
    {
      "message": "Liked post"
    }
    ```

