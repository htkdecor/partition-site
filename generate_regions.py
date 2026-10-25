import os

# 1. 槟城 100 个细分地区、城镇及商业区列表
regions_data = [
    # 槟岛 (Penang Island) 主要区域与商业/住宅区
    ("george-town", "George Town"),
    ("jelutong", "Jelutong"),
    ("green-lane", "Green Lane"),
    ("island-glades", "Island Glades"),
    ("island-park", "Island Park"),
    ("air-itam", "Air Itam"),
    ("jelutong-east", "Jelutong East"),
    ("tanjung-tokong", "Tanjung Tokong"),
    ("tanjung-bungah", "Tanjung Bungah"),
    ("batu-ferringhi", "Batu Ferringhi"),
    ("teluk-bahang", "Teluk Bahang"),
    ("pulau-tikus", "Pulau Tikus"),
    ("gurney", "Gurney"),
    ("burmah-road", "Burmah Road"),
    ("penang-road", "Penang Road"),
    ("chulia-street", "Chulia Street"),
    ("komtar", "Komtar"),
    ("armenia-street", "Armenia Street"),
    ("padang-kota", "Padang Kota"),
    ("paya-terubong", "Paya Terubong"),
    ("farlim", "Farlim"),
    ("relau", "Relau"),
    ("sungai-ara", "Sungai Ara"),
    ("bayan-lepas", "Bayan Lepas"),
    ("bayan-baru", "Bayan Baru"),
    ("sungai-dua", "Sungai Dua"),
    ("batu-maung", "Batu Maung"),
    ("teluk-kumbar", "Teluk Kumbar"),
    ("balik-pulau", "Balik Pulau"),
    ("genting-balik-pulau", "Genting Balik Pulau"),
    ("titi-teras", "Titi Teras"),
    ("sungai-pinang", "Sungai Pinang"),
    ("jelutong-expressway", "Jelutong Expressway"),
    ("seberang-perai-selatan", "Seberang Perai Selatan"),
    ("bukit-jambul", "Bukit Jambul"),
    ("gloria-heights", "Gloria Heights"),
    ("desa-permai", "Desa Permai"),
    
    # 威省 (Seberang Perai) 核心城镇与工业区
    ("butterworth", "Butterworth"),
    ("perai", "Perai"),
    ("seberang-jaya", "Seberang Jaya"),
    ("bukit-mertajam", "Bukit Mertajam"),
    ("simpang-ampat", "Simpang Ampat"),
    ("juru", "Juru"),
    ("batu-kawan", "Batu Kawan"),
    ("valdor", "Valdor"),
    ("nibong-tebal", "Nibong Tebal"),
    ("sungai-bakap", "Sungai Bakap"),
    ("kepala-batas", "Kepala Batas"),
    ("tasek-gelugor", "Tasek Gelugor"),
    ("penaga", "Penaga"),
    ("kubang-semang", "Kubang Semang"),
    ("machang-bubok", "Machang Bubok"),
    ("permatang-pauh", "Permatang Pauh"),
    ("penanti", "Penanti"),
    ("sungai-dua-butterworth", "Sungai Dua Butterworth"),
    ("bagan-ajam", "Bagan Ajam"),
    ("mak-mandin", "Mak Mandin"),
    ("raja-uda", "Raja Uda"),
    ("bagan-lallang", "Bagan Lallang"),
    ("bagan-dalam", "Bagan Dalam"),
    ("perai-industrial-estate", "Perai Industrial Estate"),
    ("juru-auto-city", "Juru Auto City"),
    ("bayan-lepas-free-industrial-zone", "Bayan Lepas Free Industrial Zone"),
    ("phase-1-bayan-lepas", "Phase 1 Bayan Lepas"),
    ("phase-2-bayan-lepas", "Phase 2 Bayan Lepas"),
    ("phase-3-bayan-lepas", "Phase 3 Bayan Lepas"),
    ("batu-kawan-industrial-park", "Batu Kawan Industrial Park"),
    ("penang-science-park", "Penang Science Park"),
    ("bukit-minyak-industrial-park", "Bukit Minyak Industrial Park"),
    ("mak-mandin-industrial-estate", "Mak Mandin Industrial Estate"),
    ("bagan-luar", "Bagan Luar"),
    ("gurney-paragon", "Gurney Paragon"),
    ("gurney-plaza", "Gurney Plaza"),
    ("queensbay", "Queensbay"),
    ("straits-quay", "Straits Quay"),
    ("auto-city", "Auto City"),
    ("icon-city", "Icon City"),
    ("spice-penang", "SPICE Penang"),
    ("penang-sentral", "Penang Sentral"),
    ("taman-sri-ginting", "Taman Sri Ginting"),
    ("taman-lip-sin", "Taman Lip Sin"),
    ("taman-bayan", "Taman Bayan"),
    ("taman-kheng-kooi", "Taman Kheng Kooi"),
    ("taman-wee-hee-toy", "Taman Wee Hee Toy"),
    ("desa-krystal", "Desa Krystal"),
    ("desa-indah", "Desa Indah"),
    ("sungai-nibong", "Sungai Nibong"),
    ("taman-sri-nibong", "Taman Sri Nibong"),
    ("taman-pelangi", "Taman Pelangi"),
    ("taman-century", "Taman Century"),
    ("taman-bukit-mertajam", "Taman Bukit Mertajam"),
    ("taman-indah", "Taman Indah"),
    ("taman-permai", "Taman Permai"),
    ("taman-sejahtera", "Taman Sejahtera"),
    ("taman-jaya", "Taman Jaya"),
    ("taman-meru", "Taman Meru"),
    ("taman-seri-maju", "Taman Seri Maju"),
    ("taman-sentosa", "Taman Sentosa"),
    ("taman-mutiara", "Taman Mutiara")
]

# 高级 SEO HTML 模板
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Office Partition Services in {name} | HTK Decor Penang Specialist</title>
    <meta name="description" content="Looking for office partition installation in {name}, Penang? Premium glass partitions, aluminum framing & drywall solutions from RM12.00/ft². Get a free quote today!">
    
    <!-- 关键修复：动态 Canonical 标签（完美解决 Alternate page 错误） -->
    <link rel="canonical" href="https://partition.htkdecor.com.my/{slug}/" />

    <meta property="og:title" content="Office Partition Services in {name} | HTK Decor">
    <meta property="og:description" content="Professional glass & office partition specialist serving {name}, Penang. Prices start from RM12.00/ft².">
    <meta property="og:url" content="https://partition.htkdecor.com.my/{slug}/">
    <meta property="og:type" content="website">

    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><circle cx='50' cy='50' r='50' fill='%23fd7e14'/><text x='50%' y='58%' font-size='38' font-weight='bold' fill='white' text-anchor='middle' dominant-baseline='middle'>HTK</text></svg>">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- 动态 Schema 结构化数据 -->
    <script type="application/ld+json">
    [
      {{
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://partition.htkdecor.com.my/"
          }},
          {{
            "@type": "ListItem",
            "position": 2,
            "name": "{name} Partition Services",
            "item": "https://partition.htkdecor.com.my/{slug}/"
          }}
        ]
      }},
      {{
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "HTK Decor Partition Specialist - {name}",
        "telephone": "+60174315233",
        "priceRange": "RM12.00 - RM50.00 per sq ft",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "{name}",
          "addressRegion": "Penang",
          "addressCountry": "MY"
        }},
        "url": "https://partition.htkdecor.com.my/{slug}/"
      }}
    ]
    </script>

    <style>
        :root {{ --primary-color: #0d6efd; --primary-hover: #0b5ed7; --dark-color: #0f172a; }}
        body {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background-color: #f8fafc; color: #334155; }}
        .top-bar {{ background-color: var(--dark-color); color: #94a3b8; font-size: 0.875rem; }}
        .hero-section {{ 
            background: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), url('../IMG-20261015-WA0011.jpg') no-repeat center center; 
            background-size: cover; 
            color: white; 
            padding: 80px 0; 
        }}
        .hero-badge {{ background-color: rgba(13, 110, 253, 0.2); color: #60a5fa; border: 1px solid rgba(96, 165, 250, 0.3); border-radius: 50px; padding: 6px 16px; font-size: 0.875rem; font-weight: 600; display: inline-block; }}
        .price-badge {{ background-color: #fd7e14; color: white; border-radius: 50px; padding: 6px 18px; font-size: 1rem; font-weight: 700; display: inline-block; box-shadow: 0 2px 8px rgba(253, 126, 20, 0.4); }}
        .btn-whatsapp {{ background-color: #25D366; color: white; font-weight: 700; border-radius: 50px; padding: 12px 28px; box-shadow: 0 4px 14px rgba(37, 211, 102, 0.3); transition: all 0.2s ease; }}
        .btn-whatsapp:hover {{ background-color: #1da851; color: white; transform: translateY(-2px); }}
        .btn-phone {{ background-color: var(--primary-color); color: white; font-weight: 700; border-radius: 50px; padding: 12px 28px; box-shadow: 0 4px 14px rgba(13, 110, 253, 0.3); transition: all 0.2s ease; }}
        .btn-phone:hover {{ background-color: var(--primary-hover); color: white; transform: translateY(-2px); }}
        .card-custom {{ border: none; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }}
    </style>
</head>
<body>
    <div class="top-bar py-2 px-3 d-none d-md-block">
        <div class="container d-flex justify-content-between align-items-center">
            <span><i class="fas fa-map-marker-alt text-warning me-2"></i>Serving {name} & Surrounding Penang Areas</span>
            <span><i class="fas fa-phone-alt text-warning me-2"></i> Call Direct: <a href="tel:0174315233" class="text-white text-decoration-none fw-bold">017-431 5233</a></span>
        </div>
    </div> 
    
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm py-3 sticky-top">
        <div class="container">
            <a class="navbar-brand fw-bold text-dark" href="https://partition.htkdecor.com.my/">
                <i class="fas fa-building text-primary me-2"></i> HTK Partition | Penang
            </a>
            <div>
                <a href="https://partition.htkdecor.com.my/" class="btn btn-outline-secondary btn-sm rounded-pill px-3 me-2">Home</a>
                <a href="https://wa.me/60174315233?text=Hi%2C%20I%20need%20office%20partition%20service%20in%20{name}" class="btn btn-success btn-sm rounded-pill px-3"><i class="fab fa-whatsapp me-1"></i> WhatsApp</a>
            </div>
        </div>
    </nav>

    <header class="hero-section text-center">
        <div class="container">
            <div class="mb-3 d-flex justify-content-center gap-2 flex-wrap">
                <span class="badge bg-primary text-white fs-6 px-3 py-2 rounded-pill fw-bold"><i class="fas fa-shield-alt me-1"></i> Professional Glass & Office Partitions</span>
            </div>
            
            <div class="mb-3 d-flex justify-content-center gap-2 flex-wrap align-items-center">
                <span class="hero-badge"><i class="fas fa-location-dot me-1"></i> {name} Specialist</span>
                <span class="price-badge"><i class="fas fa-tag me-1"></i> From RM12.00 / ft²</span>
            </div>
            
            <h1 class="display-5 fw-bold mb-3">Office & Glass Partition Installation in {name}</h1>
            
            <div class="mb-4">
                <span class="badge bg-warning text-dark fs-6 px-3 py-2 rounded-pill shadow-sm">
                    <i class="fas fa-phone-alt me-1"></i> Direct Line: 017-431 5233
                </span>
            </div>

            <p class="lead col-lg-8 mx-auto mb-5 text-light opacity-87">
                Transform commercial shoplots, corporate offices, and residential spaces in <strong>{name}</strong> with high-quality tempered glass, aluminum frame, and gypsum drywall partitions.
            </p>
            
            <div class="d-flex justify-content-center gap-3 flex-wrap">
                <a href="https://wa.me/60174315233?text=Hi%2C%20I%20need%20office%20partition%20quote%20in%20{name}" class="btn btn-whatsapp btn-lg">
                    <i class="fab fa-whatsapp me-2"></i> WhatsApp for Quote
                </a>
                <a href="tel:0174315233" class="btn btn-phone btn-lg">
                    <i class="fas fa-phone-alt me-2"></i> Call 017-431 5233
                </a>
            </div>
        </div>
    </header>

    <main class="py-5">
        <div class="container">
            <div class="row align-items-center g-5">
                <div class="col-lg-6">
                    <h2 class="fw-bold mb-3">Reliable Partition Contractor in {name}</h2>
                    <p class="text-primary fw-bold fs-5 mb-3"><i class="fas fa-coins me-2"></i>Affordable Rates Starting From RM12.00 / ft²</p>
                    <p class="mb-4">Planning to renovate or set up a new office in {name}? Our experienced installation team provides fast site measurement, layout planning, and quick project completion.</p>

                    <div class="p-4 bg-white card-custom border-start border-primary border-4 mb-4">
                        <p class="fw-bold mb-2 text-dark"><i class="fas fa-check-circle text-primary me-2"></i>Our Specialized Services in {name}:</p>
                        <ul class="row row-cols-1 g-2 list-unstyled mb-0 small text-secondary">
                            <li><i class="fas fa-check text-primary me-2"></i> Frameless Tempered Glass Partition</li>
                            <li><i class="fas fa-check text-primary me-2"></i> Gypsum Board / Drywall Acoustic Partition</li>
                            <li><i class="fas fa-check text-primary me-2"></i> Aluminum Framed Sliding Doors & Glass Walls</li>
                            <li><i class="fas fa-check text-primary me-2"></i> Custom Office Layout & Fast On-Site Installation</li>
                        </ul>
                    </div>
                </div>
                
                <div class="col-lg-6">
                    <div class="bg-white p-5 card-custom text-center border">
                        <span class="badge bg-warning text-dark font-weight-bold mb-2 px-3 py-2 rounded-pill">Fast Estimation</span>
                        <h3 class="fw-bold mb-2">Get a Free Instant Quote</h3>
                        <p class="fs-4 text-primary fw-bold mb-3">From RM12.00 / ft²</p>
                        <p class="text-muted mb-4">Send us your room dimensions or layout design via WhatsApp for a quick estimate in {name}.</p>
                        <a href="https://wa.me/60174315233?text=Hi%2C%20I%20need%20partition%20quotation%20in%20{name}" class="btn btn-whatsapp btn-lg w-100 mb-3">
                            <i class="fab fa-whatsapp me-2"></i> Chat on WhatsApp Now
                        </a>
                        <a href="tel:0174315233" class="btn btn-outline-dark btn-lg w-100 rounded-pill">
                            <i class="fas fa-phone-alt me-2"></i> Call Hotline: 017-431 5233
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <!-- 仅保留周边邻近地区推荐区块，删除了大标题和折叠按钮 -->
        <section class="py-4 bg-light border-top mt-5">
            <div class="container text-center">
                <h6 class="fw-bold mb-2 text-dark">Other Serviced Areas Near {name}:</h6>
                <div class="row row-cols-2 row-cols-md-5 g-2 mt-3 justify-content-center">
                    <div class="col"><a href="https://partition.htkdecor.com.my/george-town/" class="btn btn-sm btn-outline-primary w-100 text-truncate">George Town</a></div>
                    <div class="col"><a href="https://partition.htkdecor.com.my/jelutong/" class="btn btn-sm btn-outline-primary w-100 text-truncate">Jelutong</a></div>
                    <div class="col"><a href="https://partition.htkdecor.com.my/bayan-lepas/" class="btn btn-sm btn-outline-primary w-100 text-truncate">Bayan Lepas</a></div>
                    <div class="col"><a href="https://partition.htkdecor.com.my/butterworth/" class="btn btn-sm btn-outline-primary w-100 text-truncate">Butterworth</a></div>
                    <div class="col"><a href="https://partition.htkdecor.com.my/bukit-mertajam/" class="btn btn-sm btn-outline-primary w-100 text-truncate">Bukit Mertajam</a></div>
                </div>
            </div>
        </section>
    </main>

    <footer class="bg-dark text-white py-4 text-center small opacity-75">
        <div class="container">
            <p class="mb-0">&copy; HTK Decor - Professional Partition Specialist in {name} & Penang. All Rights Reserved.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# 2. 循环生成各个地区的文件夹与 index.html
for slug, name in regions_data:
    os.makedirs(slug, exist_ok=True)
    file_path = os.path.join(slug, "index.html")
    
    content = HTML_TEMPLATE.format(slug=slug, name=name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully updated pages without the main serviced areas block!")
