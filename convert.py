import sys, subprocess
import os

try:
    import mammoth
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mammoth'])
    import mammoth

docs = [
    ('Documents/TL1_Kế hoạch cuộc thi_v1_20.9.2026.docx', 'tl1-ke-hoach.html', 'Kế Hoạch Tổ Chức Cuộc Thi'),
    ('Documents/TL2_KHUNG TIÊU CHÍ CHẤM ĐIỂM (RUBRIC - PHỤ LỤC ĐÍNH KÈM).docx', 'tl2-rubric.html', 'Khung Tiêu Chí Chấm Điểm'),
    ('Documents/TL3_KỊCH BẢN DEMO DAY VÀ THÀNH PHẦN KHÁCH MỜI.docx', 'tl3-demoday.html', 'Kịch Bản Demo Day')
]

html_template = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - UDA AI Challenge 2027</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="./style.css">
    <style>
        .doc-container {
            max-width: 900px;
            margin: 120px auto 50px auto;
            padding: 50px;
            background: white;
            border-radius: 16px;
            box-shadow: var(--shadow-md);
        }
        .doc-container h1, .doc-container h2, .doc-container h3 {
            color: var(--primary);
            margin-top: 1.5em;
            margin-bottom: 0.8em;
        }
        .doc-container h1 { font-size: 2rem; text-align: center; margin-top: 0; margin-bottom: 30px; border-bottom: 2px solid var(--primary-light); padding-bottom: 20px;}
        .doc-container p { margin-bottom: 1.2em; font-size: 1.05rem; }
        .doc-container ul, .doc-container ol { margin-bottom: 1.2em; padding-left: 24px; font-size: 1.05rem; }
        .doc-container li { margin-bottom: 0.5em; }
        .doc-container table { width: 100%; border-collapse: collapse; margin-bottom: 1.5em; }
        .doc-container th, .doc-container td { border: 1px solid var(--border-color); padding: 12px; text-align: left; }
        .doc-container th { background: var(--bg-light); font-weight: 600; }
        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 30px;
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
        }
        .back-btn:hover { transform: translateX(-5px); }
        .doc-title { text-align: center; color: var(--text-main); margin-bottom: 40px; font-size: 2.2rem; }
    </style>
</head>
<body class="bg-light">
    <header class="navbar scrolled">
        <div class="container nav-container">
            <a href="index.html" class="logo">UDA AI <span>Challenge</span></a>
            <nav class="nav-links">
                <a href="index.html#about">Về Cuộc thi</a>
                <a href="index.html#tech">Công Nghệ</a>
                <a href="index.html#tracks">Phân Ban</a>
                <a href="index.html#roadmap">Lộ Trình</a>
                <a href="index.html#documents" class="active">Tài Liệu</a>
                <a href="index.html#register" class="btn btn-primary">Đăng Ký</a>
            </nav>
        </div>
    </header>
    
    <div class="container">
        <div class="doc-container">
            <a href="index.html#documents" class="back-btn">&larr; Quay lại trang chủ</a>
            <h1 class="doc-title">{title}</h1>
            <div class="doc-content">
                {content}
            </div>
        </div>
    </div>

    <footer>
        <div class="footer-bottom">
            <div class="container">
                <p>&copy; 2027 UDA AI Innovation Challenge.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

for doc_path, out_file, title in docs:
    if os.path.exists(doc_path):
        with open(doc_path, 'rb') as docx_file:
            result = mammoth.convert_to_html(docx_file)
            html = result.value
            final_html = html_template.replace('{content}', html).replace('{title}', title)
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(final_html)
            print(f'Converted {doc_path} to {out_file}')
    else:
        print(f'File not found: {doc_path}')
