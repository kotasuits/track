import re

files_root = ['ocr.html', 'uploads.html']
files_prints = ['prints/dispatched.html', 'prints/index.html', 'prints/scanner.html']

nav_root = '''    <nav class="nav-links">
        <a href="prints/index.html">📄 Labels</a>
        <a href="prints/scanner.html">🔍 Scanner</a>
        <a href="prints/dispatched.html">📋 Dispatched</a>
        <a href="uploads.html">📸 Upload Tracking</a>
        <a href="search.html">🔎 Search Photos</a>
        <a href="billing.html">🧾 Billing</a>
        <a href="gst-billing.html">🧾 GST Billing</a>
        <a href="customers.html">👤 Customers</a>
        <a href="online-excel.html">📊 Online Excel</a>
    </nav>'''

nav_prints = '''    <nav>
        <a href="index.html">📄 Labels</a>
        <a href="scanner.html">🔍 Scanner</a>
        <a href="dispatched.html">📋 Dispatched</a>
        <a href="../uploads.html">📸 Upload Tracking</a>
        <a href="../search.html">🔎 Search Photos</a>
        <a href="../billing.html">🧾 Billing</a>
        <a href="../gst-billing.html">🧾 GST Billing</a>
        <a href="../customers.html">👤 Customers</a>
        <a href="../online-excel.html">📊 Online Excel</a>
    </nav>'''

def update_nav(filepath, new_nav):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to match <nav>...</nav> or <nav class="...">...</nav>
    pattern = r'<nav.*?>.*?</nav>'
    
    # retain the "class='on'" for the current page if needed. Actually it's easier to just inject it.
    filename = filepath.split('/')[-1]
    
    # We will modify the new_nav to add class="on" to the corresponding link
    if filepath in files_root:
        href_match = f'href="{filename}"'
    else:
        href_match = f'href="{filename}"'
        
    custom_nav = new_nav.replace(href_match, f'{href_match} class="on"')
    
    content = re.sub(pattern, custom_nav, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for f in files_root:
    update_nav(f, nav_root)

for f in files_prints:
    update_nav(f, nav_prints)

print("Navigation updated.")
