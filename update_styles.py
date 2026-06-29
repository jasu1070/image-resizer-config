import os
import re

new_style = """<style>
        :root {
            --primary: #FFB300;
            --primary-dark: #F59E0B;
            --secondary: #4A3728;
            --bg-gradient: #ffffff;
            --text-main: #111827;
            --text-muted: #374151;
            --accent: #10b981;
            --border-color: #e5e7eb;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-gradient);
            color: var(--text-main);
            line-height: 1.7;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }

        .background-blobs { display: none; }

        .container { max-width: 800px; margin: 40px auto; padding: 0 24px; }

        .glass-card {
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 50px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            animation: fadeIn 0.4s ease-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        header { text-align: center; margin-bottom: 40px; padding-bottom: 30px; border-bottom: 1px solid var(--border-color); }

        .logo-placeholder {
            width: 70px; height: 70px;
            background: var(--primary);
            border-radius: 16px;
            margin: 0 auto 20px;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 4px 10px rgba(255, 179, 0, 0.3);
        }

        .logo-placeholder svg { width: 34px; height: 34px; fill: white; }

        h1 {
            font-size: 2.5rem; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 12px;
            color: var(--text-main);
        }

        .last-updated {
            display: inline-block; color: var(--text-muted);
            font-size: 0.9rem; font-weight: 500;
        }

        section { margin-bottom: 35px; }

        h2 { font-size: 1.35rem; font-weight: 700; color: var(--text-main); margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }
        h2::before { content: ''; width: 4px; height: 20px; background: var(--primary); border-radius: 4px; }

        p { color: var(--text-muted); margin-bottom: 16px; font-size: 1.05rem; }

        ul { list-style: none; margin-bottom: 20px; }
        li { color: var(--text-muted); margin-bottom: 10px; padding-left: 24px; position: relative; font-size: 1.05rem; }
        li::before { content: '•'; position: absolute; left: 0; color: var(--primary); font-weight: bold; font-size: 1.2rem; line-height: 1.4; }

        a { color: var(--primary-dark); text-decoration: none; font-weight: 600; transition: color 0.2s ease; border-bottom: 1px solid transparent; }
        a:hover { color: var(--primary); border-bottom: 1px solid var(--primary); }

        .contact-box { background: #f9fafb; border: 1px solid var(--border-color); padding: 30px; border-radius: 12px; margin-top: 40px; text-align: center; }
        .contact-box h2::before { display: none; }
        .contact-box h2 { justify-content: center; margin-bottom: 10px; }

        footer { margin-top: 50px; text-align: center; color: var(--text-muted); font-size: 0.9rem; padding-bottom: 20px; border-top: 1px solid var(--border-color); padding-top: 30px; }
        footer p { margin-bottom: 8px; font-size: 0.9rem; }

        @media (max-width: 768px) { .glass-card { padding: 30px 20px; } h1 { font-size: 2rem; } .container { margin: 20px auto; } }
    </style>"""

files = ['privacy-policy.html', 'terms-of-use.html', 'refund-policy.html', 'subscription-terms.html', 'contact-support.html']

for f in files:
    path = os.path.join(r"c:\Users\jashv\image-resizer-config", f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace everything between <style> and </style>
    new_content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print(f"Updated {f}")
