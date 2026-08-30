import os
import re
import glob

type_a_pattern = re.compile(r'<div class="social-links">\s*<a href="#" class="social-link">\s*<i class="fab fa-facebook-f"></i>\s*<span>Facebook</span>\s*</a>\s*<a href="#" class="social-link">\s*<i class="fab fa-twitter"></i>\s*<span>Twitter</span>\s*</a>\s*<a href="#" class="social-link">\s*<i class="fab fa-instagram"></i>\s*<span>Instagram</span>\s*</a>\s*</div>', re.MULTILINE)

type_a_replacement = '''<div class="social-links">
                        <a href="#" class="social-link">
                           <i class="fab fa-facebook-f"></i>
                           <span>Facebook</span>
                        </a>
                        <a href="#" class="social-link">
                           <i class="fab fa-instagram"></i>
                           <span>Instagram</span>
                        </a>
                        <a href="#" class="social-link">
                           <i class="fab fa-twitter"></i>
                           <span>Twitter</span>
                        </a>
                        <a href="#" class="social-link">
                           <i class="fab fa-snapchat-ghost"></i>
                           <span>Snapchat</span>
                        </a>
                        <a href="#" class="social-link">
                           <i class="fab fa-linkedin-in"></i>
                           <span>LinkedIn</span>
                        </a>
                        <a href="#" class="social-link">
                           <i class="fab fa-youtube"></i>
                           <span>YouTube</span>
                        </a>
                        <a href="https://t.me/osossytems" class="social-link">
                <i class="fab fa-telegram-plane"></i>
                           <span>Telegram</span>
                        </a>
                     </div>'''

type_b_pattern = re.compile(r'<div class="social_icon">\s*<ul>\s*<li><a href="#"><i class="fa fa-facebook"></i></a></li>\s*<li><a href="#"><i class="fa fa-twitter"></i></a></li>\s*<li><a href="#"><i class="fa fa-instagram"></i></a></li>\s*</ul>\s*</div>', re.MULTILINE)

type_b_replacement = '''<div class="social_icon">
                   <ul>
                      <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                      <li><a href="#"><i class="fa fa-instagram"></i></a></li>
                      <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                      <li><a href="#"><i class="fa fa-snapchat-ghost"></i></a></li>
                      <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                      <li><a href="#"><i class="fa fa-youtube"></i></a></li>
                      <li><a href="https://t.me/osossytems"><i class="fa fa-telegram"></i></a></li>
                   </ul>
                </div>'''

def main():
    directory = r'c:\xampp\htdocs\osos-systems'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Replace Type A
        content = type_a_pattern.sub(type_a_replacement, content)
        
        # Replace Type B
        content = type_b_pattern.sub(type_b_replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == '__main__':
    main()
