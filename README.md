# Bank-Accounts

## Description

Python program using OOP to implement two classes of bank account: BasicAccount and PremiumAccount.

<br/>
The basic account has the following methods:

1. deposit
Deposits the stated amount into the account and adjusts the balance appropriately.

2. withdraw
Withdraws the stated amount from the account and adjusts the balance appropriately.

3. getAvailableBalance
Returns the total balance that is available in the account. It should also take into account any overdraft that is available.

4. getBalance
Returns the balance of the account. If the account is overdrawn, then it should return a negative value.

5. printBalance
Should print to screen in a sensible way, the balance of the account. If an overdraft is available, then this should also be printed and it should show how much overdraft is remaining.

6. getName
Returns the name of the account holder.

7. getAcNum
Returns the account number as a string.

8. issueNewCard
Creates a new card number, with the expiry being 3 years to the month from now. (e.g. if today is 3/12/20, then the expiry date would be (12/23)).

9. closeAccount
To be called before deleting of the object instance. Returns any balance to the customer (via the withdraw method) and returns True.
Returns False if the customer is in debt to the bank.
N.B. shouldn't actually delete the account instance; this function simply does the relevant house keeping.

<br/>
The premium account has the following additional/amended methods:

1. setOverdraftLimit
Sets the overdraft limit to the stated amount

2. getAvailableBalance

3. printBalance

4. closeAccount
 
<br/>
## Libraries

- random
- datetime


