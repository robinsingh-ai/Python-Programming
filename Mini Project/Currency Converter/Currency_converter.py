"""
Author : Robin Singh
Currency Converter

"""
with open('CurrencyData.txt') as r:
    data = r.readlines()
currency_dict = {}
for line in data:
    parsed = line.split("\t")
    currency_dict[parsed[0]] = parsed[1]

r.close()

    


amt = int(input("Entre Amount\n"))
print("Entre Currency Name : ")

print("Available options\n ")
[print(item) for item in currency_dict.keys()]
Curr = input("Entre Name Of the Currency")
newmoney = amt * float(currency_dict[Curr])
print(currency_dict[Curr])
print(f"{amt} INR is equal to {newmoney} {Curr}")
