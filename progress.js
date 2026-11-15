// Local storage on hosted sites; timestamped navigation hand-off for file:// pages.
(() => {
  const key = 'ir-study-completed-v1';
  const fileMode = location.protocol === 'file:';
  const scope = new URL('.', location.href).href;
  const namePrefix = 'ir-study:';
  let state = {done: [], time: 0};
  let saved = true;
  function clean(value) {
    if (Array.isArray(value)) value = {done: value, time: 0}; // migrate v1
    if (!value || !Array.isArray(value.done) || !Number.isFinite(value.time)) return null;
    return {done: [...new Set(value.done.filter(n => Number.isInteger(n) && n >= 1 && n <= 7))], time: value.time};
  }
  function consider(value) {
    const candidate = clean(value);
    if (candidate && candidate.time >= state.time) state = candidate;
  }
  function load() {
    try { consider(JSON.parse(localStorage.getItem(key))); } catch { saved = false; }
    if (fileMode) {
      try {
        const handoff = JSON.parse(window.name.startsWith(namePrefix) ? window.name.slice(namePrefix.length) : 'null');
        if (handoff?.scope === scope) consider(handoff.state);
      } catch { /* unrelated window name */ }
      try { consider(JSON.parse(new URL(location.href).searchParams.get('study'))); } catch { /* invalid link */ }
    }
  }
  function persist() {
    try { localStorage.setItem(key, JSON.stringify(state)); saved = true; } catch { saved = false; }
    if (fileMode) {
      window.name = namePrefix + JSON.stringify({scope, state});
      try {
        const url = new URL(location.href);
        url.searchParams.set('study', JSON.stringify(state));
        history.replaceState(history.state, '', url);
      } catch { /* some file viewers disable history */ }
    }
  }
  function decorateLinks() {
    if (!fileMode) return;
    document.querySelectorAll('a[href]').forEach(a => {
      const raw = a.getAttribute('href');
      if (!raw || raw.startsWith('#')) return;
      const url = new URL(raw, location.href);
      if (new URL('.', url).href !== scope || !url.pathname.endsWith('.html')) return;
      url.searchParams.set('study', JSON.stringify(state));
      a.href = url.href;
    });
  }
  window.studyProgress = {
    has: id => state.done.includes(Number(id)), count: () => state.done.length,
    available: () => saved, decorateLinks
  };
  function update() {
    document.querySelectorAll('[data-done]').forEach(box => { box.checked = state.done.includes(Number(box.dataset.done)); });
    document.querySelectorAll('[data-study-meter], #study-meter').forEach(meter => { meter.value = state.done.length; });
    document.querySelectorAll('[data-progress-label], #progress-label').forEach(label => {
      label.textContent = `${state.done.length.toLocaleString('fa-IR')} از ۷ فصل (${Math.round(state.done.length / 7 * 100).toLocaleString('fa-IR')}٪)`;
    });
    document.querySelectorAll('[data-progress-note], #progress-note').forEach(note => {
      note.textContent = !saved ? 'ذخیرهٔ دائمی در این مرورگر در دسترس نیست؛ برای نگهداری بهتر پیشرفت، سایت را روی میزبان محلی یا آنلاین باز کنید.' : fileMode ? 'در حالت فایل، برای حفظ پیشرفت از لینک‌های داخل جزوه و همان زبانه استفاده کنید. آدرس صفحه نیز پیشرفت را همراه دارد.' : 'پیشرفت در همین مرورگر ذخیره می‌شود؛ میان دستگاه‌ها همگام نیست.';
    });
    window.dispatchEvent(new Event('study-progress'));
    decorateLinks();
  }
  load(); persist();
  document.querySelectorAll('[data-done]').forEach(box => box.addEventListener('change', () => {
    const id = Number(box.dataset.done);
    state.done = state.done.filter(n => n !== id);
    if (box.checked) state.done.push(id);
    state.time = Math.max(Date.now(), state.time + 1);
    persist(); update();
  }));
  window.addEventListener('pageshow', () => { load(); persist(); update(); });
  window.addEventListener('storage', event => {
    if (event.key === key) { try { consider(JSON.parse(event.newValue)); } catch {} update(); }
  });
  update();
})();
