import os
import re

src_dir = r'c:\Users\arsha\Downloads\With login'
dest_dir = r'c:\Users\arsha\Downloads\shipment-main\shipment-main'

f_path = r'prints\scanner.html'
nav_prints = '''    <nav>
        <a href="index.html">📄 Labels</a>
        <a href="scanner.html" class="on">🔍 Scanner</a>
        <a href="dispatched.html">📋 Dispatched</a>
        <a href="../uploads.html">📸 Upload Tracking</a>
        <a href="../search.html">🔎 Search Photos</a>
        <a href="../billing.html">🧾 Billing</a>
        <a href="../gst-billing.html">🧾 GST Billing</a>
        <a href="../customers.html">👤 Customers</a>
        <a href="../online-excel.html">📊 Online Excel</a>
    </nav>'''

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
content = re.sub(r'<nav.*?>.*?</nav>', nav_prints, content, flags=re.DOTALL)

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated scanner.html successfully!')
