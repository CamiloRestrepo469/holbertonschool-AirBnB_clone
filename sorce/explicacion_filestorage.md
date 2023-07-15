## explicacion Filestorage 

```python
import json
```
Esta línea importa el módulo `json`, que proporciona funciones para trabajar con el formato de intercambio de datos JSON. Se utiliza en este código para leer y escribir datos en formato JSON.

```python
from os import path
```
Esta línea importa la función `path` del módulo `os`. `path` proporciona funciones para manipular rutas de archivos y directorios. En este código, se utiliza para verificar si un archivo existe en una ruta determinada.

```python
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
```
Estas líneas importan las clases `BaseModel`, `Amenity`, `City`, `Place`, `Review`, `User` y `State` del paquete `models`. Estas clases son modelos de datos utilizados en la aplicación.

```python
from datetime import datetime
```
Esta línea importa la clase `datetime` del módulo `datetime`. `datetime` es una clase que proporciona funciones para trabajar con fechas y horas. Se utiliza en este código para serializar las fechas y horas en objetos JSON.

```python
import os
```
Esta línea importa el módulo `os`, que proporciona funciones para interactuar con el sistema operativo. En este código, se utiliza para verificar si un archivo existe en una ruta determinada.

```python
class FileStorage:
```
Esta línea define una clase llamada `FileStorage`.

```python
    __file_path = "file.json"
    __objects = {}
```
Estas líneas definen variables de clase `__file_path` y `__objects`. `__file_path` es una cadena que representa la ruta del archivo JSON utilizado para almacenar los objetos. `__objects` es un diccionario que almacena los objetos creados en la aplicación.

```python
    def all(self):
        return self.__objects
```
Este método `all` devuelve todos los objetos almacenados en el diccionario `__objects`.

```python
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
```
Este método `new` agrega un nuevo objeto al diccionario `__objects`. La clave del diccionario se forma concatenando el nombre de la clase y el ID del objeto.

```python
    def save(self):
        """"Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as file:
            dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic, file, indent=4)
```
Este método `save` serializa los objetos en el diccionario `__objects` en un archivo JSON. Los objetos se convierten a diccionarios utilizando el método `to_dict()` y luego se guardan en el archivo JSON.

```python
    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                loaded = json.load(file)
                for k, v in loaded.items():
                    class_name = v['__class__']
                    obj = eval(class_name)(**v)
                    self.__objects[k] = obj
```
Este método `reload` carga los objetos desde el archivo JSON y los guarda en el diccionario `__objects`. Los objetos se crean utilizando la función `eval()` para evaluar el nombre de la clase y luego se pasan los atributos del objeto al constructor de la clase.

La lógica general del código es definir la clase `FileStorage` que se utiliza para almacenar y recuperar objetos en un archivo JSON. Los métodos proporcionados permiten agregar nuevos objetos, guardarlos en el archivo JSON, cargar los objetos desde el archivo y obtener todos los objetos almacenados.