cities = {"kenya":"Nairobi","Algeria":"Algiers","Angola":"Luanda","Bennin":"portonova"}
print(cities)
for key in cities:#loop through the dictionary
    print(key)#to print the countries only
    print(cities[key])#to print couutries and their cities
for keys,value in cities.items():#to loop thrugh both the countries and their cities
    print(keys,value)#print the coutries and the cities alongside each ther