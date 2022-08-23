import requests
from requests.structures import CaseInsensitiveDict

url = "https://suppliers-api.wildberries.ru/card/getBarcodes"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NJRCI6ImMzMTBmNThkLTM5OWEtNGFjNC1hMGY0LTc0MzE4YjA1Y2JlMSJ9.xiZFCTHXxCK_Sxg9GzYnJ-ylI-MQJLS6VTqHW6Zq-iI"
headers["Content-Type"] = "application/json"

data = """
{
  "id": 1,
  "jsonrpc": "2.0",
  "params": {
    "quantity": 1,
    "supplierID": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}

"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print(resp.content)