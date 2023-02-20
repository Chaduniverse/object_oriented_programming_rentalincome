# define class
class Rental_property_analysis():
    def __init__(self):
        self.address = ""
        self.rental_income = 0
        self.expenses = 0
        self.profit = 0
        self.cash_roi = 0
        self.cashflow = {} 

#calculate income function 
    def calculate_income(self):
        rental_income = int(input(
            'How much is your total monthly income from the property in usd (add income from rents,laundry,storage,and miscellaneous income)? '))
        self.cashflow['total_income'] = rental_income
        print(f'Your total monthly rental_income is {rental_income} usd.')

#calculate expenses function
    def calculate_expenses(self):
        print("Lets calculate your total monthly expenses.")
        a = int(input('How much is your monthly mortgage? '))
        b = int(input('Taxes? '))
        c = int(input('Insurance? '))
        d = int(input('Utilities (electric,water,sewer,garbage)? '))
        e = int(input('HOA fees? '))
        f = int(input('Lawn care?'))
        g = int(input('Vacancy? '))
        h = int(input('Repairs? '))
        i = int(input('CapEx? '))
        j = int(input('Property Management? '))
        expenses =  a + b + c + d + e + f + g + h + j 
        self.cashflow['total_expenses'] = expenses
        print("Your total expenses is" + " " + str(expenses) + " " + "usd.") 

#calculate cashflow function

    def calculate_cashflow(self):
        print("Now lets calculate your total monthly cashflow by subtracting your total income from your total amount of expenses. ")
        profit = self.cashflow['total_income'] - self.cashflow['total_expenses']
        self.cashflow['cashflow'] = profit
        print('Your monthly cashflow is' + ' ' + str(profit) + ' ' + 'usd.') 

#calculate cash on cash return on investment

    def cash_on_cash(self):
        print('Now lets calculate your total cash investment.')
        a = int(input("How much is your down payment? "))
        b = int(input("Estimated closing costs? "))
        c = int(input("Rehab budget?"))
        d = int(input("Misc. other?"))
        total_investment =  a + b + c + d 
        cash_roi = (self.cashflow['cashflow'] * 12 / total_investment) * 100
        print(f'Your total cash on cash return on investment is {cash_roi}%. Good bye!')  

    #define runner function

    def runner(self):
        while True:
            user_choice = input(
                "Would you like to analyze a a rental property? Type yes or no to quit. ").lower()
            if user_choice == 'no':
                print('Good Bye!')
                break
            else:
                self.calculate_income() 
                self.calculate_expenses()
                self.calculate_cashflow()
                self.cash_on_cash()



property1 = Rental_property_analysis()
property1.runner()
