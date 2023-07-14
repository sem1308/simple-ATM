import datetime
from bank import BANK

class CARD:

    def __init__(self, cards):
        self.cards = cards

    def validate_card_num(self, card_num : str):
        # TODO: change this code for real card service
        # check digit
        if not card_num.isdigit():
            return False

        # check length
        if len(card_num) < 13 or len(card_num) > 19:
            return False

        if card_num not in self.cards :
            return False

        # check validity
        digits = [int(x) for x in card_num]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        total = sum(odd_digits)

        for digit in even_digits:
            total += sum(divmod(digit * 2, 10))

        return total % 10 == 0

    def validate_card_thru(self, card_num: str, valid_thru: list):
        if valid_thru != self.cards[card_num]["valid_thru"] : return False
        now = datetime.datetime.now()
        cur_year = now.year - 2000
        cur_month = now.month
        valid_year, valid_month = map(int,valid_thru)
        return cur_year <= valid_year and cur_month <= valid_month

    def validate_card_cvc(self, card_num : str, cvc : str):
        return self.cards[card_num]["cvc"] == cvc

    def validate_pin_num(self, card_num: str, pin_num : str):
        if not pin_num.isdigit():
            return False
        return self.cards[card_num]["pin_num"] == pin_num

    def get_accounts_by_card(self, card_num : str):
        if card_num in self.cards :
            return self.cards[card_num]["accounts"]
        else:
            return []