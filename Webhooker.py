import requests
from urllib.parse import urlparse

allowed_domains = ["discord.com", "*.discord.com"]

while True:
    webhook_url = input("Paste Discord webhook URL here: ").strip()

    # Add default scheme if missing
    if not webhook_url.startswith(("http://", "https://")):
        webhook_url = "https://" + webhook_url

    # Parse the URL
    parsed_url = urlparse(webhook_url)
    domain = parsed_url.netloc.replace("www.", "").replace("https://", "")

    # Check if the domain is in the allowed_domains list
    if any(domain.endswith(allowed) for allowed in allowed_domains):
        break
    else:
        print("Invalid URL. Only Discord URLs are allowed.")

username = input("What should the webhook name be? ").strip()
default_avatar_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png"
avatar_url = input("Paste link to pfp image (or press Enter for default): ").strip()

if not avatar_url:
    avatar_url = default_avatar_url

content = input("What should message content be? ").strip()

while True:
    if avatar_url.endswith((".jpg", ".jpeg", ".png", ".gif")):
        break
    else:
        print("Invalid URL", avatar_url)

while True:
    confirmation = input(
        "Is this correct?\n username: {}\n Profile image URL: {}\n message: {}\n yes or no? ".format(username, avatar_url, content)).strip().lower()

    if confirmation.startswith("y"):
        print("Okay, pinging webhook...")
        # request code here
        data = {
            "username": username,
            "avatar_url": avatar_url,
            "content": content,
        }
        response = requests.post(webhook_url, json=data)

        if response.status_code == 204:
            print("Webhook sent successfully!")
        else:
            print("Failed to send the webhook.")
            print("Response status code:", response.status_code)
            print("Response text:", response.text)
        break

    elif confirmation.startswith("n"):
        print("Okay, cancelling...")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no?'")
        continue

exit()
