# You have a word and a definition == dictionaries
ages = {"John": 10, "Mark": 20}

print(ages["John"])

keys = list(ages.keys())
print(keys)

vals = list(ages.values())
print(vals)

print()

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}

print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Ret", "Not a valid key"))