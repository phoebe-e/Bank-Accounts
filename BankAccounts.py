#Phoebe Edwards (200786023)
#COMP517 Assignment 4


#LIBRARIES

import random 
import datetime


#FUNCTIONS

#Account number generator function
theAcNum = 0
def acNumGenerator():
    """
    Assigns account numbers in a serial manner

    Parameters:
        None
    Returns:
        theAcNum (int) - identifies an account
    """
    #Adds 1 to the previous account number each time a new account is created
    global theAcNum
    theAcNum += 1
    return theAcNum


usedCardNums = []
#Card number generator function
def cardNumGenerator():
    """
    Randomly generates a unique card number

    Parameters:
        None
    Returns:
        theCardNum (str) - 16 digit number associated with an account
    """
    #While loop to check if card number has already been used. If so, new number is generated;
    #If not, number is added to the usedCardNums list and the candidate card number becomes theCardNum
    candidateCardNum = random.randint(1000000000000000, 9999999999999999)
    while(candidateCardNum in usedCardNums):
        candidateCardNum = random.randint(1000000000000000, 9999999999999999)
    usedCardNums.append(candidateCardNum)
    global theCardNum
    theCardNum = candidateCardNum
    return str(theCardNum)


#Card expiry date generator function
def cardExpGenerator():
    """
    Sets the expiry date of each new card

    Parameters:
        None
    Returns:
        theCardExp (tuple) - the date 3 years in the future
    """
    today = datetime.datetime.now()
    global theCardExp
    #Adds 3 years to the current date
    expYear = today.replace(year=today.year+3)
    #Date represented as a tuple, as required by the brief
    theCardExp = (today.strftime("%m"), expYear.strftime("%y"))
    return theCardExp
 

#CLASS METHODS

#Define Basic Account class
class BasicAccount:
    """ BasicAccount is the superclass account type available to all registered customers"""

    #Initialiser definition
    def __init__(self, acName, openingBalance):
        """
        Initialiser - creates an account number (acNum), card number (cardNum) and a card expiry date (cardExp) for each new customer

        Parameters:
            acName - the name of the account holder
            openingBalance - the opening balance of the account (essentially the first deposit)
        Returns:
            Nothing
        """
        #Need to ensure that acName is a string and that openingBalance is a float > 0, but unsure of how to execute
        self.name = acName
        self.acNum = acNumGenerator()
        self.balance = openingBalance 
        self.cardNum = cardNumGenerator()
        self.cardExp = cardExpGenerator()


    #Default string representation definition
    def __str__(self):
        """
        Returns a string representation of account information.
 
        Parameters:
            None
        Returns:
            String
        """            
        return "\n" + self.name + " has a Basic Account. They have an available balance of £{:.2f}.".format(self.balance) + " There is no overdraft associated with the Basic Account."


    #Deposit definition
    def deposit(self, amount):
        """
        Deposits money into the relevant account

        Parameters:
            amount (float) - amount to be depositted in £
        Returns:
            Nothing   
        """        
        print("\n*DEPOSIT*")
        #Conditions to ensure a positive amount is depositted
        if(amount < 0):
                print("Can not deposit a negative value.")
        elif(amount == 0):
                print("Can not deposit £0.00")
        elif(amount > 0):
            print(self.name, "has deposited £{:.2f}".format(amount))
            self.balance += amount
            print("New balance is £{:.2f}".format(self.balance))


    #Withdrawal definition
    def withdraw(self, amount):
        """
        Withdraws money from the relevant account

        Parameters:
            amount (float) - amount to be withdrawn in £
        Returns:
            Nothing 
        """    
        print("\n*WITHDRAWAL*")
        #Conditions to ensure a positive amount is withdrawn and sufficient funds are available
        if(self.getAvailableBalance() < amount):
            print("Can not withdraw £{:.2f}".format(amount))
        elif(amount < 0):
            print("Can not withdraw negative value.")
        elif(amount == 0):
            print("Can not withdraw £0.00")
        elif(amount > 0 and self.getAvailableBalance() >= amount):
            print(self.name, "has withdrew £{:.2f}".format(amount))
            self.balance -= amount
            print("New balance is £{:.2f}".format(self.balance))            


    #Get available balance definition
    def getAvailableBalance(self):
        """
        Returns the available balance as a float

        Parameters:
            None
        Returns:
            balance (float) - the amount of money in the account
        """            
        return self.balance


    #Get balance definition
    def getBalance(self):
        """
        Returns the actual balance. For the Premium Account, a negative value will be printed if the account is overdrawn

        Parameters:
            None
        Returns:
            balance (float) - the amount of money in the account
        """ 
        return self.balance


    #Print balance definition
    def printBalance(self):
        """
        Prints the actual and available balance.

        Parameters:
            None
        Returns:
            Nothing   
        """ 
        #Uses previously defined functions of getBalance and getAvailableBalance, then collates the information
        print("\n*PRINTED BALANCE*")
        print(self.name + "'s balance: £{:.2f}".format(self.getBalance()))
        print(self.name + "'s available balance: £{:.2f}".format(self.getAvailableBalance()))
        print("There is no overdraft associated with the Basic Account.")


    #Get name definition
    def getName(self):
        """
        Returns the name of the account holder

        Parameters:
            None
        Returns:
            name (str) - the name of the account holder
        """ 
        print("\n*ACCOUNT HOLDER*")
        print("The account holder's name is: " + self.name)
        return self.name


    #Get account no. definition
    def getAcNum(self):
        """
        Returns the account number of an account holder

        Parameters:
            None
        Returns:
            acNum (string) - the account number as a string
        """ 
        print("\n*ACCOUNT NUMBER*")
        print("The account number of", self.name, "is:", self.acNum)
        #acNum returned as string, as required by the brief
        return str(self.acNum)


    #Issue new card definition
    def issueNewCard(self):
        """
        Issues a new card number and expiry date using the previously defined functions of cardNumGenerator() and cardExpGenerator().

        Parameters:
            None
        Returns:
            Nothing   
        """ 
        print("\n*NEW CARD ISSUE*")
        #Uses previously defined function to issue a new card number and card expiry date
        cardNumGenerator()
        self.cardNum = theCardNum
        cardExpGenerator()
        self.cardExp = theCardExp
        print(self.name + "'s new card number is:", self.cardNum)
        print("Expiry date:", self.cardExp)

    
    #Account closure definition
    def closeAccount(self):
        """
        Determines if an account can be closed and, if necessary, prepares for the closure 

        Parameters:
            None
        Returns:
            closable (boolean) - returns True if the account is ready to close
        """ 
        print("\n*ACCOUNT CLOSURE*")
        #Checks if the account contains money and makes a withdrawal (if necessary) before allowing for an account closure
        if(self.balance > 0):
            self.withdraw(self.balance)
            closable = True
            print("The account is now ready to close.")
        elif(self.balance == 0):
            print(self.name + "'s account balance is £0.00.")
            closable = True
            print("The account is now ready to close.")          
        return closable



#Define Premium Account class
class PremiumAccount(BasicAccount):
    """ PremiumAccount is the account type that offers an overdraft, alongside Basic Account functions"""

    #Initialiser definition
    def __init__(self, acName, openingBalance, initialOverdraft):
        """
        Initialiser - creates an account number (acNum), card number (cardNum), card expiry date (cardExp) sets the overdraft status for each new customer

        Parameters:
            acName (str) - the name of the account holder
            openingBalance (float) - the opening balance of the account (essentially the first deposit)
            initialOverdraft (float) - overdraft value at account opening
        Returns:
            Nothing
        """
        super().__init__(acName, openingBalance)
        #Sets overdraft to False is the overdraft limit is £0.00 at initialisation. Can be changed at a later point using the changeOverdraftStatus method
        if(initialOverdraft <= 0):
            self.overdraft = False
        elif(initialOverdraft > 0):
            self.overdraft = True

        self.overdraftLimit = initialOverdraft
        
        

    #Default string representation definition
    def __str__(self):
        """
        Returns a string representation of account information.
 
        Parameters:
            None
        Returns:
            str - account name, balance and overdraft
        """           
        return self.name + " has a Premium Account. They have an available balance of £{:.2f},".format(self.balance + self.overdraftLimit) + " an overdraft status of " + str(self.overdraft) + " and an overdraft limit of £{:.2f}.".format(self.overdraftLimit)


    #Change overdraft status definition
    def changeOverdraftStatus(self):
        """
        Changes overdraft status of Premium Account, so that an overdraft can subsequently be set for an account which initally returns overdraft = False (and vice versa)

        Parameters:
            None
        Returns:
            Nothing    
        """
        print("\n*CHANGE OVERDRAFT STATUS*")
        #Conditions to ensure overdraft is not removed from an overdrawn account
        if(self.overdraft is False):
            self.overdraft = True
            print(self.name, "now has an overdraft available.")        
        elif(self.overdraft is True and self.balance >= 0):
            self.setOverdraftLimit(0)
            self.overdraft = False
            print(self.name, "no longer has an overdraft.")
        elif(self.overdraft is True and self.balance < 0):
            self.overdraft = True
            print("Cannot remove overdraft as still in use.")
            print("A deposit of £{:.2f}".format(-1*self.balance), "must first be made.")


    #Overdraft limit definition
    def setOverdraftLimit(self, newLimit):
        """
        Sets the overdraft limit if the customer is eligible

        Parameters:
            newLimit (float) - the desired overdraft amount
        Returns:
            Nothing
        """
        print("\n*SET OVERDRAFT LIMIT*")
        #Conditions to ensure that the new overdraft limit is positive, can only be set for eligible clients and is not of a lower value than the amount already overdrawn
        if(newLimit < 0):
            print("This is not a valid overdraft limit.")
        elif(self.overdraft is False):
            print(self.name, "is not eligible for an overdraft.")
        elif(self.balance*-1 > newLimit):
            print("The new overdraft limit must be more than the amount overdrawn.")
        elif(newLimit >= 0 and self.overdraft is True and self.balance*-1 <= newLimit):
            print("Updating", self.name + "'s overdraft limit...")
            self.overdraftLimit = newLimit
            print("New limit: £{:.2f}".format(self.overdraftLimit))


    #Overide getAvailableBalance method
    def getAvailableBalance(self):
        """
        Overides Basic Account getAvailableBalance(). Takes the overdraft into consideration

        Parameters:
            None
        Returns:
            Nothing 
        """    
        if(self.balance + self.overdraftLimit > 0):
            availableBalance = self.balance + self.overdraftLimit
        else:
            availableBalance = 0
        return availableBalance


    #Overide printBalance function
    def printBalance(self):
        print("\n*PRINTED BALANCE*")
        """
        Overides Basic Account printBalance(). Takes the overdraft into consideration and utilises the previously defined methods: getBalance() and getAvailaleBalance().
        Also, prints information about overdraft limit and overdraft remainder.

        Parameters:
            None
        Returns:
            Nothing 
        """  
        print(self.name + "'s balance: £{:.2f}".format(self.getBalance()))
        print(self.name + "'s available balance: £{:.2f}".format(self.getAvailableBalance()))
        if(self.overdraft is True):
            print("There is an overdraft associated with this account.")
            if(self.balance >= 0):
                print("The limit is £{:.2f}".format(self.overdraftLimit), "and the remaining balance is £{:.2f}.".format(self.overdraftLimit))
            else:
                print("The limit is £{:.2f}".format(self.overdraftLimit), "and the remaining balance is £{:.2f}.".format(self.overdraftLimit + self.balance))
        else:
            print(self.name, "does not have an overdraft.")


    #Overide closeAccount definition
    def closeAccount(self):
        """
        Determines if an account can be closed and, if necessary, prepares for the closure 

        Parameters:
            None
        Returns:
            closable (boolean) - returns True if the account is ready to close
        """ 
        print("\n*ACCOUNT CLOSURE*")
        #Conditions to ensure that the account is not overdrawn
        if(self.balance > 0):
            self.withdraw(self.balance)
            closable = True
            print("The account is now ready to close.")
        elif(self.balance == 0):
            print(self.name + "'s account balance is £0.00.")
            closable = True
            print("The account is now ready to close.")          
        else:
            print("Can not close account due to customer being overdrawn by £{:.2f}".format(-1*self.balance))
            closable = False        
        return closable

