Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... import geocoder
... import subprocess
... 
... 
... SOS_NUMBER = "9385582686"
... 
... def get_location():
...     g = geocoder.ip('me') 
...     if g.ok:
...         return f"https://www.google.com/maps?q={g.lat},{g.lng}"
...     return "Location not available"
... 
... def send_sms():
...     location_link = get_location()
...     message = f" SOS Alert! I need help. My current location: {location_link}"
... 
... 
...     url = "https://www.fast2sms.com/dev/bulkV2"
...     headers = {
...         "authorization": "UFYL7pPq65Mk0hwNAGSDI9WgfRuatiEzCKxVHsZlO21mBoXJjTBmpU4Z6Xsih8D2dCSWjkGu3IEfcrzl",
...         "Content-Type": "application/x-www-form-urlencoded"
...     }
...     data = {
...         "message": message,
...         "language": "english",
...         "route": "q",
...         "numbers": SOS_NUMBER
...     }
... 
...     response = requests.post(url, headers=headers, data=data)
...     print(f"SMS Response: {response.text}")
... 
... def make_call():
...     try:
...         subprocess.run(["xdg-open", f"tel:{SOS_NUMBER}"]) 
...         subprocess.run(["start", f"tel:{SOS_NUMBER}"], shell=True) 
...         
... 
...         
...         print("Calling SOS Number...")
...     except Exception as e:
...         print(f"Error making call: {e}")
... 
... send_sms()
... make_call()
