import requests
from urllib.parse import urlencode

# Function to send WhatsApp message to the stakeholder
def sendmessage(number, name, adhaar, location):
    # Extract location details safely with default values if keys are missing
    city = location.get('city', 'Unknown city')
    region = location.get('region', 'Unknown region')
    country = location.get('country', 'Unknown country')
    latitude = location.get('latitude', 'Unknown latitude')
    longitude = location.get('longitude', 'Unknown longitude')

    print(f"Sending message to: {number}")
    
    # Format the message to be sent
    message = (f"Your dear one with name {name}, bearing Aadhaar number {adhaar}, has been found at the location:\n"
               f"Country: {country}, Region: {region}, City: {city}, Latitude: {latitude}, Longitude: {longitude}.\n"
               "Regards, FindOne")
    
    # API details
    url = "https://api.ultramsg.com/instance98040/messages/chat"
    
    # Encode parameters correctly
    payload = {
        'token': '6i558w5oc0wyodb6',  # Use your actual token
        'to': f"+91{number}",
        'body': message,
        'priority': '1',
        'referenceId': ''
    }
    
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    # Make the POST request to send the message
    try:
        response = requests.post(url, data=urlencode(payload), headers=headers)
        
        # Print response for debugging purposes
        print("Response:", response.text)
        
        # Check if the message was sent successfully
        if response.status_code == 200:
            print(f"Message sent successfully to {number}.")
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

