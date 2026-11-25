---
title: «واژه‌نامه‌ها و بازیابی با تطبیق غیردقیق»
slug: dictionaries-and-tolerant-retrieval
chapter: 3
source: '03dict (1).pptx'
authors: [Hinrich Schütze, Christina Lioma]
---

# فصل ۳: واژه‌نامه‌ها و بازیابی با تطبیق غیردقیق

اگر کاربر `mon*` یا `informaton` را جست‌وجو کند، ممکن است هیچ واژه‌ای در سند عیناً با ورودی او یکسان نباشد. موتور جست‌وجو چطور می‌تواند واژه‌های منظور کاربر را پیدا کند و از آن‌ها به سند برسد؟ این پرسش، سه لایهٔ فصل را به هم وصل می‌کند: **یافتن واژه، سنجیدن شباهت و بازیابی سند**.

## قرارداد تحویل به عامل سایت

این فایل دو لایه دارد: طرح آموزشی فارسی زیر برای ساخت صفحه‌ها، و سپس متن انگلیسی و شکل‌های منبع به ترتیب هر ۱۱۵ اسلاید برای کنترل وفاداری. متن راهنما و پاسخ‌های توضیحی افزوده‌اند و نقل‌قول از مدرس نیستند. برای هر صفحه یک نشانی پایدار بر پایهٔ شناسهٔ زیر بساز. اسلایدهای فهرست را به ناوبری تبدیل کن؛ برای هر فریم انیمیشن صفحهٔ جدا نساز. مثال‌ها، ترتیب مراحل، نمادهای مرز واژه، اعراب لاتین و حروف کلیدی را تغییر نده. کد، فرمول، جدول ماتریس و پرس‌وجو چپ‌به‌راست، توضیحات فارسی راست‌به‌چپ باشند. تصاویر پیوست مرجع صحت‌اند؛ ماتریس‌ها و جدول‌ها را در سایت به صورت متن قابل‌دسترسی هم بساز. تمرین را پیش از نمایش اختیاری پاسخ بیاور. نام مدرس‌ها و منابع انتهای فصل حفظ شود.

### ۱. `foundations` — از رخداد واژه تا مکان آن در سند (۱–۱۰)

در جملهٔ اسلاید ۴، هر بار آمدن `the` یک token جداست، اما در شمارش typeها فقط یک بار حساب می‌شود. با یکسان‌سازی بزرگی حروف، ۱۲ رخداد و ۹ نوع داریم. به کاربر اجازه بده رخدادهای هم‌نوع را با انتخاب یک کلمه روشن کند. سپس نشان بده چرا فاصله، خط تیره یا آپاستروف همیشه مرز قابل اتکایی نیستند، و چرا تاریخ، حروف بزرگ، صرف، اشتقاق و اعراب بر انتخاب term اثر دارند. مثال‌های زبانی را از متن همان اسلاید بگیر.

در شکل Brutus/Caesar، اشاره‌گر پرش میان دو ورودی دورتر امکان رد شدن از بخشی از فهرست مرتب را هنگام اشتراک فراهم می‌کند. در نمایهٔ مکانی، افزون بر شناسهٔ سند، مکان هر رخداد را داریم. داده‌های `TO` و `BE` اسلاید ۸ را عیناً نمایش بده: در سند ۴ مثلاً ۱۶ و ۱۷ همسایه‌اند. این دو فهرست به‌تنهایی حضور کل عبارت شش‌واژه‌ای را اثبات نمی‌کنند؛ برای اجرای واقعی، مکان `or` و `not` و همهٔ فاصله‌های نسبی نیز لازم‌اند. تطبیق عبارت دقیق را از پرس‌وجوی مجاورت متمایز کن.

### ۲. `dictionary` — واژه‌نامه چه چیزی را نگه می‌دارد؟ (۱۱–۲۱)

شکل نمایهٔ معکوس را در دو حالت نشان بده: سمت واژه‌ها، واژه‌نامه است؛ سمت فهرست‌ها، شناسه‌های سند. «مجموعهٔ واژگان» داده است و «واژه‌نامه» ساختار نگهداری آن. سطر نمونه سه میدان دارد: واژه (۲۰ بایت)، بسامد سندی (۴ بایت) و اشاره‌گر (۴ بایت). بسامد سندی تعداد **سندهای** حاوی واژه است، نه تعداد همهٔ رخدادها.

در جست‌وجوی دقیق با هش، واژه به عدد تبدیل می‌شود و برخوردهای احتمالی باید حل شوند؛ زمان ثابت را به‌عنوان رفتار مورد انتظار توضیح بده، نه تضمین بدترین حالت. هش معمولی برای پیمایش مرتب واژه‌های با پیشوند `automat` مناسب نیست. درخت مرتب این پیمایش را ممکن می‌کند؛ هزینهٔ یافتن کلید در درخت دودویی متوازن `O(log M)` است، نه در هر درخت دلخواه. شکل‌های درخت دودویی و B-tree را کنار هم نشان بده و رشد واژگان، هزینهٔ توازن و الگوی دسترسی را در انتخاب ساختار دخیل کن.

### ۳. `wildcards` — ابتدا واژه‌های منطبق، سپس سندها (۲۲–۳۴)

`mon*` را به جست‌وجوی بازهٔ `mon ≤ t < moo` تبدیل کن. برای `*mon`، در واژه‌نامهٔ معکوس‌شده دنبال `nom ≤ t < non` بگرد. `m*nchen` را می‌توان با اشتراک **دو مجموعهٔ واژه** حل کرد. تازه پس از آن، فهرست سندهای واژه‌های باقی‌مانده را اجتماع می‌گیریم.

برای permuterm نشانگر `$` را به انتهای `hello` بیفزا و چرخش‌ها را به واژهٔ اصلی وصل کن. در مثال `hel*o`، جست‌وجوی پیشوند `o$hel` به `hello` می‌رسد. **نکتهٔ پیاده‌سازی:** اسلاید ۲۷ برای `X*` عبارت `X*$` را چاپ کرده؛ آن را کلید نهایی جست‌وجوی پیشوندی ندان. پس از افزودن مرز، الگو را بچرخان تا ستاره آخر باشد: `$X*`. اگر این روش را پیاده می‌کنی چرخش آغازشونده با `$` (برای نمونه `$hello`) نیز لازم است؛ این چرخش در فهرست کوتاه اسلاید نیامده است. عدد افزایش حجم در اسلاید ۲۸ مشاهدهٔ تجربی است.

در روش k-gram، مقصد فهرست یک گرم، **واژه** است نه سند. برای `mon*` اشتراک فهرست‌های `$m`، `mo` و `on` را نشان بده؛ `moon` هر سه را دارد ولی با `mon` شروع نمی‌شود. پس آزمون نهایی الگو را قبل از رجوع به نمایهٔ اسناد اجرا کن. فهرست bigram جملهٔ `April is the cruelest month` در متن اسلاید ۲۹ را به‌عنوان نقل منبع نگه دار؛ در تولید تعاملی، `month` شامل `th` هم هست. تمرین Google را با تاریخ ۲۰۱۰ نمایش بده، نه به‌عنوان مستندات فعلی. هزینهٔ گسترش `[gen* universit*]` را با AND میان دو گروه و OR درون هر گروه توضیح بده.

### ۴. `edit-distance` — تصحیح چه چیزی و با چه هزینه‌ای؟ (۳۵–۵۴)

بین اصلاح سند OCR و پیشنهاد هنگام جست‌وجو فرق بگذار. `informaton → information` با درج حل می‌شود؛ `form` در جملهٔ مربوط به سیارک خود واژه‌ای معتبر است و روش تک‌واژه‌ای شواهد لازم برای تبدیل آن به `from` را ندارد. واژگان پیکره ممکن است خود حاوی غلط باشند؛ واژه‌نامهٔ عمومی، تخصصی یا وزن‌دار سه انتخاب متفاوت‌اند.

در Levenshtein درج، حذف و جایگزینی هر کدام یک واحد هزینه دارند؛ کپی رایگان است. در Damerau–Levenshtein جابه‌جایی دو حرف مجاور نیز مجاز است. به همین دلیل `cat → act` به‌ترتیب ۲ و ۱ هزینه دارد. برای ساخت مثال‌های اسلایدهای ۴۲–۵۰، سطرها را از رشتهٔ مبدأ و ستون‌ها را از مقصد بگیر. در شکل منبع آن‌ها `cats` و `fast` هستند. زیرمسئله، فاصلهٔ دو **پیشوند** است؛ نه فاصلهٔ دو حرف آخر.

```text
D[i,0] = i; D[0,j] = j
for i = 1..len(source):
  for j = 1..len(target):
    delete  = D[i-1,j] + 1
    insert  = D[i,j-1] + 1
    replace_or_copy = D[i-1,j-1] + (source[i-1] != target[j-1])
    D[i,j] = min(delete, insert, replace_or_copy)
return D[len(source),len(target)]
```

در نمایش هر خانه، هزینهٔ قطری بالا-چپ، هزینهٔ حذف بالا-راست، هزینهٔ درج پایین-چپ و کمینه پایین-راست قرار بگیرد (اسلاید ۴۹). با وزن‌دار کردن، مثلاً `m → n` ارزان‌تر از `m → q` می‌شود؛ هزینه‌های مرز هم باید با هزینه‌های درج/حذف سازگار باشند. برای پیشنهاد املا، همسایگی فاصله‌ای را با فهرست واژه‌های مجاز اشتراک بگیر.

### ۵. `distance-lab` — کارگاه ماتریس و بازسازی مسیر (۵۵–۹۹)

اسلایدهای ۵۵–۸۸ فریم‌های پرکردن ماتریس‌اند: ابتدا سطر و ستون مرزی، سپس هزینه‌های نامزد و بعد کمینهٔ هر خانه را سطربه‌سطر نشان بده. کلیدهای «قبلی»، «بعدی» و «ماتریس کامل» بگذار. دادهٔ آزمون نهایی:

| OSLO ↓ / SNOW → | ∅ | S | N | O | W |
|---|---:|---:|---:|---:|---:|
| ∅ | 0 | 1 | 2 | 3 | 4 |
| O | 1 | 1 | 2 | 2 | 3 |
| S | 2 | 1 | 2 | 3 | 3 |
| L | 3 | 2 | 2 | 3 | 4 |
| O | 4 | 3 | 3 | 2 | 3 |

اسلایدهای ۸۹–۹۴ از پایین‌راست به ابتدا برمی‌گردند. عملیات را برای اجرا معکوسِ ترتیب برگشت بخوان: حذف `O` اول، کپی `S`، جایگزینی `L → N`، کپی `O` و درج `W`. نمایش رشته‌های حاصل: `OSLO → SLO → SNO → SNOW`. هزینهٔ کل ۳ است؛ کپی‌ها را از جدول عملیات حذف نکن.

در اسلایدهای ۹۵–۹۹، `cat → catcat` نیز فاصلهٔ ۳ دارد. چهار هم‌ترازی شکل‌ها را حفظ کن: `---cat`، `c---at`، `ca---t` و `cat---` را زیر مقصد ثابت `catcat` بگذار (خط تیره جای درج در ورودی است). پس کمینهٔ عددی یکتاست ولی مسیر بهینه لزوماً یکتا نیست.

### ۶. `spelling` — تولید پیشنهاد، رتبه‌بندی و نقش بافت (۱۰۰–۱۰۷)

برای `bordroom` هفت bigram داخلی را بدون نشانگر مرز بگیر؛ این قرارداد با مثال wildcard متفاوت است. فهرست‌های `bo`، `or` و `rd` در شکل ۱۰۳ فقط بخشی از نمایه‌اند. تعداد گرم‌های مشترک برای محدود کردن نامزدها مفید است؛ اشتراک گرم به‌تنهایی اثبات برابری واژه‌ها نیست.

در مثال `flew form munich` هر بار فقط یک جایگاه را تغییر بده و تعداد نتایج عبارت‌ها را مقایسه کن. `flew from munich` در مثال درس برنده است. اگر ۷، ۲۰ و ۳ **جایگزین** داشته باشیم، با همین قید ۳۰ عبارت اصلاح‌شده داریم (بدون عبارت دست‌نخورده)، نه حاصل‌ضرب سه عدد. سپس روش مبتنی بر سابقهٔ پرس‌وجوها را در برابر اجرای همهٔ جست‌وجوها مطرح کن. تصمیم رابط: تصحیح خودکار یا پیشنهاد؛ یک پیشنهاد یا چند انتخاب؛ اجرای همیشگی یا فقط پس از یافتن نتایج کم؟

تمرین Norvig: کد تصویری ۱۰۷ را به سه بخش توضیح بده: یادگیری فراوانی واژه‌ها از `big.txt`؛ ساخت نامزدهای یک ویرایش با شکستن رشته در همهٔ مرزها و آزمودن حذف، جابه‌جایی، جایگزینی و درج؛ و انتخاب پربسامدترین عضو نخستین گروه ناتهی (خود واژهٔ شناخته‌شده، شناخته‌شده‌های یک ویرایش، شناخته‌شده‌های دو ویرایش، و سرانجام خود ورودی). تصویر کد تاریخی است؛ اگر بازنویسی اجرایی می‌دهی آن را جدا از اصل مشخص کن.

### ۷. `soundex` — شباهت آوایی، نه شباهت نوشتاری (۱۰۸–۱۱۵)

نسخهٔ همین درس را اجرا کن: حرف اول را نگه دار؛ روی باقی حروف نگاشت اسلاید ۱۱۰ را اعمال کن؛ ارقام برابر **مجاور** را ادغام کن؛ سپس صفرها را حذف کن. در صورت نیاز صفر بیفزا و فقط یک حرف و سه رقم برگردان. ترتیب حذف صفر و ادغام ارقام مهم است. در `HERMAN`، بخش `06505` پیش از حذف صفر هیچ رقم برابرِ مجاوری ندارد؛ نتیجه `H655` است و `HERMANN` هم همان کد را می‌دهد. واژه و پرس‌وجو باید با یک قرارداد کدگذاری شوند. کد یکسان دلیل هویت یا املای یکسان نیست. تمرین نام خانوادگی را با ورودی لاتین عرضه کن؛ این جدول برای خط فارسی تعریف نشده است. فصل را با تفاوت wildcard، اصلاح املایی و بازیابی آوایی جمع‌بندی کن.

---

## پیوست مرجع: متن و شکل‌های پاورپوینت، اسلاید به اسلاید

شماره‌های تزئینی تکراری حذف شده‌اند. متن منبع در بلوک ساده آمده تا ستاره‌ها، `$` و عملگرهای جست‌وجو را Markdown تفسیر نکند. اسلایدهایی که متن بدنه ندارند، مراحل تصویری مثال هستند.


### اسلاید 1

```text
Hinrich Schütze and Christina Lioma
Lecture 3: Dictionaries and tolerant retrieval
```


### اسلاید 2

```text
Overview
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 3

```text
Outline
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 4

```text
Type/token distinction
Token – an instance of a word or term occurring in a document
Type – an equivalence class of tokens
In June, the dog likes to chase the cat in the barn.
12 word tokens, 9 word types
```


### اسلاید 5

```text
Problems in tokenization
What are the delimiters? Space? Apostrophe? Hyphen?
For each of these: sometimes they delimit, sometimes they don’t.
No whitespace in many languages! (e.g., Chinese)
No whitespace in Dutch, German, Swedish compounds (Lebensversicherungsgesellschaftsangestellter)
```


### اسلاید 6

```text
Problems with equivalence classing
A term is an equivalence class of tokens.
How do we define equivalence classes?
Numbers (3/20/91 vs. 20/3/91)
Case folding
Stemming, Porter stemmer
Morphological analysis: inflectional vs. derivational
Equivalence classing problems in other languages
More complex morphology than in English
Finnish: a single verb may have 12,000 different forms
Accents, umlauts
```


### اسلاید 7

```text
Skip pointers
```

![Skip pointers — اسلاید 7][slide-007-1]


### اسلاید 8

```text
Positional indexes
Postings lists in a nonpositional index: each posting is just a docID
Postings lists in a positional index: each posting is a docID and a list of positions
Example query: “to1 be2 or3 not4 to5 be6” 
TO, 993427:
‹ 1: ‹7, 18, 33, 72, 86, 231›;
  2: ‹1, 17, 74, 222, 255›;
  4: ‹8, 16, 190, 429, 433›;
  5: ‹363, 367›;
  7: ‹13, 23, 191›; . . . ›
BE, 178239:
‹ 1: ‹17, 25›;
  4: ‹17, 191, 291, 430, 434›;
  5: ‹14, 19, 101›; . . . › Document 4 is a match!
```


### اسلاید 9

```text
Positional indexes
With a positional index, we can answer phrase queries.
With a positional index, we can answer proximity queries.
```


### اسلاید 10

```text
Take-away
Tolerant retrieval: What to do if there is no exact match between query term and document term
Wildcard queries
Spelling correction
```


### اسلاید 11

```text
Outline
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 12

```text
Inverted index
```

![Inverted index — اسلاید 12][slide-012-1]


### اسلاید 13

```text
Inverted index
```

![Inverted index — اسلاید 13][slide-013-1]


### اسلاید 14

```text
Dictionaries
The dictionary is the data structure for storing the term vocabulary.
Term vocabulary: the data
Dictionary: the data structure for storing the term vocabulary
```


### اسلاید 15

```text
Dictionary as array of fixed-width entries
For each term, we need to store a couple of items:
document frequency
pointer to postings list
. . .
Assume for the time being that we can store this information in a fixed-length entry.
Assume that we store these entries in an array.
```


### اسلاید 16

```text
Dictionary as array of fixed-width entries
space needed:   20 bytes   4 bytes            4 bytes
How do we look up a query term qi in this array at query time? That is: which data structure do we use to locate the entry (row) in the array where qi is stored?
```

![Dictionary as array of fixed-width entries — اسلاید 16][slide-016-1]


### اسلاید 17

```text
Data structures for looking up term
Two main classes of data structures: hashes and trees
Some IR systems use hashes, some use trees.
Criteria for when to use hashes vs. trees:
Is there a fixed number of terms or will it keep growing?
What are the relative frequencies with which various keys will be accessed?
How many terms are we likely to have?
```


### اسلاید 18

```text
Hashes
Each vocabulary term is hashed into an integer.
Try to avoid collisions
At query time, do the following: hash query term, resolve collisions, locate entry in fixed-width array
Pros: Lookup in a hash is faster than lookup in a tree.
Lookup time is constant.
Cons
no way to find minor variants (resume vs. résumé)
no prefix search (all terms starting with automat)
need to rehash everything periodically if vocabulary keeps growing
```


### اسلاید 19

```text
Trees
Trees solve the prefix problem (find all terms starting with automat).
Simplest tree: binary tree
Search is slightly slower than in hashes: O(logM), where M is the size of the vocabulary.
O(logM) only holds for balanced trees.
Rebalancing binary trees is expensive.
B-trees mitigate the rebalancing problem.
B-tree definition: every internal node has a number of children in the interval [a, b] where a, b are appropriate positive integers, e.g., [2, 4].
```


### اسلاید 20

```text
Binary tree
```

![Binary tree — اسلاید 20][slide-020-1]


### اسلاید 21

```text
B-tree
```

![B-tree — اسلاید 21][slide-021-1]


### اسلاید 22

```text
Outline
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 23

```text
Wildcard queries
mon*: find all docs containing any term beginning with mon
Easy with B-tree dictionary: retrieve all terms t in the range: mon ≤ t < moo
*mon: find all docs containing any term ending with mon
Maintain an additional tree for terms backwards
Then retrieve all terms t in the range: nom ≤ t < non
Result: A set of terms that are matches for wildcard query
Then retrieve documents that contain any of these terms
```


### اسلاید 24

```text
How to handle * in the middle of a term
Example: m*nchen
We could look up m* and *nchen in the B-tree and intersect the two term sets.
Expensive
Alternative: permuterm index
Basic idea: Rotate every wildcard query, so that the * occurs at the end.
Store each of these rotations in the dictionary, say, in a B-tree
```


### اسلاید 25

```text
Permuterm index
For term HELLO: add hello$, ello$h, llo$he, lo$hel, and o$hell to the B-tree where $ is a special symbol
```


### اسلاید 26

```text
Permuterm → term mapping
```

![Permuterm → term mapping — اسلاید 26][slide-026-1]


### اسلاید 27

```text
Permuterm index
For HELLO, we’ve stored: hello$, ello$h, llo$he, lo$hel, and o$hell
Queries
For X, look up X$
For X*, look up X*$
For *X, look up X$*
For *X*, look up X*
For X*Y, look up Y$X*
Example: For hel*o, look up o$hel*
Permuterm index would better be called a permuterm tree.
But permuterm index is the more common name.
```


### اسلاید 28

```text
Processing a lookup in the permuterm index
Rotate query wildcard to the right
Use B-tree lookup as before
Problem: Permuterm more than quadruples the size of the dictionary compared to a regular B-tree. (empirical number)
```


### اسلاید 29

```text
k-gram indexes
More space-efficient than permuterm index
Enumerate all character k-grams (sequence of k characters) occurring in a term
2-grams are called bigrams.
Example: from April is the cruelest month we get the bigrams: $a ap pr ri il l$ $i is s$ $t th he e$ $c cr ru ue el le es st t$ $m mo on nt h$
$ is a special word boundary symbol, as before.
Maintain an inverted index from bigrams to the terms that contain the bigram
```


### اسلاید 30

```text
Postings list in a 3-gram inverted index
```

![Postings list in a 3-gram inverted index — اسلاید 30][slide-030-1]


### اسلاید 31

```text
k-gram (bigram, trigram, . . . ) indexes
Note that we now have two different types of inverted indexes
The term-document inverted index for finding documents based on a query consisting of terms
The k-gram index for finding terms based on a query consisting of k-grams
```


### اسلاید 32

```text
Processing wildcarded terms in a bigram index
Query mon* can now be run as: $m AND mo AND on
Gets us all terms with the prefix mon . . .
. . . but also many “false positives” like MOON.
We must postfilter these terms against query.
Surviving terms are then looked up in the term-document inverted index.
k-gram index vs. permuterm index
k-gram index is more space efficient.
Permuterm index doesn’t require postfiltering.
```


### اسلاید 33

```text
Exercise
Google has very limited support for wildcard queries.
For example, this query doesn’t work very well on Google: [gen* universit*]
Intention: you are looking for the University of Geneva, but don’t know which accents to use for the French words for university and Geneva.
According to Google search basics, 2010-04-29: “Note that the * operator works only on whole words, not parts of words.”
But this is not entirely true. Try [pythag*] and [m*nchen]
Exercise: Why doesn’t Google fully support wildcard queries?
```


### اسلاید 34

```text
Processing wildcard queries in the term-document index
Problem 1: we must potentially execute a large number of Boolean queries.
Most straightforward semantics: Conjunction of disjunctions
For [gen* universit*]: geneva university OR geneva université OR genève university OR genève université OR general universities OR . . .
Very expensive
Problem 2: Users hate to type.
If abbreviated queries like [pyth* theo*] for [pythagoras’ theorem] are allowed, users will use them a lot.
This would significantly increase the cost of answering queries.
Somewhat alleviated by Google Suggest
```


### اسلاید 35

```text
Outline
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 36

```text
Spelling correction
Two principal uses
Correcting documents being indexed
Correcting user queries
Two different methods for spelling correction
Isolated word spelling correction
Check each word on its own for misspelling
Will not catch typos resulting in correctly spelled words, e.g., an asteroid that fell form the sky
Context-sensitive spelling correction
Look at surrounding words
Can correct form/from error above
```


### اسلاید 37

```text
Correcting documents
We’re not interested in interactive spelling correction of documents (e.g., MS Word) in this class.
In IR, we use document correction primarily for OCR’ed documents. (OCR = optical character recognition)
The general philosophy in IR is: don’t change the documents.
```


### اسلاید 38

```text
Correcting queries
First: isolated word spelling correction
Premise 1: There is a list of “correct words” from which the correct spellings come.
Premise 2: We have a way of computing the distance between a misspelled word and a correct word.
Simple spelling correction algorithm: return the “correct” word that has the smallest distance to the misspelled word.
Example: informaton → information
For the list of correct words, we can use the vocabulary of all words that occur in our collection.
Why is this problematic?
```


### اسلاید 39

```text
Alternatives to using the term vocabulary
A standard dictionary (Webster’s, OED etc.)
An industry-specific dictionary (for specialized IR systems)
The term vocabulary of the collection, appropriately weighted
```


### اسلاید 40

```text
Distance between misspelled word and “correct” word
We will study several alternatives.
Edit distance and Levenshtein distance
Weighted edit distance
k-gram overlap
```


### اسلاید 41

```text
Edit distance
The edit distance between string s1 and string s2 is the minimum number of basic operations that convert s1 to s2.
Levenshtein distance: The admissible basic operations are insert, delete, and replace
Levenshtein distance dog-do: 1
Levenshtein distance cat-cart: 1
Levenshtein distance cat-cut: 1
Levenshtein distance cat-act: 2
Damerau-Levenshtein distance cat-act: 1
Damerau-Levenshtein includes transposition as a fourth possible operation.
```


### اسلاید 42

```text
Levenshtein distance: Computation
```

![Levenshtein distance: Computation — اسلاید 42][slide-042-1]


### اسلاید 43

```text
Levenshtein distance: Algorithm
```

![Levenshtein distance: Algorithm — اسلاید 43][slide-043-1]


### اسلاید 44

```text
Levenshtein distance: Algorithm
```

![Levenshtein distance: Algorithm — اسلاید 44][slide-044-1]


### اسلاید 45

```text
Levenshtein distance: Algorithm
```

![Levenshtein distance: Algorithm — اسلاید 45][slide-045-1]


### اسلاید 46

```text
Levenshtein distance: Algorithm
```

![Levenshtein distance: Algorithm — اسلاید 46][slide-046-1]


### اسلاید 47

```text
Levenshtein distance: Algorithm
```

![Levenshtein distance: Algorithm — اسلاید 47][slide-047-1]


### اسلاید 48

```text
Levenshtein distance: Example
```

![Levenshtein distance: Example — اسلاید 48][slide-048-1]


### اسلاید 49

```text
Each cell of Levenshtein matrix
cost of getting here from
my upper left neighbor
(copy or replace) | cost of getting here
from my upper neighbor
(delete)
cost of getting here from
my left neighbor (insert) | the minimum of the three possible “movements”;
the cheapest way of getting here
```


### اسلاید 50

```text
Levenshtein distance: Example
```

![Levenshtein distance: Example — اسلاید 50][slide-050-1]


### اسلاید 51

```text
Dynamic programming (Cormen et al.)
Optimal substructure: The optimal solution to the problem contains within it subsolutions, i.e., optimal solutions to subproblems.
Overlapping subsolutions: The subsolutions overlap. These subsolutions are computed over and over again when computing the global optimal solution in a brute-force algorithm.
Subproblem in the case of edit distance: what is the edit distance of two prefixes
Overlapping subsolutions: We need most distances of prefixes 3 times – this corresponds to moving right, diagonally, down.
```


### اسلاید 52

```text
Weighted edit distance
As above, but weight of an operation depends on the characters involved.
Meant to capture keyboard errors, e.g., m more likely to be mistyped as n than as q.
Therefore, replacing m by n is a smaller edit distance than by q.
We now require a weight matrix as input.
Modify dynamic programming to handle weights
```


### اسلاید 53

```text
Using edit distance for spelling correction
Given query, first enumerate all character sequences within a preset (possibly weighted) edit distance
Intersect this set with our list of “correct” words
Then suggest terms in the intersection to the user.
→ exercise in a few slides
```


### اسلاید 54

```text
Exercise
Compute Levenshtein distance matrix for OSLO – SNOW
What are the Levenshtein editing operations that transform cat into catcat?
```


### اسلاید 55

![ماتریس فاصلهٔ ویرایشی — اسلاید 55][slide-055-1]


### اسلاید 56

![ماتریس فاصلهٔ ویرایشی — اسلاید 56][slide-056-1]


### اسلاید 57

![ماتریس فاصلهٔ ویرایشی — اسلاید 57][slide-057-1]


### اسلاید 58

![ماتریس فاصلهٔ ویرایشی — اسلاید 58][slide-058-1]


### اسلاید 59

![ماتریس فاصلهٔ ویرایشی — اسلاید 59][slide-059-1]


### اسلاید 60

![ماتریس فاصلهٔ ویرایشی — اسلاید 60][slide-060-1]


### اسلاید 61

![ماتریس فاصلهٔ ویرایشی — اسلاید 61][slide-061-1]


### اسلاید 62

![ماتریس فاصلهٔ ویرایشی — اسلاید 62][slide-062-1]


### اسلاید 63

![ماتریس فاصلهٔ ویرایشی — اسلاید 63][slide-063-1]


### اسلاید 64

![ماتریس فاصلهٔ ویرایشی — اسلاید 64][slide-064-1]


### اسلاید 65

![ماتریس فاصلهٔ ویرایشی — اسلاید 65][slide-065-1]


### اسلاید 66

![ماتریس فاصلهٔ ویرایشی — اسلاید 66][slide-066-1]


### اسلاید 67

![ماتریس فاصلهٔ ویرایشی — اسلاید 67][slide-067-1]


### اسلاید 68

![ماتریس فاصلهٔ ویرایشی — اسلاید 68][slide-068-1]


### اسلاید 69

![ماتریس فاصلهٔ ویرایشی — اسلاید 69][slide-069-1]


### اسلاید 70

![ماتریس فاصلهٔ ویرایشی — اسلاید 70][slide-070-1]


### اسلاید 71

![ماتریس فاصلهٔ ویرایشی — اسلاید 71][slide-071-1]


### اسلاید 72

![ماتریس فاصلهٔ ویرایشی — اسلاید 72][slide-072-1]


### اسلاید 73

![ماتریس فاصلهٔ ویرایشی — اسلاید 73][slide-073-1]


### اسلاید 74

![ماتریس فاصلهٔ ویرایشی — اسلاید 74][slide-074-1]


### اسلاید 75

![ماتریس فاصلهٔ ویرایشی — اسلاید 75][slide-075-1]


### اسلاید 76

![ماتریس فاصلهٔ ویرایشی — اسلاید 76][slide-076-1]


### اسلاید 77

![ماتریس فاصلهٔ ویرایشی — اسلاید 77][slide-077-1]


### اسلاید 78

![ماتریس فاصلهٔ ویرایشی — اسلاید 78][slide-078-1]


### اسلاید 79

![ماتریس فاصلهٔ ویرایشی — اسلاید 79][slide-079-1]


### اسلاید 80

![ماتریس فاصلهٔ ویرایشی — اسلاید 80][slide-080-1]


### اسلاید 81

![ماتریس فاصلهٔ ویرایشی — اسلاید 81][slide-081-1]


### اسلاید 82

![ماتریس فاصلهٔ ویرایشی — اسلاید 82][slide-082-1]


### اسلاید 83

![ماتریس فاصلهٔ ویرایشی — اسلاید 83][slide-083-1]


### اسلاید 84

![ماتریس فاصلهٔ ویرایشی — اسلاید 84][slide-084-1]


### اسلاید 85

![ماتریس فاصلهٔ ویرایشی — اسلاید 85][slide-085-1]


### اسلاید 86

![ماتریس فاصلهٔ ویرایشی — اسلاید 86][slide-086-1]


### اسلاید 87

![ماتریس فاصلهٔ ویرایشی — اسلاید 87][slide-087-1]


### اسلاید 88

![ماتریس فاصلهٔ ویرایشی — اسلاید 88][slide-088-1]


### اسلاید 89

```text
How do I read out the editing operations that transform OSLO into SNOW?
```

![ماتریس فاصلهٔ ویرایشی — اسلاید 89][slide-089-1]


### اسلاید 90

![ماتریس فاصلهٔ ویرایشی — اسلاید 90][slide-090-1]

![جدول عملیات — اسلاید 90][slide-090-2]


### اسلاید 91

![ماتریس فاصلهٔ ویرایشی — اسلاید 91][slide-091-1]

![جدول عملیات — اسلاید 91][slide-091-2]


### اسلاید 92

![ماتریس فاصلهٔ ویرایشی — اسلاید 92][slide-092-1]

![جدول عملیات — اسلاید 92][slide-092-2]


### اسلاید 93

![ماتریس فاصلهٔ ویرایشی — اسلاید 93][slide-093-1]

![جدول عملیات — اسلاید 93][slide-093-2]


### اسلاید 94

![ماتریس فاصلهٔ ویرایشی — اسلاید 94][slide-094-1]

![جدول عملیات — اسلاید 94][slide-094-2]


### اسلاید 95

![ماتریس فاصلهٔ ویرایشی — اسلاید 95][slide-095-1]


### اسلاید 96

![ماتریس فاصلهٔ ویرایشی — اسلاید 96][slide-096-1]

![جدول عملیات — اسلاید 96][slide-096-2]


### اسلاید 97

![ماتریس فاصلهٔ ویرایشی — اسلاید 97][slide-097-1]

![جدول عملیات — اسلاید 97][slide-097-2]


### اسلاید 98

![ماتریس فاصلهٔ ویرایشی — اسلاید 98][slide-098-1]

![جدول عملیات — اسلاید 98][slide-098-2]


### اسلاید 99

![ماتریس فاصلهٔ ویرایشی — اسلاید 99][slide-099-1]

![جدول عملیات — اسلاید 99][slide-099-2]


### اسلاید 100

```text
Outline
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 101

```text
Spelling correction
Now that we can compute edit distance: how to use it for isolated word spelling correction – this is the last slide in this section.
k-gram indexes for isolated word spelling correction.
Context-sensitive spelling correction
General issues
```


### اسلاید 102

```text
k-gram indexes for spelling correction
Enumerate all k-grams in the query term
Example: bigram index, misspelled word bordroom
Bigrams: bo, or, rd, dr, ro, oo, om
Use the k-gram index to retrieve “correct” words that match query term k-grams
Threshold by number of matching k-grams
E.g., only vocabulary terms that differ by at most 3 k-grams
```


### اسلاید 103

```text
k-gram indexes for spelling correction: bordroom
```

![k-gram indexes for spelling correction: bordroom — اسلاید 103][slide-103-1]


### اسلاید 104

```text
Context-sensitive spelling correction
Our example was: an asteroid that fell form the sky
How can we correct form here?
One idea: hit-based spelling correction
Retrieve “correct” terms close to each query term
for flew form munich: flea for flew, from for form, munch for
munich
Now try all possible resulting phrases as queries with one word “fixed” at a time
Try query “flea form munich”
Try query “flew from munich”
Try query “flew form munch”
The correct query “flew from munich” has the most hits.
Suppose we have 7 alternatives for flew, 20 for form and 3 for munich, how many “corrected” phrases will we enumerate?
```


### اسلاید 105

```text
Context-sensitive spelling correction
The “hit-based” algorithm we just outlined is not very efficient.
More efficient alternative: look at “collection” of queries, not documents
```


### اسلاید 106

```text
General issues in spelling correction
User interface
automatic vs. suggested correction
Did you mean only works for one suggestion.
What about multiple possible corrections?
Tradeoff: simple vs. powerful UI
Cost
Spelling correction is potentially expensive.
Avoid running on every query?
Maybe just on queries that match few documents.
Guess: Spelling correction of major search engines is efficient enough to be run on every query.
```


### اسلاید 107

```text
Exercise: Understand Peter Norvig’s 
spelling corrector
```

![Exercise: Understand Peter Norvig’s 
spelling corrector — اسلاید 107][slide-107-1]


### اسلاید 108

```text
Outline
Recap 
 Dictionaries
 Wildcard queries
 Edit distance
Spelling correction
Soundex
```


### اسلاید 109

```text
Soundex
Soundex is the basis for finding phonetic (as opposed to orthographic) alternatives.
Example: chebyshev / tchebyscheff
Algorithm:
Turn every token to be indexed into a 4-character reduced form
Do the same with query terms
Build and search an index on the reduced forms
```


### اسلاید 110

```text
Soundex algorithm
Retain the first letter of the term.
Change all occurrences of the following letters to ’0’ (zero): A, E, I, O, U, H, W, Y
Change letters to digits as follows:
B, F, P, V to 1
C, G, J, K, Q, S, X, Z to 2
D,T to 3
L to 4
M, N to 5
R to 6
Repeatedly remove one out of each pair of consecutive identical digits
Remove all zeros from the resulting string; pad the resulting string
     with trailing zeros and return the first four positions, which will
     consist of a letter followed by three digits
```


### اسلاید 111

```text
Example: Soundex of HERMAN
Retain H
ERMAN → 0RM0N
0RM0N → 06505
06505 → 06505
06505 → 655
Return H655
Note: HERMANN will generate the same code
```


### اسلاید 112

```text
How useful is Soundex?
Not very – for information retrieval
Ok for “high recall” tasks in other applications (e.g., Interpol)
Zobel and Dart (1996) suggest better alternatives for phonetic matching in IR.
```


### اسلاید 113

```text
Exercise
Compute Soundex code of your last name
```


### اسلاید 114

```text
Take-away
Tolerant retrieval: What to do if there is no exact match between query term and document term
Wildcard queries
Spelling correction
```


### اسلاید 115

```text
Resources
Chapter 3 of IIR
Resources at http://ifnlp.org/ir
Soundex demo
Levenshtein distance demo
Peter Norvig’s spelling corrector
```

[slide-007-1]: assets/slide-007-1.png
[slide-012-1]: assets/slide-012-1.png
[slide-013-1]: assets/slide-013-1.png
[slide-016-1]: assets/slide-016-1.png
[slide-020-1]: assets/slide-020-1.png
[slide-021-1]: assets/slide-021-1.png
[slide-026-1]: assets/slide-026-1.png
[slide-030-1]: assets/slide-030-1.png
[slide-042-1]: assets/slide-042-1.png
[slide-043-1]: assets/slide-043-1.png
[slide-044-1]: assets/slide-044-1.png
[slide-045-1]: assets/slide-045-1.png
[slide-046-1]: assets/slide-046-1.png
[slide-047-1]: assets/slide-047-1.png
[slide-048-1]: assets/slide-048-1.png
[slide-050-1]: assets/slide-050-1.png
[slide-055-1]: assets/slide-055-1.png
[slide-056-1]: assets/slide-056-1.png
[slide-057-1]: assets/slide-057-1.png
[slide-058-1]: assets/slide-058-1.png
[slide-059-1]: assets/slide-059-1.png
[slide-060-1]: assets/slide-060-1.png
[slide-061-1]: assets/slide-061-1.png
[slide-062-1]: assets/slide-062-1.png
[slide-063-1]: assets/slide-063-1.png
[slide-064-1]: assets/slide-064-1.png
[slide-065-1]: assets/slide-065-1.png
[slide-066-1]: assets/slide-066-1.png
[slide-067-1]: assets/slide-067-1.png
[slide-068-1]: assets/slide-068-1.png
[slide-069-1]: assets/slide-069-1.png
[slide-070-1]: assets/slide-070-1.png
[slide-071-1]: assets/slide-071-1.png
[slide-072-1]: assets/slide-072-1.png
[slide-073-1]: assets/slide-073-1.png
[slide-074-1]: assets/slide-074-1.png
[slide-075-1]: assets/slide-075-1.png
[slide-076-1]: assets/slide-076-1.png
[slide-077-1]: assets/slide-077-1.png
[slide-078-1]: assets/slide-078-1.png
[slide-079-1]: assets/slide-079-1.png
[slide-080-1]: assets/slide-080-1.png
[slide-081-1]: assets/slide-081-1.png
[slide-082-1]: assets/slide-082-1.png
[slide-083-1]: assets/slide-083-1.png
[slide-084-1]: assets/slide-084-1.png
[slide-085-1]: assets/slide-085-1.png
[slide-086-1]: assets/slide-086-1.png
[slide-087-1]: assets/slide-087-1.png
[slide-088-1]: assets/slide-088-1.png
[slide-089-1]: assets/slide-089-1.png
[slide-090-1]: assets/slide-090-1.png
[slide-090-2]: assets/slide-090-2.png
[slide-091-1]: assets/slide-091-1.png
[slide-091-2]: assets/slide-091-2.png
[slide-092-1]: assets/slide-092-1.png
[slide-092-2]: assets/slide-092-2.png
[slide-093-1]: assets/slide-093-1.png
[slide-093-2]: assets/slide-093-2.png
[slide-094-1]: assets/slide-094-1.png
[slide-094-2]: assets/slide-094-2.png
[slide-095-1]: assets/slide-095-1.png
[slide-096-1]: assets/slide-096-1.png
[slide-096-2]: assets/slide-096-2.png
[slide-097-1]: assets/slide-097-1.png
[slide-097-2]: assets/slide-097-2.png
[slide-098-1]: assets/slide-098-1.png
[slide-098-2]: assets/slide-098-2.png
[slide-099-1]: assets/slide-099-1.png
[slide-099-2]: assets/slide-099-2.png
[slide-103-1]: assets/slide-103-1.png
[slide-107-1]: assets/slide-107-1.png
