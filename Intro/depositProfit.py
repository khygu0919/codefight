'''
You have deposited a specific amount of dollars into your bank account. Each year your balance increases at the same growth rate. Find out how long it would take for your balance to pass a specific threshold with the assumption that you don't make any additional deposits.
'''
def depositProfit(deposit, rate, threshold):
    deposit=float(deposit)
    rate = float(rate)
    i=0
    while (deposit<threshold):
        deposit=deposit*(1+rate/100)
        i+=1
    return i