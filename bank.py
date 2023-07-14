class BANK:
    # TODO: change this code for real back service
    def __init__(self, accounts):
        self.accounts = accounts

    def deposit(self, account_num : str, amount : int):
        self.accounts[account_num]["balance"] += amount
        return self.accounts[account_num]

    def withdraw(self, account_num : str, amount : int):
        is_lack = False
        if self.accounts[account_num]["balance"] < amount :
            is_lack = True
        else:
            self.accounts[account_num]["balance"] -= amount
        return self.accounts[account_num], is_lack