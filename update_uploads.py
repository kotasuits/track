import os
import re

src_dir = r'c:\Users\arsha\Downloads\With login'
dest_dir = r'c:\Users\arsha\Downloads\shipment-main\shipment-main'

files_to_copy = ['uploads.html', r'prints\dispatched.html']

nav_root = '''    <nav class="nav-links">
        <a href="prints/index.html">📄 Labels</a>
        <a href="prints/scanner.html">🔍 Scanner</a>
        <a href="prints/dispatched.html">📋 Dispatched</a>
        <a href="uploads.html" class="on">📸 Upload Tracking</a>
        <a href="search.html">🔎 Search Photos</a>
        <a href="billing.html">🧾 Billing</a>
        <a href="gst-billing.html">🧾 GST Billing</a>
        <a href="customers.html">👤 Customers</a>
        <a href="online-excel.html">📊 Online Excel</a>
    </nav>'''

nav_prints = '''    <nav>
        <a href="index.html">📄 Labels</a>
        <a href="scanner.html">🔍 Scanner</a>
        <a href="dispatched.html" class="on">📋 Dispatched</a>
        <a href="../uploads.html">📸 Upload Tracking</a>
        <a href="../search.html">🔎 Search Photos</a>
        <a href="../billing.html">🧾 Billing</a>
        <a href="../gst-billing.html">🧾 GST Billing</a>
        <a href="../customers.html">👤 Customers</a>
        <a href="../online-excel.html">📊 Online Excel</a>
    </nav>'''

for f_path in files_to_copy:
    src_file = os.path.join(src_dir, f_path)
    dest_file = os.path.join(dest_dir, f_path)
    
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Auth Guard
    content = content.replace('<style id="auth-guard-style">body { display: none !important; }</style>', '')
    content = content.replace('<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>', '')
    content = content.replace('<script>enforceAuth();</script>', '')
    content = re.sub(r'<a href="#" onclick="handleLogout.*?Logout</a>', '', content)

    # 2. Update navigation
    if f_path == 'uploads.html':
        content = re.sub(r'<nav.*?>.*?</nav>', nav_root, content, flags=re.DOTALL)
    else:
        content = re.sub(r'<nav.*?>.*?</nav>', nav_prints, content, flags=re.DOTALL)

    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated uploads.html and prints/dispatched.html successfully!")
