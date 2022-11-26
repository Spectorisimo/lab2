bank_account=100
def add_to_bank_account(amount:float) -> float:
    return bank_account+amount
def substract_from_bank_account(amount:float) -> float:
    return bank_account-amount
def money_conversion(amount:float,usd:bool) -> float:
    if usd is True:
        return str(amount*470)+" ₸"
    return str(round(amount/470,2))+" $"
print(add_to_bank_account(100))
print(substract_from_bank_account(10))
print(money_conversion(300,True))
print(money_conversion(141000,False))
