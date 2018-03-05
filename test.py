import requests

url = "https://www.digikey.com/product-detail/leadtime/en/"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"language\"\r\n\r\nen\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"partid\"\r\n\r\n992047\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"quantity\"\r\n\r\n1000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "5e45fd65-e678-1653-11f3-8af451116857"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
