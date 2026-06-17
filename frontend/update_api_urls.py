import os
import re

frontend_src = r'e:\others\InsightForge AI\frontend\src'

for root, dirs, files in os.walk(frontend_src):
    for file in files:
        if file.endswith('.tsx') or file.endswith('.ts'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('http://127.0.0.1:8000/api', '/api')
            # WebSocket replacement
            new_content = re.sub(
                r'"ws://127\.0\.0\.1:8000/ws/([^"]+)"',
                r'`ws://${window.location.host}/ws/\1`',
                new_content
            )
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
