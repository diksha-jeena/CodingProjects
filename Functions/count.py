def countNow(PLACES):
    for city in PLACES.values():
        if len(city) > 5 :
            print(city.upper())
PLACES = {1 : "Delhi" , 2 : "Mumbai" , 3 : "Surat"}
countNow(PLACES)
