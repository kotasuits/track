import os
import re

src_file = r'c:\Users\arsha\Downloads\With login\prints\index.html'
dest_file = r'c:\Users\arsha\Downloads\shipment-main\shipment-main\prints\index.html'

with open(src_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Auth Guard
content = content.replace('<style id="auth-guard-style">body { display: none !important; }</style>', '')
content = content.replace('<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>', '')
content = content.replace('<script>enforceAuth();</script>', '')

# 2. Update navigation to match what we did before
new_nav = '''    <nav>
        <a href="index.html" class="on">📄 Labels</a>
        <a href="scanner.html">🔍 Scanner</a>
        <a href="dispatched.html">📋 Dispatched</a>
        <a href="../uploads.html">📸 Upload Tracking</a>
        <a href="../search.html">🔎 Search Photos</a>
        <a href="../billing.html">🧾 Billing</a>
        <a href="../gst-billing.html">🧾 GST Billing</a>
        <a href="../customers.html">👤 Customers</a>
        <a href="../online-excel.html">📊 Online Excel</a>
    </nav>'''

content = re.sub(r'<nav.*?>.*?</nav>', new_nav, content, flags=re.DOTALL)

with open(dest_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated prints/index.html successfully!")
