# Backend

is the main oppration of the project, it contain all the class and functions we want.

1. BaseModel and Classes represent tables in database.

2. Function that manplate data.

3. Checker model to valdiate a submation.


## BaseModel

made basemodel class that will intract with database latter.
every other objects will be inhertic from it.

it contain main functions to fetch data
- add: add to database.
- save: save current updates.
- delete: delete data.
- to_dict: convert data to jison dictionary file.