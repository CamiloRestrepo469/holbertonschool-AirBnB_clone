# The Console 🔧



## Description. 📝

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

### Fucionalities. 🧰

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Files. 🗂️

| Name | Description |
| ------------------------------ | -------------------------------------------- |
| AUTHORS | Contributors in this repository.|
| console.py | Command line interpreter. file. |
| models/ | Package with the base classes. |
| base_model.py | defines all common attributes/methods for other classes. |
| models/engine | Package with in storage file. |
| file_storage.py | Class FileStorage. serializes/deserializes instances to a JSON file. |
| tests/ | Directory with class tests. |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
| | |

## Console description. 📋

* ```quit``` - exits console
* ```create``` - Creates a new instance of ```BaseModel```, saves it (to the JSON file) and prints the id.

* ```destroy``` - Deletes an instance based on the class name and id (save the change into the JSON file).
* ```show``` - Prints the string representation of an instance based on the class name and id.
* ```all``` - Prints all string representation of all instances based or not on the class name.
* ```update``` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).


## Requeriments. ⚙️

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Install. 💾

* Clone  https://github.com/CamiloRestrepo469/holbertonschool-AirBnB_clone.git 


## Usage. 💿

* Run the interactive mode: ```./console.py```
* Run the non-interactive mode: ```echo "help" | ./console.py```


### Examples. 🖇️

* **Run console in interactive mode:**

```$ 
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

* **Run console in Non-interactive mode:**

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

## Authors.

<a href = 'https://www.github.com/Crisgrva'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a> [@CamiloRestrepo469](https://github.com/CamiloRestrepo469) | [@Briana1984](https://github.com/Briana1984)
| [@andresrivera](https://github.com/andresrivera)
