def add_user(name, surname, iban, db):
    user_info={}
    user_info['name']=name
    user_info['surname']=surname
    user_info['iban']=iban
    user_info['amount']=0
    db.append(user_info)
    return db

def check_existance(iban, db):
    iban_exists=False
    for account in db:
        if account['iban']==iban:
            iban_exists=True
    return iban_exists

def check_validity(iban):
    validity=True
    if len(iban)!=5 or iban[0:2]!='TB':
        validity=False
    return validity
