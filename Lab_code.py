# Name: Miles Van Denburg
# Assignment title: Final Lab Assignment
# Time to complete: 10 minutes. 
# Description: The program prints out the coutnries and populations of a declared dictionary containing 5 countries
# It then associates the relavent country to its population and prints out the information for the user. 

#Dictionary containing 5 countries and populations
d = {'Algeria':90000, 'Bangladesh':13176, 'Burundi':7001, 'Kenya':88486, 'Thailand':46978}

#function that will print out just the countries' names,
#by looping through the keys of your dictionary.
def countryNames(x):
    for key in sorted(x.keys()):
        print key
countryNames(d)
            
#function that will print out just the populations,
#by looping through the values of your dictionary.
def populations(x):
    for value in sorted(x.values()):
        print value
populations(d)


#Print out a series of statements
#telling how many refugees are in each country: "CountryX has 1234567 refugees."
def printData(x):
    for (key,value) in x.items():
        print("The country of " + str(key) + " has a population of " + str(value))
    
printData(d)
