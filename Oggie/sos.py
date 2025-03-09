import requests
import geocoder
import subprocess

# SOS Number (Hardcoded)
SOS_NUMBER = "8610709094"  # Change this to your emergency contact

def get_location():
    g = geocoder.ip('me')  # Get approximate location
    if g.ok:
        return f"https://www.google.com/maps?q={g.lat},{g.lng}"
    return "Location not available"

def send_sms():
    location_link = get_location()
    message = f"⚠️ SOS Alert! I need help. My current location: {location_link}"

    # Fast2SMS API (Free for India, register at https://www.fast2sms.com/)
    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        "authorization": "your_fast2sms_api_key",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "message": message,
        "language": "english",
        "route": "q",
        "numbers": SOS_NUMBER
    }

    response = requests.post(url, headers=headers, data=data)
    print(f"SMS Response: {response.text}")

def make_call():
    try:
        # For Windows/Linux (via Skype or Command Line)
        subprocess.run(["xdg-open", f"tel:{SOS_NUMBER}"])  # Linux
        subprocess.run(["start", f"tel:{SOS_NUMBER}"], shell=True)  # Windows
        
        # For Android (Uncomment if using an Android phone with Termux)
        # subprocess.run(["termux-telephony-call", SOS_NUMBER])
        
        print("Calling SOS Number...")
    except Exception as e:
        print(f"Error making call: {e}")

# Run SOS alert
send_sms()
make_call()
