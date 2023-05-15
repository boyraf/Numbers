Day = "Wednesday"

dict_map ={
    "Sunday": "Go to church.",
    "Monday": "Go to school",
    "Tuesday": "Go to school",
    "Wednesday": "Online classes",
    "Thurday": "Online classes",
    "Friday": "Online classes",
    "Saturday": "Sherehe",

}

Event = dict_map.get(Day, "Sleep in")
print(Day, Event)