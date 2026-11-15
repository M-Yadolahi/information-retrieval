(() => {
  const root = document.querySelector('#porter-demo');
  if (!root) return;
  // Curated traces of the original (1980) Porter algorithm, not Porter2.
  const examples = [
    ['digitizer', 'digitizer', 'digitize', 'digitize', 'digit', 'digit',
      'پسوند izer به ize تبدیل می‌شود؛ ساقهٔ digit دارای m=2 است و شرط m>0 برقرار است.',
      'هیچ پسوندی از مرحلهٔ 3 منطبق نیست؛ ize در این مرحله حذف نمی‌شود.',
      'پسوند ize حذف می‌شود؛ ساقهٔ digit دارای m=2 است و شرط m>1 برقرار است.',
      'نه e پایانی داریم و نه ll؛ خروجی نهایی digit است.'],
    ['interpretation', 'interpretation', 'interpretate', 'interpretate', 'interpret', 'interpret',
      'پسوند ation به ate تبدیل می‌شود؛ ساقهٔ interpret دارای m=3 است و شرط m>0 برقرار است.',
      'پسوندی از مرحلهٔ 3 منطبق نیست؛ ate در این مرحله حذف نمی‌شود.',
      'پسوند ate حذف می‌شود؛ ساقهٔ interpret دارای m=3 است و شرط m>1 برقرار است.',
      'نه e پایانی داریم و نه ll؛ خروجی نهایی interpret است.'],
    ['lemmatization', 'lemmatization', 'lemmatize', 'lemmatize', 'lemmat', 'lemmat',
      'پسوند ization به ize تبدیل می‌شود؛ ساقهٔ lemmat دارای m=2 است و شرط m>0 برقرار است.',
      'هیچ پسوندی از مرحلهٔ 3 منطبق نیست؛ ize در این مرحله حذف نمی‌شود.',
      'پسوند ize حذف می‌شود؛ ساقهٔ lemmat دارای m=2 است و شرط m>1 برقرار است.',
      'نه e پایانی داریم و نه ll؛ خروجی نهایی lemmat است.'],
    ['translators', 'translator', 'translate', 'translate', 'translate', 'translat',
      'پسوند ator به ate تبدیل می‌شود؛ ساقهٔ transl دارای m=1 است و شرط m>0 برقرار است.',
      'پسوندی از مرحلهٔ 3 منطبق نیست.',
      'پسوند ate منطبق است، اما ساقهٔ transl دارای m=1 است؛ شرط m>1 برقرار نیست و ate باقی می‌ماند.',
      'ساقهٔ پیش از e یعنی translat دارای m=2 است؛ در مرحلهٔ 5a حرف e حذف می‌شود. قاعدهٔ 5b تغییری نمی‌دهد؛ خروجی translat است.'],
    ['generalizations', 'generalization', 'generalize', 'general', 'gener', 'gener',
      'پسوند ization به ize تبدیل می‌شود؛ ساقهٔ general دارای m=3 است و شرط m>0 برقرار است.',
      'پسوند alize به al تبدیل می‌شود؛ ساقهٔ gener دارای m=2 است و شرط m>0 برقرار است. قاعدهٔ این مرحله alize است؛ خودِ ize در مرحلهٔ 3 قاعدهٔ حذف ندارد.',
      'پسوند al حذف می‌شود؛ ساقهٔ gener دارای m=2 است و شرط m>1 برقرار است.',
      'نه e پایانی داریم و نه ll؛ خروجی نهایی gener است.']
  ];
  const traces = Object.fromEntries(examples.map(([input, a, b, c, d, e, bNote, cNote, dNote, eNote]) => [input, [
    ['شروع', input, 'واژهٔ ورودی؛ خروجی‌های میانی لزوماً ریشهٔ نهایی یا واژهٔ فرهنگ لغت نیستند.'],
    ['1a', a, input === a ? 'هیچ‌یک از قواعد مرحلهٔ 1a منطبق نیست؛ واژه بدون تغییر می‌ماند.' : 'حرف s پایانی طبق قاعدهٔ مرحلهٔ 1a حذف می‌شود.'],
    ['1b', a, 'پسوندهای eed، ed یا ing وجود ندارند؛ حذف و پاک‌سازی این مرحله اجرا نمی‌شود.'],
    ['1c', a, 'واژه به y ختم نمی‌شود؛ تغییری نداریم.'],
    ['2', b, bNote], ['3', c, cNote], ['4', d, dNote], ['5', e, eNote]
  ]]));
  const select = root.querySelector('select');
  // Build choices here so updating this file alone also updates existing HTML.
  select.replaceChildren(...Object.keys(traces).map(value => {
    const option = document.createElement('option');
    option.value = option.textContent = value;
    return option;
  }));
  const stage = root.querySelector('.porter-stage');
  const word = root.querySelector('.porter-word');
  const explanation = root.querySelector('.porter-explanation');
  const counter = root.querySelector('.porter-counter');
  const trail = root.querySelector('.porter-trail');
  const prev = root.querySelector('[data-porter="prev"]');
  const next = root.querySelector('[data-porter="next"]');
  let index = 0;
  function render() {
    const steps = traces[select.value];
    const [label, current, text] = steps[index];
    const before = index ? steps[index - 1][1] : current;
    let shared = 0;
    while (shared < Math.min(before.length, current.length) && before[shared] === current[shared]) shared++;
    word.replaceChildren();
    const span = document.createElement('span');
    span.textContent = before;
    if (before !== current) {
      span.textContent = before.slice(0, shared);
      const removed = document.createElement('del'); removed.textContent = before.slice(shared); span.append(removed);
    }
    word.append(span);
    if (before !== current) {
      word.append(document.createTextNode(' → '));
      const result = document.createElement('span'); result.textContent = current.slice(0, shared);
      const added = document.createElement('mark'); added.textContent = current.slice(shared); result.append(added); word.append(result);
    }
    stage.textContent = label === 'شروع' ? label : `مرحلهٔ ${label}`;
    explanation.textContent = text;
    counter.textContent = `${(index + 1).toLocaleString('fa-IR')} از ${steps.length.toLocaleString('fa-IR')} · ${index === steps.length - 1 ? 'پایان اجرا' : 'در حال بررسی'}`;
    trail.textContent = steps.slice(0, index + 1).map(s => s[1]).filter((w, i, a) => i === 0 || w !== a[i - 1]).join(' → ');
    prev.disabled = index === 0; next.disabled = index === steps.length - 1;
    root.querySelector('progress').value = index;
    root.querySelector('progress').max = steps.length - 1;
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches && word.animate) word.animate([{opacity: .25, transform: 'translateY(8px)'}, {opacity: 1, transform: 'translateY(0)'}], {duration: 260});
  }
  select.addEventListener('change', () => { index = 0; render(); });
  prev.addEventListener('click', () => { if (index > 0) index--; render(); });
  next.addEventListener('click', () => { if (index < traces[select.value].length - 1) index++; render(); });
  root.querySelector('[data-porter="reset"]').addEventListener('click', () => { index = 0; render(); });
  root.querySelector('.porter-controls').hidden = false;
  render();
})();
