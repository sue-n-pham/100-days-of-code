capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris","Lille", "Dijon"], # nesting list in dictionary
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1]) # print Lille

# nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1]) # print D
