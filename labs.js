// Each frame keeps the data visible and marks the entries being compared.
const lessons = {
  1: ['ساخت ایندکس معکوس', [
    ['متن دو سند','D1: red blue red\nD2: blue','هر رخداد باید به سند خودش متصل بماند.'],
    ['زوج‌های اولیه','red:1   blue:1   red:1   blue:2','دو بار آمدن red در سند اول، دو زوج یکسان می‌سازد.'],
    ['پس از مرتب‌سازی','[blue:1]   [blue:2]   red:1   red:1','ابتدا واژه و سپس شناسهٔ سند را مرتب کردیم؛ حالا رخدادهای هر واژه کنار هم‌اند.'],
    ['فهرست‌های نهایی','blue → [1, 2]\nred  → [1]','در ایندکس بولی، شناسهٔ تکراری حذف می‌شود. پس df واژهٔ red یک است، نه دو.']]],
  4: ['چه وقت پرش مجاز است؟', [
    ['آغاز مقایسه','A: [4]  11  31  45\nB: [11]  31','در فهرست A یک اشاره‌گر از ۴ به ۳۱ داریم. آیا می‌توان از آن استفاده کرد؟'],
    ['رد پرش','A: 4  [11]  31  45\nB: [11]  31','نه؛ ۳۱ از ۱۱ بزرگ‌تر است. فقط یک خانه جلو می‌رویم و به پاسخ ۱۱ می‌رسیم.'],
    ['پس از ثبت ۱۱','A: 4  11  [31]  45\nB: 11  [31]','هر دو نشانگر جلو آمده‌اند؛ ۳۱ هم مشترک است.'],
    ['اگر B از ۳۱ شروع می‌شد','A: [4] ─────→ [31]  45\nB: [31]','این بار مقصد پرش برابر مقدار مقابل است؛ رد کردن ۱۱ هیچ پاسخ مشترکی را حذف نمی‌کند.']]],
  5: ['آیا عبارت data mining پیدا شد؟', [
    ['نامزدهای سند','data:   D1, D2\nmining: D1, D2','هر دو سند هر دو واژه را دارند. آیا هر دو شامل عبارت دقیق‌اند؟'],
    ['موقعیت‌ها در سند اول','data:   [1]  7\nmining: [2]  9','۲ دقیقاً یک واحد بعد از ۱ است. پس یک رخداد عبارت از موقعیت ۱ آغاز می‌شود.'],
    ['رخداد بعدی در همان سند','data:   1  [7]\nmining: 2  [9]','بعد از ۷ دنبال ۸ هستیم، نه ۹. رخداد دوم عبارت ساخته نمی‌شود.'],
    ['آزمون سند دوم','data:   [2]\nmining: [5]','۵ دقیقاً پس از ۲ نیست. پاسخ عبارت فقط سند اول است؛ پاسخ AND هر دو سند بود.']]]
};
for (const host of document.querySelectorAll('[data-ir-lab]')) {
  const [title, frames] = lessons[host.dataset.irLab]; let i = 0;
  host.innerHTML = '<h2></h2><div aria-live="polite" aria-atomic="true"><strong></strong><pre dir="ltr"></pre><p></p></div><button type="button">گام قبل</button> <button type="button">گام بعد</button>';
  host.querySelector('h2').textContent = title;
  const [prev,next] = host.querySelectorAll('button');
  function render() {
    const [label,code,note] = frames[i]; const pre = host.querySelector('pre');
    host.querySelector('strong').textContent = `گام ${(i+1).toLocaleString('fa')} از ${frames.length.toLocaleString('fa')} · ${label}`;
    pre.textContent = code; host.querySelector('p').textContent = note;
    if(pre.animate && !matchMedia('(prefers-reduced-motion: reduce)').matches) pre.animate([{opacity:.35, transform:'translateY(5px)'},{opacity:1, transform:'none'}],{duration:250});
    prev.disabled = i===0; next.disabled = i===frames.length-1;
  }
  prev.onclick = () => {if(i>0){i--;render();}}; next.onclick = () => {if(i<frames.length-1){i++;render();}}; render();
}
