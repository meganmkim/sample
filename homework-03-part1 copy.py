# #Megan Kim
# #June 10, 2023
# #Homework 3 Part 1

# Using the Pokemon API:
# What is the URL to the documentation? - https://pokeapi.co/docs/v2#namedapiresource


import requests
url ='https://pokeapi.co/api/v2/pokemon/55/'
response = requests.get(url)
print(response)
print(response.text)

#Converting data into dictionary
data_55 = response.json()
print(data_55)

#printing keys from dictionary
print(data_55.keys())

# What pokemon has the ID of 55?
print("The name of pokemon is", data_55['name'])

# How tall is that pokemon?
print("The pokemon is", data_55['height'])

# How many versions of Pokemon games have been released?
#Connecting general pokemon API 

all_versions = "https://pokeapi.co/api/v2/version/"
pokemon = requests.get(all_versions)
print(pokemon)
print(pokemon.text)

#Converting pokemon data into dictionary
#questions: how do we know to retrieve 'count' for versions?

data_all = pokemon.json()
print("there are", data_all['count'], "versions in Pokemon")

# Print out the name of every electric-type pokemon.

electric_url = "https://pokeapi.co/api/v2/type/electric/"
electric_poke = requests.get(electric_url).json()

print(electric_poke.keys())

print("These are the electric pokemons:")

for item in electric_poke['pokemon']:
    electric = item['pokemon']['name']
    print(electric)

#Alternative way to print electric pokemons. Create an array that stores each of the electric pokemon's inside and print]
all_names = [electric['pokemon']['name'] for electric in electric_poke['pokemon']]
print("These are the electric pokemons:", all_names)

# What are electric-type Pokemon called in the Korean version of the game? (i.e. what do they call electric-type pokemon in Korean if not "electric")
for objects in electric_poke['names']:
    if objects['language']['name'] == 'ko':
            print(objects['name'])


# Who has a higher speed stat, Eevee or Pikachu?
eevee_url= 'https://pokeapi.co/api/v2/pokemon/eevee/'
eevee_data = requests.get(eevee_url).json()

pikachu_url ='https://pokeapi.co/api/v2/pokemon/pikachu/'
pikachu_data= requests.get(pikachu_url).json()

eevee_speed = eevee_data['stats'][-1]['base_stat']
print(eevee_speed)

pikachu_speed = pikachu_data['stats'][-1]['base_stat']
print(pikachu_speed)

if eevee_speed > pikachu_speed:
     print("Eevee is faster than Pikachu")
if pikachu_speed > eevee_speed:
    print("Pikachu is faster than Eevee")