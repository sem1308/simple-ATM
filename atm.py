from card import CARD
from bank import BANK
from enums import *
from utils import input_by_ui, error, is_return_home
from bank_num_name import bank_dict

class ATM:
    # TODO: change code like "print" for integrating ATM hardware

    def __init__(self, money : int, bank : BANK, card : CARD):
        self.money = money
        self.bank = bank
        self.card = card
        self.init()

    def init(self):
        ### card_info
        #{ "card_num": "0000000000000000",
        #  "valid_thru": ["yy", "mm"],
        #  "cvc": "000" }
        self.card_info = {}
        ### accounts_info
        # [{
        #   "bank_num" : -1,
        #   "bank_name" : "",
        #   "account_num" : "",
        #   "balance" : -1
        #   }, ...]
        self.accounts_info = []
        self.account = {}
        self.is_exit = False # is end ATM
        self.is_return_to_home = False # check error occurred
        self.is_error = False # check error occurred

    ### account menu ###
    def show_account_menu(self):
        print("\n=== Functions ===")
        for menu in AccountMenu:
            print(f"[{menu.value}] {menu.name}")
        print("select wanted num : ", end='')

    def select_account_menu(self):
        choice = input_by_ui()
        print()
        if choice == AccountMenu.SEE_BALANCE:
            self.see_balance(1)
        elif choice == AccountMenu.DEPOSIT:
            self.deposit()
        elif choice == AccountMenu.WITHDRAW:
            self.withdraw()
        elif choice == AccountMenu.HOME:
            print("return to home.")
            self.is_return_to_home = True
        else:
            print("select correct number")

    def see_balance(self, log = 0):
        if log : print(f"## SEE_BALANCE ##")
        print(f"balance : {self.account['balance']}$")
        return

    def deposit(self):
        print(f"## DEPOSIT ##")
        print("Enter amount of deposit money($) : ", end='')
        try :
            amount = int(input_by_ui())
        except :
            print("incorrect amount")
            return

        print("=== before balance ===")
        self.see_balance()

        self.account = self.bank.deposit(self.account["account_num"], amount)
        self.money += amount

        print(f"\n{amount}$ was deposited to {self.account['account_num']}")
        print("=== after balance ===")
        self.see_balance()

    def withdraw(self):
        print(f"## WITHDRAW ##")
        print("Enter amount of withdraw money($) : ", end='')
        try :
            amount = int(input_by_ui())
        except :
            print("incorrect amount")
            return

        if self.is_lack_cash(amount):
            print("withdrawl denied due to 'lack of cash of ATM'")
            return

        print("===== before balance =====")
        self.see_balance()
        self.account, is_lack = self.bank.withdraw(self.account["account_num"], amount)

        if is_lack :
            print("\nwithdrawl denied due to 'lack of balance'")
        else:
            print(f"\n{amount}$ was withdrawn from {self.account['account_num']}")
            self.money -= amount
        print("===== after balance =====")
        self.see_balance()
        return

    def is_lack_cash(self, amount):
        return self.money < amount

    ### main menu ###
    def show_main_menu(self):
        print("\n========= ATM =========")
        for menu in MainMenu:
            print(f"[{menu.value}] {menu.name}")
        print("select wanted num : ", end='')

    def select_main_menu(self):
        choice = input_by_ui()
        if choice != MainMenu.INSERT_CARD : self.is_exit = True

    ### card process ###
    def wait_insert_card(self):
        # TODO: change code for integrating ATM hardware
        return True

    def read_card(self):
        # TODO: change code for integrating ATM hardware
        self.is_error = True

        card_num = input("Enter card number (include '-') : ")
        # remove space and hyphen
        card_num = card_num.replace(" ", "").replace("-", "")
        if not self.card.validate_card_num(card_num) :
            print("incorrect card number")
            return

        valid_thru = input("Enter valid thru (ex 11/23) : ").split('/')
        if not self.card.validate_card_thru(card_num,valid_thru) :
            print("card is not valid")
            return

        cvc = input("Enter cvc (ex 012) : ")
        if not self.card.validate_card_cvc(card_num,cvc) :
            print("incorrect cvc number")
            return

        self.is_error = False

        return {
            "card_num" : card_num,
            "valid_thru" : valid_thru,
            "cvc" : cvc
        }

    def process_card(self):
        print("\n========= CARD UI =========")
        # wait card inserted
        while True :
            if self.wait_insert_card() : break
        self.card_info = self.read_card()

    def enter_pin_num(self):
        print("\n========= PIN NUMBER UI =========")
        print("Enter pin number : ", end='')
        pin_num = input_by_ui()
        self.is_error = not self.card.validate_pin_num(self.card_info["card_num"],pin_num)
        return pin_num

    ### accounts ###
    def set_accounts(self):
        self.accounts_info = self.card.get_accounts_by_card(self.card_info['card_num'])

    def show_accounts(self):
        print("\n========= ACCOUNTS UI =========")
        for i, account in enumerate(self.accounts_info):
            print(f"[{i}] - {bank_dict[account['bank_num']]} , {account['account_num']}")
        print("[any else button] : exit")
        print("select wanted num : ", end='')

    def select_account(self):
        try:
            choice = int(input_by_ui())
            self.account = self.accounts_info[choice]
        except:
            self.is_return_to_home = True

    def routine(self):
        self.init()
        # show main(home)
        self.show_main_menu()
        self.select_main_menu()
        if self.is_exit : return
        # card processing
        self.process_card()
        if self.is_error : return
        # enter pin number
        while True:
            self.enter_pin_num()
            if not self.is_error : break
            error('[!] pin number is incorrect.')
            if is_return_home() : return
        # select account
        self.set_accounts()
        self.show_accounts()
        self.select_account()
        if self.is_return_to_home : return
        # select function
        while True:
            self.show_account_menu()
            self.select_account_menu()
            if self.is_return_to_home : return

    ### run ATM ###
    def run(self):
        while True:
            self.routine()
            if self.is_exit : break