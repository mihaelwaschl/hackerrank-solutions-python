import re

for i in range(int(input())):
    card_num = input()
    replace_hyphen = card_num.replace('-', '')
    first_num = bool(re.search(r'^[456]\d+$', replace_hyphen))
    four_numbers = bool(re.findall(r'(?=(\d)\1\1\1)', replace_hyphen))
    if len(card_num) == 16:
        if first_num and not four_numbers:
            print('Valid')
        else:
            print('Invalid')
    elif len(card_num) == 19:
        card_num_19 = bool(re.search(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', card_num))
        if card_num_19 and first_num and not four_numbers:
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')