# -*- coding: utf-8 -*-

import re

html="<script>var datas=(FonHen_JieMa('*104*116*116*112*58*47*47*97*117*100*105*111*46*120*109*99*100*110*46*99*111*109*47*103*114*111*117*112*50*50*47*77*48*49*47*50*53*47*51*70*47*119*75*103*74*77*49*103*101*115*51*105*103*71*85*75*122*65*70*99*65*67*106*99*116*76*118*48*57*50*54*46*109*52*97*38*49*50*50*48*38*109*52*97').split('&'));var datas2 = ''; var part='特种兵在都市-第1258章'; var play_vid='4094';</script>"
#print chr(116)
m = re.search(u"FonHen_JieMa\('([0-9,*]*)'\)", html);
print m.group(0)

pattern = re.compile(r'FonHen_JieMa')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match(html)
print match

if match:
    # 使用Match获得分组信息
    print match.group()
