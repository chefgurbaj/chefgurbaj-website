import os
import glob

src_dir = '/Users/vik/.gemini/antigravity/scratch/chefgurbaj/src'

for filepath in glob.glob(os.path.join(src_dir, '**', '*.astro'), recursive=True):
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content.replace('GURBAJ SINGH', 'CHEF GURBAJ')
    new_content = new_content.replace('Chef Gurbaj Singh', 'Chef Gurbaj')
    new_content = new_content.replace('Gurbaj Singh', 'Chef Gurbaj')
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
