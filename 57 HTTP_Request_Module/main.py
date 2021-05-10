import requests
# r = requests.get("https://sandyedemo.co/app_dashboard/dashboard.php")
# print(r.text)

url = "https://sandyedemo.co/app_dashboard/dashboard.php"
data = {"ID":"admin@gmail.com", "Password":"Admin***"}
r2 = requests.post(url=url, data=data)
print(r2.status_code)