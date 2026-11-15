from pathlib import Path
import re,json,html
import mistune
from bs4 import BeautifulSoup
root=Path(__file__).parent
md=mistune.create_markdown(plugins=['table'])
source=(root/'course.md').read_text()
extras={
1: '''
### نیاز اطلاعاتی، پرس‌وجو و ارتباط
نیاز اطلاعاتی مسئلهٔ واقعی کاربر است؛ پرس‌وجو فقط بیان کوتاه آن است. ممکن است سندی واژه‌های پرس‌وجو را داشته باشد اما پاسخ نیاز کاربر نباشد. IR الزاماً رتبه‌بندی‌شده نیست: مدل بولی نیز یک مدل IR است و خروجی آن مجموعه‌ای بدون امتیاز ارتباط است.

### ماتریس وقوع و ایندکس معکوس
ماتریس وقوع برای هر زوج ترم–سند یک بیت حضور دارد. برای یک میلیون سند و ۵۰۰ هزار ترم، تعداد خانه‌ها `5 × 10^11` است؛ حتی ذخیرهٔ بیتی خام حدود ۶۲٫۵ گیگابایت فضا می‌خواهد. اگر کل مجموعه یک میلیارد توکن داشته باشد، حداکثر ۰٫۲٪ خانه‌ها یک هستند. بنابراین نگهداری فقط حضورها مناسب‌تر است.

```text
d1: دانشگاه تهران در تهران است
d2: دانشگاه شریف در تهران است
d3: دانشجو در دانشگاه درس می‌خواند
دانشگاه → [1, 2, 3]
تهران → [1, 2]
شریف → [2]
دانشجو → [3]
```
هر DocID در فهرست سادهٔ یک ترم فقط یک‌بار ثبت می‌شود، حتی اگر ترم چند بار در آن سند باشد. دیکشنری معمولاً ترم، df و اشاره‌گر به postings را نگه می‌دارد. محل نگهداری در RAM یا دیسک یک تصمیم مهندسی است، نه بخشی از تعریف ایندکس.

### پردازش AND، OR و NOT
AND اشتراک، OR اجتماع و `A AND NOT B` تفاضل مجموعه‌هاست. NOT مستقل به مجموعهٔ کل اسناد U نیاز دارد. برای جلوگیری از ابهام، عبارت‌های ترکیبی را پرانتزگذاری کنید.

```text
A = [1, 2, 4, 11, 31]
B = [2, 31, 54]
A AND B     = [2, 31]
A OR B      = [1, 2, 4, 11, 31, 54]
A AND NOT B = [1, 4, 11]
```
برای اشتراک دو فهرست مرتب، دو نشانگر i و j می‌گذاریم: در برابری، مقدار را خروجی می‌دهیم و هر دو جلو می‌روند؛ در نابرابری، نشانگر مقدار کوچک‌تر جلو می‌رود. زمان `O(x+y)` است؛ مرتب بودن فهرست‌ها پیش‌شرط الگوریتم است.

### تمرین حل‌شدهٔ بولی
مطابق اسلاید ۳۱ و تصویر صفحهٔ ۴ PDF فارسی:

```text
france = [1,2,3,4,5,7,8,9,11,12,13,14,15]
paris  = [2,6,10,12,14]
lear   = [12,15]
paris AND NOT france = [6,10]
(paris AND NOT france) OR lear = [6,10,12,15]
```
لازم نیست ابتدا مکمل بزرگ france را بسازیم؛ تفاضل مستقیم paris و france کافی است.

### ترتیب اجرای پرس‌وجو
برای AND چند ترم، شروع از df کمتر یک راهکار ساده و مؤثر است تا نتیجهٔ میانی کوچک بماند؛ این یک ابتکار عملی است، نه تضمین بهترین زمان در تمام پیاده‌سازی‌ها. برای زیرعبارت OR، جمع dfها یک کران بالای اندازهٔ اجتماع است، چون اسناد مشترک نباید دوباره شمرده شوند.

### چرا اسکن ساده کافی نیست؟
grep برای متن‌های کوچک مفید است، اما اسکن مکرر کل مجموعه هزینه دارد و پردازش سندمحور، مجاورت و رتبه‌بندی با یک grep ساده فراهم نمی‌شود. این به معنی ناممکن بودن ساخت این قابلیت‌ها با برنامه‌نویسی نیست؛ هدف ایندکس، پاسخ‌گویی سریع به پرس‌وجوهای متعدد است.
''',
2: '''
### Token، Type و Term را جدا کنیم
Token هر رخداد در متن، Type شکل متمایز توکن، و Term واحد نهایی واردشده به واژگان ایندکس است. پس Type و Term همیشه برابر نیستند.

```text
cat dog cat bird dog cat
Tokens = 6
Types = 3  → {cat, dog, bird}
```
در `Dog dog dogs` پیش از کوچک‌سازی سه Type داریم؛ بعد از کوچک‌سازی دو شکل و بعد از یکسان‌سازی جمع ممکن است یک Term باقی بماند.

### مرز سند و توکن‌سازی
پیش از ایندکس باید تعیین شود یک ایمیل و پیوست‌هایش یک سندند یا چند سند. استخراج متن PDF با HTML یکسان نیست؛ PDF اسکن‌شده ممکن است به OCR نیاز داشته باشد. فاصله معیار همیشگی مرز واژه نیست: نام‌هایی مثل `New York`، کلمات خط‌تیره‌دار و زبان‌های بدون فاصله تصمیم‌های ویژه می‌خواهند.

### نرمال‌سازی فارسی و کلمات توقف
یکسان‌سازی «ي/ی» و «ك/ک»، اعراب، کشیده و نیم‌فاصله به کاهش اختلاف نوشتاری کمک می‌کند. همان خط لوله باید روی سند و پرس‌وجو اعمال شود. حذف کورکورانهٔ همهٔ فاصله‌ها یا علائم می‌تواند معنی را خراب کند.

حذف کلمات توقف اختیاری است؛ برای عبارت‌هایی مانند `to be or not to be` این کلمات مهم‌اند. اگر حذف انجام شود، برای جست‌وجوی موقعیتی نباید فاصله‌های اصلی توکن‌ها بی‌دلیل فشرده شوند. نگهداری توقف‌واژه‌ها و استفاده از وزن‌دهی، گزینهٔ دیگری است.

### خطاهای ریشه‌یابی
**Over-stemming:** ادغام واژه‌های متفاوت و احتمال کاهش Precision. **Under-stemming:** جدا ماندن صورت‌های مرتبط و احتمال کاهش Recall. ریشه‌یابی لزوماً واژهٔ معتبر تولید نمی‌کند؛ مثلاً `ponies → poni` ایراد اجرایی نیست. لماتیزاسیون ممکن است به نقش دستوری نیاز داشته باشد: `saw` می‌تواند اسم یا گذشتهٔ see باشد.
''',
3: '''
### محاسبهٔ دقیق m و شرط‌ها
در `[C](VC)^m[V]`، C و V گروه‌های متوالی بی‌صدا و صدادارند، نه لزوماً یک حرف. در شروع کلمه y بی‌صداست؛ در ادامه، وضعیت آن نسبت به حرف قبلی تعیین می‌شود. شرط m روی **ساقهٔ قبل از پسوند مورد بررسی** سنجیده می‌شود.

```text
trouble:    tr | ou | bl | e       → C V C V       → m=1
relational: r | e | l | a | t | io | n | a | l → m=4
boy:        b | o | y             → C V C         → m=1
sky:        sk | y                → C V           → m=0
```
نماد `*v*` یعنی ساقه حداقل یک صدادار دارد؛ `*d` یعنی پایان با بی‌صدای تکراری؛ `*o` یعنی پایان CVC که آخرین حرف w یا x یا y نیست.

### فازهای ۲ تا ۵: تکمیل قواعد
این جدول مرور آموزشی قواعد است؛ فازهای ۲ و ۳ روی ساقه شرط `m > 0` دارند. قواعد با ترتیب و انتخاب پسوند مناسب اجرا می‌شوند، نه جایگزینی آزاد همهٔ رشته‌ها.

| فاز | قواعد |
|---|---|
| ۲ | ational→ate، tional→tion، enci→ence، anci→ance، izer→ize، abli→able، alli→al، entli→ent، eli→e، ousli→ous |
| ۲ (ادامه) | ization→ize، ation→ate، ator→ate، alism→al، iveness→ive، fulness→ful، ousness→ous، aliti→al، iviti→ive، biliti→ble |
| ۳ | icate→ic، ative→∅، alize→al، iciti→ic، ical→ic، ful→∅، ness→∅ |
| ۴ | اگر m>1 باشد: حذف al، ance، ence، er، ic، able، ible، ant، ement، ment، ent، ou، ism، ate، iti، ous، ive، ize |
| ۴: ion | حذف با شرط m>1 و پایان ساقه به s یا t |
| ۵a | حذف e نهایی اگر m>1، یا m=1 و ساقه شرط CVC ویژه را نداشته باشد |
| ۵b | تبدیل ll نهایی به l اگر m>1 باشد |

### ردگیری مرحله‌ای و دام امتحانی
```text
caresses → caress                  (1a)
hopping → hopp → hop               (1b + پاک‌سازی)
filing → fil → file                (1b + افزودن e)
agreed → agree → agre              (1b سپس 5a)
relational → relate → relat        (2 سپس 5a)
cry → cry                          (1c اجرا نمی‌شود)
```
در `agreed` قاعدهٔ eed انتخاب می‌شود؛ اگر شرط آن برقرار نبود نباید همان واژه را با قاعدهٔ کوتاه‌تر ed حذف کنیم. قواعد 1a، 1b، 1c به‌ترتیب اجرا می‌شوند و سپس فازهای بعدی می‌آیند.
''',
4: '''
### هزینه و محدودیت پرش
پرش‌ها نتیجهٔ اشتراک را عوض نمی‌کنند؛ فقط تعداد مقایسه‌ها را کاهش می‌دهند. اگر مقصد از عنصر جاری فهرست مقابل بزرگ‌تر باشد، پرش مجاز نیست چون ممکن است پاسخ را رد کند. تعداد و فاصلهٔ حدود √P یک قاعدهٔ تجربی برای فهرست نسبتاً ثابت است، نه قانون بهینگی.

پرش‌ها فضا و هزینهٔ نگهداری دارند؛ با درج و حذف زیاد توزیع مناسب آن‌ها تغییر می‌کند. برای اجتماع OR معمولاً همان سود AND را ندارند، زیرا عناصر ردشده نیز باید در خروجی اجتماع بیایند.

### مثال ردگیری
```text
A = [1,2,4,11,31,45,173]
B = [2,31,54,101]
1 < 2 → حرکت در A
2 = 2 → خروجی 2
A روی 4 و B روی 31: پرش 4 → 31 مجاز است
31 = 31 → خروجی 31
نتیجه: [2,31]
```
**مرور:** اگر B روی 11 بود، پرش از 4 به 31 مجاز نبود.
''',
5: '''
### مثال حل‌شدهٔ جست‌وجوی موقعیتی
```text
data   → d1:[1,7], d2:[2]
mining → d1:[2,9], d2:[5]
class  → d1:[3],   d2:[6]
```
برای عبارت `data mining` فقط d1 پاسخ است، چون ۲ برابر ۱+۱ است؛ رخدادهای ۷ و ۹ مجاور نیستند. عبارت سه‌واژه‌ای `data mining class` نیز در d1 از موقعیت ۱ شروع می‌شود. اشتراک DocIDها فقط مرحلهٔ کاندیدسازی است، نه پاسخ نهایی.

### مثبت کاذب Biword
سند `data mining is useful; mining class starts today` هر دو biword یعنی `data mining` و `mining class` را دارد، ولی عبارت کامل `data mining class` را ندارد. پس AND دو biword برای عبارت بلند کافی نیست و باید متن یا موقعیت‌ها بررسی شود.

### قرارداد فاصله و واژه‌های تکراری
اگر فاصله را اختلاف موقعیت تعریف کنیم، `|p2-p1| ≤ k` یعنی اختلاف اندیس حداکثر k؛ اما اگر «تعداد کلمات بین دو واژه» منظور باشد، این تعداد `|p2-p1|-1` است. ترتیب نیز باید مشخص باشد: برای نسخهٔ مرتب `0 < p2-p1 ≤ k`.

برای `to be or not to be` تمام موقعیت‌های شروع باید با یک زنجیرهٔ مشترک بررسی شوند: `to:p`، `be:p+1`، `or:p+2`، `not:p+3`، `to:p+4`، `be:p+5`. حضور مستقل واژه‌ها کافی نیست.
''',
6: '''
### TF، DF و CF با مثال عددی
```text
d1: data data mining
d2: data class
d3: mining
TF(data,d1)=2
DF(data)=2
CF(data)=3
```
CF تعداد کل رخدادهای یک ترم در مجموعه است و برابر مجموع TF آن روی همهٔ اسناد است. در postings ساده طول فهرست برابر DF است، نه CF. همیشه `df(t) ≤ N` و `cf(t) ≥ df(t)` برقرار است.

### انتخاب ساختار در عمل
Hash برای تطابق کامل مناسب است ولی ترتیب واژگان را به‌طور طبیعی نگه نمی‌دارد. جست‌وجوی میانگین O(1) به تابع هش و ضریب بار مناسب وابسته است؛ زمان بدترین حالت می‌تواند خطی باشد. BST نامتوازن نیز می‌تواند O(V) شود. درخت متوازن جست‌وجوی O(log V) دارد؛ B-Tree با شاخه‌زایی زیاد برای کاهش I/O صفحه‌ای مناسب است.

برای جست‌وجوی پیشوندی ابتدا ابتدای بازهٔ مرتب پیدا می‌شود و سپس نتایج خوانده می‌شوند؛ هزینهٔ خروجی نتایج را نباید از محاسبهٔ زمان حذف کرد.
''',
7: '''
### Wildcard از واژگان به اسناد
ایندکس کمکی wildcard معمولاً ابتدا **واژه‌های واژگان** را برمی‌گرداند، نه DocIDها. پس از فیلتر نامزدها، postings واژه‌های پذیرفته‌شده با OR ترکیب می‌شوند تا اسناد حاصل شوند. در این درس * به معنی صفر یا چند نویسه است.

### مثال کامل Permuterm
```text
word: hello → hello$
query: he*o → he*o$ → o$he*
prefix to look up: o$he
matching rotation: o$hell → original word: hello
```
برای واژه‌ای با طول L، تعداد چرخش‌ها L+1 است. ذخیرهٔ سادهٔ رشتهٔ کامل هر چرخش هزینهٔ قابل‌توجه دارد. تبدیل تک‌ستاره به یک پیشوند مستقیم است؛ چند ستاره به پردازش اضافی و تطبیق نهایی نیاز دارد.

### مثال k-gram و دلیل فیلتر نهایی
برای الگوی `re*ve` و bigram، شرط‌های ضروری شامل `$r`، `re`، `ve` و `e$` هستند. واژهٔ `receive` این شرط‌ها را دارد و با الگو سازگار است. واژهٔ `reverse` نیز این قطعات را دارد، اما به ve ختم نمی‌شود؛ پس باید در مرحلهٔ تطبیق با الگوی اصلی حذف شود.

برای قطعه‌ای کوتاه‌تر از k ممکن است هیچ k-gram قابل‌استفاده‌ای تولید نشود. کاهش k نامزدها را بیشتر می‌کند؛ افزایش k برخی قطعات کوتاه را بی‌استفاده می‌کند. قطعاتی که از روی * عبور می‌کنند نباید به‌عنوان زیررشتهٔ قطعی استخراج شوند.
'''
}
questions={
1:('آیا مدل بولی اسناد را بر اساس ارتباط رتبه‌بندی می‌کند؟','خیر. عضویت در پاسخ صفر و یک است؛ مرتب‌سازی احتمالی خروجی با رتبه‌بندی ارتباط تفاوت دارد.'),
2:('در cat dog cat چند Token و چند Type داریم؟','سه Token و دو Type؛ هر رخداد یک توکن است.'),
3:('چرا cry در پورتر کلاسیک تغییر نمی‌کند؟','ساقهٔ cr هیچ صداداری ندارد؛ شرط قاعدهٔ 1c برقرار نیست.'),
4:('اگر عنصر مقابل ۲۰ باشد، آیا پرش از ۴ به ۳۱ مجاز است؟','خیر؛ مقصد باید کوچک‌تر یا مساوی عنصر مقابل باشد.'),
5:('آیا وجود همهٔ biwordها، وجود عبارت بلند را تضمین می‌کند؟','خیر؛ ممکن است در قسمت‌های جداگانهٔ سند باشند.'),
6:('یک واژه ۴ بار در d1 و ۲ بار در d2 است؛ DF و CF چیست؟','DF=2 و CF=6؛ TF در d1 برابر 4 است.'),
7:('چرا بعد از اشتراک k-gramها فیلتر لازم است؟','وجود قطعات، ترتیب و محل درست آن‌ها نسبت به مرز و ستاره را تضمین نمی‌کند.')}
practice=json.loads((root/'practice.json').read_text())
def practice_block(n):
 items=[('پرسش اصلی', *questions[n])]+practice[str(n)]
 cards=''.join(f'<div class="practice-card"><span class="eyebrow">{i} / {label}</span><p>{html.escape(q)}</p><details><summary>پاسخ را ببین</summary><p>{html.escape(a)}</p></details></div>' for i,(label,q,a) in enumerate(items,1))
 return f'<section class="self-test"><h2>خودت را بسنج · ۴ پرسش کوتاه</h2><p>بدون عجله جواب بده؛ هر پاسخ را جدا باز کن و با جواب خودت مقایسه کن.</p><div class="practice-grid">{cards}</div></section>'
porter_demo='''<section id="porter-demo" class="porter-demo"><h2>پورتر را مرحله‌به‌مرحله اجرا کن</h2><p>ردگیری آموزشیِ پنج واژه در پورتر کلاسیک (۱۹۸۰)، نه Porter2. هر کلیک یک مرحله یا زیرمرحله را نشان می‌دهد؛ این بخش ورودی آزاد و موتور عمومی ریشه‌یابی نیست.</p><div class="porter-controls" hidden><label for="porter-word-select">واژهٔ نمونه</label> <select id="porter-word-select" dir="ltr"><option>caresses</option><option>hopping</option><option>filing</option><option>relational</option><option>cry</option></select><div class="porter-display" aria-live="polite" aria-atomic="true"><strong class="porter-stage"></strong><div class="porter-word" dir="ltr"></div><p class="porter-explanation"></p><small class="porter-counter"></small></div><progress max="7" value="0" aria-label="پیشرفت مراحل پورتر"></progress><div class="porter-buttons"><button type="button" data-porter="prev">مرحلهٔ قبل</button><button type="button" data-porter="next">مرحلهٔ بعد</button><button type="button" data-porter="reset">شروع دوباره</button></div><p>مسیر تغییر واژه (صورت‌های بدون تغییر تکرار نمی‌شوند):</p><p class="porter-trail" dir="ltr"></p><small>بخش خط‌خورده حذف می‌شود؛ بخش رنگی اضافه می‌شود. خروجی هر مرحله لزوماً خروجی نهایی نیست.</small></div><noscript>برای نمایش تعاملی، جاوااسکریپت را فعال کنید. مثال‌های متنی فصل بدون آن قابل مطالعه‌اند.</noscript></section>'''
refs={1:('01intro.pdf',4,'اسلایدهای ۴ تا ۴۰؛ تعریف، بولی و ایندکس'),2:('مبانی جست و جوی اطلاعات.pdf',12,'صفحات ۱۲، ۱۵ و ۱۶؛ پردازش متن'),3:('مبانی جست و جوی اطلاعات.pdf',11,'صفحات ۶ تا ۱۴؛ پورتر'),4:('1000025343.jpg',None,'عکس جزوه؛ پرش و فهرست‌ها'),5:('1000025344.jpg',None,'عکس جزوه؛ biword و موقعیت'),6:('1000025346.jpg',None,'عکس جزوه؛ دیکشنری و بسامد'),7:('1000025347.jpg',None,'عکس جزوه؛ wildcard و k-gram')}
def shell(title,body,script=''):
 return f'''<!doctype html><html lang="fa" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | دفتر مطالعه</title><link rel="stylesheet" href="site.css"><link rel="stylesheet" href="course.css">{script}</head><body><header class="site-header"><a class="brand" href="index.html">▤ دفتر مطالعه</a><nav><a href="index.html#lessons">فصل‌ها</a> · <a href="resources.html">منابع</a> · <a href="review.html">مرور</a></nav></header>{body}<footer class="site-footer">بازیابی اطلاعات · بازنویسی آموزشی منابع ارسالی؛ مثال‌های افزوده برای یادگیری هستند.</footer></body></html>'''
chapters=[]
for n,part in enumerate(re.split(r'^## ',source,flags=re.M)[1:],1):
 title,body=part.split('\n',1)
 title=re.sub(r'^[۰-۹]+\.\s*','',title)
 body+=extras[n]
 # Render plain mathematical notation without online MathJax dependency.
 body=re.sub(r'\$\$(.*?)\$\$',lambda m:'\n```text\n'+m[1].replace(r'df(t) = |\{d : t \text{ در سند } d \text{ حضور دارد}\}|','df(t) = number of documents containing t').replace(r'\text{فاصلهٔ پرش}', 'skip span').replace(r'\approx','≈').replace(r'\sqrt{P}','√P').replace(r'\le','≤').replace(r'\{','{').replace(r'\}','}').replace(r'\text{ در سند }',' in ').replace(r'\text{ حضور دارد}',' occurs')+'\n```\n',body,flags=re.S)
 rendered=md(body)
 soup=BeautifulSoup(rendered,'html.parser'); topics=[]
 for i,h in enumerate(soup.find_all(['h3','h4']),1):
  h['id']=f'slide-{i}'; texts=[]
  for sib in h.next_siblings:
   if getattr(sib,'name',None) in ['h3','h4']:break
   texts.append(sib.get_text(' ',strip=True) if hasattr(sib,'get_text') else str(sib))
  topics.append(dict(title=h.get_text(),text=' '.join(texts),slide=i))
 # Include introductory prose/tables in full-text search as well.
 if topics:
  intro=[]
  for child in soup.children:
   if getattr(child,'name',None) in ['h3','h4']: break
   intro.append(child.get_text(' ',strip=True) if hasattr(child,'get_text') else str(child))
  topics[0]['text']=' '.join(intro)+' '+topics[0]['text']
 filename=f'chapter-{n}.html';ref,page,label=refs[n];link='bin/'+ref+(f'#page={page}' if page else '')
 toc=''.join(f'<a href="#slide-{t["slide"]}">{html.escape(t["title"])}</a>' for t in topics)
 q,a=questions[n]
 content=f'''<main class="reading-layout"><aside class="toc"><span class="eyebrow">در این فصل</span>{toc}</aside><article class="lesson"><span class="eyebrow">فصل {n} / درس‌نامهٔ بازنویسی‌شده</span><h1>{title}</h1><p class="source-note">مبنای فصل: <a href="{link}">{label} ↗</a> و متن تایپ‌شدهٔ جزوه. توضیح‌ها و مثال‌های تکمیلی به متن افزوده شده‌اند؛ این صفحه رونویسی کلمه‌به‌کلمه نیست.</p><button class="print-button" onclick="window.print()">چاپ / ذخیره PDF</button>{soup}{porter_demo if n == 3 else ''}{practice_block(n)}<label class="complete"><input type="checkbox" data-done="{n}"> این فصل را مطالعه کردم</label><div class="study-progress"><label for="lesson-study-meter">پیشرفت کل مطالعه: <span data-progress-label role="status" aria-live="polite">۰ از ۷ فصل</span></label><progress id="lesson-study-meter" data-study-meter max="7" value="0"></progress><small data-progress-note></small></div><nav class="chapter-nav">{f'<a href="chapter-{n-1}.html">→ فصل قبل</a>' if n>1 else '<a href="index.html">خانه</a>'}{f'<a href="chapter-{n+1}.html">فصل بعد ←</a>' if n<7 else '<a href="review.html">مرور نهایی ←</a>'}</nav></article></main>'''
 (root/filename).write_text(shell(title,content,'<script src="progress.js" defer></script>' + ('<script src="porter.js" defer></script>' if n == 3 else '')))
 chapters.append(dict(id=n,title=title,url=filename,description=topics[0]['title']+'، '+topics[-1]['title'],topics=topics))
(root/'topics.js').write_text('window.chapters = '+json.dumps(chapters,ensure_ascii=False)+';')
# Keep all original sources accessible, without altering them.
labels=['مقایسهٔ IR و DB و ایندکس معکوس','Stemming و Lemmatization','ساختار واژه و قواعد پورتر','Skip Pointers و اشتراک','Biword و پرس‌وجوی عبارتی','ایندکس موقعیتی و عبارت تکراری','دیکشنری، TF و DF','درخت‌ها، Wildcard و k-gram']
gallery=''.join(f'<figure><a href="bin/{p.name}"><img src="bin/{p.name}" loading="lazy" alt="{label}"></a><figcaption>{label}<br><a href="bin/{p.name}">نمایش تصویر اصلی ↗</a></figcaption></figure>' for p,label in zip(sorted((root/'bin').glob('*.jpg')),labels))
resources='''<main><section class="page-intro"><span class="eyebrow">کتابخانهٔ منابع</span><h1>جزوه‌ها، عکس‌ها و نسخهٔ اصلی</h1><p>فایل‌های ارسالی بدون تغییر نگه داشته شده‌اند. بعضی عکس‌ها چرخیده یا کم‌خوانا هستند؛ برای جزئیات تصویر اصلی را باز کنید. مطالب ناخوانا به‌عنوان نقل‌قول قطعی بازسازی نشده‌اند.</p></section><div class="resource-links"><a href="bin/01intro.pdf">PDF مقدمه و بازیابی بولی · ۴۰ صفحه ↗</a><a href="bin/مبانی جست و جوی اطلاعات.pdf">PDF فارسی و تصاویر کلاس · ۱۶ صفحه ↗</a><a href="bin/information_retrieval_notes.md">متن تایپ‌شدهٔ اولیه (بدون اصلاح) ↗</a><a href="html/artifact%20(1).html">اسلایدهای قبلی فصل اول (آرشیو) ↗</a><a href="html/artifact%20(2).html">اسلایدهای قبلی فصل دوم (آرشیو) ↗</a></div><p class="source-note">آرشیو نسخهٔ قدیمی است و ممکن است ساده‌سازی یا خطاهای قبلی را داشته باشد. برای مطالعه، درس‌نامه‌های بازنویسی‌شده پیشنهاد می‌شوند.</p><h2>گالری جزوهٔ دست‌نویس</h2><div class="gallery">'''+gallery+'</div></main>'
(root/'resources.html').write_text(shell('منابع درس',resources,'<script src="progress.js" defer></script>'))
review='''<main class="lesson review"><span class="eyebrow">قبل از امتحان</span><h1>مرور سریع و پرسش‌های کلیدی</h1><p>پاسخ را ابتدا خودت بنویس، سپس بخش پاسخ تشریحی را باز کن.</p><div class="formula"><p>AND = اشتراک · OR = اجتماع · AND NOT = تفاضل</p><p dir="ltr">Merge: O(x+y) · Skip span ≈ √P<br>Phrase: pos(B) = pos(A)+1<br>DF(t) ≤ N · CF(t) = Σ TF(t,d)</p></div>'''
for n in questions:
 review+=f'<h2>فصل {n}</h2>'+practice_block(n)+f'<a href="chapter-{n}.html">بازگشت به فصل مربوط ←</a>'
review+='''<h2>اشتباه‌های رایج</h2><ul><li>IR همیشه رتبه‌بندی ندارد؛ بازیابی بولی هم IR است.</li><li>Type و Term لزوماً یکسان نیستند.</li><li>m روی ساقهٔ پیش از پسوند سنجیده می‌شود.</li><li>cry در Porter کلاسیک بدون تغییر می‌ماند.</li><li>پرش نباید از عنصر مقابل عبور کند.</li><li>اشتراک biword یا k-gram نیازمند بررسی نهایی است.</li><li>DF تعداد اسناد است؛ TF تعداد رخداد در یک سند.</li></ul><h2>یادداشت اصلاح علمی</h2><p>در مقایسه با متن اولیه، شرط استثنای l/s/z در پاک‌سازی 1b، مثال cry، تفاوت هزینهٔ پیش‌پردازش و سرعت جست‌وجو، و تضمینی نبودن اثر ریشه‌یابی بر کیفیت اصلاح شده‌اند. مباحث رتبه‌بندی پیشرفته مانند BM25 در منابع حاضر به‌صورت درس کامل ارائه نشده‌اند و این سایت نیز آن‌ها را به‌عنوان محتوای تدریس‌شده معرفی نمی‌کند.</p></main>'''
(root/'review.html').write_text(shell('مرور امتحان',review,'<script src="progress.js" defer></script>'))
print('Built',len(chapters),'chapters;',sum(len(c['topics']) for c in chapters),'topics')
