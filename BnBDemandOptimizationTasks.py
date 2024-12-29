# Display team information
print("Programming Team:\n1. 23i-0653\n2. 23i-0696\n3. 23i-0732\nPress any key to continue")
input()

# Function to calculate demand of BnB
def demand_bnb(P_B, P_A, P_C):
    # Calculate demand of BnB using given formula
    return round((10000 - 2.5 * P_B**2 + 3 * P_A + 1.5 * P_C), 2)

# Function to calculate demand of BnB after a price increase
def demand_bnb_after(P_B, P_A, P_C):
    # Calculate demand of BnB after a price increase using given formula
    return round((10000 - 2.5*(P_B*1.2)**2 + 3*1.2*P_A + 1.5*1.2*P_C), 2)

# Loop for continuous execution of the program
while True:
    # Task 1: Displaying initial demand of BnB
    print("\nTask 1:")
    P_B = P_A = P_C = 100  # Prices of all products are initially $100 each
    print("Demand of BnB when all prices are $100 each:", demand_bnb(P_B, P_A, P_C))
    
    # Task 2: Calculating derivative of demand of BnB with respect to price of BnB
    print("\nTask 2:")
    def derivative_bnb_wrt_price_B(P_B):
        # Calculate the derivative of demand of BnB with respect to price of BnB
        return round((-2.5*1.2 *2*1.2), 2)
    print("Derivative of demand of BnB with respect to price of BnB:", derivative_bnb_wrt_price_B(P_B), "P_B")
    
    # Task 3: Calculating derivative of demand of BnB with respect to price of product A
    print("\nTask 3:")
    def derivative_bnb_wrt_price_A(P_A):
        # Calculate the derivative of demand of BnB with respect to price of product A
        return round((3*1.2), 2)
    print("Derivative of demand of BnB with respect to price of product A:", derivative_bnb_wrt_price_A(P_A))
    
    # Task 4: Suggestions to increase demand of BnB
    print("\nTask 4:\nTo increase demand of BnB, the company should consider reducing the price of BnB.")
    print("Additionally, improving product features or increasing advertising might help in increasing demand.")
    
    # Program termination or continuation based on user input
    choice = input("\nDo you wish to run another query? (Y/N): ").strip().lower()
    if choice == 'n':
        # If user chooses not to run another query, terminate the program
        print("Program terminated.")
        break
