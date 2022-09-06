title = {
  "ValCurs": {
    "@Date": "31.08.2022",
    "@name": "Foreign Currency Market",
    "Valute": [
      {
        "@ID": "R01010",
        "NumCode": "036",
        "CharCode": "AUD",
        "Nominal": "1",
        "Name": "Австралийский доллар",
        "Value": "41,6839"
      },
      {
        "@ID": "R01020A",
        "NumCode": "944",
        "CharCode": "AZN",
        "Nominal": "1",
        "Name": "Азербайджанский манат",
        "Value": "35,5104"
      }
    ]
  }
}

def rec(sl, search):
    if search in sl.keys():
        return sl[search]

    for n in sl.values():
        if type(n) == dict or type(n) == set:
          ret = rec(n, search)
          if ret !=None:
            return ret


print(rec(title, input('Enter \n')))