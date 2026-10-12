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

# 2. 读取根目录的 index.html 作为模版
if not os.path.exists("index.html"):
    print("未找到 index.html 模板文件！")
    exit(1)

with open("index.html", "r", encoding="utf-8") as f:
    template_content = f.read()

# 3. 循环创建 100 个地区文件夹并生成对应的 index.html
for region in regions:
    os.makedirs(region, exist_ok=True)
    region_title = region.replace("-", " ").title() + ", Penang"
    page_content = template_content.replace("{{REGION}}", region_title)
    
    with open(f"{region}/index.html", "w", encoding="utf-8") as f:
        f.write(page_content)
    
    print(f"已生成槟城细分页面: {region}/index.html")

# 4. 自动生成包含这 100 个地区的 sitemap.xml
domain = "https://partition.htkdecor.com.my"
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_content += f'  <url><loc>{domain}/</loc></url>\n'

for region in regions:
    sitemap_content += f'  <url><loc>{domain}/{region}/</loc></url>\n'

sitemap_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print("100个槟城地区的 sitemap.xml 生成成功！")
