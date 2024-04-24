def transfer(sender_iban, receiver_iban, amount, db):
    for account in db:
        if account['iban']==sender_iban:
            account['amount']-=amount
        elif account['iban']==receiver_iban:
            account['amount']+=amount
    return db

def is_enough(sender_iban, amount, db):
    amount_enough=False
    for account in db:
        if account['iban']==sender_iban and account['amount']>=amount:
            amount_enough=True
    return amount_enough