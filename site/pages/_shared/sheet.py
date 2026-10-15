import sys, glob, os
from PIL import Image
slug, w = sys.argv[1], sys.argv[2]
d = f'/workspace/pages/{slug}/shots/'
names = sorted({os.path.basename(f).rsplit('-', 2)[0] for f in glob.glob(d + f'??-*-{w}-a.png')})
os.makedirs(d + 'sheets', exist_ok=True)
for n in names:
    a = Image.open(f'{d}{n}-{w}-a.png'); b = Image.open(f'{d}{n}-{w}-b.png')
    W = a.width + b.width + 10; H = max(a.height, b.height)
    im = Image.new('RGB', (W, H), (40, 40, 40)); im.paste(a, (0, 0)); im.paste(b, (a.width + 10, 0))
    im.save(f'{d}sheets/{n}-{w}.png')
print(names)
