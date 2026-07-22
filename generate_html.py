import json

with open('c:\\vendorsouvenir-main\\vendorsouvenir-main\\souvenir-elegan-mitra-bisnis-terpercaya.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta and Title
html = html.replace(
    '<title>Souvenir Kantor Elegan untuk Mitra Bisnis Terpercaya | Maroon Souvenir</title>',
    '<title>Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya | Maroon Souvenir</title>'
)
html = html.replace(
    'content="Souvenir kantor elegan untuk mitra bisnis adalah produk hadiah dengan desain premium dan material berkualitas seperti kulit, kayu, atau logam yang dipilih untuk merepresentasikan profesionalisme perusahaan."',
    'content="Harga set hadiah perusahaan ditentukan oleh jenis produk, jumlah item dalam satu set, bahan yang digunakan, teknik cetak logo, serta volume pemesanan yang diajukan."'
)
html = html.replace(
    '<meta property="og:title" content="Souvenir Kantor Elegan untuk Mitra Bisnis Terpercaya">',
    '<meta property="og:title" content="Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya">'
)
html = html.replace(
    '<meta name="twitter:title" content="Souvenir Kantor Elegan untuk Mitra Bisnis Terpercaya">',
    '<meta name="twitter:title" content="Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya">'
)
html = html.replace(
    'href="https://vendorsouvenir.web.id/souvenir-elegan-mitra-bisnis-terpercaya"',
    'href="https://vendorsouvenir.web.id/harga-set-hadiah-perusahaan"'
)
html = html.replace(
    'content="https://vendorsouvenir.web.id/souvenir-elegan-mitra-bisnis-terpercaya"',
    'content="https://vendorsouvenir.web.id/harga-set-hadiah-perusahaan"'
)
html = html.replace('assets/Hampers-Eksklusif-Mewah.webp', 'assets/Pricelist-Corporate-Gift-Set-Mewah.webp')
html = html.replace('Souvenir Kantor Elegan untuk Mitra Bisnis Terpercaya', 'Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya')
html = html.replace('2026-07-21T16:10:00+07:00', '2026-07-22T10:00:00+07:00')
html = html.replace('souvenir-elegan-mitra-bisnis-terpercaya', 'harga-set-hadiah-perusahaan')

# The main article content replacement
article_content = '''
                    <figure style="margin-bottom: 2rem;">
                        <img src="assets/Pricelist-Corporate-Gift-Set-Mewah.webp" alt="Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya"
                            style="width: 100%; height: auto; border-radius: 12px; box-shadow: var(--shadow-card);" fetchpriority="high">
                        <figcaption style="font-size: 0.9rem; color: #64748B; text-align: center; margin-top: 0.5rem;">
                            Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya (Sumber: Maroon Souvenir)</figcaption>
                    </figure>

                    <!-- TOC -->
                    <div id="toc-container"
                        style="background: #F1F5F9; padding: 1.5rem; border-radius: 8px; margin-bottom: 2rem; border-left: 4px solid var(--accent);">
                        <div style="display: flex; justify-content: space-between; align-items: center; cursor: pointer;"
                            onclick="toggleToc()">
                            <h3 style="margin: 0; font-size: 1.25rem;">Daftar Isi</h3>
                            <i id="toc-icon" class="fa-solid fa-chevron-down"></i>
                        </div>
                        <ul id="toc-list" style="margin-top: 1rem; list-style: none; padding-left: 0; display: block;">
                        </ul>
                    </div>

                    <p class="lead" style="font-size: 1.15rem; line-height: 1.8;">
                        <strong>Harga set hadiah perusahaan ditentukan oleh</strong> jenis produk, jumlah item dalam satu set, bahan yang digunakan, teknik cetak logo, serta volume pemesanan yang diajukan. 
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Secara umum, paket dengan bahan standar dan jumlah pesanan besar memiliki harga per unit yang lebih efisien dibandingkan paket premium dalam jumlah kecil. Memahami faktor-faktor ini membantu perusahaan merencanakan anggaran hadiah korporat secara lebih tepat.
                    </p>
                    <ul style="margin-bottom: 2rem; line-height: 1.8;">
                        <li style="margin-bottom: 0.75rem;">Harga dipengaruhi oleh jenis produk, bahan, jumlah item, dan teknik cetak logo.</li>
                        <li style="margin-bottom: 0.75rem;">Volume pemesanan besar umumnya memberikan harga per unit lebih efisien.</li>
                        <li style="margin-bottom: 0.75rem;">Paket ekonomis dan paket premium memiliki struktur biaya yang berbeda.</li>
                        <li style="margin-bottom: 0.75rem;">Waktu pemesanan turut memengaruhi biaya produksi tambahan.</li>
                        <li style="margin-bottom: 0.75rem;">Konsultasi langsung membantu perusahaan mendapatkan estimasi biaya paling akurat.</li>
                    </ul>

                    <div style="background: #F1F5F9; padding: 1rem 1.5rem; border-left: 4px solid var(--accent); border-radius: 4px; margin-bottom: 2rem;">
                        <strong>Baca Juga:</strong> <a href="souvenir-elegan-mitra-bisnis-terpercaya" style="color: var(--accent); text-decoration: none; font-weight: 500;">Souvenir Kantor Elegan untuk Mitra Bisnis Terpercaya</a>
                    </div>

                    <h2 id="kisaran-harga">Berapa Kisaran Harga Set Hadiah Perusahaan Secara Umum</h2>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Kisaran harga set hadiah perusahaan sangat bervariasi tergantung kombinasi produk yang dipilih. 
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Paket ekonomis dengan satu hingga dua item berbahan standar umumnya berada pada rentang harga yang lebih terjangkau, sementara paket premium dengan tiga item atau lebih menggunakan bahan seperti kulit asli atau stainless steel berkualitas tinggi berada pada rentang harga yang lebih tinggi.
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Selain jenis produk, kemasan turut memengaruhi total biaya. Box standar dengan cetak logo sederhana memiliki biaya lebih rendah dibandingkan box magnetik custom dengan finishing khusus. Perusahaan yang menginginkan estimasi biaya sesuai kebutuhan spesifik disarankan berkonsultasi langsung dengan tim penyedia souvenir untuk mendapatkan penawaran yang akurat.
                    </p>

                    <!-- Secondary Image 1 -->
                    <div style="margin: 2rem 0;">
                        <img src="assets/Corporate-Gift-Set-Kisaran-Harga.webp" alt="Corporate Gift Set Kisaran Harga"
                            style="width: 100%; border-radius: 8px;" loading="lazy">
                        <p style="text-align: center; font-size: 0.9rem; color: #64748B; margin-top: 0.5rem;">Perbandingan Kisaran Harga Set Hadiah Perusahaan</p>
                    </div>

                    <h2 id="perbandingan-paket">Perbandingan Paket Ekonomis dan Paket Premium</h2>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Paket ekonomis umumnya cocok untuk kebutuhan hadiah dalam jumlah sangat besar seperti seminar atau acara internal perusahaan berskala besar, karena fokus utamanya adalah efisiensi biaya dengan tetap mempertahankan kualitas cetak logo yang baik. 
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Sementara itu, paket premium lebih sesuai untuk hadiah eksklusif kepada klien utama atau mitra strategis, karena menonjolkan kesan mewah melalui bahan dan kemasan yang lebih baik.
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Pemilihan antara kedua jenis paket ini sebaiknya disesuaikan dengan tujuan pemberian hadiah dan target penerima agar anggaran yang dikeluarkan sebanding dengan dampak branding yang diharapkan.
                    </p>

                    <h2 id="faktor-harga">Apa Saja Faktor yang Memengaruhi Harga Set Hadiah Perusahaan</h2>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Beberapa faktor utama yang memengaruhi harga set hadiah perusahaan meliputi jenis dan jumlah produk dalam satu set, kualitas bahan baku, kompleksitas desain logo, teknik cetak yang digunakan, jenis kemasan, serta jumlah total pesanan. 
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Penelitian mengenai industri produk promosi di Amerika Serikat pada tahun 2023 menunjukkan bahwa volume pemesanan merupakan salah satu faktor terpenting dalam menentukan efisiensi harga per unit untuk produk hadiah perusahaan.
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Kompleksitas desain logo juga berperan penting. Logo dengan banyak warna atau detail rumit umumnya membutuhkan proses produksi tambahan dibandingkan logo simpel satu warna, sehingga dapat memengaruhi biaya produksi secara keseluruhan.
                    </p>

                    <h3 id="waktu-pemesanan" style="margin-bottom: 1rem;">Pengaruh Waktu Pemesanan terhadap Biaya</h3>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Pemesanan yang dilakukan menjelang tenggat waktu acara dapat dikenakan biaya tambahan untuk mempercepat produksi. Sebaliknya, perencanaan pemesanan yang dilakukan jauh-jauh hari memberikan fleksibilitas lebih besar dalam negosiasi harga serta waktu produksi yang lebih longgar tanpa biaya tambahan.
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Perusahaan disarankan merencanakan kebutuhan set hadiah perusahaan minimal beberapa minggu sebelum acara berlangsung agar proses produksi dan pengiriman dapat berjalan lancar tanpa tekanan waktu.
                    </p>

                    <!-- Secondary Image 2 -->
                    <div style="margin: 2rem 0;">
                        <a href="https://www.corporategifts.id/" target="_blank" rel="noopener noreferrer">
                            <img src="assets/gift-vendor-souvenir.webp" alt="Corporate Gift dari Vendor Terpercaya"
                            style="width: 100%; border-radius: 8px;" loading="lazy">
                        </a>
                        <p style="text-align: center; font-size: 0.9rem; color: #64748B; margin-top: 0.5rem;">Solusi Set Hadiah Perusahaan yang Efisien</p>
                    </div>

                    <h2 id="cara-efisien">Bagaimana Cara Mendapatkan Harga Set Hadiah Perusahaan yang Efisien</h2>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Cara paling efektif untuk mendapatkan harga set hadiah perusahaan yang efisien adalah dengan memesan dalam jumlah besar sekaligus, memilih kombinasi produk dengan bahan yang seragam, serta merencanakan desain logo yang sederhana namun tetap representatif. 
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Konsolidasi pemesanan untuk beberapa kebutuhan sekaligus, misalnya untuk klien dan karyawan dalam satu periode, juga dapat membantu menekan biaya produksi secara keseluruhan.
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Selain itu, memilih penyedia souvenir yang menawarkan layanan konsultasi turut membantu perusahaan menghindari pemborosan anggaran akibat kombinasi produk yang kurang efisien.
                    </p>

                    <h3 id="tips-anggaran" style="margin-bottom: 1rem;">Tips Menyusun Anggaran Hadiah Korporat</h3>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Menyusun anggaran hadiah korporat sebaiknya mempertimbangkan jumlah penerima, tujuan pemberian hadiah, serta target kesan yang ingin dibangun. 
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Perusahaan dapat membagi anggaran menjadi beberapa tingkatan, misalnya paket standar untuk penerima dalam jumlah besar dan paket premium terbatas untuk klien utama, sehingga anggaran tetap terkendali namun kesan eksklusif tetap terjaga untuk pihak-pihak strategis.
                    </p>

                    <h2 id="kesimpulan">Kesimpulan</h2>
                    <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                        Harga set hadiah perusahaan dipengaruhi oleh berbagai faktor seperti jenis produk, bahan, teknik cetak logo, dan volume pemesanan. Perencanaan yang matang serta pemilihan kombinasi produk yang tepat dapat membantu perusahaan mendapatkan hasil premium dengan anggaran yang efisien.
                    </p>
                    <p style="line-height: 1.8; margin-bottom: 2rem;">
                        Dapatkan estimasi harga set hadiah perusahaan sesuai kebutuhan Anda melalui konsultasi gratis bersama VendorSouvenir.web.id. Hubungi kami sekarang untuk penawaran terbaik pemesanan korporat Anda.
                    </p>

                    <!-- Promo Banner -->
                    <a href="https://wa.me/62895639068080?text=Halo%20Admin,%20saya%20ingin%20konsultasi%20harga%20set%20hadiah%20perusahaan"
                        style="display: block; margin: 3rem 0; width: 100%; text-decoration: none;">
                        <div
                            style="background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%); color: white; padding: 2.5rem; border-radius: 12px; text-align: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
                            <h3 style="color: white; font-size: 1.8rem; margin-bottom: 0.5rem;">Butuh Estimasi Harga Set Hadiah Perusahaan?</h3>
                            <p style="font-size: 1.1rem; margin-bottom: 1.5rem; opacity: 0.9; line-height: 1.8;">
                                Tim ahli kami siap membantu Anda menyusun paket hadiah dengan biaya paling efisien.<br><br>
                                Pilihan barang akan disesuaikan dengan ketersediaan budget dan kebutuhan Anda.<br><br>
                                Seluruh desain kemasan akan kami selaraskan dengan identitas visual perusahaan Anda.
                            </p>
                            <span
                                style="background: white; color: #0284c7; padding: 0.85rem 2.5rem; border-radius: 50px; font-weight: bold; display: inline-block; margin-bottom: 1rem;">Konsultasi Gratis Sekarang <i class="fa-solid fa-arrow-right"></i></span>
                            <br>
                            <small style="color: #e0f2fe;">Dapatkan penawaran harga terbaik untuk pesanan massal!</small>
                        </div>
                    </a>

                    <h2 id="faq">FAQ Harga Set Hadiah Perusahaan</h2>
                    <div style="display: grid; gap: 1rem;">
                        <details style="background: #f8fafc; padding: 1rem; border-radius: 8px; cursor: pointer;">
                            <summary style="font-weight: bold; color: var(--foreground);">Apa saja yang memengaruhi harga set hadiah perusahaan?</summary>
                            <p style="margin-top: 1rem; color: #64748B; line-height: 1.8;">
                                Harga dipengaruhi oleh jenis produk, bahan, teknik cetak logo, jenis kemasan, dan jumlah pesanan.
                            </p>
                        </details>
                        <details style="background: #f8fafc; padding: 1rem; border-radius: 8px; cursor: pointer;">
                            <summary style="font-weight: bold; color: var(--foreground);">Apakah pemesanan dalam jumlah besar lebih murah?</summary>
                            <p style="margin-top: 1rem; color: #64748B; line-height: 1.8;">
                                Pada umumnya ya, harga per unit cenderung lebih efisien pada volume pemesanan yang lebih besar.
                            </p>
                        </details>
                        <details style="background: #f8fafc; padding: 1rem; border-radius: 8px; cursor: pointer;">
                            <summary style="font-weight: bold; color: var(--foreground);">Bagaimana cara mendapatkan penawaran harga dari VendorSouvenir.web.id?</summary>
                            <p style="margin-top: 1rem; color: #64748B; line-height: 1.8;">
                                Perusahaan dapat menghubungi tim VendorSouvenir.web.id untuk konsultasi kebutuhan dan mendapatkan estimasi harga sesuai spesifikasi yang diinginkan.
                            </p>
                        </details>
                    </div>

                    <!-- Share Buttons -->
                    <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e2e8f0;">
                        <h4 style="margin-bottom: 1rem;">Bagikan Artikel Ini:</h4>
                        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                            <a href="https://wa.me/?text=Harga%20Set%20Hadiah%20Perusahaan,%20Cek%20Kisaran%20Biayanya%20https://vendorsouvenir.web.id/harga-set-hadiah-perusahaan"
                                target="_blank" class="btn"
                                style="background: #25D366; color: white; border: none; flex: 1; min-width: 140px; justify-content: center;"><i
                                    class="fa-brands fa-whatsapp"></i> WhatsApp</a>
                            <a href="https://www.facebook.com/sharer/sharer.php?u=https://vendorsouvenir.web.id/harga-set-hadiah-perusahaan"
                                target="_blank" class="btn"
                                style="background: #1877F2; color: white; border: none; flex: 1; min-width: 140px; justify-content: center;"><i
                                    class="fa-brands fa-facebook-f"></i> Facebook</a>
                            <a href="https://twitter.com/intent/tweet?url=https://vendorsouvenir.web.id/harga-set-hadiah-perusahaan&text=Harga%20Set%20Hadiah%20Perusahaan,%20Cek%20Kisaran%20Biayanya"
                                target="_blank" class="btn"
                                style="background: #1DA1F2; color: white; border: none; flex: 1; min-width: 140px; justify-content: center;"><i
                                    class="fa-brands fa-twitter"></i> Twitter</a>
                        </div>
                    </div>

                    <!-- Author Bio -->
                    <div
                        style="margin-top: 3rem; background: #FFFDF5; padding: 2rem; border-radius: 12px; display: flex; align-items: center; gap: 1.5rem; box-shadow: var(--shadow-card);">
                        <img src="assets/logo.webp" alt="Maroon Souvenir"
                            style="width: 80px; height: 80px; border-radius: 50%; border: 2px solid var(--accent); padding: 5px; background: white;" loading="lazy">
                        <div>
                            <h4 style="margin-bottom: 0.5rem;">Maroon Souvenir</h4>
                            <p style="font-size: 0.9rem; color: #64748B; margin-bottom: 0.5rem;">Partner Corporate Gift
                                terpercaya di Indonesia. Berpengalaman melayani ratusan perusahaan sejak 2018.</p>
                            <a href="about"
                                style="color: var(--accent); font-weight: bold; text-decoration: none;">Lihat Portofolio
                                Kami <i class="fa-solid fa-arrow-right"></i></a>
                        </div>
                    </div>

'''

start_idx = html.find('<div class="lg-col-span-2 article-content">')
if start_idx != -1:
    end_idx = html.find('<!-- Sidebar -->', start_idx)
    html = html[:start_idx + len('<div class="lg-col-span-2 article-content">')] + '\\n' + article_content + '                </div>\\n\\n                ' + html[end_idx:]

related_html = '''
                        <div class="card" style="border: none; background: #F8FAFC;">
                            <h3
                                style="font-size: 1.25rem; border-bottom: 2px solid var(--accent); padding-bottom: 0.5rem; margin-bottom: 1.5rem; display: inline-block;">
                                Artikel Terkait</h3>
                            <div style="display: grid; gap: 1.5rem;">
                                <!-- Related Listing -->
                                <div style="display: flex; gap: 1rem; align-items: start;">
                                    <img src="assets/Hampers-Eksklusif-Mewah.webp"
                                        style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px;" onerror="this.src='assets/logo.webp'" loading="lazy">
                                    <div>
                                        <a href="souvenir-elegan-mitra-bisnis-terpercaya"
                                            style="text-decoration: none; color: var(--foreground); font-weight: bold; font-size: 0.95rem; line-height: 1.4; display: block; margin-bottom: 0.25rem;">Souvenir Kantor Elegan</a>
                                        <span style="font-size: 0.8rem; color: #64748B;">Produk hadiah dengan desain premium dan material berkualitas.</span>
                                    </div>
                                </div>
                                <div style="display: flex; gap: 1rem; align-items: start;">
                                    <img src="assets/corporate-gift-book-pen.webp"
                                        style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px;" onerror="this.src='assets/logo.webp'" loading="lazy">
                                    <div>
                                        <a href="set-hadiah-perusahaan-premium"
                                            style="text-decoration: none; color: var(--foreground); font-weight: bold; font-size: 0.95rem; line-height: 1.4; display: block; margin-bottom: 0.25rem;">Set Hadiah Perusahaan</a>
                                        <span style="font-size: 0.8rem; color: #64748B;">Paket souvenir korporat berisi kombinasi produk pilihan.</span>
                                    </div>
                                </div>
                                <div style="display: flex; gap: 1rem; align-items: start;">
                                    <img src="assets/souvenir_idul_fitri_premium_eksekutif.webp"
                                        style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px;" onerror="this.src='assets/logo.webp'" loading="lazy">
                                    <div>
                                        <a href="corporate-gift-package-hari-raya"
                                            style="text-decoration: none; color: var(--foreground); font-weight: bold; font-size: 0.95rem; line-height: 1.4; display: block; margin-bottom: 0.25rem;">Corporate Gift Hari Raya</a>
                                        <span style="font-size: 0.8rem; color: #64748B;">Hadiah korporat bertema musiman untuk klien dan karyawan.</span>
                                    </div>
                                </div>
                            </div>
                        </div>
'''

rel_start = html.find('<div class="card" style="border: none; background: #F8FAFC;">')
if rel_start != -1:
    rel_end = html.find('</div>\\n                    </div>\\n                </div>', rel_start)
    html = html[:rel_start] + related_html + html[rel_end + 6:]

start_schema = html.find('<script type="application/ld+json">')
end_schema = html.find('</script>', start_schema)
start_schema2 = html.find('<script type="application/ld+json">', end_schema)
end_schema2 = html.find('</script>', start_schema2)

schema1_str = html[start_schema + 35:end_schema].strip()
schema2_str = html[start_schema2 + 35:end_schema2].strip()

schema1 = json.loads(schema1_str)
schema1['mainEntityOfPage']['@id'] = 'https://vendorsouvenir.web.id/harga-set-hadiah-perusahaan'
schema1['headline'] = 'Harga Set Hadiah Perusahaan, Cek Kisaran Biayanya'
schema1['image'] = [
    'https://vendorsouvenir.web.id/assets/Pricelist-Corporate-Gift-Set-Mewah.webp',
    'https://vendorsouvenir.web.id/assets/Corporate-Gift-Set-Kisaran-Harga.webp',
    'https://vendorsouvenir.web.id/assets/gift-vendor-souvenir.webp'
]
schema1['datePublished'] = '2026-07-22T10:00:00+07:00'
schema1['dateModified'] = '2026-07-22T10:00:00+07:00'
schema1['description'] = 'Harga set hadiah perusahaan ditentukan oleh jenis produk, jumlah item dalam satu set, bahan yang digunakan, teknik cetak logo, serta volume pemesanan yang diajukan.'

schema2 = json.loads(schema2_str)
schema2['mainEntity'] = [
    {
        "@type": "Question",
        "name": "Apa saja yang memengaruhi harga set hadiah perusahaan?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Harga dipengaruhi oleh jenis produk, bahan, teknik cetak logo, jenis kemasan, dan jumlah pesanan."
        }
    },
    {
        "@type": "Question",
        "name": "Apakah pemesanan dalam jumlah besar lebih murah?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Pada umumnya ya, harga per unit cenderung lebih efisien pada volume pemesanan yang lebih besar."
        }
    },
    {
        "@type": "Question",
        "name": "Bagaimana cara mendapatkan penawaran harga dari VendorSouvenir.web.id?",
        "acceptedAnswer": {
            "@type": "Answer",
            "text": "Perusahaan dapat menghubungi tim VendorSouvenir.web.id untuk konsultasi kebutuhan dan mendapatkan estimasi harga sesuai spesifikasi yang diinginkan."
        }
    }
]

new_schema = '<script type="application/ld+json">\\n' + json.dumps(schema1, indent=4) + '\\n    </script>\\n    <script type="application/ld+json">\\n' + json.dumps(schema2, indent=4) + '\\n    </script>'
html = html[:start_schema] + new_schema + html[end_schema2 + 9:]

with open('c:\\vendorsouvenir-main\\vendorsouvenir-main\\harga-set-hadiah-perusahaan.html', 'w', encoding='utf-8') as f:
    f.write(html)
