def find_people(
        list, max_age=None, min_age=None,
        sex=None, professions=None):
    """Find people by specific criterias
>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}]\
)]
['John', 'Scarlet', 'Kventin']

>>> [person["name"] for person in find_peoples([])]
[]

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
max_age=60, min_age=30, sex="male", professions=["driver"])]
[]

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
sex="female")]
['Scarlet']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
max_age=40)]
['John', 'Scarlet']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
min_age=30)]
['Scarlet', 'Kventin']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
professions=["editor", "actor"])]
['Scarlet', 'Kventin']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
max_age=40)]
['Scarlet']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
min_age=20)]
['Scarlet', 'Kventin']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "age" : 23, "prof":"driver"},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}],\
sex="male")]
['Kventin']

>>> [person["name"] for person in find_peoples(\
[{"name":"John", "sex":"male", "age" : 23},\
{"name":"Scarlet", "sex":"female", "age" : 32, "prof":"actor"},\
{"name":"Kventin", "sex":"male", "age" : 57, "prof":"editor"}]\
)]
['John', 'Scarlet', 'Kventin']
"""

    found_people = []

    for person in list:
        result = True

        if (result and max_age is not None):
            result = person.get("age") and person["age"] <= max_age

        if (result and min_age is not None):
            result = person.get("age") and person["age"] >= min_age

        if (result and sex is not None):
            result = person.get("sex") and person["sex"] == sex

        if (result and professions is not None):
            result = person.get("prof") and person["prof"] in professions

        if result:
            found_people.append(person)
    return found_people
