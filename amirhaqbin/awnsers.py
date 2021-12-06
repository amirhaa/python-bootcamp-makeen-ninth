_wallet_value = 100

def wallet_increase(x):
    global _wallet_value
    _wallet_value = _wallet_value + x

wallet_increase(10)    

def wallet_decrease(y):
    global _wallet_value
    _wallet_value = _wallet_value - y
    
wallet_decrease(20)
 
def wallet_value():

    return _wallet_value

print(wallet_value())