import re
from bs4 import BeautifulSoup

TITLE = 'واژه‌نامه‌ها و بازیابی با تطبیق غیردقیق'
QA = [('اگر فقط مکان‌های TO و BE را داشته باشیم، آیا کل عبارت شش‌واژه‌ای ثابت می‌شود؟','خیر؛ مکان or و not و فاصله‌های نسبی همهٔ رخدادها نیز لازم است.'),('چرا moon در نامزدهای mon* دیده می‌شود؟','هر سه bigram را دارد، اما پیشوند mon را ندارد و در پالایش نهایی رد می‌شود.'),('آیا فاصلهٔ ۳ یعنی دقیقاً یک مسیر بهینه داریم؟','خیر. برای cat → catcat چند هم‌ترازی با سه درج وجود دارد.'),('چرا form را به تنهایی نمی‌توان غلط اعلام کرد؟','خودش واژهٔ معتبری است؛ بافتی مانند flew from munich به تصمیم کمک می‌کند.')]

def quiz():
    return ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in QA)

def build(root,md,shell):
    base='supplements/ch8/'
    src=(root/base/'chapter-03.md').read_text()
    annex=BeautifulSoup(md(src.split('## پیوست مرجع:',1)[1]),'html.parser')
    slides={}
    for h in annex.find_all('h3'):
        num=int(h.get_text().split()[-1]); parts=[]
        for el in h.next_siblings:
            if el.name=='h3': break
            if not el.name: continue
            for img in el.select('img'):
                img['src']=base+img['src']; img['loading']='lazy'
            parts.append(str(el))
        slides[num]=f'<details id="source-{num}"><summary>اسلاید {num}</summary>'+''.join(parts)+'</details>'
    ids=['foundations','dictionary','wildcards','edit-distance','distance-lab','spelling','soundex']; ends=[10,21,34,54,99,107,115]; topics=[]; sections=[]; toc=[]; start=1
    for i,chunk in enumerate((root/base/'lesson.md').read_text().split('### ')[1:]):
        heading,text=chunk.split('\n',1); html=md(text.strip()); slug=ids[i]; end=ends[i]; number=i+1
        topics.append(dict(title=heading,text=BeautifulSoup(html,'html.parser').get_text(' ',strip=True),slide=number));toc.append(f'<a href="#{slug}">{heading}</a>')
        demo={'foundations':'<div id="tokens"></div>', 'soundex':'<div id="sound-lab"></div>', 'distance-lab':'<div id="matrix-lab"></div>'}.get(slug,'')
        sections.append(f'<section id="{slug}"><h2 id="slide-{number}">{heading}</h2>{html}{demo}<details><summary>متن و شکل‌های منبع · اسلایدهای {start} تا {end}</summary>'+''.join(slides[n] for n in range(start,end+1))+'</details></section>'); start=end+1
    body='<main class="reading-layout"><aside class="toc"><span class="eyebrow">در این فصل</span>'+''.join(toc)+'</aside><article class="lesson tolerant"><span class="eyebrow">فصل ۸ سایت · درس ۳ منبع</span><h1>'+TITLE+'</h1><p class="source-note">منبع: درس Dictionaries and tolerant retrieval از Hinrich Schütze و Christina Lioma. متن و شکل‌های اصلی هر بخش زیر همان بخش باز می‌شوند.</p><p>اگر کاربر mon* یا informaton را بنویسد، موتور جست‌وجو چطور از این ورودی به واژه و از واژه به سند می‌رسد؟</p><button class="print-button" onclick="window.print()">چاپ / ذخیره PDF</button>'+''.join(sections)+'<section class="self-test"><h2>خودت را بسنج</h2>'+quiz()+'</section><label class="complete"><input type="checkbox" data-done="8"> این فصل را مطالعه کردم</label><div class="study-progress"><label for="meter8" data-progress-label>پیشرفت مطالعه</label><progress id="meter8" data-study-meter max="8" value="0"></progress><small data-progress-note></small></div><nav class="chapter-nav"><a href="chapter-7.html">→ فصل قبل</a><a href="review.html">مرور نهایی ←</a></nav></article></main>'
    (root/'chapter-8.html').write_text(shell(TITLE,body,f'<link rel="stylesheet" href="{base}lesson.css"><script defer src="progress.js"></script><script defer src="{base}lab.js"></script>'))
    return dict(id=8,title=TITLE,url='chapter-8.html',description='از واژه‌های نامزد تا اصلاح املا و بازیابی آوایی',topics=topics)
