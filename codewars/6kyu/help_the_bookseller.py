# https://www.codewars.com/kata/54dc6f5a224c26032800005c

def stock_list(list_of_art, list_of_cat):
    if list_of_art and list_of_cat:
        count_in_cat = dict.fromkeys(list_of_cat, 0)
        for cat in list_of_cat:
            for art in list_of_art:
                if art.startswith(cat):
                    count_of_art = art.split()[1]
                    count_in_cat[cat] += int(count_of_art)
        return ' - '.join((f'({k} : {v})' for k, v in count_in_cat.items()))
    return ''


b = ['BBAR 150', 'CDXE 515', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
c = ['A', 'B', 'C', 'D']
assert stock_list(b, c) == '(A : 0) - (B : 1290) - (C : 515) - (D : 600)'

b = ['ABAR 200', 'CDXE 500', 'BKWR 250', 'BTSQ 890', 'DRTY 600']
c = ['A', 'B']
assert stock_list(b, c) == '(A : 200) - (B : 1140)'
