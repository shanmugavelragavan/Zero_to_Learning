import requests
import json
import base64

api_key = "4JJzk3JC5mbsJIf6ZIx"
freshdesk_domain = "shanmugavelragavan0.freshdesk.com"

ticket_id = 10

url = f"https://{freshdesk_domain}/api/v2/tickets/{ticket_id}"

auth_str = api_key + ":X"
encoded_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {encoded_auth}"
}

try:
    response = requests.delete(url, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 204:
        print("Success! Ticket deleted.")
    else:
        print(f"Failed to delete ticket. Error: {response.text}")
        
except Exception as e:
    print(f"An error occurred: {str(e)}") 