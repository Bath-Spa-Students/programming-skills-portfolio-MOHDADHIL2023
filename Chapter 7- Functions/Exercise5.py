#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
#such as Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

#creating a function called describe_city() that accepts the name of a city and its country
def describe_city(city="Sharjah",country="UAE"):
    print(city,"is in",country)

#calling in function
#Call your function for three different cities
describe_city("Sharjah")
describe_city("Dubai")
#at least one of which is not in the default country.
describe_city("Dhaka","Bangladesh")
    