import os
import re

directory = r"c:\xampp\htdocs\osos-systems"

# Regex to find the telegram link block and replace its href
# We are looking for something like: <a href="...">\s*<i class="fa fa-telegram"></i> or <i class="fab fa-telegram-plane"></i>
# Actually, the structure varies.
# In about.html:
# <a href="#" class="social-link">
#   <i class="fab fa-telegram-plane"></i>

def update_telegram_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern 1: <a href="..." class="social-link">\s*<i class="fab fa-telegram-plane">
    content = re.sub(
        r'<a href="[^"]*"\s*class="social-link"\s*>\s*<i class="fab fa-telegram-plane">',
        r'<a href="https://t.me/osossytems" class="social-link">\n                <i class="fab fa-telegram-plane">',
        content
    )
    
    # Pattern 2: <li><a href="#"><i class="fa fa-telegram"></i></a></li>
    content = re.sub(
        r'<li><a href="[^"]*"><i class="fa fa-telegram"></i></a></li>',
        r'<li><a href="https://t.me/osossytems"><i class="fa fa-telegram"></i></a></li>',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html") or file.endswith(".php") or file.endswith(".py"):
            if file == "update_telegram.py":
                continue
            file_path = os.path.join(root, file)
            update_telegram_links(file_path)
            
print("Done updating Telegram links.")
