country = input('Insert Country Name : ') # Add country name
visits = int(input('Insert Number of Visits : ')) # Number of visits
list_of_cities = (input('Insert City Names : ')) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

def add_new_country(nameOfCountry,numVisits,nameOfCities):
  new_country = {} 
  new_country['country'] = nameOfCountry
  new_country['visits'] = numVisits
  new_country['cities'] = nameOfCities
  print(new_country)
  travel_log.append(new_country)
  print(travel_log)

print(travel_log)
# Do not change the code below 👇
add_new_country(nameOfCountry = country, numVisits = visits, nameOfCities = list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")