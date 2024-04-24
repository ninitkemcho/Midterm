def add_balance(iban, amount, db):
    for account in db:
        if account['iban']==iban:
            account['amount']=amount
    return db


def check_float(amount): 
    amount_float=False
    if amount.replace('.','',1).isdigit():
        amount_float=True
    return amount_float