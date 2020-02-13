tax_brackets = [[9525, .1], [38700, .12], [82500, .22], [157500, .24]]


def calculate_tax_withheld(annual_pay):
    taxes_withheld = 0
    for tax_threshold in tax_brackets:
        if annual_pay > tax_threshold[0]:
            taxes_withheld += tax_threshold[0] * tax_threshold[1]
            annual_pay -= tax_threshold[0]
        else:
            taxes_withheld += annual_pay * tax_threshold[1]
            break
    return taxes_withheld


print(calculate_tax_withheld(150000))
