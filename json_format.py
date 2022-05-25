import json, time

def stringify(path):
    f = open(path)
    data = json.load(f)
    f.close()
    data = json.dumps(data, separators=(",", ":"))
    with open(path,'w') as f:
        f.write(data)

def unstringify(path):
    f = open(path)
    data = json.loads(f.readline())
    f.close()
    data = json.dumps(data, indent=4,separators=(",", ": "))
    with open(path,'w') as f:
        f.write(data)

def verif_path(path):
    try:
        f = open(path)
        f.close()
        if path.endswith(".json"):
            print("File found")
            return path
        else:
            print("File should be a json file")
            return None
    except FileNotFoundError:
        print("File not found")
        return None

def choices():
    # Make the user choose the path
    choosen_path  = input("Enter the path of the file: ")
    # Make sure the file exists and is a json file
    choosen_path = verif_path(choosen_path)
    if not choosen_path:
        choices()
    while True:
        # Make the user choose the action between (1) stringify and (2) unstringify
        choosen_action = input("Enter the action you want to perform:\n (1) Stringify\n (2) Unstringify\n")
        if choosen_action == "1":
            stringify(choosen_path)
            break
        elif choosen_action == "2":
            unstringify(choosen_path)
            break
        else:
            print("This action is not available")
    print("Done changing the JSON format")

# path = "./auchan_ip.json"
choices()
