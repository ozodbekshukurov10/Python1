import json
import os

class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id


class Account:
    def __init__(self, account_id, password, balance=0):
        self.account_id = account_id
        self.password = password
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({"type": "deposit", "amount": amount})
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append({"type": "withdraw", "amount": amount})
            return self.balance
        else:
            return "Not enough balance!"

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class Customer(Person):
    def __init__(self, name, age, person_id, account):
        super().__init__(name, age, person_id)
        self.account = account

    def check_balance(self):
        return self.account.get_balance()

    def deposit_money(self, amount):
        return self.account.deposit(amount)

    def withdraw_money(self, amount):
        return self.account.withdraw(amount)

    def transaction_history(self):
        return self.account.get_transactions()


class Worker(Person):
    def __init__(self, name, age, person_id):
        super().__init__(name, age, person_id)

    def create_account(self, account_id, password):
        return Account(account_id, password)

    def add_customer(self, name, age, person_id, account):
        return Customer(name, age, person_id, account)


class Bank:
    def __init__(self, name, filename="bank_full.json"):
        self.name = name
        self.filename = filename
        self.data = self.load_json()

    def load_json(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "accounts" not in data:
                    data["accounts"] = {}
                return data
        else:
            return {"bank_name": self.name, "accounts": {}}

    def save_json(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

    def add_account(self, customer):
        acc = customer.account
        self.data["accounts"][acc.account_id] = {
            "name": customer.name,
            "age": customer.age,
            "id": customer.person_id,
            "password": acc.password,
            "balance": acc.balance,
            "transactions": acc.transactions
        }
        self.save_json()

    def update_account(self, customer):
        acc = customer.account
        self.data["accounts"][acc.account_id]["balance"] = acc.balance
        self.data["accounts"][acc.account_id]["transactions"] = acc.transactions
        self.save_json()

    def login(self, account_id, password):
        if account_id in self.data["accounts"]:
            acc_data = self.data["accounts"][account_id]
            if acc_data["password"] == password:
                acc = Account(account_id, password, acc_data["balance"])
                acc.transactions = acc_data["transactions"]
                customer = Customer(acc_data["name"], acc_data["age"], acc_data["id"], acc)
                return customer
        return None


def worker_menu(bank, worket):
    print('1-yangi mijoz uchun accaunt ochish')
    print('2-barcha accaunlardi korish')
    print('3-chiqish')

    choise = input('tanlov: ')

    if choise == '1':
        name = input('ism: ')
        age = input('yosh: ')
        person_id = input('mijoz id: ')
        accaunt_id = input('accaunt id: ')
        password = input('password kiriting: ')

        Account = Worker.create_account(accaunt_id, password)
        customer = Worker.add_customer(name, age, person_id, Account)
        Bank.add_account(customer)
        print('accaunt yaratildi')

    elif choise == '2':
        print('accauntlar')
        for acc_id, acc_data in bank.data['accaunts'].items():
            print(f'id: {acc_id}  ism: {acc_data['name']}, balans: {acc_data['balance']}')

    elif choise == '3':
        print('chiqildi')


    else: 
        print('xatolik')



def customer_menu(bank, customer):
    while True:
        print("1 - Balansni korish")
        print("2 - Pul qoshish")
        print("3 - Pul yechish")
        print("4 - Tranzaksiyalar tarixi")
        print("5 - Chiqish")

        choice = input("Tanlov: ")

        if choice == "1":
            print("Balans:", customer.check_balance())

        elif choice == "2":
            amount = int(input("Qoshiladigan summa: "))
            customer.deposit_money(amount)
            bank.update_account(customer)
            print("Pul qo‘shildi!")

        elif choice == "3":
            amount = int(input("Yechiladigan summa: "))
            result = customer.withdraw_money(amount)
            bank.update_account(customer)
            print("Natija:", result)

        elif choice == "4":
            print("Tranzaksiyalar:", customer.transaction_history())

        elif choice == "5":
            print("Mijoz menyusidan chiqildi.")
            break

        else:
            print(" Notogri tanlov!")


def main():
    bank = Bank("MyBank")
    worker = Worker("Ali", 30, "W001")

    while True:
        print("1 - Yangi account ochish")
        print("2 - Accountga kirish")
        print('3-ishchi sifatida kirish')
        print("4 - Chiqish")

        choice = input("Tanlovingiz: ")

        if choice == "1":
            name = input("Ism: ")
            age = int(input("Yosh: "))
            person_id = input("ID: ")
            account_id = input("Account ID: ")
            password = input("Parol: ")

            account = worker.create_account(account_id, password)
            customer = worker.add_customer(name, age, person_id, account)
            bank.add_account(customer)
            print(" Account yaratildi!")

            customer_menu(bank, customer)

        elif choice == "2":
            acc_id = input("Account ID: ")
            pwd = input("Parol: ")
            customer = bank.login(acc_id, pwd)

            if customer:
                print(f"Xush kelibsiz, {customer.name}!")
                customer_menu(bank, customer)
            else:
                print(" Account ID yoki parol xato!")

        elif choice == '3':
            worker_id = input('ishchi id: ')
            if worker_id in worker:
                worker_menu(bank, worker[worker_id])

        elif choice == "4":
            print("Dastur tugadi.")
            break

        else:
            print(" Noto‘g‘ri tanlov!")

        


if __name__ == "__main__":
    main()
