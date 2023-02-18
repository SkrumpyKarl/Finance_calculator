"""T06 CAPSTONE PROJECT TASK 1

START,
Print programme introduction.
Request user select 'investmenet' or 'bond', lower,
If else user select investment,
    Request variables based on interest formula,
        Nest if else, on investment for 'simple' vs 'compound' interest,
         Calculate simple interest,
         Print output,
    Else compound, on bond, request variables , 
        Calculate compound interest,
        Print output,
Elif user selects bond
    Request variables based on bond formula,
    Calculate bond repayment value,
    Print output,
Else
    Print user input error message
Print closing message,
END.

"""
# ***************SMALL FINANCIAL COMPANY LTD - FIANCE CALCULATORS**************

"""Finance Calculators and related operations.
    
This programme is for sole use by SMALL FINANCIAL COMPANY LTD (SFC) and shall 
only be used for the purposes of allowing users to review investment returns 
or mortgage debt. 
"""

# Modulus and related operations & variables.
import math

line_space = "-------------------------------------------------------------" \
             "-------------------------------------------------------------"
# To print terminal line divider, presentation.

# SFC welcome and  available products with calculators.
print("\nWelcome to Small Financial Company Ltd.")
print(line_space)
print("\nChoose either 'investment' or 'mortgage' from the menu below to" \
      " proceed :\n")

    # SFC Products Menu.
print("Investment\t-\tto calcluate the amount of interest you'll earn on" \
      " your investment. Enter 'investment'.")
print("Mortgage\t-\tto calcluate the amount you'll have to pay on a home" \
      " loan. Enter 'mortgage'.\n")

user_calculate = input("Please choose a calculator 'name' : ").lower()

# Command Structure for Calculators.
if user_calculate == 'investment':
    # Investment calculator branch, request and store variables.
    print("\n" + line_space)
    print("Investment Calculator")
    print(line_space)
    interest_typ_txt = print("\nChoose either 'simple' or 'compound' from" \
                             " the menu below to proceed : \n" )
    print("Simple\t\t-\tto calcluate the amount of interest you'll earn per" \
          " year on the principal amount. Enter 'simple'.")
    print("Compound\t-\tto calcluate the amount of interest you'll earn per" \
          " year on any accumulated amount. Enter 'compound'.\n")
    user_interest = input("Please choose a 'interest type' : ").lower() 
    inv_p = float(input("\nPlease enter the value of your deposit in GBP" \
                       " (£) \t\t: "))
    inv_t = int(input("Please enter the number of years you plan on" \
                      " investing for \t: "))
    inv_r = float(input("Please enter the annual interest rate" \
                        " (as a percentage '%') \t: ")) / 100  

    if user_interest == 'simple':
        # Investment calculator branch, simple interest once per year.
        inv_simple_a = round((inv_p * (1+inv_r*inv_t)),2)  
        print("\nYour total amount would be £{:.2f} after {} years.\n"\
                .format(inv_simple_a,inv_t))
    
    elif user_interest == 'compound':
        # Investment calculator branch, compound interest once per year.
        inv_compound_a = round((inv_p * math.pow((1+inv_r),inv_t)),2)
        print("\nYour total amount would be £{:.2f} after {} years.\n"\
                .format(inv_compound_a,inv_t))  
    else:
        print("Error - undefined interest type. Please enter a correct" \
              " interest type.\n")
        
elif user_calculate == 'mortgage':
    # mortgage calculator branch, request and store variables.
    print("\n" + line_space)
    print("Mortgage Calculator")
    print(line_space)
    mort_p = float(input("\nPlease enter the present value of your house" \
                        " in GBP (£) \t\t\t: "))
    mort_n = int(input("Please enter the number of months you plan on taking" \
                    " to repay this mortgage \t: "))
    mort_i = float(input("Please enter the annual interest rate" \
                        " (as a percentage '%') \t\t\t: ")) / (12 * 100)  
    
    # Mortgage calculator function
    mort_x = round(((mort_i*mort_p) / (1-math.pow((1+mort_i),(-mort_n)))),2)
    print("\nYour total mortgage repayment cost per month would be £{:.2f}.\n"\
            .format(mort_x))  
else:
    # Incorrect calculator selection, error message, close command structure.
    print("\nError - undefined calculator entered. Please only select from" \
          " the menu.\n")
 
#Terminate
print(line_space)
print("SFC Ltd thanks you for your time.")  
print(line_space+"\n")

"""End Notes on T07

Attempting to follow PEP8 Style guide concerning line length @79 characters,
comments, whitespace in expressions and statements, and blank lines. 
There is still a bit to learn moving forwards. 
"""