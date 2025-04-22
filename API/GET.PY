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
    response = requests.get(url, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("Success! Tickets retrieved.")
        tickets = response.json()
        
        if tickets:
            for ticket in tickets:
                print(f"\nTicket ID: {ticket['id']}")
                print(f"Subject: {ticket['subject']}")
                print(f"Status: {ticket['status']}")
                print(f"Priority: {ticket['priority']}")
        else:
            print("No tickets found.")
    else:
        print(f"Failed to retrieve tickets. Error: {response.text}")
        
except Exception as e:
    print(f"An error occurred: {str(e)}") 