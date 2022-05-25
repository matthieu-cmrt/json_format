# json_format
Python script to change format of a JSON file. (Stringify &amp; Unstringify)
> :warning: The format stays is changed in the same file

Running example of the programme
```console
c:\\> python ./json_format.py
Enter the path of the file: ./test.son
File should be a json file
Enter the path of the file: ./tst.json
File not found
Enter the path of the file: ./test.json
File found
Enter the action you want to perform:
 (1) Stringify
 (2) Unstringify
avfe
This action is not available
Enter the action you want to perform:
 (1) Stringify
 (2) Unstringify
 1
 Done changing the JSON format
```

Old Format:
```json
[
    {
        "name": "Juan",
        "age": "23",
        "hobbies": [
            "coding",
            "reading",
            "playing"
        ]
    },
    {
        "name": "Roger",
        "age": "25",
        "hobbies": [
            "eating",
            "sleeping",
            "coding"
        ]
    },
    {
        "name": "Jorge",
        "age": "19",
        "hobbies": [
            "coding",
            "reading",
            "sleeping"
        ]
    }
]
```

New Format:
```json
[{"name":"Juan","age":"23","hobbies":["coding","reading","playing"]},{"name":"Roger","age":"25","hobbies":["eating","sleeping","coding"]},{"name":"Jorge","age":"19","hobbies":["coding","reading","sleeping"]}]
```
