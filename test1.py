import requests
print(requests.__version__)

res = requests.get("https://raw.githubusercontent.com/peterschefffer/404lab1/main/test1.py")
raw = res.text
print(raw)