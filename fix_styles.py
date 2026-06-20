import re

# Fix style.css
with open('/home/bin-naqeeb/Documents/Efhashaa/style.css', 'r') as f:
    css = f.read()

css = css.replace('--gold: #1e3a8a;', '--gold: #3b82f6;')
css = css.replace('--gold-light: #3b82f6;', '--gold-light: #93c5fd;')
css = css.replace('--gold-dark: #1e40af;', '--gold-dark: #2563eb;')
css = css.replace('rgba(30,58,138,', 'rgba(59,130,246,')

with open('/home/bin-naqeeb/Documents/Efhashaa/style.css', 'w') as f:
    f.write(css)

# Fix index.html
with open('/home/bin-naqeeb/Documents/Efhashaa/index.html', 'r') as f:
    html = f.read()

html = html.replace('rgba(30,58,138,', 'rgba(59,130,246,')

# Add white background to logos in reports hub
html = html.replace('style="height: 40px; margin-bottom: 15px; border-radius: 4px;"', 'style="height: 40px; margin-bottom: 15px; border-radius: 8px; background: white; padding: 4px;"')

# Add Korean flag to Korea card
old_korea = """                <div class="service-card" style="background: var(--bg-dark);">
                    <h3>تقارير كوريا</h3>
                    <p>للسيارات المستوردة من كوريا</p>
                </div>"""
new_korea = """                <div class="service-card" style="background: var(--bg-dark);">
                    <img src="https://flagcdn.com/w80/kr.png" alt="كوريا" style="height: 40px; margin-bottom: 15px; border-radius: 8px; background: white; padding: 4px;">
                    <h3>تقارير كوريا</h3>
                    <p>للسيارات المستوردة من كوريا</p>
                </div>"""
html = html.replace(old_korea, new_korea)

# Wrap SVGs in Social Platform section with white background if they are not already
html = html.replace('style="color: #fff; flex-shrink: 0;"', 'style="color: #000; flex-shrink: 0; background: #fff; border-radius: 8px; padding: 8px;"') # for X
html = html.replace('style="flex-shrink: 0;"', 'style="flex-shrink: 0; background: #fff; border-radius: 8px; padding: 8px;"') # for other svgs

with open('/home/bin-naqeeb/Documents/Efhashaa/index.html', 'w') as f:
    f.write(html)
