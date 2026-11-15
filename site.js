const search = document.querySelector('#search');
const list = document.querySelector('#chapter-list');
const clear = document.querySelector('#clear-search');
let filter = 'all';
const fa = n => n.toLocaleString('fa-IR');
const normalize = value => value.toLowerCase().replace(/[يى]/g,'ی').replace(/ك/g,'ک').replace(/[\u064B-\u065F\u0670\u0640]/g,'').replace(/[\s\u200c]+/g,' ').trim();
const escapeHTML = value => value.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const descriptions = ['مفاهیم پایه، ایندکس معکوس و پردازش پرس‌وجوهای بولی', 'توکن‌سازی، نرمال‌سازی، کلمات توقف و ریشه‌یابی', 'ساختار واژه، معیار m، قواعد پورتر و ردگیری مرحله‌ای', 'اشتراک فهرست‌ها، شرط پرش و محدودیت‌های آن', 'Biword، ایندکس موقعیتی و مثال‌های جست‌وجوی عبارتی', 'ساختارهای دیکشنری، TF، DF و CF', 'Wildcard، Permuterm، k-gram و فیلتر نامزدها'];
const filters = document.querySelector('.filters');
filters.innerHTML = '<button class="selected" data-filter="all" aria-pressed="true">همهٔ فصل‌ها</button>' + window.chapters.map(ch => `<button data-filter="${ch.id}" aria-pressed="false">فصل ${fa(ch.id)}</button>`).join('');
document.querySelector('#chapter-count').textContent = fa(window.chapters.length).padStart(2,'۰');
document.querySelector('#topic-count').textContent = fa(window.chapters.reduce((sum,ch) => sum + ch.topics.length, 0));
function render() {
  const query = normalize(search.value);
  const words = query.split(' ').filter(Boolean);
  let count = 0;
  list.innerHTML = window.chapters.filter(ch => filter === 'all' || String(ch.id) === filter).map(ch => {
    const topics = ch.topics.filter(t => words.every(w => normalize(t.title + ' ' + t.text + ' ' + ch.title).includes(w)));
    count += topics.length;
    if (!topics.length) return '';
    const url = encodeURI(ch.url);
    const description = descriptions[ch.id - 1];
    const done = window.studyProgress?.has(ch.id) ? '<span class="done-badge">✓ مطالعه‌شده</span>' : '';
    return `<article class="chapter"><div class="chapter-top"><div class="chapter-label"><span class="chapter-number">${fa(ch.id).padStart(2,'۰')}</span><span>فصل ${fa(ch.id)} · ${fa(ch.topics.length)} موضوع ${done}</span></div><h3>${escapeHTML(ch.title)}</h3><p class="chapter-description">${description}</p><a class="start-link" href="${url}#slide-1">شروع مطالعهٔ فصل ${fa(ch.id)}<span aria-hidden="true">←</span></a></div><details ${query ? 'open' : ''}><summary>${query ? `${fa(topics.length)} موضوع مرتبط` : 'مشاهدهٔ موضوعات فصل'}</summary><ol class="topic-list">${topics.map(t => `<li><a class="topic-link" href="${url}#slide-${t.slide}"><span class="topic-index">${fa(t.slide).padStart(2,'۰')}</span><span>${escapeHTML(t.title)}</span><span class="topic-arrow" aria-hidden="true">←</span></a></li>`).join('')}</ol></details></article>`;
  }).join('');
  document.querySelector('#empty').hidden = count !== 0;
  document.querySelector('#result-status').textContent = query ? `${fa(count)} موضوع برای «${search.value.trim()}»` : `${fa(count)} موضوع برای مطالعه`;
  clear.hidden = !search.value;
  window.studyProgress?.decorateLinks();
}
search.addEventListener('input', render);
clear.addEventListener('click', () => { search.value = ''; render(); search.focus(); });
document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
  filter = button.dataset.filter;
  document.querySelectorAll('[data-filter]').forEach(b => { b.classList.toggle('selected', b === button); b.setAttribute('aria-pressed', String(b === button)); });
  render();
}));
window.addEventListener('study-progress', render);
render();
