from pathlib import Path
import re, json, html

root = Path(__file__).parent
folder = root / 'html'
chapters = []
def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
for n, title in [(1, 'مقدمه و بازیابی بولی'), (2, 'واژگان و لیست‌های پستینگ')]:
    path = folder / f'artifact ({n}).html'
    source = path.read_text(encoding='utf-8')
    starts = list(re.finditer(r'<(?:section|div) class="slide(?: active)?">', source))
    topics = []
    for i, match in enumerate(starts):
        end = starts[i+1].start() if i+1 < len(starts) else source.index('<!-- پنل کنترل پایین -->') if n == 2 else source.index('    <footer>')
        block = source[match.start():end]
        heading = re.search(r'<h[12][^>]*>(.*?)</h[12]>', block, re.S)
        topics.append({'title': plain(heading[1]), 'text': plain(block), 'slide': i+1})
    chapters.append({'id': n, 'title': title, 'url': f'html/artifact ({n}).html', 'topics': topics})
    before = re.sub(r'<script\b[^>]*>.*?</script>', '', source, flags=re.S)
    before = before[before.index(starts[0][0]):before.index('    <footer>') if n == 1 else before.index('<!-- پنل کنترل پایین -->')]
    source = source.replace('width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no', 'width=device-width, initial-scale=1.0')
    if '../reader.css' not in source:
        source = source.replace('</head>', '    <link rel="stylesheet" href="../reader.css">\n</head>')
        source = source.replace('<body>', f'<body class="reader chapter-{n}">\n<nav class="reader-top" aria-label="ناوبری جزوه"><a href="../index.html">← فهرست درس‌ها</a><span>{title}</span></nav>')
    source = re.sub(r'<script\b[^>]*>.*?</script>', '<script src="../reader.js"></script>', source, flags=re.S)
    after = source[source.index(starts[0][0]):source.index('    <footer>') if n == 1 else source.index('<!-- پنل کنترل پایین -->')]
    assert before == after, 'Lesson content changed'
    path.write_text(source, encoding='utf-8')
    print(f'Chapter {n}: {len(topics)} slides; original lesson markup preserved')
(root / 'topics.js').write_text('window.chapters = ' + json.dumps(chapters, ensure_ascii=False) + ';', encoding='utf-8')
