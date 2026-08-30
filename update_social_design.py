import os
import glob
import re

css_pattern = re.compile(
    r'\.social-links\s*\{[^}]*\}\s*\.social-link\s*\{[^}]*\}\s*\.social-link:hover\s*\{[^}]*\}\s*\.social-link i\s*\{[^}]*\}',
    re.DOTALL
)

css_replacement = '''    .social-links {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
      gap: 10px;
      margin-bottom: 20px;
    }

    .social-link {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 10px 12px;
      background: #2d3748;
      border: 1px solid #4a5568;
      border-radius: 8px;
      color: #e2e8f0;
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: all 0.3s ease;
    }

    .social-link:hover {
      background: #dc2626;
      border-color: #dc2626;
      transform: translateY(-2px);
      color: #ffffff;
      text-decoration: none;
    }

    .social-link i, .social-link svg {
      font-size: 16px;
    }'''

def main():
    directory = r'c:\xampp\htdocs\osos-systems'
    html_files = glob.glob(os.path.join(directory, '*.html'))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Replace CSS
        content = css_pattern.sub(css_replacement, content)
        
        # Replace X span to Twitter span to avoid X X
        x_link_pattern = re.compile(r'(<a href="https://x\.com/osossystems"[^>]*>.*?<svg[^>]*>.*?</svg>\s*)<span>X</span>', re.DOTALL)
        content = x_link_pattern.sub(r'\1<span>Twitter</span>', content)
        
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == '__main__':
    main()
