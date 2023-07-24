def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    if fee <=30:
        fee = 30
    elif fee >= 600:
        fee = 600
    return fee

def calculate_interest(amount):
    return amount * 0.03

def calculate_wealth_tax(balance,amount):
    if balance > 5000000:
        print("налог на богатство: ", amount * 0.1)
        return amount * 0.1
    return 0

def main():
    balance = 0
    transaction_count = 0
    file = []

    while True:
        print("Доступные действия: пополнить-1, снять-2, выйти-3")
        action = input("Введите действие: ")

        if action == "1":
            deposit = int(input("Введите сумму пополнения: "))
            while deposit % 50 != 0:
                deposit = int(input("Сумма пополнения кратны 50: "))

            transaction_count += 1
            if transaction_count % 3 == 0:
                interest = calculate_interest(deposit)
                balance += interest
                print("процента после каждой третьей операции", interest)

            balance += deposit
            wealth_tax = calculate_wealth_tax(balance,deposit)
            balance -= wealth_tax
            file.append(deposit)
            file.append(balance)

        elif action == "2":
            transaction_count += 1
            withdrawal = int(input("Введите сумму снятия: "))
            while withdrawal>balance:
                print('Nedostatochno Sredstv')
                withdrawal = int(input("Введите Другую сумму: "))
            while deposit % 50 != 0:
                deposit = int(input("Сумма снятия кратны 50: "))

            if transaction_count % 3 == 0:
                interest = calculate_interest(withdrawal)
                balance += interest
                print("процента после каждой третьей операции", interest)

            withdrawal_fee = calculate_withdrawal_fee(withdrawal)
            balance -= withdrawal + withdrawal_fee
            wealth_tax = calculate_wealth_tax(balance,withdrawal)
            balance -= wealth_tax
            print("комиссии за снятие: ", withdrawal_fee)
            file.append(deposit)
            file.append(balance)

        elif action == "3":
            wealth_tax = calculate_wealth_tax(balance,balance)
            balance -= wealth_tax
            print("Ваш баланс: ", balance)
            break
                
        print("Ваш баланс: ", balance)
        print (file)
        

main()
