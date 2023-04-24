# Checked a stackoverflow site on how to round to 2 decimals then implimended code.
#https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

''' I hope i didnt make things to complicated, I wanted to make sure the user could only input the correct values, and to
notify if the wrong input had been entered. I also wanted the questions to loop if they were entered incorectly instead of going to the start.
Thanks!'''

import math
i = 0
j = 0

while True:

    # Checks inputs for opening question.
    print("\nInvestment   - to calculate the amount of interest you'll earn on your investment.")
    print("Bond         - to calculate the amount you'll have to pay on a home loan.\n")

    user_input1 = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")
    user_input1 = user_input1.lower()

    if user_input1 == "investment":
            i += 1

    if user_input1 == "bond":
            j += 1

    if i == 0 and j == 0:
        print("\nInvalid input, please re-enter.")

    # Checks inputs dealing with investment deposit.
    while i == 1:
        money_deposited = input("\nPlease enter the amount of money you wish to deposit: ")
        try:
            money_deposited = int(money_deposited)        
        except ValueError:
            print("\nInvalid input, please enter numbers only.")
        if  type(money_deposited) == int and money_deposited > 0:
            i += 1

    # Checks inputs dealing with investment interest rate.
    while i == 2:
        investment_interest_rate = input("Please enter the interest rate as just a number (no % needed): ")
        try:
            investment_interest_rate = int(investment_interest_rate)
        except ValueError:
            print("\nInvalid Input, please enter numbers only.")
        if  type(investment_interest_rate) == int and investment_interest_rate > 0:
            i += 1
        
    # Checks inputs dealing with years of investment.
    while i == 3:
        investment_years = input("Please enter the number of years you plan to invest: ")
        try:
            investment_years = int(investment_years)
        except ValueError:
            print("\nInvalid Input, please enter numbers only.")
        if  type(investment_years) == int and investment_years > 0:
            i += 1

    # Checks inputs for simple or compund interest question.
    while i == 4:
        print("\nsimple   - if you would like simple interest.")
        print("compound - if you would like compound interest.")

        interest = input("\nPlease enter either 'simple' or 'compound' from the menu above to proceed: ")
        interest = interest.lower()

    # Investment interest formulas
        if interest == "simple":
            simple_total = money_deposited * ( 1 + investment_interest_rate / 100 * investment_years)
            simple_total = str(round(simple_total, 2))
            print("\nYour total investment return will be £" + simple_total)
            i += 1
            exit()
           

        if interest == "compound":
            compound_total = money_deposited * math.pow ((1 + investment_interest_rate / 100), investment_years)
            compound_total = str(round(compound_total, 2))
            print("\nYour total investment return will be £" + compound_total)
            i += 1
            exit()
            
        
        if i == 4:
            print("\nInvalid input, please re-enter.")

    ### Start of bond section ###
    # Checks input dealing with home value.
    while j == 1:
        home_value = input("\nPlease enter the value of your home: ")
        try:
            home_value = int(home_value)        
        except ValueError:
            print("\nInvalid input, please enter numbers only.")
        if  type(home_value) == int and home_value > 0:
            j += 1

    # Checks input dealing with bond interest rate.
    while j == 2:
        bond_interest_rate = input("Please enter the interest rate as a number (no % needed): ")
        try:
            bond_interest_rate = int(bond_interest_rate)        
        except ValueError:
            print("\nInvalid input, please enter numbers only.")
        if  type(bond_interest_rate) == int and bond_interest_rate > 0:
            j += 1

    # Checks input dealing with bond repayment.
    while j == 3:
        bond_repayments = input("Please enter the number of months you plan to take to repay the bond: ")
        try:
            bond_repayments = int(bond_repayments)        
        except ValueError:
            print("\nInvalid input, please enter numbers only.")
        if  type(bond_repayments) == int and bond_repayments > 0:
            j += 1

    # Bond interest formula.
    while j == 4:
        bond_interest_rate = bond_interest_rate / 100 / 12
        repayment = (bond_interest_rate * home_value) / (1 - (1 + bond_interest_rate) ** (- bond_repayments))
        repayment = str(round(repayment, 2))
        print("\nYou will be required to pay £" + repayment, "each month.")
        exit()
    