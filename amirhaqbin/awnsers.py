#_wallet_value = 100

#def wallet_increase(x):
    #global _wallet_value
    #_wallet_value = _wallet_value + x

#wallet_increase(10)    

#def wallet_decrease(y):
    #global _wallet_value
   # _wallet_value = _wallet_value - y

#wallet_decrease(20)
 
#def wallet_value():

    #return _wallet_value

#print(wallet_value())
# print('.......................................')

# class Wallet:

#     def __init__(self, holding):
#         self.wallet = holding
#     def deposit_balance(self, add):    
#         self.wallet += add
#     def withdraw_balance(self, increase):        
#         self.wallet -= increase
#     def balance(self):
#         return self.wallet

# w1 = Wallet(100) 
# w1.deposit_balance(20)
# w1.withdraw_balance(5)
# print(w1.balance())



# class UnRegisteredUser:
#     def __init__(self, name, username):
#         self.name = name
#         self.username = username
    
#     def view_blog_post(self):
#         return True

#     def comment(self):
#         print(f"You can not do this action")
#         return False


#     def delete(self):
#         print(f"You can not do this action")
#         return False
    

# class RegisteredUser(UnRegisteredUser):
#     def __init__(self, name, username):
#         super().__init__(name, username)
    
#     def write_comment(self, comment):
#         return f"{comment}\n {self.name} @{self.username}"

#     def comment(self):
#         return super().comment(True)
        
# class Admin(RegisteredUser):
#     def delete(self):
#         return True
