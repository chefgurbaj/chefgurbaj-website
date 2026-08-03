import os
import glob

src_dir = '/Users/vik/.gemini/antigravity/scratch/chefgurbaj/src'

for filepath in glob.glob(os.path.join(src_dir, '**', '*.astro'), recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content.replace('WhatsAppButton', 'ContactButton')
    
    if filepath.endswith('Footer.astro'):
        new_content = new_content.replace('https://wa.me/917021293289', 'mailto:hello@chefgurbaj.com')
        new_content = new_content.replace('WhatsApp', 'Email')
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
