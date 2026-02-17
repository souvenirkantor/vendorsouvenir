# 📘 Maroon Souvenir - Article Template Documentation

## 🎯 Overview

Template CSS universal untuk semua artikel blog Maroon Souvenir yang dioptimalkan untuk:
- ✅ **SEO Maximum** - Sesuai algoritma Google terbaru 2026
- ✅ **Layout Maksimal** - Max-width 1200px (bukan 800px)
- ✅ **Gambar Berkualitas Tinggi** - Full width untuk better image preview
- ✅ **Mobile-First Design** - Responsive di semua device
- ✅ **Accessibility** - WCAG 2.1 compliant

---

## 📦 File Template

**File CSS:** `article-template.css`

**Lokasi:** `f:\Anti Gravity Project\Maroon Souvenir\article-template.css`

---

## 🚀 Cara Penggunaan

### Metode 1: Link External CSS (Recommended)

Tambahkan di `<head>` section artikel:

```html
<head>
    <!-- Existing styles -->
    <link rel="stylesheet" href="style.css">
    
    <!-- Add Article Template -->
    <link rel="stylesheet" href="article-template.css">
    
    <!-- Other head content -->
</head>
```

### Metode 2: Inline CSS (Untuk artikel existing)

Copy CSS dari `article-template.css` dan paste di dalam tag `<style>` di artikel.

---

## 📐 Struktur HTML yang Direkomendasikan

```html
<!-- Main Content Section -->
<section class="section-padding">
    <div class="container">
        <div class="grid grid-cols-1 lg-grid-cols-3 gap-12">
            
            <!-- Article Content (Left Column) -->
            <div class="lg-col-span-2 article-content">
                
                <!-- Hero Image -->
                <figure class="article-image-figure">
                    <img src="assets/image.webp" alt="Descriptive Alt Text" width="1200" height="675">
                    <figcaption class="article-image-caption">
                        Caption untuk gambar (Sumber: Maroon Souvenir)
                    </figcaption>
                </figure>

                <!-- Table of Contents -->
                <div class="toc-container">
                    <div class="toc-title" onclick="toggleToc()">
                        Daftar Isi <i class="fa-solid fa-chevron-down" id="toc-icon"></i>
                    </div>
                    <ul class="toc-list" id="toc-list">
                        <!-- JS will populate -->
                    </ul>
                </div>

                <!-- Lead Paragraph -->
                <p class="lead">
                    Paragraf pembuka yang menarik perhatian pembaca...
                </p>

                <!-- Main Content -->
                <h2>Heading 2 - Section Title</h2>
                <p>Konten paragraf...</p>

                <h3>Heading 3 - Subsection</h3>
                <p>Konten paragraf...</p>

                <!-- Image in Content -->
                <figure class="article-image-figure">
                    <img src="assets/image2.webp" alt="Alt Text">
                    <figcaption class="article-image-caption">Caption</figcaption>
                </figure>

                <!-- Blockquote -->
                <blockquote>
                    "Quote yang powerful dan memorable"
                </blockquote>

                <!-- Baca Juga Section -->
                <div class="baca-juga">
                    <h4>Baca Juga:</h4>
                    <ul>
                        <li><a href="link1">Artikel Terkait 1</a></li>
                        <li><a href="link2">Artikel Terkait 2</a></li>
                    </ul>
                </div>

                <!-- Responsive Table -->
                <div class="responsive-table">
                    <table>
                        <thead>
                            <tr>
                                <th>Header 1</th>
                                <th>Header 2</th>
                                <th>Header 3</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Data 1</td>
                                <td>Data 2</td>
                                <td>Data 3</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Warning/Info Box -->
                <div class="warning-box">
                    <strong>⚠️ Perhatian:</strong> Informasi penting yang perlu diperhatikan.
                </div>

                <div class="info-box">
                    <strong>ℹ️ Info:</strong> Informasi tambahan yang berguna.
                </div>

                <!-- Conclusion -->
                <h2>Kesimpulan</h2>
                <p>Ringkasan dan call to action...</p>

                <!-- FAQ Section -->
                <div class="faq-container">
                    <h2>Pertanyaan Sering Diajukan (FAQ)</h2>
                    
                    <div class="faq-item">
                        <div class="faq-question">
                            Pertanyaan 1? <i class="fa-solid fa-chevron-down faq-icon"></i>
                        </div>
                        <div class="faq-answer">
                            Jawaban untuk pertanyaan 1.
                        </div>
                    </div>

                    <div class="faq-item">
                        <div class="faq-question">
                            Pertanyaan 2? <i class="fa-solid fa-chevron-down faq-icon"></i>
                        </div>
                        <div class="faq-answer">
                            Jawaban untuk pertanyaan 2.
                        </div>
                    </div>
                </div>

                <!-- Promo Banner -->
                <div class="promo-banner">
                    <a href="https://wa.me/62895639068080" target="_blank">
                        <img src="assets/promo-banner.webp" alt="Promo Banner">
                    </a>
                </div>

                <!-- Share Buttons -->
                <div class="share-buttons">
                    <p style="font-weight: 600; margin-bottom: 1rem; width: 100%;">Bagikan artikel ini:</p>
                    <a href="https://wa.me/?text=Title%20URL" class="share-btn whatsapp" target="_blank">
                        <i class="fa-brands fa-whatsapp"></i> WhatsApp
                    </a>
                    <a href="https://www.facebook.com/sharer/sharer.php?u=URL" class="share-btn facebook" target="_blank">
                        <i class="fa-brands fa-facebook"></i> Facebook
                    </a>
                    <a href="https://twitter.com/intent/tweet?text=Title&url=URL" class="share-btn twitter" target="_blank">
                        <i class="fa-brands fa-twitter"></i> Twitter
                    </a>
                    <a href="https://www.linkedin.com/shareArticle?mini=true&url=URL&title=Title" class="share-btn linkedin" target="_blank">
                        <i class="fa-brands fa-linkedin"></i> LinkedIn
                    </a>
                </div>

                <!-- Author Bio -->
                <div class="author-bio">
                    <img src="assets/logo.webp" alt="Maroon Souvenir" class="author-avatar">
                    <div>
                        <h4>Maroon Souvenir Editorial Team</h4>
                        <p>
                            Kami adalah tim profesional di industri souvenir kantor dan merchandise promosi. 
                            Berpengalaman melayani ratusan perusahaan di Indonesia sejak 2015.
                        </p>
                    </div>
                </div>

                <!-- Related Articles -->
                <div style="margin-top: 4rem;">
                    <h2>Artikel Terkait</h2>
                    <div class="related-grid">
                        <div class="related-card">
                            <img src="assets/related1.webp" alt="Related 1" class="related-img">
                            <div class="related-content">
                                <h4 class="related-title">Judul Artikel Terkait 1</h4>
                                <p class="related-excerpt">Excerpt singkat dari artikel...</p>
                                <a href="link1" class="related-link">Baca Selengkapnya →</a>
                            </div>
                        </div>
                        
                        <div class="related-card">
                            <img src="assets/related2.webp" alt="Related 2" class="related-img">
                            <div class="related-content">
                                <h4 class="related-title">Judul Artikel Terkait 2</h4>
                                <p class="related-excerpt">Excerpt singkat dari artikel...</p>
                                <a href="link2" class="related-link">Baca Selengkapnya →</a>
                            </div>
                        </div>

                        <div class="related-card">
                            <img src="assets/related3.webp" alt="Related 3" class="related-img">
                            <div class="related-content">
                                <h4 class="related-title">Judul Artikel Terkait 3</h4>
                                <p class="related-excerpt">Excerpt singkat dari artikel...</p>
                                <a href="link3" class="related-link">Baca Selengkapnya →</a>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Sidebar (Right Column) -->
            <div>
                <div style="position: sticky; top: 120px;">
                    <!-- CTA Widget, Categories, etc. -->
                </div>
            </div>

        </div>
    </div>
</section>
```

---

## 🎨 Class Reference

### Layout Classes
- `.article-content` - Main article container (max-width: 1200px)
- `.article-hero` - Hero image styling
- `.article-image-figure` - Figure wrapper for images
- `.article-image-caption` - Image caption styling

### Typography Classes
- `.lead` - Lead paragraph (larger font)
- `h1, h2, h3, h4` - Automatic heading styles

### Content Blocks
- `.toc-container` - Table of contents
- `.blockquote-custom` - Styled blockquote
- `.baca-juga` - "Read also" section
- `.warning-box` - Warning/alert box (red)
- `.info-box` - Information box (blue)
- `.checklist-box` - Success/checklist box (green)
- `.budget-box` - Budget/pricing box (yellow)

### Tables
- `.responsive-table` - Wrapper for responsive tables
- `.comparison-table` - Comparison table styling

### Interactive Elements
- `.share-buttons` - Share button container
- `.share-btn` - Individual share button
- `.faq-container` - FAQ section container
- `.faq-item` - Individual FAQ item
- `.faq-question` - FAQ question (clickable)
- `.faq-answer` - FAQ answer (toggleable)

### Author & Related
- `.author-bio` - Author bio section
- `.author-avatar` - Author avatar image
- `.related-grid` - Related articles grid
- `.related-card` - Individual related article card

### Promo
- `.promo-banner` - Promotional banner section

---

## 📱 Responsive Breakpoints

```css
/* Mobile First */
Default: Mobile (< 768px)

/* Tablet & Desktop */
@media (min-width: 768px) {
    - Related grid: 3 columns
    - Author bio: horizontal layout
}
```

---

## 🎯 SEO Best Practices

### 1. **Image Optimization**
```html
<!-- Always include width & height for CLS -->
<img src="image.webp" alt="Descriptive Alt Text" width="1200" height="675">

<!-- Use WebP format -->
<!-- Recommended sizes: 1200x675 (16:9) or 1200x800 (3:2) -->
```

### 2. **Heading Hierarchy**
```html
<!-- Only ONE H1 per page (in hero section) -->
<h1>Main Article Title</h1>

<!-- Use H2 for main sections -->
<h2>Section Title</h2>

<!-- Use H3 for subsections -->
<h3>Subsection Title</h3>
```

### 3. **Internal Linking**
```html
<!-- Link to related articles -->
<a href="related-article">Anchor Text with Keywords</a>
```

### 4. **Schema Markup**
Always include Article schema in `<head>`:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "image": "https://vendorsouvenir.web.id/assets/image.webp",
  "author": {...},
  "publisher": {...},
  "datePublished": "2026-02-16T21:00:00+07:00",
  "dateModified": "2026-02-16T21:00:00+07:00"
}
```

---

## 🔧 JavaScript Functions

### Toggle TOC
```javascript
function toggleToc() {
    const list = document.getElementById('toc-list');
    const icon = document.getElementById('toc-icon');
    list.classList.toggle('collapsed');
    if(list.classList.contains('collapsed')) {
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-right');
    } else {
        icon.classList.remove('fa-chevron-right');
        icon.classList.add('fa-chevron-down');
    }
}
```

### Auto-Generate TOC
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const articleContent = document.querySelector('.article-content');
    const tocList = document.getElementById('toc-list');
    const headers = articleContent.querySelectorAll('h2, h3');
    
    let idCounter = 1;
    
    headers.forEach(header => {
        const text = header.textContent;
        // Skip certain headings
        if (text === 'Kesimpulan' || text.includes('FAQ') || text === 'Artikel Terkait') return;

        const id = 'header-' + idCounter++;
        header.id = id;
        
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = '#' + id;
        a.textContent = text;
        
        if (header.tagName === 'H3') {
            li.classList.add('toc-h3');
        }
        
        li.appendChild(a);
        tocList.appendChild(li);
    });
});
```

### FAQ Toggle
```javascript
// Method 1: Simple toggle
document.querySelectorAll('.faq-item').forEach(item => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
        item.classList.toggle('active');
    });
});

// Method 2: With icon rotation
function toggleFaq(element) {
    const body = element.nextElementSibling;
    const icon = element.querySelector('i');
    body.classList.toggle('active');
    icon.classList.toggle('fa-chevron-down');
    icon.classList.toggle('fa-chevron-up');
}
```

---

## ✅ Checklist untuk Artikel Baru

- [ ] Link `article-template.css` di `<head>`
- [ ] Hero image dengan alt text & dimensions
- [ ] H1 hanya satu (di hero section)
- [ ] H2 untuk section utama
- [ ] H3 untuk subsection
- [ ] Table of Contents (auto-generated)
- [ ] Lead paragraph dengan class `.lead`
- [ ] Minimal 2-3 gambar berkualitas tinggi (WebP)
- [ ] Blockquote untuk highlight
- [ ] Baca Juga section dengan internal links
- [ ] FAQ section dengan schema markup
- [ ] Share buttons (WA, FB, Twitter, LinkedIn)
- [ ] Author bio
- [ ] 3 related articles
- [ ] Promo banner/CTA
- [ ] Mobile responsive test
- [ ] Schema markup (Article + FAQPage)

---

## 🚀 Performance Tips

1. **Lazy Loading Images**
```html
<img src="image.webp" alt="Alt Text" loading="lazy">
```

2. **Preload Critical Images**
```html
<link rel="preload" as="image" href="assets/hero-image.webp">
```

3. **Optimize CSS Delivery**
```html
<!-- Inline critical CSS, defer non-critical -->
<link rel="stylesheet" href="article-template.css" media="print" onload="this.media='all'">
```

---

## 📊 Expected Results

### SEO Metrics
- ✅ Core Web Vitals: PASS
- ✅ Mobile-Friendly: YES
- ✅ Image Preview: LARGE
- ✅ Rich Results: Article + FAQ

### User Experience
- ✅ Reading time: Comfortable
- ✅ Navigation: Easy (TOC)
- ✅ Engagement: High (FAQ, Related)
- ✅ Conversion: Optimized (CTA, Share)

---

## 🆘 Troubleshooting

### Issue: Layout terlalu lebar di mobile
**Solution:** Pastikan ada `<meta name="viewport">` di `<head>`

### Issue: Gambar tidak full width
**Solution:** Cek parent container tidak ada `max-width` yang lebih kecil

### Issue: TOC tidak muncul
**Solution:** Pastikan JavaScript sudah diload dan `id="toc-list"` ada

### Issue: FAQ tidak toggle
**Solution:** Cek JavaScript function `toggleFaq()` sudah ada

---

## 📞 Support

Untuk pertanyaan atau issue, hubungi:
- **Email:** dev@maroonsouvenir.com
- **WhatsApp:** +62 895 6390 68080

---

**Version:** 2.0  
**Last Updated:** 16 Februari 2026  
**Author:** Maroon Souvenir Development Team
