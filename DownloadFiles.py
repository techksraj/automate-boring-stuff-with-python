import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[:500])
