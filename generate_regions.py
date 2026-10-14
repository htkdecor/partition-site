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

# 2. 读取根目录的 index.html 作为模版
if not os.path.exists("index.html"):
    print("未找到 index.html 模板文件！")
    exit(1)

with open("index.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# 3. 动态生成 100 个地区的 HTML 链接 HTML 代码块
links_html = '<div class="row row-cols-2 row-cols-md-4 row-cols-lg-5 g-2 mt-3">\n'
for region in regions:
    region_display_name = region.replace("-", " ").title()
    links_html += f'    <div class="col"><a href="{domain}/{region}/" class="btn btn-sm btn-outline-secondary w-100 text-truncate">{region_display_name}</a></div>\n'
links_html += '</div>\n'

# 如果 index.html 里面有 {{REGION_LINKS}} 占位符就替换；如果没有，自动拼接到 </main> 前面
if "{{REGION_LINKS}}" in template_content:
    template_content = template_content.replace("{{REGION_LINKS}}", links_html)
else:
    section_html = f'''
    <section class="py-5 bg-light border-top">
        <div class="container text-center">
            <h4 class="fw-bold mb-3 text-dark">Serviced Areas in Penang</h4>
            <p class="text-muted small">We provide professional office partition services across all major districts and industrial parks in Penang:</p>
            {links_html}
        </div>
    </section>
    '''
    if "</main>" in template_content:
        template_content = template_content.replace("</main>", f"{section_html}\n</main>")
    else:
        template_content += section_html

# 4. 循环创建 100 个地区文件夹并生成对应的 index.html
for region in regions:
    os.makedirs(region, exist_ok=True)
    region_title = region.replace("-", " ").title() + ", Penang"
    page_content = template_content.replace("{{REGION}}", region_title)
    
    with open(f"{region}/index.html", "w", encoding="utf-8") as f:
        f.write(page_content)

# 5. 自动生成包含这 100 个地区的 sitemap.xml
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_content += f'  <url><loc>{domain}/</loc></url>\n'

for region in regions:
    sitemap_content += f'  <url><loc>{domain}/{region}/</loc></url>\n'

sitemap_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print("包含 100 个地区页面链接的 HTML 与 sitemap.xml 已全部成功重新生成！")
