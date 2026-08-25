# -*- coding: utf-8 -*-
import re, io, os

BASE = os.path.dirname(os.path.abspath(__file__))
tpl_path = os.path.join(BASE, 'e3z-d61.html')
tpl = open(tpl_path, encoding='utf-8').read()

# ---------- 产品数据 ----------
products = [
{
 'file': 'e3z-t61.html',
 'title': 'OMRON E3Z-T61 Through-beam Photoelectric Sensor 15m NPN',
 'img': 'images/e3z-t61.jpg',
 'img_alt': 'OMRON E3Z-T61 Through-beam Photoelectric Sensor 15m Front View',
 'h2': 'OMRON E3Z-T61 Through-beam Photoelectric Sensor 15m',
 'desc': 'Brand new original OMRON through-beam photoelectric sensor (emitter + receiver set) for long-range detection up to 15m. Ideal for belt conveyors, door/gate detection and long-distance automation. 12-24VDC, NPN output.',
 'desc2': 'This E3Z-T61 (OMRON) is a complete emitter/receiver pair supplied brand new and ready to ship worldwide. Contact us for bulk pricing or to confirm current stock.',
 'specs': [
   ['Model', 'E3Z-T61'],
   ['Sensing method', 'Through-beam (emitter + receiver)'],
   ['Sensing distance', '15m'],
   ['Output type', 'NPN'],
   ['Supply voltage', 'DC 12-24V'],
   ['Light source', 'Infrared LED'],
   ['Operation', 'Light-ON / Dark-ON (switchable)'],
   ['Connection', '2m pre-wired cable (each unit)'],
   ['Response time', '1ms'],
   ['Protection', 'IP67'],
   ['Certification', 'CE · UL/cUL · RoHS'],
   ['Condition', 'Brand new, original OMRON product'],
   ['Price', 'US $45.99 with free international shipping'],
 ],
 'sku': 'E3Z-T61 (OMRON)', 'mpn': 'E3Z-T61 (OMRON)', 'price': '45.99',
 'url': 'https://tuochen-trade-website.vercel.app/e3z-t61.html',
},
{
 'file': 'cjx2-1210.html',
 'title': 'CHINT CJX2-1210 AC Contactor 12A 220V 3P 1NO',
 'img': 'images/cjx2-1210.jpg',
 'img_alt': 'CHINT CJX2-1210 AC Contactor 12A Front View',
 'h2': 'CHINT CJX2-1210 AC Contactor 12A 3P 220V',
 'desc': 'Brand new original CHINT CJX2-1210 AC contactor, 12A rated current, 3 poles, for motor starting and control circuits. Standard motor control building block, pairs with NR2 thermal overload relay. 220V/380V AC coil, IEC/EN 60947-4-1.',
 'desc2': 'This CHINT CJX2-1210 (CHINT) is supplied brand new and ready to ship worldwide. Contact us for bulk pricing or to confirm current stock.',
 'specs': [
   ['Model', 'CJX2-1210'],
   ['Brand', 'CHINT (Zheng Tai)'],
   ['Rated current', '12A'],
   ['Poles', '3P'],
   ['Main contacts', '3NO'],
   ['Auxiliary contacts', '1NO'],
   ['Coil voltage', '220V / 380V AC (50Hz)'],
   ['Standard', 'IEC/EN 60947-4-1'],
   ['Condition', 'Brand new, original CHINT product'],
   ['Price', 'US $28.00 with free international shipping'],
 ],
 'sku': 'CJX2-1210 (CHINT)', 'mpn': 'CJX2-1210 (CHINT)', 'price': '28.00',
 'url': 'https://tuochen-trade-website.vercel.app/cjx2-1210.html',
},
{
 'file': 'nr2-25.html',
 'title': 'CHINT NR2-25 Thermal Overload Relay 7-10A',
 'img': 'images/nr2-25.jpg',
 'img_alt': 'CHINT NR2-25 Thermal Overload Relay Front View',
 'h2': 'CHINT NR2-25 Thermal Overload Relay',
 'desc': 'Brand new original CHINT NR2-25 thermal overload relay for three-phase motor overload protection. Adjustable current range, ideal partner for CJX2 contactors in standard motor starters. IP20, IEC/EN 60947-4-1.',
 'desc2': 'This CHINT NR2-25 (CHINT) is supplied brand new and ready to ship worldwide. Contact us for bulk pricing or to confirm current stock.',
 'specs': [
   ['Model', 'NR2-25'],
   ['Brand', 'CHINT (Zheng Tai)'],
   ['Function', 'Three-phase motor overload & phase-failure protection'],
   ['Current range', 'Adjustable (e.g. 7-10A / 12-18A)'],
   ['Use with', 'CJX2 contactor (motor starter combo)'],
   ['Standard', 'IEC/EN 60947-4-1'],
   ['Condition', 'Brand new, original CHINT product'],
   ['Price', 'US $32.00 with free international shipping'],
 ],
 'sku': 'NR2-25 (CHINT)', 'mpn': 'NR2-25 (CHINT)', 'price': '32.00',
 'url': 'https://tuochen-trade-website.vercel.app/nr2-25.html',
},
{
 'file': 'kg316t.html',
 'title': 'CHINT KG316T Time Relay Timer Switch 220V 16 Groups',
 'img': 'images/kg316t.jpg',
 'img_alt': 'CHINT KG316T Time Relay Timer Switch Front View',
 'h2': 'CHINT KG316T Time Relay Timer Switch',
 'desc': 'Brand new original CHINT KG316T programmable time relay / timer switch. 16 groups of on/off settings per week, AC 220V/380V 50/60Hz, ±2s/day accuracy, battery-backed memory for power-off retention. For lighting, street lamps and schedule control.',
 'desc2': 'This CHINT KG316T (CHINT) is supplied brand new and ready to ship worldwide. Contact us for bulk pricing or to confirm current stock.',
 'specs': [
   ['Model', 'KG316T'],
   ['Brand', 'CHINT (Zheng Tai)'],
   ['Supply voltage', 'AC 220V / 380V, 50/60Hz'],
   ['Program', '16 groups of on/off timers per week'],
   ['Time range', '1 minute to 168 hours'],
   ['Accuracy', '±2 seconds / day'],
   ['Memory', 'AAA battery for power-off backup'],
   ['Contacts', '1NO'],
   ['Contact rating', 'AC-15 240V/3A · AC-12 240V/30A'],
   ['Standard', 'IEC/EN 60947-5-1'],
   ['Condition', 'Brand new, original CHINT product'],
   ['Price', 'US $28.00 with free international shipping'],
 ],
 'sku': 'KG316T (CHINT)', 'mpn': 'KG316T (CHINT)', 'price': '28.00',
 'url': 'https://tuochen-trade-website.vercel.app/kg316t.html',
},
{
 'file': 'jqx-13f.html',
 'title': 'JQX-13F Intermediate Relay 12V/24V DC 2NO 2NC + Base',
 'img': 'images/jqx-13f.jpg',
 'img_alt': 'JQX-13F Intermediate Relay Front View',
 'h2': 'JQX-13F Intermediate Relay with Base',
 'desc': 'Brand new JQX-13F general purpose intermediate relay, compact DPDT with 2NO/2NC contacts. Coil options 12V/24V DC or 24V/220V AC. Supplied with matching socket base for easy wiring in control panels.',
 'desc2': 'This JQX-13F relay (with base) is supplied brand new and ready to ship worldwide. Contact us for bulk pricing or to confirm current stock.',
 'specs': [
   ['Model', 'JQX-13F'],
   ['Type', 'General purpose intermediate relay (DPDT)'],
   ['Contacts', '2NO / 2NC (double-pole changeover)'],
   ['Coil voltage', '12V / 24V DC or 24V / 220V AC (selectable)'],
   ['Socket base', 'Included (matching plug-in base)'],
   ['Use', 'Control panels, automation, isolation switching'],
   ['Condition', 'Brand new'],
   ['Price', 'US $14.00 with free international shipping'],
 ],
 'sku': 'JQX-13F (+ base)', 'mpn': 'JQX-13F (+ base)', 'price': '14.00',
 'url': 'https://tuochen-trade-website.vercel.app/jqx-13f.html',
},
]

def build_specs_li(specs):
    out = []
    for k, v in specs:
        out.append('                            <li><strong>{}</strong> {}</li>'.format(k, v))
    return '\n'.join(out)

def build_page(p):
    html = tpl
    # 替换 title
    html = html.replace('OMRON E3Z-D61 2M NPN Diffuse Reflective Photoelectric Sensor 100mm | Tuochen Trade', p['title'] + ' | Tuochen Trade')
    # 替换 meta description（用一个短描述）
    html = html.replace('Brand new original OMRON diffuse reflective photoelectric sensor, wide beam for short-range detection. Ideal for packaging, material handling and general automation. 12-24VDC, NPN output.', p['desc'])
    # JSON-LD name
    html = html.replace('"name": "OMRON E3Z-D61 2M NPN Diffuse Reflective Photoelectric Sensor 100mm"', '"name": "' + p['h2'] + '"')
    html = html.replace('"sku": "E3Z-D61 2M (OMRON)"', '"sku": "' + p['sku'] + '"')
    html = html.replace('"mpn": "E3Z-D61 2M (OMRON)"', '"mpn": "' + p['mpn'] + '"')
    html = html.replace('https://tuochen-trade-website.vercel.app/images/e3z-d61.jpg', 'https://tuochen-trade-website.vercel.app/' + p['img'])
    html = html.replace('"price": "42.99"', '"price": "' + p['price'] + '"')
    html = html.replace('https://tuochen-trade-website.vercel.app/e3z-d61.html', p['url'])
    # description in JSON-LD (reuse desc)
    html = html.replace('"description": "Brand new original OMRON diffuse reflective photoelectric sensor, wide beam for short-range detection. Ideal for packaging, material handling and general automation. 12-24VDC, NPN output."', '"description": "' + p['desc'] + '"')
    # H1
    html = html.replace('OMRON E3Z-D61 2M NPN Diffuse Reflective Photoelectric Sensor 100mm', p['h2'])
    # 面包屑 current
    html = html.replace('aria-current="page">OMRON E3Z-D61 2M NPN Diffuse Reflective Photoelectric Sensor 100mm', 'aria-current="page">' + p['h2'])
    # 图片
    html = html.replace('images/e3z-d61.jpg', p['img'])
    html = html.replace('OMRON E3Z-D61 2M NPN Diffuse Reflective Photoelectric Sensor 100mm Front View', p['img_alt'])
    # 规格列表替换：整段替换
    # 用正则把 <ul class="product-specs">...</ul> 替换
    m = re.search(r'<ul class="product-specs">.*?</ul>', html, flags=re.S)
    if m:
        new_ul = '<ul class="product-specs">\n' + build_specs_li(p['specs']) + '\n                        </ul>'
        html = html[:m.start()] + new_ul + html[m.end():]
    else:
        print('WARN: specs ul not found for', p['file'])
    # 替换 h2（产品卡内标题）
    # 用 replace 上限：把第一个出现的产品名(无价格)的 h2 —— 直接替换 h2 名称
    html = html.replace('>OMRON E3Z-D61 2M NPN Diffuse Reflective Photoelectric Sensor 100mm</h2>', '>' + p['h2'] + '</h2>')
    # desc2（This E3Z-D61 2M...）
    html = html.replace('This E3Z-D61 2M (OMRON) is a OMRON unit supplied brand new and ready to ship worldwide. Contact us for bulk pricing or to confirm current stock.', p['desc2'])
    # 价格行在规格里已处理
    out = os.path.join(BASE, p['file'])
    open(out, 'w', encoding='utf-8', newline='\n').write(html)
    print('OK', p['file'])

for p in products:
    build_page(p)
print('DONE', len(products))
