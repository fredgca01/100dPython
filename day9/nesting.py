program_dictionnary = {
    "bug":"An error occured", 
    "Function":"Check a value"
}

print(program_dictionnary["bug"])

program_dictionnary["Function"]="duplicate a value"
print(program_dictionnary)

#program_dictionnary={}
#print(program_dictionnary)

for key in program_dictionnary:
    print(program_dictionnary[key])

capitals={
    "France":"Paris",
    "Italie":"Rome",
    "Allemagne":"Berlin"
}

travel_log={
    "France":["Paris","Dijon","Orange"],
    "Italie":["Rome","Catane"]
}

travel_log_ext=[
    {
        "country":"France",
        "cities_visited":["Paris","Dijon","Orange"], 
        "total_visits":"12"
    },
    {
        "country":"Italie",
        "cities_visited":["Rome","Catane"], 
        "total_visits":"2"
    }
]
travel_log_ext.append({"country":"Allemagne", "cities_visited":["Berlin"],"total_visits":"1"})

print(travel_log_ext)