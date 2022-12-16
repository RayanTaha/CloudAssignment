import requests

api_url = "https://reqres.in/api/unknown/2"
#Get 
response = requests.get(api_url)
print(response.json())
response.status_code

if response.status_code == 200 : 
    print("200 response: OK")
    
elif response.status_code == 404 :
    print("404 response: Not Found")
    
elif response.status_code == 400 :
    print("400 response: Bad Request")
    