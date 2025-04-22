import requests
import json
import base64

api_key = "4JJzk3JC5mbsJIf6ZIx"
freshdesk_domain = "shanmugavelragavan0.freshdesk.com"
url = f"https://{freshdesk_domain}/api/v2/tickets"

auth_str = api_key + ":X"
encoded_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {encoded_auth}"
}

ticket_data = {
    "subject": "Test Ticket from API",
    "description": "This is a test ticket created using the Freshdesk API",
    "email": "test@example.com",
    "priority": 1,
    "status": 2
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(ticket_data))
    
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(json.dumps(response.json(), indent=4))
    
    if response.status_code == 201:
        print("Success! Ticket created.")
    else:
        print(f"Failed to create ticket. Error: {response.text}")
        
except Exception as e:
    print(f"An error occurred: {str(e)}")