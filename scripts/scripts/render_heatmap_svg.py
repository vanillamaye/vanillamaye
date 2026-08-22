import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

with open("data/contributions.json") as f:
    days = json.load(f)

svg_rects = []
for idx, day in enumerate(days[-371:]):  # last 53 weeks
    col = idx // 7
    row = idx % 7
    x = 15 + col * 15
    y = 35 + row * 15
    color = PALETTE[min(day["level"], len(PALETTE) - 1)]
    delay = (col * 7 + row) * 0.003
    svg_rects.append(
        f'<rect x="{x}" y="{y}" width="11" height="11" rx="2" fill="{color}" '
        f'style="animation: slideIn 0.4s ease forwards {delay:.3f}s; opacity: 0; transform: translateY(6px);"/>'
    )

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 170" width="860" height="170">
<style>
  @keyframes slideIn {{
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  .bg {{ fill: #0d1117; rx: 8px; }}
  .title {{ fill: #58a6ff; font-family: monospace; font-size: 13px; font-weight: bold; }}
</style>
<rect width="860" height="170" class="bg"/>
<text x="15" y="22" class="title">vanillamaye@github ~ $ git log --graph --contributions</text>
{"".join(svg_rects)}
</svg>"""

with open("contrib-heatmap.svg", "w") as f:
    f.write(svg_content)

print("Generated contrib-heatmap.svg successfully!")
