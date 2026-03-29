import json

cards_data = [
    {"category": "software-development", "img": "img/POS_KANA1.png", "title": "Sistem POS Kana", "desc_en": "A web-based business management platform that integrates procurement, sales, warehouse inventory, distribution partners, petty cash, sales team KPIs, and business reports into a single unified system.", "desc_id": "Platform manajemen bisnis berbasis web yang mengintegrasikan pengadaan, penjualan, inventaris gudang, mitra distribusi, kas kecil, KPI tim penjualan, dan laporan bisnis dalam satu sistem terpadu.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_all_telkom.svg", "title": "INDIPRO TELKOM SURABAYA", "desc_en": "Effortless online booking experience for home internet installation, enriched with advanced GIS features.", "desc_id": "Pengalaman pemesanan online pemasangan internet rumah yang praktis, dilengkapi fitur GIS tingkat lanjut.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_all_zelltech.svg", "title": "E-SALES ZELLTECH", "desc_en": "Zelltech's application: A powerful tool for PT Celcius Indo Perkasa, enabling seamless sales tracking and project monitoring.", "desc_id": "Aplikasi Zelltech untuk PT Celcius Indo Perkasa yang memudahkan pelacakan penjualan dan monitoring proyek.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_all_unilever.svg", "title": "SISTEM WAREHOUSE - MJS UNILEVER", "desc_en": "Efficient system facilitating inventory tracking for MJA Company, a trusted Unilever distributor.", "desc_id": "Sistem efisien untuk pelacakan inventaris MJA Company, distributor terpercaya Unilever.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_all_wika.svg", "title": "QPS WIKA GEDUNG", "desc_en": "Revolutionizing property assessments, PT. WIKA Gedung employs an innovative application for surveying residential units at Puncak CBD Apartments.", "desc_id": "Transformasi proses penilaian properti melalui aplikasi inovatif PT WIKA Gedung untuk survei unit hunian di Apartemen Puncak CBD.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_softdev_silly.svg", "title": "SILY", "desc_en": "Unveiling the Lamongan District's Smart City Portal App. Explore 360-degree photos, report issues, and ensure swift emergency responses.", "desc_id": "Portal Smart City Kabupaten Lamongan dengan fitur foto 360 derajat, pelaporan isu, dan respons darurat cepat.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_softdev_banjarbaru.svg", "title": "SIPINTAR", "desc_en": "Application used by the Public Works and Housing Department of Banjarbaru City to search for information on spatial planning.", "desc_id": "Aplikasi Dinas PUPR Kota Banjarbaru untuk pencarian informasi tata ruang.", "badge": "software"},
    {"category": "software-development", "img": "img/proyek_all_pamekasan.svg", "title": "TOWER IN YOUR HAND", "desc_en": "Application for supervision of telecommunication towers in Pamekasan Regency by the Department of Communication and Information Technology.", "desc_id": "Aplikasi pengawasan menara telekomunikasi di Kabupaten Pamekasan oleh Dinas Komunikasi dan Informatika.", "badge": "software"},
    {"category": "digital-branding", "img": "img/proyek_digital_ubaya.svg", "title": "Promotion Video Teknik Manufaktur Universitas Surabaya", "desc_en": "The promotional video showcases the Manufacturing Engineering program at the University of Surabaya, highlighting its unique features and offerings.", "desc_id": "Video promosi Program Teknik Manufaktur Universitas Surabaya yang menampilkan keunggulan program secara menarik.", "badge": "digital"},
    {"category": "digital-branding", "img": "img/proyek_digital_aisya.svg", "title": "Rebranding Digital Marketing Queen Aisya Salon and SPA", "desc_en": "Revitalizing the digital marketing strategy for Queen Aisya Salon and SPA through a comprehensive rebranding initiative.", "desc_id": "Revitalisasi strategi pemasaran digital Queen Aisya Salon and SPA melalui inisiatif rebranding yang menyeluruh.", "badge": "digital"},
    {"category": "digital-branding", "img": "img/proyek_digital_jmf.png", "title": "Aerial Video Company Profile PT JMF", "desc_en": "Crafting an engaging aerial company profile video for PT JMF, showcasing their expertise and services from a captivating perspective.", "desc_id": "Pembuatan video company profile aerial PT JMF yang menonjolkan kapabilitas dan layanan perusahaan.", "badge": "digital"},
    {"category": "startup-incubator", "img": "img/proyek_startup_kontraktor.jpg", "title": "Sistem Informasi Manajemen Rumah Sakit - MEDIFY", "desc_en": "Digital startup incubation guiding startups focused on hospital management systems, covering investment and managed services.", "desc_id": "Inkubasi startup digital untuk mendampingi pengembangan startup yang berfokus pada sistem manajemen rumah sakit, termasuk aspek investasi dan managed services.", "badge": "startup"},
    {"category": "startup-incubator", "img": "img/proyek_all_industri.jpg", "title": "Sistem Ruang Komunitas - RUANGTEMU", "desc_en": "Digital-based startup incubation providing community event news and event management, focused on Tech Investment and Tech Consultants.", "desc_id": "Inkubasi startup berbasis digital yang menyajikan informasi event komunitas dan mendukung manajemen acara, berfokus pada investasi dan konsultasi teknologi.", "badge": "startup"},
    {"category": "startup-incubator", "img": "img/proyek_startup_kontraktor.jpg", "title": "Sistem Aplikasi Kontraktor", "desc_en": "Digital-based startup incubation providing a project monitoring application for construction contractors, covering Tech Consultant and Managed Services.", "desc_id": "Inkubasi startup berbasis digital melalui aplikasi monitoring proyek untuk kontraktor konstruksi, mencakup konsultasi teknologi dan managed services.", "badge": "startup"},
    {"category": "startup-incubator", "img": "img/proyek_all_industri.jpg", "title": "Sistem Aplikasi Manufaktur Industri", "desc_en": "Digital-based startup incubation providing manufacturing application systems for industry, covering Tech Consultant and Managed Services.", "desc_id": "Inkubasi startup berbasis digital melalui sistem aplikasi manufaktur untuk industri, mencakup konsultasi teknologi dan managed services.", "badge": "startup"},
    {"category": "startup-incubator", "img": "img/proyek_all_calcius.jpg", "title": "Sistem Koperasi CALCIUS", "desc_en": "Digital-based startup incubation providing cooperative organization information systems, covering Tech Investment and Business Consultant.", "desc_id": "Inkubasi startup berbasis digital melalui sistem informasi koperasi, mencakup investasi teknologi dan konsultasi bisnis.", "badge": "startup"},
    {"category": "it-consultant", "img": "img/proyek_all_kana.jpg", "title": "Analisa Pengembangan dan Kebutuhan KOPERASI KANA", "desc_en": "Analysis and development of application systems involving planning, design, and development to meet user needs of KOPERASI KANA.", "desc_id": "Analisis dan pengembangan sistem aplikasi meliputi perencanaan, perancangan, dan pengembangan untuk memenuhi kebutuhan KOPERASI KANA.", "badge": "consultant"},
    {"category": "it-consultant", "img": "img/proyek_all_pamekasan.svg", "title": "Perencanaan Sistem Monitoring Ternak", "desc_en": "Technology for real-time livestock condition monitoring in collaboration with Telkom Indonesia for the Lamongan district government.", "desc_id": "Teknologi untuk monitoring kondisi ternak secara real-time bersama Telkom Indonesia untuk Pemerintah Kabupaten Lamongan.", "badge": "consultant"},
    {"category": "it-consultant", "img": "img/proyek_all_ppdb.jpg", "title": "Perencanaan Pengembangan Sistem PPDB", "desc_en": "Online platform for managing student admissions, including registration, data verification, selection, and announcement of results.", "desc_id": "Platform online untuk pengelolaan penerimaan siswa baru, mencakup pendaftaran, verifikasi data, seleksi, dan pengumuman hasil.", "badge": "consultant"},
    {"category": "it-consultant", "img": "img/proyek_all_bmt.jpg", "title": "Analisa Pengembangan Koperasi BMT MUDA", "desc_en": "Analysis and development of application systems involving planning and design to meet the user needs of KOPERASI BMT MUDA.", "desc_id": "Analisis dan pengembangan sistem aplikasi melalui tahap perencanaan dan perancangan untuk memenuhi kebutuhan KOPERASI BMT MUDA.", "badge": "consultant"},
    {"category": "it-consultant", "img": "img/proyek_all_beraucoal.jpg", "title": "POC dan Perencanaan Sistem Job Center Berau Coal", "desc_en": "Development of a prototype (POC) to prove that the design concept for the job center application can be carried out and implemented.", "desc_id": "Pengembangan prototipe (POC) untuk membuktikan bahwa konsep desain aplikasi job center dapat dijalankan dan diimplementasikan.", "badge": "consultant"},
    {"category": "it-consultant", "img": "img/proyek_consult_telkom.png", "title": "Perencanaan Sistem Pemetaan Bangunan", "desc_en": "Technology implementation planning for building mapping using digital imagery, in collaboration with Telkom Indonesia for the Lamongan district government.", "desc_id": "Perencanaan implementasi teknologi pemetaan bangunan berbasis citra digital bersama Telkom Indonesia untuk Pemerintah Kabupaten Lamongan.", "badge": "consultant"}
]

badge_colors = {
    "software": "text-blue-600 bg-blue-100",
    "digital": "text-orange-600 bg-orange-100",
    "startup": "text-emerald-600 bg-emerald-100",
    "consultant": "text-purple-600 bg-purple-100"
}

cards_html = ""
for idx, card in enumerate(cards_data):
    bcol = badge_colors[card['badge']]
    bname = ""
    if card['badge'] == "software": bname = "Software Development"
    if card['badge'] == "digital": bname = "Digital Branding"
    if card['badge'] == "startup": bname = "Startup Incubator"
    if card['badge'] == "consultant": bname = "IT Consultant"
    
    cards_html += f'''
    <a href="detail_project.html" class="wc-card group bg-white border border-gray-100 rounded-2xl overflow-hidden hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 flex flex-col items-start" data-category="{card['category']}">
        <div class="h-64 w-full bg-slate-100 flex items-center justify-center p-6 border-b border-gray-100 overflow-hidden relative">
            <img src="{card['img']}" alt="{card['title']}" class="max-h-full max-w-full object-contain group-hover:scale-110 transition-transform duration-500" onerror="this.src='img/brand-logo-main.png'; this.classList.add('opacity-30', 'grayscale');">
        </div>
        <div class="p-8 flex-1 flex flex-col">
            <span class="inline-block px-3 py-1 text-xs font-bold rounded-full mb-4 w-max {bcol} wc-badge" data-badge="{card['badge']}">{bname}</span>
            <h3 class="text-xl font-bold text-slate-900 mb-4 line-clamp-2 wc-card-title">{card['title']}</h3>
            <p class="text-slate-500 text-sm leading-relaxed mb-6 line-clamp-4 wc-card-text" data-desc-en="{card['desc_en']}" data-desc-id="{card['desc_id']}">{card['desc_en']}</p>
            <div class="mt-auto flex items-center gap-2 text-blue-600 font-bold text-sm group-hover:gap-3 transition-all wc-readmore">Read More <span class="material-symbols-outlined text-sm">arrow_forward</span></div>
        </div>
    </a>'''

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hexavara - Works</title>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL,GRAD,opsz@100..700,0,0,20..48" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;400;500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/output.css" />
    <style>
        body { font-family: 'Inter', sans-serif; }
        .hide-scrollbar::-webkit-scrollbar { display: none; }
        .hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
        .lang-btn-active { background-color: #2563eb; color: white; }
        .hero-mosaic { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; opacity: 0.15; display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1rem; padding: 1rem; overflow: hidden; }
        .hero-mosaic img { width: 100%; height: auto; border-radius: 1rem; object-fit: cover; filter: grayscale(1); mix-blend-mode: multiply; }
        .wc-pg-num.active { background-color: #2563eb; color: white; }
        .filter-active { background-color: #1e293b; color: white; border-color: #1e293b; }
    </style>
</head>
<body class="bg-gray-50 text-slate-800 antialiased overflow-x-hidden relative" id="top">

<!-- Navbar -->
<nav class="fixed w-full bg-white/90 backdrop-blur-md z-50 border-b border-gray-100 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-20 items-center">
            <div class="flex-shrink-0 flex items-center">
                <a href="index.html">
                    <img class="h-10 w-auto" src="img/brand-logo-main.png" alt="Hexavara Logo">
                </a>
            </div>
            <div class="hidden md:flex items-center space-x-8">
                <a href="works.html" class="nav-link text-blue-600 font-bold transition-colors" data-i18n="Works">Works</a>
                <a href="about_us.html" class="nav-link text-slate-600 hover:text-blue-600 font-medium transition-colors" data-i18n="About Us">About Us</a>
                <a href="service.html" class="nav-link text-slate-600 hover:text-blue-600 font-medium transition-colors" data-i18n="Services">Services</a>
                <div class="relative group">
                    <button id="solutions-trigger" class="flex items-center text-slate-600 hover:text-blue-600 font-medium transition-colors focus:outline-none" data-i18n="Solutions">
                        Solutions <span class="material-symbols-outlined ml-1 text-sm">expand_more</span>
                    </button>
                    <!-- Mega Menu -->
                    <div id="solutions-mega-menu" class="absolute top-12 left-1/2 -translate-x-1/2 w-screen max-w-5xl bg-white border border-gray-100 rounded-xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 p-8 grid grid-cols-1 md:grid-cols-3 gap-8">
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 border-b pb-3 mb-4 solusi-title" data-i18n="Solution by Service">Solution by Service</h3>
                            <div class="space-y-3">
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-orange-500 transition-colors"><span class="material-symbols-outlined text-orange-500">account_tree</span> <span class="solusi-link" data-i18n="Enterprise Resource Planning">Enterprise Resource Planning</span></a>
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-orange-500 transition-colors"><span class="material-symbols-outlined text-orange-500">groups</span> <span class="solusi-link" data-i18n="Customer Relationship Management">Customer Relationship Management</span></a>
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-orange-500 transition-colors"><span class="material-symbols-outlined text-orange-500">query_stats</span> <span class="solusi-link" data-i18n="Business Intelligence & Analytics">Business Intelligence & Analytics</span></a>
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-orange-500 transition-colors"><span class="material-symbols-outlined text-orange-500">cloud_sync</span> <span class="solusi-link" data-i18n="Cloud Migration & Strategy">Cloud Migration & Strategy</span></a>
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-orange-500 transition-colors"><span class="material-symbols-outlined text-orange-500">verified_user</span> <span class="solusi-link" data-i18n="Cybersecurity & Compliance">Cybersecurity & Compliance</span></a>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 border-b pb-3 mb-4 solusi-title" data-i18n="Solution by Industry">Solution by Industry</h3>
                            <div class="space-y-3">
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-blue-600 transition-colors"><span class="material-symbols-outlined text-blue-600">shopping_bag</span> <span class="solusi-link" data-i18n="Consumer Goods">Consumer Goods</span></a>
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-blue-600 transition-colors"><span class="material-symbols-outlined text-blue-600">monitor_heart</span> <span class="solusi-link" data-i18n="Healthcare">Healthcare</span></a>
                                <a href="solution.html" class="flex items-center gap-3 text-slate-600 hover:text-blue-600 transition-colors"><span class="material-symbols-outlined text-blue-600">conveyor_belt</span> <span class="solusi-link" data-i18n="Supply Chain">Supply Chain</span></a>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-lg font-bold text-slate-900 border-b pb-3 mb-4 solusi-title" data-i18n="Ready to Use Platform">Ready to Use Platform</h3>
                            <div class="space-y-4">
                                <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-teal-100 text-teal-700 flex items-center justify-center"><span class="material-symbols-outlined">diversity_3</span></div><div><p class="font-bold text-sm text-slate-900 solusi-plat">Crowdfunding</p><p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Platform</p></div></div>
                                <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-red-100 text-red-700 flex items-center justify-center"><span class="material-symbols-outlined">account_balance_wallet</span></div><div><p class="font-bold text-sm text-slate-900 solusi-plat">Corporate Budgeting</p><p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Platform</p></div></div>
                                <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-orange-100 text-orange-700 flex items-center justify-center"><span class="material-symbols-outlined">shopping_cart</span></div><div><p class="font-bold text-sm text-slate-900 solusi-plat">E-Commerce</p><p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Platform</p></div></div>
                                <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-green-100 text-green-700 flex items-center justify-center"><span class="material-symbols-outlined">event</span></div><div><p class="font-bold text-sm text-slate-900 solusi-plat">Event Management</p><p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Platform</p></div></div>
                                <div class="flex items-center gap-3"><div class="w-10 h-10 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center"><span class="material-symbols-outlined">storefront</span></div><div><p class="font-bold text-sm text-slate-900 solusi-plat">Multi-Merchant</p><p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Platform</p></div></div>
                            </div>
                        </div>
                    </div>
                </div>
                <a href="cta.html" class="px-6 py-2 bg-blue-600 text-white font-bold rounded-full hover:bg-blue-700 transition-colors shadow-lg hover:shadow-blue-500/30" data-i18n="Start a Project?">Start a Project?</a>
            </div>
            <!-- Mobile menu button -->
            <div class="md:hidden flex items-center">
                <button class="text-slate-600 hover:text-slate-900 focus:outline-none">
                    <span class="material-symbols-outlined text-3xl">menu</span>
                </button>
            </div>
        </div>
    </div>
</nav>

<!-- Hero Section -->
<section class="relative pt-32 pb-24 bg-gradient-to-br from-blue-900 to-slate-900 text-white overflow-hidden">
    <div class="hero-mosaic hidden md:grid">
        <img src="img/proyek_all_wika.svg" alt="wika">
        <img src="img/proyek_all_telkom.svg" alt="telkom">
        <img src="img/proyek_all_beraucoal.jpg" alt="beraucoal">
        <img src="img/proyek_all_calcius.jpg" alt="calcius">
        <img src="img/proyek_all_industri.jpg" alt="industri">
        <img src="img/proyek_all_bmt.jpg" alt="bmt">
        <img src="img/proyek_all_unilever.svg" alt="unilever">
        <img src="img/proyek_all_kana.jpg" alt="kana">
        <img src="img/proyek_all_ppdb.jpg" alt="ppdb">
        <img src="img/proyek_all_zelltech.svg" alt="zelltech">
        <img src="img/proyek_digital_ubaya.svg" alt="ubaya">
        <img src="img/proyek_all_pamekasan.svg" alt="pamekasan">
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center py-16">
        <h1 class="text-5xl md:text-7xl font-bold tracking-tight mb-6 leading-tight max-w-4xl mx-auto hero-title">
            Consult, Design,<br />
            &amp; <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-teal-300">Develop</span>
        </h1>
        <p class="text-lg md:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed hero-desc">
            Help businesses realize their digitalization goals. Use Free 60-minute consultation
            to start your digital journey.
        </p>
    </div>
</section>

<!-- Our Works -->
<section class="py-24 bg-gray-50" id="works-projects">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-bold text-slate-900 mb-6 section-title">Our Works</h2>
            <div class="w-16 h-1 bg-blue-600 mx-auto rounded-full mb-6"></div>
            <p class="text-lg text-slate-600 max-w-3xl mx-auto section-desc">
                Experience innovation, explore excellence. Our Works exhibit a harmonious blend of
                creativity and functionality, setting new standards in design and client satisfaction.
            </p>
        </div>

        <!-- Filters -->
        <div class="flex flex-wrap justify-center gap-3 mb-16">
            <button class="wc-chip px-6 py-2.5 rounded-full border border-slate-300 bg-white text-slate-600 font-bold hover:bg-slate-100 transition-colors active filter-active shadow-sm" data-filter="all">All</button>
            <button class="wc-chip px-6 py-2.5 rounded-full border border-slate-300 bg-white text-slate-600 font-bold hover:bg-slate-100 transition-colors shadow-sm" data-filter="software-development" data-i18n="Software Development">Software Development</button>
            <button class="wc-chip px-6 py-2.5 rounded-full border border-slate-300 bg-white text-slate-600 font-bold hover:bg-slate-100 transition-colors shadow-sm" data-filter="digital-branding" data-i18n="Digital Branding">Digital Branding</button>
            <button class="wc-chip px-6 py-2.5 rounded-full border border-slate-300 bg-white text-slate-600 font-bold hover:bg-slate-100 transition-colors shadow-sm" data-filter="startup-incubator" data-i18n="Startup Incubator">Startup Incubator</button>
            <button class="wc-chip px-6 py-2.5 rounded-full border border-slate-300 bg-white text-slate-600 font-bold hover:bg-slate-100 transition-colors shadow-sm" data-filter="it-consultant" data-i18n="IT Consultant">IT Consultant</button>
        </div>

        <!-- Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8" id="wc-grid">
            <!-- CARDS GENERATED HERE -->
            REPLACE_CARDS_HERE
        </div>

        <!-- Pagination -->
        <div class="mt-20 flex justify-center items-center gap-2" id="wc-pagination">
            <button type="button" class="w-12 h-12 rounded-full border border-slate-200 bg-white flex items-center justify-center text-slate-600 hover:bg-slate-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed shadow-sm font-bold" id="wc-pg-prev">&#8592;</button>
            <div class="flex gap-2" id="wc-pg-numbers"></div>
            <button type="button" class="w-12 h-12 rounded-full border border-slate-200 bg-white flex items-center justify-center text-slate-600 hover:bg-slate-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed shadow-sm font-bold" id="wc-pg-next">&#8594;</button>
        </div>
    </div>
</section>

<!-- CTA -->
<section class="py-24 relative bg-blue-600 text-white overflow-hidden text-center">
    <div class="max-w-4xl mx-auto px-4 relative z-10">
        <span class="inline-block px-4 py-1.5 rounded-full bg-blue-500 text-white text-xs font-bold uppercase tracking-widest mb-6 border border-blue-400 cta-lbl">Ready to Get Started?</span>
        <h2 class="text-4xl md:text-5xl font-bold mb-8 leading-tight cta-title">Get the Right IT Solutions from the <span class="text-teal-300">Best IT Vendor</span> - Consult with Us Today!</h2>
        <p class="text-lg text-blue-100 mb-10 max-w-2xl mx-auto cta-desc">Discuss your IT challenges, and our team of experienced experts will provide tailored solutions to drive your business growth and success.</p>
        <a href="cta.html" class="inline-block px-10 py-4 bg-white text-blue-600 font-bold rounded-full hover:bg-slate-50 shadow-xl hover:-translate-y-1 transition-all mx-auto duration-300 text-lg cta-btn">Consult Now</a>
    </div>
</section>

<!-- Footer -->
<footer class="bg-slate-900 text-slate-300 py-16 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12 border-b border-slate-800 pb-12">
            <div class="lg:col-span-2">
                <img src="img/brand-logo-main.png" alt="Hexavara logo" class="h-12 w-auto mb-6 opacity-90 brightness-0 invert">
                <div class="font-bold text-white text-xl mb-2">Hexavara Technology</div>
                <div class="text-slate-400 max-w-md ft-tag">Software Development and IT Consulting</div>
                <div class="text-slate-400 max-w-md mt-4">
                    <strong class="text-white">Surabaya</strong><br/>
                    Graha Bukopin Lantai 7 dan 12, Jl. Panglima Sudirman No. 10-18, Embong Kaliasin, Genteng, Kota Surabaya, Jawa Timur 60271
                </div>
            </div>
            <div>
                <h4 class="text-white font-bold mb-6 uppercase tracking-wider text-xs ft-hd" data-i18n="Company">Company</h4>
                <ul class="space-y-4">
                    <li><a href="works.html" class="hover:text-white transition-colors ft-lk" data-i18n="Works">Works</a></li>
                    <li><a href="about_us.html" class="hover:text-white transition-colors ft-lk" data-i18n="About Us">About Us</a></li>
                    <li><a href="service.html" class="hover:text-white transition-colors ft-lk" data-i18n="Services">Services</a></li>
                    <li><a href="solution.html" class="hover:text-white transition-colors ft-lk" data-i18n="Solutions">Solutions</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold mb-6 uppercase tracking-wider text-xs ft-hd" data-i18n="Contact Us">Contact Us</h4>
                <ul class="space-y-4 mb-8">
                    <li class="flex items-center gap-3"><span class="material-symbols-outlined text-slate-500">mail</span> info@hexavara.com</li>
                    <li class="flex items-center gap-3"><span class="material-symbols-outlined text-slate-500">call</span> +628113451550</li>
                </ul>
                <h4 class="text-white font-bold mb-6 uppercase tracking-wider text-xs ft-hd" data-i18n="Follow Us">Follow Us</h4>
                <div class="flex gap-4">
                    <a href="https://instagram.com/hexavara" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-slate-700 hover:text-white transition-colors"><span class="material-symbols-outlined">photo_camera</span></a>
                    <a href="https://linkedin.com/company/hexavara" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-slate-700 hover:text-white transition-colors"><span class="material-symbols-outlined">work</span></a>
                    <a href="https://api.whatsapp.com/send?phone=628113451550" class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center hover:bg-slate-700 hover:text-white transition-colors"><span class="material-symbols-outlined">chat</span></a>
                </div>
            </div>
        </div>
        <div class="flex justify-between items-center text-slate-500">
            <div class="ft-cy">© 2026 Hexavara Tech. All rights reserved.</div>
        </div>
    </div>
</footer>

<!-- Language Switcher -->
<div class="fixed bottom-6 right-6 flex bg-white rounded-full shadow-lg border border-gray-200 overflow-hidden z-40 p-1">
    <button id="lang-en-btn" class="lang-btn lang-btn-active px-4 py-2 font-bold text-sm rounded-full transition-colors">EN</button>
    <button id="lang-id-btn" class="lang-btn px-4 py-2 font-bold text-sm rounded-full transition-colors hover:bg-slate-100 text-slate-700">ID</button>
</div>

<!-- Scroll to top -->
<button class="fixed bottom-24 right-6 w-12 h-12 bg-blue-600 text-white rounded-full shadow-lg flex items-center justify-center opacity-0 invisible transition-all duration-300 hover:bg-blue-700 z-40" id="scroll-top-btn"><span class="material-symbols-outlined">keyboard_arrow_up</span></button>

<script>
    // Language logic
    const translations = {
        en: { 
            "Works": "Works", "About Us": "About Us", "Services": "Services", "Solutions": "Solutions",
            "Solution by Service": "Solution by Service", "Solution by Industry": "Solution by Industry", "Ready to Use Platform": "Ready to Use Platform",
            "Enterprise Resource Planning": "Enterprise Resource Planning", "Customer Relationship Management": "Customer Relationship Management",
            "Business Intelligence & Analytics": "Business Intelligence & Analytics", "Cloud Migration & Strategy": "Cloud Migration & Strategy",
            "Cybersecurity & Compliance": "Cybersecurity & Compliance", "Consumer Goods": "Consumer Goods", "Healthcare": "Healthcare", "Supply Chain": "Supply Chain",
            "Software Development": "Software Development", "Digital Branding": "Digital Branding", "Startup Incubator": "Startup Incubator", "IT Consultant": "IT Consultant",
            "Start a Project?": "Start a Project?",
            "heroTitle": 'Consult, Design,<br />&amp; <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-teal-300">Develop</span>',
            "heroDesc": "Help businesses realize their digitalization goals. Use Free 60-minute consultation to start your digital journey.",
            "sectionTitle": "Our Works", "sectionDesc": "Experience innovation, explore excellence. Our Works exhibit a harmonious blend of creativity and functionality, setting new standards in design and client satisfaction.",
            "ctaLbl": "Ready to Get Started?", "ctaTitle": 'Get the Right IT Solutions from the <span class="text-teal-300">Best IT Vendor</span> - Consult with Us Today!',
            "ctaDesc": "Discuss your IT challenges, and our team of experienced experts will provide tailored solutions to drive your business growth and success.", "ctaBtn": "Consult Now",
            "ftTag": "Software Development and IT Consulting", "Company": "Company", "Contact Us": "Contact Us", "Follow Us": "Follow Us", "ftCy": "© 2026 Hexavara Tech. All rights reserved.",
            "Read More": "Read More"
        },
        id: {
            "Works": "Portofolio", "About Us": "Tentang Kami", "Services": "Layanan", "Solutions": "Solusi",
            "Solution by Service": "Solusi Berdasarkan Layanan", "Solution by Industry": "Solusi Berdasarkan Industri", "Ready to Use Platform": "Platform Siap Pakai",
            "Enterprise Resource Planning": "Perencanaan Sumber Daya Perusahaan (ERP)", "Customer Relationship Management": "Manajemen Hubungan Pelanggan (CRM)",
            "Business Intelligence & Analytics": "Business Intelligence & Analitik", "Cloud Migration & Strategy": "Migrasi & Strategi Cloud",
            "Cybersecurity & Compliance": "Keamanan Siber & Kepatuhan", "Consumer Goods": "Barang Konsumsi", "Healthcare": "Kesehatan", "Supply Chain": "Rantai Pasok",
            "Software Development": "Pengembangan Software", "Digital Branding": "Branding Digital", "Startup Incubator": "Inkubator Startup", "IT Consultant": "Konsultan TI",
            "Start a Project?": "Mulai Proyek?",
            "heroTitle": 'Konsultasi, Rancang,<br />&amp; <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-teal-300">Kembangkan</span>',
            "heroDesc": "Bantu bisnis mewujudkan transformasi digitalnya. Manfaatkan konsultasi gratis 60 menit untuk memulai perjalanan digital Anda.",
            "sectionTitle": "Portofolio Kami", "sectionDesc": "Lihat inovasi dan kualitas kerja kami. Portofolio ini menampilkan perpaduan kreativitas dan fungsi untuk menghasilkan solusi terbaik bagi klien.",
            "ctaLbl": "Siap Memulai?", "ctaTitle": 'Dapatkan Solusi IT yang Tepat dari <span class="text-teal-300">Vendor IT Terbaik</span> - Konsultasi dengan Kami Hari Ini!',
            "ctaDesc": "Diskusikan tantangan IT Anda, dan tim ahli kami akan memberikan solusi yang tepat untuk mendorong pertumbuhan dan keberhasilan bisnis Anda.", "ctaBtn": "Konsultasi Sekarang",
            "ftTag": "Pengembangan Software dan Konsultasi IT", "Company": "Perusahaan", "Contact Us": "Kontak", "Follow Us": "Ikuti Kami", "ftCy": "© 2026 Hexavara Tech. Seluruh hak cipta dilindungi.",
            "Read More": "Selengkapnya"
        }
    };

    let currentLang = localStorage.getItem('hexavara-lang') || 'en';
    
    function applyLang(lang) {
        currentLang = lang;
        const config = translations[lang];
        
        document.querySelectorAll('[data-i18n]').forEach(el => {
            if(config[el.getAttribute('data-i18n')]) {
                el.textContent = config[el.getAttribute('data-i18n')];
            }
        });
        
        document.querySelector('.hero-title').innerHTML = config.heroTitle;
        document.querySelector('.hero-desc').textContent = config.heroDesc;
        document.querySelector('.section-title').textContent = config.sectionTitle;
        document.querySelector('.section-desc').textContent = config.sectionDesc;
        document.querySelector('.cta-lbl').textContent = config.ctaLbl;
        document.querySelector('.cta-title').innerHTML = config.ctaTitle;
        document.querySelector('.cta-desc').textContent = config.ctaDesc;
        document.querySelector('.cta-btn').textContent = config.ctaBtn;
        document.querySelector('.ft-tag').textContent = config.ftTag;
        document.querySelector('.ft-cy').textContent = config.ftCy;

        document.querySelectorAll('.wc-card-text').forEach(el => {
            el.textContent = el.getAttribute(`data-desc-${lang}`);
        });

        document.querySelectorAll('.wc-badge').forEach(el => {
            const b = el.getAttribute('data-badge');
            let t = '';
            if(b==='software') t = config['Software Development'];
            if(b==='digital') t = config['Digital Branding'];
            if(b==='startup') t = config['Startup Incubator'];
            if(b==='consultant') t = config['IT Consultant'];
            el.textContent = t;
        });

        document.querySelectorAll('.wc-readmore').forEach(el => {
            el.innerHTML = `${config['Read More']} <span class="material-symbols-outlined text-sm">arrow_forward</span>`;
        });
    }

    document.getElementById('lang-en-btn').addEventListener('click', () => {
        document.getElementById('lang-en-btn').classList.add('lang-btn-active');
        document.getElementById('lang-en-btn').classList.remove('hover:bg-slate-100', 'text-slate-700');
        document.getElementById('lang-id-btn').classList.remove('lang-btn-active');
        document.getElementById('lang-id-btn').classList.add('hover:bg-slate-100', 'text-slate-700');
        applyLang('en');
        localStorage.setItem('hexavara-lang', 'en');
    });

    document.getElementById('lang-id-btn').addEventListener('click', () => {
        document.getElementById('lang-id-btn').classList.add('lang-btn-active');
        document.getElementById('lang-id-btn').classList.remove('hover:bg-slate-100', 'text-slate-700');
        document.getElementById('lang-en-btn').classList.remove('lang-btn-active');
        document.getElementById('lang-en-btn').classList.add('hover:bg-slate-100', 'text-slate-700');
        applyLang('id');
        localStorage.setItem('hexavara-lang', 'id');
    });

    if(currentLang === 'id') {
        document.getElementById('lang-id-btn').click();
    }

    // Pagination and Filtering logic
    const ITEMS_PER_PAGE = 6;
    let currentFilter = 'all';
    let currentPage = 1;
    const allCards = Array.from(document.querySelectorAll('.wc-card'));
    const chips = document.querySelectorAll('.wc-chip');
    const pgPrev = document.getElementById('wc-pg-prev');
    const pgNext = document.getElementById('wc-pg-next');
    const pgNumbers = document.getElementById('wc-pg-numbers');
    const pagination = document.getElementById('wc-pagination');

    function renderPagination(totalPages) {
        pgNumbers.innerHTML = '';
        for (let parse = 1; parse <= totalPages; parse++) {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = `w-12 h-12 rounded-full border border-slate-200 bg-white flex items-center justify-center font-bold text-sm shadow-sm hover:bg-slate-50 transition-colors wc-pg-num ${parse === currentPage ? 'active' : 'text-slate-600'}`;
            btn.setAttribute('data-page', parse);
            btn.textContent = parse;
            pgNumbers.appendChild(btn);
        }
    }

    function renderCards() {
        const filtered = currentFilter === 'all' ? allCards : allCards.filter(c => c.getAttribute('data-category') === currentFilter);
        const totalPages = Math.max(1, Math.ceil(filtered.length / ITEMS_PER_PAGE));
        const start = (currentPage - 1) * ITEMS_PER_PAGE;
        const end = start + ITEMS_PER_PAGE;

        allCards.forEach(c => c.style.display = 'none');
        filtered.slice(start, end).forEach(c => c.style.display = 'flex');

        if (filtered.length <= ITEMS_PER_PAGE) {
            pagination.style.display = 'none';
        } else {
            pagination.style.display = 'flex';
            renderPagination(totalPages);
            pgPrev.disabled = currentPage === 1;
            pgNext.disabled = currentPage === totalPages;
        }
    }

    chips.forEach(chip => {
        chip.addEventListener('click', () => {
            currentFilter = chip.getAttribute('data-filter');
            currentPage = 1;
            chips.forEach(c => {
                const isActive = c.getAttribute('data-filter') === currentFilter;
                c.classList.toggle('filter-active', isActive);
                c.classList.toggle('text-slate-600', !isActive);
            });
            renderCards();
        });
    });

    pgNumbers.addEventListener('click', e => {
        const btn = e.target.closest('.wc-pg-num');
        if (btn) {
            currentPage = parseInt(btn.getAttribute('data-page'), 10);
            renderCards();
            document.getElementById('works-projects').scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });

    pgPrev.addEventListener('click', () => {
        if (currentPage > 1) { currentPage--; renderCards(); document.getElementById('works-projects').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });

    pgNext.addEventListener('click', () => {
        const totalPages = Math.max(1, Math.ceil((currentFilter === 'all' ? allCards : allCards.filter(c => c.getAttribute('data-category') === currentFilter)).length / ITEMS_PER_PAGE));
        if (currentPage < totalPages) { currentPage++; renderCards(); document.getElementById('works-projects').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });

    renderCards();

    // Scroll top
    const scrollTopBtn = document.getElementById('scroll-top-btn');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) scrollTopBtn.classList.remove('opacity-0', 'invisible');
        else scrollTopBtn.classList.add('opacity-0', 'invisible');
    });
    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
</script>
</body>
</html>'''

with open('works.html', 'w', encoding='utf-8') as f:
    f.write(html_content.replace('REPLACE_CARDS_HERE', cards_html))
print("works.html successfully regenerated")
