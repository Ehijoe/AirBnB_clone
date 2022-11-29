# The AirBnB Clone Project
![AriBnB Architecture](https://i.ibb.co/RSzZ5yh/815046647d23428a14ca.png)

## Project Description
This is the first part of the AirBnB clone project where we worked of the backend of the project whiles inferfacing it with the console application with the help of the cmd model in python.

The data generated are store in a json file.

## Description of the command interpeter
The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter  serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
- show
- create
- update
- destroy
- count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:
-   Creating new objects (ex: a new User or a new Place)
-   Retrieving an object from a file, a database etc…
-   Doing operations on objects (count, compute stats, etc…)
-   Updating attributes of an object
-   Destroying an object
## Installation
 
 For use this console you need to have:
 * Linux ubuntu 14.04.3 LTS
 * Python 3.7

## Files



 -  HBNHCommand: console.py
 -  Amenity: models/amenity.py
 -  BaseModel: models/base_model.py
 -  City: models/city.py
 -  models.init : models/__init__.py
 -  Place: models/place.py
 -  Review: models/review.py
 -  State: models/state.py
 -  User: models/user.py
 -  FileStorage: models/engine/file_storage.py
 -  engine.init: models/engine/__init__.py

```
How To run the command interpreter:
```
$ ./console.py


## Examples

Interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Authors
Lawrence Mugwena | Email: <mugwenalawrence121@gmail.com> <br>
Joseph Alikah \| Email:<alikahjoseph@gmail.com>
