(() => {
  const slides = [...document.querySelectorAll('.slide')];
  let current = 0;
  const fa = n => n.toLocaleString('fa-IR');
  function update() {
    slides.forEach((slide, i) => { slide.classList.toggle('active', i === current); slide.setAttribute('aria-hidden', String(i !== current)); if (i === current) slide.scrollTop = 0; });
    ['slideCounter','progressText'].forEach(id => { const el = document.getElementById(id); if(el) {el.textContent = `اسلاید ${fa(current+1)} از ${fa(slides.length)}`;el.setAttribute('aria-live','polite');} });
    const bar = document.getElementById('progressBar');
    if(bar) bar.style.width = `${(current+1)/slides.length*100}%`;
    document.getElementById('prevBtn').disabled = current === 0;
    document.getElementById('nextBtn').disabled = current === slides.length-1;
  }
  function fromHash() { const match = location.hash.match(/^#slide-(\d+)$/); current = match ? Math.max(0,Math.min(slides.length-1, Number(match[1])-1)) : 0; update(); }
  window.changeSlide = direction => { const next = Math.max(0,Math.min(slides.length-1,current+direction)); if(next !== current) location.hash = `slide-${next+1}`; };
  window.toggleFullScreen = () => { if(document.fullscreenElement) document.exitFullscreen?.().catch(()=>{}); else document.documentElement.requestFullscreen?.().catch(()=>{}); };
  const full = document.querySelector('.fs-btn'); if(full) full.setAttribute('aria-label','نمایش تمام‌صفحه');
  document.addEventListener('keydown', e => {
    if(e.target.closest('input,textarea,select,button,a,[contenteditable]') || e.altKey || e.ctrlKey || e.metaKey) return;
    if(['ArrowLeft','PageDown','ArrowRight','PageUp',' '].includes(e.key)) {e.preventDefault();window.changeSlide(['ArrowRight','PageUp'].includes(e.key)?-1:1);}
  });
  const container = document.querySelector('#slideContainer, #presentation-container');
  let touch = null;
  container.addEventListener('touchstart', e => { const t=e.touches[0];touch=e.touches.length === 1 && !e.target.closest('a,button,.table-responsive,.code-block,pre') ? {x:t.clientX,y:t.clientY}:null; },{passive:true});
  container.addEventListener('touchend', e => { if(!touch)return;const t=e.changedTouches[0],dx=t.clientX-touch.x,dy=t.clientY-touch.y;touch=null;if(Math.abs(dx)>65 && Math.abs(dx)>Math.abs(dy)*1.8) window.changeSlide(dx<0?1:-1); },{passive:true});
  container.addEventListener('touchcancel',()=>{touch=null;},{passive:true});
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
