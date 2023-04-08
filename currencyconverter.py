
def main():

    print('This program converts US dollars to Indian Rupees')

    dollars = eval(input("enter amount in dollars: "))

    rupees = convert_to_rupees(dollars)

    print('this is',rupees,"rupees. ")

convert_to_rupees = lambda dollars: dollars * 81.80

main()