#API api.nbp.pl

slownik = { "usd":4.5, "chf":4.8 ,"eur":4.15 }
print(slownik["usd"])
# 4.5
kurs = {"table":"A","currency":"frank szwajcarski","code":"CHF","rates":[{"no":"036/A/NBP/2023","effectiveDate":"2023-02-21","mid":4.8160}]}
print(kurs["currency"])
# 'frank szwajcarski'
print(kurs["rates"])
# [{'no': '036/A/NBP/2023', 'effectiveDate': '2023-02-21', 'mid': 4.816}]
print(kurs["rates"][0])
# {'no': '036/A/NBP/2023', 'effectiveDate': '2023-02-21', 'mid': 4.816}
print(kurs["rates"][0]["no"])
'036/A/NBP/2023'
print(kurs["rates"][0]["mid"])
# 4.816