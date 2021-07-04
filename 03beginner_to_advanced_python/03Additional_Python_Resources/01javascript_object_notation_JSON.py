import simplejson as json
import os

# Will check if file exists and if it is empty
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:

    # Opening in read/write mode
    old_file = open("./ages.json", "r+")

    # This will load the data from the file
    data = json.loads(old_file.read())

    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    # If there is no new file, we will create one
    old_file = open("./ages.json", "w+")
    data = {"name": "Nick", "age": 27}
    print("No file found, setting default age to", data["age"])

# We will dump the data into the file
old_file.seek(0)
old_file.write(json.dumps(data))