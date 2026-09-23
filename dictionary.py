

capitals = {"USA" : "Washington D.C.",
            "INDIA" : "NEW DEHLI",
            "CHINA" : "BEIJING",
            "RUSSIA" : "MOSCOW"}

print(capitals.get("USA"))

#If cant find key, returs none

if capitals.get("JAPAN"):
    print("THAT CAPITAL EXIST")
else:
    print("THAT DOES NOT")

capitals.update({"GERMANY" : "BERLIN"})

#capitals.popitem()#REmoves last key value, in dict
capitals.pop("CHINA")
keys = capitals.keys() #give keys
print(keys)
print(capitals)
values = capitals.values()
for key in capitals.keys():
    print(key)


print(capitals.items()) #returns 2d list type

for key, value in capitals.items():
    print(f"{key}: {value}")
