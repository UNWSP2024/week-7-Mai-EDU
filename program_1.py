# Programmer: Mai Lillie
# Date: 10/17/24
# Program #1: Rainfall
def main():
    rainfall = []

    #loop to get input from the user
    for x in range(0, 12):
        rainfall.append(float(input("What was the amount of rainfall this month?: ")))
        x += 1

    #organizes data into variables and does math
    rainfall.sort()
    total = sum(rainfall)
    average = total/12
    high = rainfall[-1]
    low = rainfall[0]

    #Prints the output
    print(f"Total: {total} \nAverage: {average:.1f} \nHigh: {high} \nLow: {low}")
main()
