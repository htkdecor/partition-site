import os

# 1. 槟城 100 个细分地区、城镇及商业区列表
regions = [
    # 槟岛 (Penang Island) 主要区域与商业/住宅区
    "george-town", "jelutong", "green-lane", "island-glades", "island-park",
    "ayang", "jelutong-east", "tanjung-tokong", "tanjung-bungah", "batu-ferringhi",
    "teluk-bahang", "pulau-tikus", "gurney", "burmah-road", "penang-road",
    "chulia-street", "komtar", "armenia-street", "padang-kota", "heah-ooi-ghee",
    "air-itam", "paya-terubong", "farlim", "relau", "sungai-ara",
    "bayan-lepas", "bayan-baru", "sungai-dua", "batu-maung", "teluk-kumbar",
    "balik-pulau", "genting-balid-pulau", "titi-teras", "sungai-pinang", "jelutong-expressway",
    "seberang-perai-selatan", "bukit-jambul", "gloria-heights", "desas-permai",
    
    # 威省 (Seberang Perai) 核心城镇
    "butterworth", "perai", "seberang-jaya", "bukit-mertajam", "simpang-ampat",
    "juru", "batu-kawan", "valdor", "nibong-tebal", "sungai-bakap",
    "kepala-batas", "taseklugor", "penaga", "kubang-semang", "machang-bubok",
    "permatang-pauh", "penanti", "sungai-dua-butterworth", "bagan-ajerial", "mak-mandin",
    "raja-uda", "bagan-lallang", "bagan-dalam", "perai-industrial-estate", "juru-auto-city",
    
    # 工业区与商业中心 (Industrial & Commercial Hubs)
    "bayan-lepas-free-industrial-zone", "phase-1-bayan-lepas", "phase-2-bayan-lepas", "phase-3-bayan-lepas", "batu-kawan-industrial-park",
    "malih", "penang-science-park", "bukit-minyak-industrial-park", "mak-mandin-industrial-estate", "bagan-luar",
    "gurney-paragon", "gurney-plaza", "queensbay", "strait-quay", "auto-city",
    "icon-city", "subterranean-penang-international-convention-centre", "spic", "komtar-jodoh", "penang-sentral",
    
    # 其他热门卫星市与住宅区
    "taman-sri-ginting", "taman-lip-sin", "taman-bayan", "taman-kheng-kooi", "taman-wee-hee-toy",
    "desas-krystal", "desas-indah", "sungai-nibong", "taman-sri-nibong", "taman-pelangi",
    "taman-century", "taman-bkt-mertajam", "taman-indah", "taman-permai", "taman-sejahtera",
    "taman-jaya", "taman-meru", "taman-seri-maju", "taman-sentosa", "taman-mutiara"
]

domain = "https://partition.htkdecor.com.my"

# 2. 读取根目录的 index.html 模板
if not os.path.exists("index.html"):
    print("未找到 index.html 模板文件！请确保当前目录下有 index.html")
    exit(1)

with open("index.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# 移除模板中可能残留的 {{REGION_LINKS}} 占位符
base_template = template_content.replace("{{REGION_LINKS}}", "")

# 主页保持 index.html 原样（不作替换），直接写入
with open("index.html", "w", encoding="utf-8") as f:
    f.write(base_template)

# 4. 循环创建 100 个子地区文件夹，并为每个子页面定制专属 H1 和 H2 标题
total_regions = len(regions)
for i, region in enumerate(regions):
    os.makedirs(region, exist_ok=True)
    
    r_title_clean = region.replace("-", " ").title()
    region_title = r_title_clean + ", Penang"
    
    # 子页面专属的 H1 标题内容
    sub_h1_title = f"{r_title_clean} Partition 017-431 5233 Call"
    
    related_indices = [(i + step) % total_regions for step in range(1, 6)]
    sub_links_html = '<div class="row row-cols-2 row-cols-md-5 g-2 mt-3 justify-content-center">\n'
    for idx in related_indices:
        r_item = regions[idx]
        r_name = r_item.replace("-", " ").title()
        sub_links_html += f'    <div class="col"><a href="{domain}/{r_item}/" class="btn btn-sm btn-outline-primary w-100 text-truncate">{r_name}</a></div>\n'
    sub_links_html += '</div>\n'
    
    sub_section = f'''
    <section class="py-4 bg-light border-top">
        <div class="container text-center">
            <h6 class="fw-bold mb-2 text-dark">Other Serviced Areas Near {r_title_clean}:</h6>
            {sub_links_html}
        </div>
    </section>
    '''
    
    # 针对子页面，动态替换模板中的 H1 和大标题，同时把 H2 改为 Expert Partition Service
    sub_base_template = base_template.replace(
        '<h1 class="display-4 fw-bold mb-4">Office Partition in Penang</h1>',
        f'<h1 class="display-4 fw-bold mb-4">{sub_h1_title}</h1>'
    ).replace(
        '<h2 class="fw-bold mb-3">Expert Partition Services in Penang</h2>',
        '<h2 class="fw-bold mb-3">Expert Partition Service</h2>'
    )
    
    sub_page_content = sub_base_template.replace("{{REGION}}", region_title)
    if "</main>" in sub_page_content:
        sub_page_content = sub_page_content.replace("</main>", f"{sub_section}\n</main>")
    else:
        sub_page_content += sub_section
        
    with open(f"{region}/index.html", "w", encoding="utf-8") as f:
        f.write(sub_page_content)

# 5. 自动生成 sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_content += f'  <url><loc>{domain}/</loc></url>\n'

for region in regions:
    sitemap_content += f'  <url><loc>{domain}/{region}/</loc></url>\n'

sitemap_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print("🎉 子页面标题已成功更新：顶部 H1 改为地区+电话，正文 H2 改为 Expert Partition Service！")
