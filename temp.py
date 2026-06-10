import os
import re

src_dir = r'c:\Users\arsha\Downloads\With login'
dest_dir = r'c:\Users\arsha\Downloads\shipment-main\shipment-main'

# 1. Update firebase-config.js
with open(os.path.join(src_dir, 'firebase-config.js'), 'r', encoding='utf-8') as f:
    fb_content = f.read()

# Replace enforceAuth to do nothing or remove the redirect
fb_content = re.sub(r'function enforceAuth\(\) \{.*?\n\}', r'function enforceAuth() {\n    const guard = document.getElementById(\'auth-guard-style\');\n    if (guard) guard.remove();\n}', fb_content, flags=re.DOTALL)
with open(os.path.join(dest_dir, 'firebase-config.js'), 'w', encoding='utf-8') as f:
    f.write(fb_content)

# 2. Update HTML files
files = ['billing.html', 'gst-billing.html', 'customers.html', 'online-excel.html']

for file in files:
    with open(os.path.join(src_dir, file), 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove auth-guard style
    content = content.replace('<style id="auth-guard-style">body { display: none !important; }</style>', '')
    
    # Remove auth script
    content = content.replace('<script src="https://www.gstatic.com/firebasejs/9.23.0/firebase-auth-compat.js"></script>', '')
    
    # Remove enforceAuth() call
    content = content.replace('<script>enforceAuth();</script>', '')
    
    # Remove Logout button
    content = re.sub(r'<a href="#" onclick="handleLogout.*?Logout</a>', '', content)
    
    with open(os.path.join(dest_dir, file), 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
