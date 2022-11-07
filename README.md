# strapi
Strapi docker and python queries for quick development.

### Install
    docker-compose up -d --build
    
### Get your JWT token with get-jwt.py and put it into an os environment variable:

    python3 get-jwt.py
    export strapi_token='RESULT OF get-jwt.py GOES HERE'

### Requests

* add.py adds row to an existing table
* put.py updates rows
* delete.py deletes specific row
* get.py gets an entire table or row
