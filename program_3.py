# Programmer: Mai Lillie
# Date: 10/18/24
# Program #3: US_Population

# Gathers data from the user about state population
def main():
    x = "yes"
    master_list = []
    while x != "no":
        year = int(input("What's the year?: "))
        state = (input("What's the state?: "))
        population = int(input("What's the population?: "))
        master_list.append([year, state, population])
        x = input("Would you like to continue? (yes or no): ")

    #Starts the main addition of the function
    main_year = int(input("What year would you like to add up?: "))
    sum_population_for_year(master_list, main_year)

# adds together all the populations from each year
def sum_population_for_year(all_entered_values, year_to_sum):
    x = 0
    total = 0
    while x < len(all_entered_values):
        if all_entered_values[x][0] == year_to_sum:
            total += all_entered_values[x][2]
            x += 1
        else:
            x += 1
    print("The total population is", total)

# Call the main function.
if __name__ == '__main__':
    main()
