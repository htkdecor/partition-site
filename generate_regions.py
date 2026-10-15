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

# 3. 制作【主页】专属的 100 个地区完整链接 HTML（默认隐藏在折叠面板内）
all_links_html = '<div class="row row-cols-2 row-cols-md-4 row-cols-lg-5 g-2">\n'
for region in regions:
    r_name = region.replace("-", " ").title()
    all_links_html += f'    <div class="col"><a href="{domain}/{region}/" class="btn btn-sm btn-outline-secondary w-100 text-truncate">{r_name}</a></div>\n'
all_links_html += '</div>\n'

home_section = f'''
<section class="py-5 bg-light border-top">
    <div class="container text-center">
        <h4 class="fw-bold mb-3 text-dark">Serviced Areas in Penang</h4>
        <p class="text-muted small mb-3">We provide professional office partition services across all major districts and industrial parks in Penang:</p>
        
        <!-- 点击后可展开/收起的按钮 -->
        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#allServicedAreas" aria-expanded="false" aria-controls="allServicedAreas">
            Show All Serviced Areas (查看所有服务地区)
        </button>
        
        <!-- 默认折叠隐藏的 100 个地区链接区块 -->
        <div class="collapse mt-3" id="allServicedAreas">
            {all_links_html}
        </div>
    </div>
</section>
'''

# 写入主页 index.html
home_content = base_template.replace("{{REGION}}", "Penang")
if "</main>" in home_content:
    home_content = home_content.replace("</main>", f"{home_section}\n</main>")
else:
    home_content += home_section

with open("index.html", "w", encoding="utf-8") as f:
    f.write(home_content)

# 4. 循环创建 100 个子地区文件夹，并为每个子页面定制专属 H2 标题
total_regions = len(regions)
for i, region in enumerate(regions):
    os.makedirs(region, exist_ok=True)
    
    r_title_clean = region.replace("-", " ").title()
    region_title = r_title_clean + ", Penang"
    
    # 【核心定制】每个子页面的专属 H2 主标题
    sub_h2_title = f"{r_title_clean} Partition 017-431 5233 Call"
    
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
    
    # 针对子页面，动态替换模板中的 Expert 标题为该地区专属标题
    sub_base_template = base_template.replace(
        '<h2 class="fw-bold mb-3">Expert Partition Services in Penang</h2>',
        f'<h2 class="fw-bold mb-3">{sub_h2_title}</h2>'
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

print("🎉 主页折叠隐藏、100个子页面专属标题（带名称与电话）生成完毕！")
