import requests

url = "https://csgoempire.io/api/v2/trading/items?per_page=10&page=1&price_max_above=15&sort=desc&order=market_value&auction=yes"

payload = {}
headers = {
  'Authorization': 'Bearer 117a4b983df3e12b36132e60d46b6df0',
  'Cookie': '__cf_bm=qpuMbSG7m3KUmp.5Zd7_ajkdLAifiDem.JjrF6LFnSg-1682967420-0-AaXpzCCnVltr3zZ6X6p2VhQse/c7WfpuVHlrpLxa0dgKz0JS10s2iO24cmmIZHC8LUiIZiRcAbIpWxJaFrcFoys='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)