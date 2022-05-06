import requests
import json
bozulan = input('Bozulan döviz türü: ')
bozulan = bozulan.upper()
dvz = requests.get(f"https://api.exchangeratesapi.io/latest?base={bozulan}")
dvz = dvz.text
dvz = json.loads(dvz)
dvz = dvz["rates"]
alinan = input('Alınan döviz türü: ')
alinan = alinan.upper()
aldvz = dvz[f"{alinan}"]
miktar =float(input(f'Ne kadar {bozulan} bozdurmak istiyorsunuz: '))
print(f'1 {bozulan} = {aldvz} {alinan}')
print(f"{miktar} {bozulan} = {aldvz*miktar} {alinan}")