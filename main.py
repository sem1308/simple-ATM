from atm import ATM
from bank import BANK
from card import CARD

if __name__ == '__main__':
    dummy_accounts = {
        "111112341234" : {"bank_num" : "001",
                          "account_num" : "111112341234",
                        "balance" : 100000},
        "222212341234" : {"bank_num" : "002",
                          "account_num" : "222212341234",
                        "balance" : 15300},
        "333312341234" : {"bank_num" : "003",
                          "account_num" : "333312341234",
                        "balance" : 553000},
        "444412341234" : {"bank_num" : "004",
                          "account_num" : "444412341234",
                        "balance" : 4379200}
    }
    dummy_cards = {
        "4579730071247055" : {
            "valid_thru": ["24", "08"],
            "cvc": "302",
            "pin_num" : "1234",
            "accounts" : [dummy_accounts["111112341234"],
                          dummy_accounts["333312341234"]]
        }
    }
    # input below for card information
    # card number : 4579-7300-7124-7055
    # valid thru : 24/08
    # cvc : 302
    # pin number : 1234
    cash = 10**6 # assume that 1,000,000$ is in ATM / 100만 $가 ATM기기에 있다 가정
    machine = ATM(cash,BANK(dummy_accounts),CARD(dummy_cards))
    machine.run()

