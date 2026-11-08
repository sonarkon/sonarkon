F = "node_modules/@fontsource"
HEAD = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Fraunces;font-weight:600;src:url({F}/fraunces/files/fraunces-latin-600-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:400;src:url({F}/inter/files/inter-latin-400-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:600;src:url({F}/inter/files/inter-latin-600-normal.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:800px;height:400px;overflow:hidden}}
body{{font-family:Inter,sans-serif;color:#ececee;position:relative;
 background:radial-gradient(520px 340px at 76% 50%,{{glow}} 0%,rgba(23,24,27,0) 65%),#17181b}}
.l{{position:absolute;left:52px;top:62px;width:340px}}
.over{{font:600 12px Inter;letter-spacing:.2em;color:{{acc}}}}
h1{{font:600 50px/1.03 Fraunces,serif;letter-spacing:-.02em;margin-top:12px}}
p{{font:400 16.5px/1.45 Inter;color:#c9cad0;margin-top:16px}}
.tags{{margin-top:20px;display:flex;flex-wrap:wrap;gap:8px}}
.tags span{{font:600 12px Inter;color:{{acc}};background:{{accbg}};padding:4px 10px;border-radius:20px}}
.mono{{font-family:"DejaVu Sans Mono",monospace}}
{{css}}
</style></head><body>
<div class="l"><div class="over">{{over}}</div><h1>{{title}}</h1><p>{{desc}}</p>
<div class="tags">{{tags}}</div></div>
{{visual}}
</body></html>"""

CARDS = {
 "hope-tv": dict(
  acc="#ffa24a", accbg="rgba(255,162,74,.13)", glow="#3a2a1c",
  over="HARDWARE · ESP8266 · OSC", title="HOPE TV",
  desc="A tiny Wi-Fi “TV” with a 1.44″ display: test patterns, static, clip playlists and slideshows – all remote-controlled over OSC.",
  tags=["Wemos D1 mini", "ST7735", "OSC"],
  css="""
.tv{position:absolute;right:70px;top:104px;width:300px;height:250px;background:linear-gradient(160deg,#4a3b2e,#2b231c);
 border-radius:28px;box-shadow:0 26px 60px rgba(0,0,0,.6),inset 0 2px 0 rgba(255,255,255,.08);transform:rotate(-2deg)}
.scr{position:absolute;left:26px;top:28px;width:194px;height:194px;border-radius:18px;overflow:hidden;
 background:#000;box-shadow:inset 0 0 22px rgba(0,0,0,.9),0 0 0 6px #1b1612}
.scr img{width:100%;height:100%;image-rendering:pixelated;filter:saturate(1.1) contrast(1.05)}
.scr:after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.18) 0 2px,transparent 2px 4px);
 box-shadow:inset 0 0 40px rgba(0,0,0,.55)}
.k{position:absolute;right:26px;width:34px;height:34px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#8a7a68,#3a3028);
 box-shadow:0 2px 4px rgba(0,0,0,.5)}
.k1{top:46px}.k2{top:100px}
.grill{position:absolute;right:28px;top:156px;width:30px;height:60px;background:repeating-linear-gradient(0deg,#1a1511 0 3px,transparent 3px 7px)}
.ant{position:absolute;width:3px;height:74px;background:#9a8d7e;top:-68px;left:148px;transform-origin:bottom}
.a1{transform:rotate(-28deg)}.a2{transform:rotate(24deg)}
.leg{position:absolute;bottom:-16px;width:16px;height:18px;background:#2b231c;border-radius:0 0 4px 4px}
.leg1{left:50px}.leg2{right:50px}""",
  visual="""<div class="tv"><div class="ant a1"></div><div class="ant a2"></div>
<div class="scr"><img src="moon.jpg"></div><div class="k k1"></div><div class="k k2"></div><div class="grill"></div>
<div class="leg leg1"></div><div class="leg leg2"></div></div>"""),
 "airplay-onkyo": dict(
  acc="#5ad19a", accbg="rgba(90,209,154,.12)", glow="#1c3a2e",
  over="HARDWARE · ESP32 · AIRPLAY", title="AirPlay ESP32<br>for Onkyo",
  desc="Turns an Onkyo R-1045DAB receiver into an AirPlay 2 speaker – with RI-bus control and Home Assistant integration.",
  tags=["AirPlay 2", "RI bus", "Fork"],
  css="""
.rcv{position:absolute;right:46px;top:96px;width:350px;height:118px;border-radius:10px;
 background:linear-gradient(180deg,#3a3c42,#24262b 55%,#1c1d21);box-shadow:0 24px 56px rgba(0,0,0,.6),inset 0 1px 0 rgba(255,255,255,.12)}
.disp{position:absolute;left:84px;top:30px;width:170px;height:44px;background:#071311;border-radius:4px;
 box-shadow:inset 0 0 10px rgba(0,0,0,.9);padding:6px 10px;color:#6ff3c4;font:13px/1.35 "DejaVu Sans Mono",monospace;
 text-shadow:0 0 6px rgba(111,243,196,.6)}
.knob{position:absolute;right:22px;top:24px;width:66px;height:66px;border-radius:50%;
 background:radial-gradient(circle at 38% 32%,#6b6e76,#2a2c31 70%);box-shadow:0 3px 8px rgba(0,0,0,.6)}
.pw{position:absolute;left:22px;top:44px;width:14px;height:14px;border-radius:50%;background:#2a2c31;box-shadow:0 0 0 2px #444}
.pw:after{content:"";position:absolute;left:4px;top:4px;width:6px;height:6px;border-radius:50%;background:#5ad19a;box-shadow:0 0 6px #5ad19a}
.foot{position:absolute;bottom:-8px;width:40px;height:8px;background:#151619;border-radius:0 0 4px 4px}.f1{left:30px}.f2{right:30px}
.pcb{position:absolute;right:120px;top:256px;width:170px;height:70px;background:linear-gradient(160deg,#1f6b4a,#145036);border-radius:6px;
 box-shadow:0 14px 30px rgba(0,0,0,.55);transform:rotate(-3deg)}
.chip{position:absolute;left:20px;top:14px;width:58px;height:42px;background:linear-gradient(#c9ccd2,#9da1a8);border-radius:3px}
.pins{position:absolute;left:8px;right:8px;height:5px;background:repeating-linear-gradient(90deg,#d4b45a 0 4px,transparent 4px 9px)}
.pt{top:3px}.pb{bottom:3px}
.lbl{position:absolute;right:14px;top:24px;font:600 11px Inter;color:#bfe9d4;letter-spacing:.08em}
.cable{position:absolute;right:202px;top:206px;width:3px;height:60px;background:#6b6e76;border-radius:2px;transform:rotate(8deg)}""",
  visual="""<div class="rcv"><div class="pw"></div><div class="disp">AirPlay ▸ CD/COAX<br>♪ now playing</div>
<div class="knob"></div><div class="foot f1"></div><div class="foot f2"></div></div>
<div class="cable"></div>
<div class="pcb"><div class="pins pt"></div><div class="pins pb"></div><div class="chip"></div><div class="lbl">ESP32-S3</div></div>"""),
 "slop-assistant": dict(
  acc="#5cc6f5", accbg="rgba(92,198,245,.12)", glow="#1b3242",
  over="SMART HOME · HOME ASSISTANT", title="Slop-Assistant",
  desc="Home Assistant blueprints and ESPHome configs – smooth dimming on an IKEA scroll wheel, an Onkyo RI bridge and more. Vibe-coded with Claude.",
  tags=["Blueprints", "ESPHome", "YAML"],
  css="""
.win{position:absolute;right:44px;top:58px;width:356px;height:284px;background:#0e0f11;border-radius:12px;
 box-shadow:0 24px 60px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.07);transform:rotate(1.4deg);overflow:hidden}
.bar{height:30px;background:#1d1e22;display:flex;align-items:center;gap:7px;padding-left:12px;font:12px Inter;color:#777}
.bar i{width:11px;height:11px;border-radius:50%;background:#3a3b41;display:block}
pre{font:13px/1.62 "DejaVu Sans Mono",monospace;color:#b9bbc2;padding:14px 18px;white-space:pre}
.k{color:#5cc6f5}.s{color:#e8c37a}.c{color:#6a6d75}
.dial{position:absolute;right:30px;bottom:30px;width:92px;height:92px;border-radius:50%;
 background:radial-gradient(circle at 40% 35%,#f4f1ea,#cfc9bd 70%);box-shadow:0 14px 30px rgba(0,0,0,.6);
 border:6px solid #e7e2d8}
.dial:after{content:"";position:absolute;inset:18px;border-radius:50%;border:2px dashed rgba(0,0,0,.18)}""",
  visual="""<div class="win"><div class="bar"><i></i><i></i><i></i></div>
<pre><span class="k">blueprint</span>:
  <span class="k">name</span>: <span class="s">Onkyo Bridge –</span>
        <span class="s">Power &amp; Input Sync</span>
  <span class="k">domain</span>: automation
<span class="c"># TV on      → optical in</span>
<span class="c"># turntable  → LINE 1</span>
<span class="c"># AirPlay    → CD/COAX</span>
<span class="c"># all idle   → ri-off</span></pre></div>
<div class="dial"></div>"""),
 "tba-builder": dict(
  acc="#b48cff", accbg="rgba(180,140,255,.12)", glow="#2c2440",
  over="INTERACTIVE · UNITY · C#", title="TBA Builder<br>for Flintridge",
  desc="Pop's text-adventure builder, customised for Flintridge / Holodeck: German language, extOSC control and other tweaks.",
  tags=["Text adventure", "extOSC", "Fork"],
  css="""
.term{position:absolute;right:44px;top:58px;width:350px;height:284px;background:#0e0f11;border-radius:12px;
 box-shadow:0 24px 60px rgba(0,0,0,.55),0 0 0 1px rgba(255,255,255,.07);transform:rotate(1.4deg);overflow:hidden}
.bar{height:30px;background:#1d1e22;display:flex;align-items:center;gap:7px;padding-left:12px}
.bar i{width:11px;height:11px;border-radius:50%;background:#3a3b41;display:block}
.body{position:absolute;inset:30px 0 0 0;background:#000;display:flex;flex-direction:column;justify-content:flex-end;padding:22px}
.t{font:16px/1.55 "DejaVu Sans Mono",monospace;color:#e6e6e6}
.in{margin-top:14px;font:16px "DejaVu Sans Mono",monospace;color:#8b8d94;border-top:1px solid #2a2b30;padding-top:12px}
.in b{color:#7fe0a8;font-weight:400}
.cur{display:inline-block;width:9px;height:17px;background:#7fe0a8;vertical-align:-3px;margin-left:3px}
.osc{position:absolute;right:16px;top:44px;font:600 11px Inter;color:#b48cff;background:rgba(180,140,255,.12);padding:3px 8px;border-radius:10px}""",
  visual="""<div class="term"><div class="bar"><i></i><i></i><i></i></div>
<div class="osc">OSC ●</div>
<div class="body"><div class="t">Text go here</div><div class="in"><b>&gt;</b> Enter text…<span class="cur"></span></div></div></div>"""),
}

for name, c in CARDS.items():
    h = HEAD
    for k in ("acc", "accbg", "glow", "over", "title", "desc", "css", "visual"):
        h = h.replace("{" + k + "}", c[k])
    h = h.replace("{tags}", "".join(f"<span>{t}</span>" for t in c["tags"]))
    open(f"{name}.html", "w").write(h)
print("ok")
