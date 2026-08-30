import os
import glob
import re

def main():
    directory = r'c:\xampp\htdocs\osos-systems'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    # regex to match <a href="#"> or <a href="#" class="..."> before the svg
    pattern = re.compile(r'<a href="#"(.*?)(>\s*<svg xmlns="http://www\.w3\.org/2000/svg" viewBox="0 0 512 512")', re.DOTALL)
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # We need to ensure we only replace the ones that contain the X icon SVG path
        # Let's match the whole block including the specific path
        x_svg_path_fragment = r'd="M389.2 48h70.6'
        
        def replacer(match):
            if x_svg_path_fragment in match.group(0):
                return '<a href="https://x.com/osossystems"' + match.group(1) + match.group(2)
            return match.group(0)

        # wait, the pattern above only matches up to <svg ..., it doesn't match the path.
        # Let's write a pattern that captures the whole thing to verify
        # or we just replace any <a href="#"> that leads to an SVG which has the X path.
        pass

    # A better pattern:
    # Match <a href="#"... followed by up to 500 chars (lazy) then the path fragment
    pattern2 = re.compile(r'<a href="#"([^>]*?>(?:\s*<svg[^>]*>\s*<path d="M389\.2 48h70\.6[^>]*>\s*</svg>|\s*<svg[^>]*>.*?d="M389\.2 48h70\.6.*?))', re.DOTALL)
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        content = re.sub(
            r'<a href="#"([^>]*?>\s*<svg xmlns="http://www\.w3\.org/2000/svg" viewBox="0 0 512 512".*?d="M389\.2 48h70\.6)',
            r'<a href="https://x.com/osossystems"\1',
            content,
            flags=re.DOTALL
        )
        
        # Also let's check for <i class="fa fa-twitter"></i> inside <a href="#">
        content = re.sub(
            r'<a href="#"([^>]*?>\s*<i class="(?:fa|fab) fa-(?:twitter|x-twitter)"></i>)',
            r'<a href="https://x.com/osossystems"\1',
            content,
            flags=re.DOTALL
        )
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == '__main__':
    main()
