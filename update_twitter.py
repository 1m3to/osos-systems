import os
import glob
import re

def main():
    directory = r'c:\xampp\htdocs\osos-systems'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Replace Type A (with span)
        content = content.replace('<i class="fab fa-twitter"></i>\n                           <span>Twitter</span>', '<i class="fab fa-x-twitter"></i>\n                           <span>X</span>')
        # Also just in case the indentation differs:
        content = re.sub(r'<i class="fab fa-twitter"></i>\s*<span>Twitter</span>', r'<i class="fab fa-x-twitter"></i>\n                           <span>X</span>', content)
        
        # Replace Type B (just the icon class)
        content = content.replace('<i class="fa fa-twitter"></i>', '<i class="fa fa-x-twitter"></i>')
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == '__main__':
    main()
