# userservice

## Prepare your environment

    ## 1) mkdir Playvox (check if was already created)
    ## 2) cd Playvox
    ## 3) git clone https://github.com/magalvez/userservice.git
    ## 4) docker-compose up -d

## MongoDB
This database contain the following collection:
    ## 1) user
    
This collection is populated when the docker container is created with the following data:

db.user.insert({"_id": ObjectId("5c9ccc140aee604c4ab6cd06"), "user_id": "105398890", "pin": 2091, "user_name": "playvox", "password": "pl4yv0x", "create_date": ISODate("2021-03-06 01:37:14.422Z")})
db.user.insert({"_id": ObjectId("5c9ccc140aee604c4ab6cd07"), "user_id": "105398891", "pin": 2090, "user_name": "docker", "password": "d0ck3r", "create_date": ISODate("2021-03-06 01:57:14.422Z")})

The data is auto populated each time the folder `mongodb` is deleted

# Service URL
http://localhost:8200/

## Testing via postmant
To test it with postman use the following collection:
https://www.getpostman.com/collections/e1daefda0d281339afeb

---------------------------------------------

To use without dokcer pipenv follow this steps:

1) pip install pipenv
2) pipenv shell
3) pipenv install

Pipenv is going to look automatically the Pipfile and install the dependencies

Note if you want to analyze your dependencies you can run:
 * pipenv graph

Yo will something like this:
 
 Flask==1.1.2
  - click [required: >=5.1, installed: 7.1.2]
  - itsdangerous [required: >=0.24, installed: 1.1.0]
  - Jinja2 [required: >=2.10.1, installed: 2.11.3]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - Werkzeug [required: >=0.15, installed: 1.0.1]
  
Pipenv will generate a Pipfile.lock file to manages the following:
  * The Pipfile.lock file enables deterministic builds by specifying the exact 
    requirements for reproducing an environment. It contains exact versions for 
    packages and hashes to support more secure verification