import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update root CSS for glassmorphism
content = re.sub(
    r'--surface: #111118;.*?--border2: rgba\(255, 255, 255, 0.12\);',
    '--surface: rgba(20, 20, 30, 0.5);\n      --surface2: rgba(30, 30, 45, 0.6);\n      --border: rgba(255, 255, 255, 0.1);\n      --border2: rgba(255, 255, 255, 0.18);',
    content,
    flags=re.DOTALL
)

# 2. Add glass CSS to cards
for card in ['.stat-card {', '.skill-card {', '.cert-card {', '.project-card {', '.edu-card {']:
    content = content.replace(card, card + '\n      backdrop-filter: blur(16px);\n      -webkit-backdrop-filter: blur(16px);')

# 3. Add ambient orb CSS
orb_css = """
    /* AMBIENT ORBS */
    .ambient-orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(120px);
      z-index: -1;
      opacity: 0.5;
      pointer-events: none;
      animation: floatOrb 10s infinite alternate ease-in-out;
    }
    .orb-1 { width: 400px; height: 400px; background: var(--accent); top: 10%; left: -100px; }
    .orb-2 { width: 350px; height: 350px; background: var(--accent3); top: 40%; right: -50px; }
    .orb-3 { width: 500px; height: 500px; background: rgba(124,110,245,0.4); bottom: 10%; left: 20%; }
    @keyframes floatOrb {
      0% { transform: translate(0, 0) scale(1); }
      100% { transform: translate(50px, 50px) scale(1.1); }
    }
"""
content = content.replace('/* NAV */', orb_css + '\n    /* NAV */')

# 4. Update Nav Links
nav_links_old = """    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#certifications">Certifications</a></li>
      <li><a href="#experience">Experience</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>"""
nav_links_new = """    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#services">Services</a></li>
      <li><a href="#skills">Skills</a></li>
      <li><a href="#experience">Experience</a></li>
      <li><a href="#projects">Projects</a></li>
      <li><a href="#testimonials">Testimonials</a></li>
      <li><a href="#blog">Blog</a></li>
      <li><a href="#contact">Contact</a></li>
    </ul>"""
content = content.replace(nav_links_old, nav_links_new)

# 5. Add ambient orbs to body
content = content.replace('<!-- MAIN CONTENT -->', '<!-- AMBIENT ORBS -->\n  <div class="ambient-orb orb-1"></div>\n  <div class="ambient-orb orb-2"></div>\n  <div class="ambient-orb orb-3"></div>\n\n  <!-- MAIN CONTENT -->')

# 6. Add Services Section
services_html = """
  <!-- SERVICES -->
  <section id="services">
    <div class="section-inner">
      <p class="section-label reveal">Services</p>
      <h2 class="section-title reveal">What I Do</h2>
      <p class="section-sub reveal">Delivering high-quality solutions across multiple disciplines.</p>

      <div class="projects-grid">
        <div class="project-card reveal">
          <div class="skill-icon" style="font-size:2rem; width:60px; height:60px;">🤖</div>
          <h3 class="project-title">QA Automation & Testing</h3>
          <p class="project-desc">End-to-end software testing using Selenium, Playwright, and Java. API validation with Postman, ensuring zero-defect product launches.</p>
        </div>
        <div class="project-card reveal">
          <div class="skill-icon" style="font-size:2rem; width:60px; height:60px;">💻</div>
          <h3 class="project-title">Web Development</h3>
          <p class="project-desc">Building responsive, high-performance websites and web applications tailored for users in Nepal and globally.</p>
        </div>
        <div class="project-card reveal">
          <div class="skill-icon" style="font-size:2rem; width:60px; height:60px;">🎨</div>
          <h3 class="project-title">Graphic Design</h3>
          <p class="project-desc">Crafting stunning visual assets, UI/UX mockups, and marketing materials using Photoshop and Canva.</p>
        </div>
        <div class="project-card reveal">
          <div class="skill-icon" style="font-size:2rem; width:60px; height:60px;">🎧</div>
          <h3 class="project-title">Technical Support</h3>
          <p class="project-desc">Expert technical diagnostics and customer support, managing networks, GPON, and live chat platforms.</p>
        </div>
      </div>
    </div>
  </section>

  <hr class="divider">
"""
content = content.replace('<!-- SKILLS -->', services_html + '\n  <!-- SKILLS -->')

# 7. Add Testimonials & Blog
testi_blog_html = """
  <!-- TESTIMONIALS -->
  <section id="testimonials">
    <div class="section-inner">
      <p class="section-label reveal">Testimonials</p>
      <h2 class="section-title reveal">What People Say</h2>
      
      <div class="projects-grid">
        <div class="project-card reveal">
          <p class="project-desc" style="font-style: italic;">"Krijan is an exceptional QA Engineer. His attention to detail in automation testing saved our team countless hours and prevented major bugs from hitting production."</p>
          <div style="display:flex; gap:1rem; align-items:center;">
            <div style="width:40px; height:40px; border-radius:50%; background:var(--accent); display:flex; align-items:center; justify-content:center; font-weight:bold;">S</div>
            <div>
              <div style="font-weight:bold;">Senior Developer</div>
              <div style="font-size:0.8rem; color:var(--muted);">Tech Corp</div>
            </div>
          </div>
        </div>
        <div class="project-card reveal">
          <p class="project-desc" style="font-style: italic;">"Working with Krijan on our web project was a breeze. He not only designed a beautiful interface but ensured it was perfectly responsive and accessible."</p>
          <div style="display:flex; gap:1rem; align-items:center;">
            <div style="width:40px; height:40px; border-radius:50%; background:var(--accent3); display:flex; align-items:center; justify-content:center; font-weight:bold;">P</div>
            <div>
              <div style="font-weight:bold;">Project Manager</div>
              <div style="font-size:0.8rem; color:var(--muted);">Creative Agency</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <hr class="divider">

  <!-- BLOG -->
  <section id="blog">
    <div class="section-inner">
      <p class="section-label reveal">Blog</p>
      <h2 class="section-title reveal">Latest Insights</h2>
      
      <div class="projects-grid">
        <div class="project-card reveal">
          <div class="project-num">Article</div>
          <h3 class="project-title">The Future of QA Automation in 2026</h3>
          <p class="project-desc">Exploring how AI and modern tools like Playwright are reshaping the software testing landscape.</p>
          <a href="#" class="cert-btn">Read More →</a>
        </div>
        <div class="project-card reveal">
          <div class="project-num">Article</div>
          <h3 class="project-title">Web Performance Optimization</h3>
          <p class="project-desc">A deep dive into Core Web Vitals, SEO, and achieving a 100/100 Lighthouse score.</p>
          <a href="#" class="cert-btn">Read More →</a>
        </div>
      </div>
    </div>
  </section>

  <hr class="divider">
"""
content = content.replace('<!-- EDUCATION -->', testi_blog_html + '\n  <!-- EDUCATION -->')

# 8. Add Resume Section
resume_html = """
  <!-- RESUME -->
  <section id="resume">
    <div class="section-inner" style="text-align:center;">
      <h2 class="section-title reveal">Ready to dive deeper?</h2>
      <p class="section-sub reveal" style="margin: 0 auto 2rem;">Get a full overview of my career, skills, and education by downloading my official resume.</p>
      <a href="krijan_raigai_cv.pdf" download class="btn-primary reveal" style="padding: 1rem 2.5rem; font-size: 1rem;">
        <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
          <path d="M5 20h14v-2H5v2zM19 9h-4V3H9v6H5l7 7 7-7z"/>
        </svg> Download Resume
      </a>
    </div>
  </section>

  <hr class="divider">
"""
content = content.replace('<!-- CONTACT -->', resume_html + '\n  <!-- CONTACT -->')

# 9. Update the timeline-item class for Glassmorphism
content = content.replace('.timeline-item {', '.timeline-item {\n      background: var(--surface);\n      border: 1px solid var(--border);\n      border-radius: 16px;\n      padding: 1.5rem 1.5rem 1.5rem 3rem;\n      backdrop-filter: blur(16px);\n      -webkit-backdrop-filter: blur(16px);')
# Fix the timeline item dot positioning for the new padding
content = content.replace('left: -2.35rem;', 'left: -1rem;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
