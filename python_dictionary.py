"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}

import re
class Location:
    def __init__(self, city, country, continent):
        self.location = {continent: {country: [city]}}
    
    def my_location_update(self, addition):
        city_list = re.split('\ \(|,\ |\)', addition)
        continent = self.location.setdefault(city_list[2], {})
        country = continent.setdefault(city_list[1], [])
        country.append(city_list[0])
        
    def city_list(self, d_country):
        for continent in self.location:
            for country in self.location[continent]:
                if country == d_country:
                    cities = self.location[continent][country]
                    for city in sorted(cities):
                        print(city)
    
                        
    
    def city_country_list(self, d_continent):
        cities = []
        for country in self.location[d_continent]:
            for city in self.location[d_continent][country]:
                cities.append([city, country])
        for city in sorted(cities):
            print("{} - {}".format(city[0], city[1]))
            
    

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
location = Location('Mountain View', 'USA', 'North America')
location.my_location_update("Bangalore (India, Asia)")
location.my_location_update("Atlanta (USA, North America)")
location.my_location_update("Cairo (Egypt, Africa)")
location.my_location_update("Shanghai (China, Asia)")

print(1)
location.city_list('USA')
print(2)
location.city_country_list('Asia')

