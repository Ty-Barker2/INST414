import requests

ExApi = "https://www.freeforexapi.com/api/live?"
resp = requests.get(
    ExApi + "pairs=USDEUR,USDGBP,USDJPY,USDAUD,USDCHF,USDNZD,USDCAD,USDZAR")

res = resp.json()
# print (res)

UsdRates=dict()
for each in res['rates']:
    UsdRates[each] = res['rates'][each]['rate']

print(dict(sorted(UsdRates.items(),key=lambda item:item[1],reverse=True)))



