import os
import glob
from PIL import Image

def main():
    img_dir = '/home/bin-naqeeb/Documents/Efhashaa/assets/images'
    
    # 1. Convert all images to WebP
    extensions = ['*.png', '*.jpg', '*.jpeg']
    files_to_convert = []
    for ext in extensions:
        files_to_convert.extend(glob.glob(os.path.join(img_dir, ext)))
        
    for file_path in files_to_convert:
        if file_path.endswith('.webp'):
            continue
        print(f"Converting {file_path}")
        try:
            img = Image.open(file_path)
            new_path = file_path.rsplit('.', 1)[0] + '.webp'
            img.save(new_path, 'webp')
            os.remove(file_path) # Remove original to save space
        except Exception as e:
            print(f"Failed to convert {file_path}: {e}")

    # 2. Update index.html
    html_path = '/home/bin-naqeeb/Documents/Efhashaa/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # First, replace the google favicon URLs with local paths
    html = html.replace('https://www.google.com/s2/favicons?domain=haraj.com.sa&sz=128', 'assets/images/haraj.webp')
    html = html.replace('https://www.google.com/s2/favicons?domain=mstaml.com&sz=128', 'assets/images/mstaml.webp')
    
    # Now replace all image extensions
    import re
    # Replace .png, .jpg, .jpeg with .webp in HTML
    html = re.sub(r'\.png"', '.webp"', html)
    html = re.sub(r'\.jpg"', '.webp"', html)
    html = re.sub(r'\.jpeg"', '.webp"', html)
    
    # Just in case there are some with single quotes or no quotes, but standard is double quotes in our HTML
    html = re.sub(r"\.png'", ".webp'", html)
    html = re.sub(r"\.jpg'", ".webp'", html)
    html = re.sub(r"\.jpeg'", ".webp'", html)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Done converting and updating.")

if __name__ == "__main__":
    main()
