"""소스(src/*.src.html) + 폰트 + 아이콘 → 단일 HTML 빌드.
사용: python3 tools/build.py   (pip install fonttools brotli 필요)
 - src/demo.iphone.src.html  → index.html   (iPhone 16 Pro 풀스크린, GitHub Pages 기본 페이지)
 - src/demo.desktop.src.html → desktop.html (PC 발표용, 설명 패널 포함)"""
import base64, io, os
from fontTools import subset
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=lambda *a: os.path.join(ROOT,*a)
icons=open(P('assets','icons.json'),encoding='utf-8').read()
def faces(text):
    chars=set(text)|set(chr(c) for c in range(0x20,0x7f))|set(chr(c) for c in range(0xAC00,0xD7A4))
    chars|=set('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ…·→←↑↓↕↺‘’“”—–•')
    out=[]
    for w,name in [(400,'400Regular'),(600,'600SemiBold'),(700,'700Bold')]:
        opt=subset.Options(); opt.flavor='woff2'; opt.layout_features=['*']; opt.hinting=False; opt.desubroutinize=True
        f=subset.load_font(P('fonts','OneUISansGUI-%s.ttf'%name),opt); ss=subset.Subsetter(opt)
        ss.populate(unicodes=[ord(c) for c in chars if len(c)==1]); ss.subset(f)
        b=io.BytesIO(); subset.save_font(f,b,opt)
        out.append("@font-face{font-family:'One UI Sans GUI';font-weight:%d;font-style:normal;font-display:block;src:url(data:font/woff2;base64,%s) format('woff2')}"%(w,base64.b64encode(b.getvalue()).decode()))
    return '\n'.join(out)
for src,dst in [('demo.iphone.src.html','index.html'),('demo.desktop.src.html','desktop.html')]:
    s=open(P('src',src),encoding='utf-8').read()
    html=s.replace('/*FONTFACE*/',faces(s+icons)).replace('/*ICONS*/',icons)
    open(P(dst),'w',encoding='utf-8').write(html); print(dst,len(html))
