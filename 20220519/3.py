#     Masz dany tekst:
#
#     I have television. teleWizor I like my TeeeeleWizor, and I have many tlviiiiisions
#
#     Napisz wyrażenie regularne, które odpowiada różnym pisowniom wyrazu "telewizor". Policz, ile jest tych wyrazów.
#     Przykładowe działanie programu:
#
#     ['television', 'teleWizor', 'TeeeeleWizor', 'tlviiiiisions']
#     The word 'telewizor was found 4 times.

import re

text = "I have television. teleWizor I like my TeeeeleWizor, and I have many tlviiiiisions"

# https://regex101.com/
regex = "(t|T)e{0,}le{0,}(v|V|w|W)i{1,}(s|z)(or|ion)s{0,}"

print(re.findall(regex, text))
