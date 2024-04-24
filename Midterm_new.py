import user
import balance
import transfer

print('________Menu________')
print('\n1. Add user')
print('2. Fill balance')
print('3. Transfer money')
print('4. Exit')

db=[]

while True:
    answer=int(input('Enter a corresponding number for action: '))
    
    if answer==1:
        name=input('Enter your name: ')
        surname=input('Enter your surname: ')
        while True:
            iban=input('Enter your IBAN: ')
            if not user.check_validity(iban):
                print('\nINVALID IBAN')
            else:
                if not user.check_existance(iban, db):
                    print('Registration was successful!')
                    user.add_user(name,surname,iban,db)
                    break
                else:
                    print(f'\nUser with {iban} already exists')
                
    elif answer==2:
        while True:
            iban=input('Enter IBAN to add balance: ')
            if not user.check_validity(iban):
                print('\nINVALID IBAN')
                continue
            if not user.check_existance(iban, db):
                print(f'\nUser with {iban} do not exist')
                continue
            else:
                break
            
        while True:
            amount=input('Enter amount to fill in balance: ')
            if balance.check_float(amount):
                amount=float(amount)
                balance.add_balance(iban, amount, db)
                print(f'{iban} was filled in with ${amount}')
                break
            else:
                print('INVALID NUMBER')
    
    elif answer==3:
        while True:
            sender_iban=input("Enter sender's IBAN: ")
            if not user.check_validity(sender_iban):
                print('\nINVALID IBAN')
                continue
            if not user.check_existance(sender_iban, db):
                print(f'\nUser with {sender_iban} do not exist')
                continue
            else:
                break
            
        while True:
            receiver_iban=input("Enter reciever's IBAN: ")
            if not user.check_validity(receiver_iban):
                print('\nINVALID IBAN')
                continue
            if not user.check_existance(receiver_iban, db):
                print(f'\nUser with {receiver_iban} do not exist')
                continue
            else:
                break
            
        while True:
            amount=input('Enter amount to transfer: ')
            if balance.check_float(amount):
                amount=float(amount)
                break
            else:
                print('INVALID NUMBER')
                continue
            
        if not transfer.is_enough(sender_iban, amount, db):
            print('\nNot enough balance')
        else:
            transfer.transfer(sender_iban,receiver_iban,amount,db)
            print(f'Succesfully transfered to {name} {surname}')
        
    elif answer==4:
        break
    else:
        print('\nINVALID ACTION')
        






