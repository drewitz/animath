import os
import json

def write_data(meta):
    """
    write the meta_data and add it to the file in an appropriate way
    """
    file = "data.json"
    the_data = []
    if os.path.isfile(file):
        with open(file, "r") as f:
            print(f)
            the_data = json.loads(f.read())
    the_data.append(meta)
    with open(file, "w") as f:
        f.write(json.dumps(the_data, indent=2))
