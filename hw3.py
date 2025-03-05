from build_data import get_data
#ddd
import data
import county_demographics
#task 1
# this function takes the entire list of county data and filters through it to find all population dictionaries and then finds
# the keys with 2014 population and then takes the associated value and adds it to the running total of the data set, and then returns the total at the end.
county_dem = get_data()


def population_total(list:list[data.CountyDemographics]) -> int:
    total_population = 0
    for x in list:
        individual_county_population_dictionary = x.population
        add_population = individual_county_population_dictionary['2014 Population']
        total_population = total_population + add_population
    return total_population



#part 2
# this function takes the input list of class objects countydemographics as well as a specified target state,
# and identifies which county objects are present within the target state, and then appends the county demographic object to the new list
#the new list is then returned
def filter_by_state(list:list[data.CountyDemographics], state_abrv:str) -> list[data.CountyDemographics]:
    filtered_list = []
    for x in list:
        if x.state == state_abrv:
            filtered_list.append(x)
    return filtered_list

print(len(filter_by_state(county_dem, 'CA')))

#Part 3a
#this function takes a list of countydemographic objects as well as the target education level in the form of a string and
#goes into each county object, finds the value of the population of the county as well as the percentage of the county with the
#target ed level, and then multiplies these two values together. This value is then added to the running total of people from each county with
#that education level. Once the entire list of demographic objects has been gone through, the float value is then returned (which is the total of
#people from the list of counties with that education level

def population_by_education(list:list[data.CountyDemographics], edkey:str) -> float:
    total_ed_pop = 0
    for x in list:
        individual_county_population_dictionary = x.population
        ind_county_pop = individual_county_population_dictionary['2014 Population']
        ind_county_ed_dict = x.education
        percent_ed = ind_county_ed_dict[edkey]/100
        total_ed_pop = total_ed_pop + percent_ed*ind_county_pop
    return total_ed_pop

#part 3b
#this function takes a list of countydemographic objects, as well as a target ethnicity string. The function then filters through
#each class object in the list, finds the value of the population of the county and the percentage of the county from the target ethnicity
#and then multiplies the two found values together. This total is then added to the running total. The total number of people of the target ethnicity
#from the list of countydemographic objects is then returned after all classdemographic objects have been evaluated.

def population_by_ethnicity(list:list[data.CountyDemographics], ethkey:str) -> float:
    total_ethnicity_pop = 0
    for x in list:
        individual_county_population_dictionary = x.population
        ind_county_pop = individual_county_population_dictionary['2014 Population']/100
        ind_county_eth_dict = x.ethnicities
        percent_eth = ind_county_eth_dict[ethkey]
        total_ethnicity_pop = total_ethnicity_pop + percent_eth*ind_county_pop
    return total_ethnicity_pop

#part 3c
#this function takes a list of countydemographic objects, goes into each one, finds the value of the total population, as well as
# the percentage of the population below the poverty line, then multiplies these values together. This value is then added to a
# running total before the function moves onto the next class function within the list. The running total is then returned at the end of the function

def population_below_poverty_level(list:list[data.CountyDemographics]) -> float:
    total_pov_pop = 0
    for x in list:
        individual_county_income_dictionary = x.income
        ind_county_percent = individual_county_income_dictionary['Persons Below Poverty Level']/100
        individual_county_population_dictionary = x.population
        ind_county_pop = individual_county_population_dictionary['2014 Population']
        total_pov_pop = total_pov_pop + ind_county_pop*(ind_county_percent)
    return total_pov_pop

#part 4a
#this function takes a list of countydemographics class objects and an education level string and then recruits the previously
#described function population_by_education, which the input list and input string are put into to then yield the number of people with a
#certain education level. Then the population_total function is recruited to yield the total population of the counties in the list.
#The value of the number of people of a certain education level (from the first function) is divided by the total value of the number
# of people in the list of county objects, and then this is multiplied by 100 to give a percentage value which is then returned

def percent_by_education(list:list[data.CountyDemographics], edkey:str) -> float:
    a = population_by_education(list,edkey)
    b = population_total(list)
    return (a/b)*100


#this function takes a list of countydemographics class objects and ethnicity string and then recruits the previously
#described function population_by_ethnicity, which the input list and input string are put into to then yield the number of people of a
#certain ethnicity. Then the population_total function is recruited to yield the total population of the counties in the list.
#The value of the number of people of a certain ethnicity (from the first function) is divided by the total value of the number
# of people in the list of county objects, and then this is multiplied by 100 to give a percentage value which is then returned

#part 4b
def percent_by_ethnicity(list:list[data.CountyDemographics], ethkey:str) -> float:
    a = population_by_ethnicity(list,ethkey)
    b = population_total(list)
    return (a/b)*100

#this function takes a list of countydemographics class objects and then recruits the previously
#described function population_below_poverty, which the input list is put into to then yield the number of people of a
#below poverty. Then the population_total function is recruited to yield the total population of the counties in the list.
#The value of the number of people below poverty (from the first function) is divided by the total value of the number
# of people in the list of county objects, and then this is multiplied by 100 to give a percentage value which is then returned

#part 4c
def percent_below_poverty_level(list:list[data.CountyDemographics]) -> float:
    a = population_below_poverty_level(list)
    b = population_total(list)
    return (a/b)*100

#This function takes a list of countydemographics class objects, a target education level string, as well as a threshold float value. The
# function then creates a new list, goes into each class object, and evaluates whether the percentage value of the population with the target
# education level is above the threshold value. If the percentage value is above the threshold, the county is then appended to the new list.
# The function runs through each county in the input list and returns the new list at the end of the function.

#part 5a
def education_greater_than(list:list[data.CountyDemographics], edkey:str, thresh:float) -> list[data.CountyDemographics]:
    new_list = []
    for x in list:
        if x.education[edkey] > thresh:
            new_list.append(x)
    return new_list


#This function takes a list of countydemographics class objects, a target education level string, as well as a threshold float value. The
# function then creates a new list, goes into each class object, and evaluates whether the percentage value of the population with the target
# education level is below the threshold value. If the percentage value is below the threshold, the county is then appended to the new list.
# The function runs through each county in the input list and returns the new list at the end of the function.


def education_less_than(list:list[data.CountyDemographics], edkey:str, thresh:float) -> list[data.CountyDemographics]:
    new_list = []
    for x in list:
        if x.education[edkey] < thresh:
            new_list.append(x)
    return new_list


#part 5b
#This function takes a list of countydemographics class objects, a target ethnicity string, as well as a threshold float value. The
# function then creates a new list, goes into each class object, and evaluates whether the percentage value of the population of the
# target ethnicity is above the threshold value. If the percentage value is above the threshold, the county is then appended to the new list.
# The function runs through each county in the input list and returns the new list at the end of the function.
def ethnicity_greater_than(list:list[data.CountyDemographics], ethkey:str, thresh:float) -> list[data.CountyDemographics]:
    new_list = []
    for x in list:
        if x.ethnicities[ethkey] > thresh:
            new_list.append(x)
    return new_list

#This function takes a list of countydemographics class objects, a target ethnicity string, as well as a threshold float value. The
# function then creates a new list, goes into each class object, and evaluates whether the percentage value of the population of the
# target ethnicity is below the threshold value. If the percentage value is below the threshold, the county is then appended to the new list.
# The function runs through each county in the input list and returns the new list at the end of the function.
def ethnicity_less_than(list:list[data.CountyDemographics], ethkey:str, thresh:float) -> list[data.CountyDemographics]:
    new_list = []
    for x in list:
        if x.ethnicities[ethkey] < thresh:
            new_list.append(x)
    return new_list

#This function takes a list of countydemographics class objects as well as a threshold float value. The
# function then creates a new list, goes into each class object, and evaluates whether the percentage value of people of the population of the
# county that live below the poverty level is above the threshold value. If the percentage value is above the threshold, the county
# is then appended to the new list.  The function runs through each county in the input list and returns the new list at the end of the function.

#part 5c
def below_poverty_level_greater_than(list:list[data.CountyDemographics], thresh:float) -> list[data.CountyDemographics]:
    new_list = []
    for x in list:
        if x.income['Persons Below Poverty Level'] > thresh:
            new_list.append(x)
    return new_list

#This function takes a list of countydemographics class objects as well as a threshold float value. The
# function then creates a new list, goes into each class object, and evaluates whether the percentage value of people of the population of the
# county that live below the poverty level is below the threshold value. If the percentage value is below the threshold, the county
# is then appended to the new list.  The function runs through each county in the input list and returns the new list at the end of the function.

def below_poverty_level_less_than(list:list[data.CountyDemographics], thresh:float) -> list[data.CountyDemographics]:
    new_list = []
    for x in list:
        if x.income['Persons Below Poverty Level'] < thresh:
            new_list.append(x)
    return new_list

sd





