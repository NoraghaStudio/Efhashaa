import re

def migrate_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The block to replace is:
    # const reviews = [...];
    # We replace it with:
    # let reviews = [];
    # const response = await fetch('/api/reviews');
    # if (response.ok) reviews = await response.json();
    
    # We need to make the DOMContentLoaded callback async.
    html = html.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', async () => {")
    
    # Replace `const reviews = [...];` with the fetch call
    pattern = re.compile(r'const reviews = \[.*?\];', re.DOTALL)
    
    fetch_code = """let reviews = [];
                    try {
                        const res = await fetch('/api/reviews');
                        if (res.ok) {
                            reviews = await res.json();
                        }
                    } catch(e) {
                        console.error('Failed to load reviews', e);
                    }"""
                    
    html = pattern.sub(fetch_code, html)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
if __name__ == '__main__':
    migrate_index()
    print("Migrated index.html")
