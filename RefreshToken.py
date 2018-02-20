import http.client
import json


conn = http.client.HTTPSConnection("sso.digikey.com")

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    }

ref_tok = "grsborxvBJ0RS1e9TkN2axUihMOyplP0wjyuzmcrCU"
#grsborxvBJ0RS1e9TkN2axUihMOyplP0wjyuzmcrCU

obj = {
    "refresh_token" : ref_tok,
    "client_id" : "c32a6a44-8532-4649-a426-ecd4b5ae7e54",
    "client_secret" : "aV2dH1iS5sG4fF1tX7kO7jU1nK3cR2qY5hF8bI8bD4eS8lU6yH",
    "grant_type" : "authorization_code"
}

pay = json.dumps(obj)

conn.request("POST", "/as/token.oauth2", pay, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
