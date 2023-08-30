import requests


def rainbow_text(text):
    colors = [31, 33, 32, 36, 35, 34]
    rainbow = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        rainbow += f"\x1b[{color}m{char}\x1b[0m"
    return rainbow


def center_text(text, width=80):
    return text.center(width)


banner_text = "Discord Bot Creator"


rainbow_banner = rainbow_text(banner_text)


terminal_width = 80


centered_banner = center_text(rainbow_banner, terminal_width)


print(centered_banner)


name = input("Enter bot name: ")
token = input("Enter token: ")

url = "https://discord.com/api/v9/applications"


payload = {
    "name": name
}


headers = {
    "Authorization": token
}

r = requests.post(url, json=payload, headers=headers)

if r.status_code == 201:
    print("Bot application created successfully!")
else:
    print(f"Failed to create bot application. Status code: {r.status_code}")
