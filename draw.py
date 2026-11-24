#!/usr/bin/env python3
"""Draw the 24 November 2026 front page: 'THE WORLD TODAY'.
Deterministic PIL render, 1024x1024, no timestamps, no randomness.
All 35 stories are dated Tuesday 24 November 2026 (see NOTES.md).
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (28, 52, 96)
TEAL = (14, 92, 84)
RULE = (120, 110, 92)
CARD_BG = (255, 252, 244)
FAINT = (90, 84, 72)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, w=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=w)


# ---------------------------------------------------------------- icons
def icon_plane(d, x, y, s, col=NAVY):
    # clean top-view jet: tapered fuselage, swept wings, tail fin
    d.polygon([(x + s * .05, y + s * .48), (x + s * .75, y + s * .4),
               (x + s * .97, y + s * .5), (x + s * .75, y + s * .6)],
              fill=col)
    d.polygon([(x + s * .45, y + s * .5), (x + s * .6, y + s * .15),
               (x + s * .7, y + s * .15), (x + s * .55, y + s * .5)],
              fill=col)
    d.polygon([(x + s * .45, y + s * .5), (x + s * .6, y + s * .85),
               (x + s * .7, y + s * .85), (x + s * .55, y + s * .5)],
              fill=col)
    d.polygon([(x + s * .1, y + s * .47), (x + s * .16, y + s * .22),
               (x + s * .24, y + s * .47)], fill=col)
    d.polygon([(x + s * .08, y + s * .52), (x + s * .14, y + s * .74),
               (x + s * .2, y + s * .52)], fill=col)


def icon_chess(d, x, y, s):
    cell = s / 4
    for r in range(4):
        for c in range(4):
            if (r + c) % 2 == 0:
                d.rectangle([x + c * cell, y + r * cell,
                             x + (c + 1) * cell, y + (r + 1) * cell], fill=INK)
    d.rectangle([x, y, x + s, y + s], outline=INK, width=2)
    d.ellipse([x + s * .62, y + s * .08, x + s * .86, y + s * .32], fill=RED)
    d.rectangle([x + s * .66, y + s * .3, x + s * .82, y + s * .42], fill=RED)


def icon_chip(d, x, y, s, col=TEAL):
    d.rectangle([x + s * .2, y + s * .2, x + s * .8, y + s * .8], fill=col)
    d.rectangle([x + s * .38, y + s * .38, x + s * .62, y + s * .62], fill=PAPER)
    for i in range(3):
        px = x + s * (.3 + i * .2)
        d.line([(px, y), (px, y + s * .2)], fill=col, width=3)
        d.line([(px, y + s * .8), (px, y + s)], fill=col, width=3)
        py = y + s * (.3 + i * .2)
        d.line([(x, py), (x + s * .2, py)], fill=col, width=3)
        d.line([(x + s * .8, py), (x + s, py)], fill=col, width=3)


def icon_graph(d, x, y, s, col=RED):
    d.line([(x, y + s * .85), (x + s, y + s * .85)], fill=INK, width=2)
    d.line([(x, y + s * .85), (x, y + s * .1)], fill=INK, width=2)
    pts = [(x + s * .05, y + s * .7), (x + s * .28, y + s * .55),
           (x + s * .48, y + s * .62), (x + s * .7, y + s * .3),
           (x + s * .95, y + s * .12)]
    d.line(pts, fill=col, width=4, joint="curve")
    for px, py in pts:
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=col)


def icon_rocket(d, x, y, s, col=NAVY):
    d.polygon([(x + s * .5, y), (x + s * .72, y + s * .42),
               (x + s * .72, y + s * .78), (x + s * .5, y + s * .68),
               (x + s * .28, y + s * .78), (x + s * .28, y + s * .42)],
              fill=col)
    d.ellipse([x + s * .42, y + s * .14, x + s * .58, y + s * .3], fill=PAPER)
    d.polygon([(x + s * .28, y + s * .62), (x + s * .08, y + s * .9),
               (x + s * .28, y + s * .78)], fill=RED)
    d.polygon([(x + s * .72, y + s * .62), (x + s * .92, y + s * .9),
               (x + s * .72, y + s * .78)], fill=RED)
    d.polygon([(x + s * .44, y + s * .72), (x + s * .56, y + s * .72),
               (x + s * .5, y + s)], fill=(230, 120, 30))


def icon_crowd(d, x, y, s, col=NAVY):
    # three heads over shoulders, no extra shapes
    for i, cx in enumerate((0.22, 0.5, 0.78)):
        cy = y + s * (.42 + (i % 2) * .1)
        d.ellipse([x + s * cx - 8, cy - 8, x + s * cx + 8, cy + 8], fill=col)
        d.pieslice([x + s * cx - 15, cy + 6, x + s * cx + 15, cy + 34],
                   180, 360, fill=col)


def icon_factory(d, x, y, s, col=NAVY):
    d.rectangle([x + s * .08, y + s * .45, x + s * .92, y + s * .92], fill=col)
    d.polygon([(x + s * .08, y + s * .45), (x + s * .28, y + s * .25),
               (x + s * .48, y + s * .45)], fill=col)
    d.rectangle([x + s * .72, y + s * .1, x + s * .84, y + s * .5], fill=col)
    for wx in (0.18, 0.4, 0.62):
        d.rectangle([x + s * wx, y + s * .58, x + s * (wx + .1), y + s * .72],
                    fill=PAPER)
    d.ellipse([x + s * .78, y + s * .02, x + s * .9, y + s * .14], fill=RED)


def icon_drone_map(d, x, y, w, h):
    """Lead art: stylised map of Poland/Ukraine with a drone and path."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 236, 244),
                outline=NAVY, width=2)
    # landmass blobs, kept inside the frame
    d.polygon([(x + 20, y + 28), (x + 110, y + 12), (x + 190, y + 24),
               (x + 225, y + 52), (x + 200, y + 82), (x + 120, y + 88),
               (x + 50, y + 78), (x + 18, y + 54)], fill=(196, 214, 178))
    d.polygon([(x + 235, y + 36), (x + 296, y + 28), (x + 312, y + 66),
               (x + 288, y + 88), (x + 240, y + 84)], fill=(214, 196, 164))
    d.text((x + 22, y + 12), "POLAND", font=font(SANS_B, 13), fill=NAVY)
    d.text((x + 232, y + 56), "UKRAINE", font=font(SANS_B, 12), fill=NAVY)
    # dashed intrusion path, kept clear of the labels
    px, py = x + 296, y + 14
    for i in range(8):
        nx, ny = px - 15, py + 5
        d.line([(px, py), (nx, ny)], fill=RED, width=3)
        px, py = nx - 5, ny + 2
    # drone silhouette, above the caption strip, clear of the labels
    dx, dy = x + 150, y + 52
    d.ellipse([dx - 22, dy - 8, dx + 22, dy + 8], fill=INK)
    d.ellipse([dx - 30, dy - 16, dx - 12, dy - 2], outline=INK, width=2)
    d.ellipse([dx + 12, dy - 16, dx + 30, dy - 2], outline=INK, width=2)
    d.line([(dx - 30, dy - 9), (dx - 12, dy - 9)], fill=INK, width=2)
    d.line([(dx + 12, dy - 9), (dx + 30, dy - 9)], fill=INK, width=2)
    d.text((x + 12, y + h - 22), "RUSSIAN DRONE INCURSION",
           font=font(SANS_B, 11), fill=RED)


# ---------------------------------------------------------------- cards
# (kicker, colour, headline, deck, icon or None)
FEATURED = [
    ("ASIA", NAVY, "Russian jet sparks alert on Ulleung island",
     "Seoul: brief evacuation warning for Ulleung, lifted after 3 minutes.",
     "plane"),
    ("ASIA", NAVY, "Pyongyang may shut Swiss office in protest",
     "North Korea weighs closing Switzerland's Pyongyang mission over sanctions.",
     None),
    ("MIDDLE EAST", RED, "Gaza now a 'toxic wasteland', report says",
     "Oxfam & CEOBS: Israeli strikes polluted air, soil and water across Gaza.",
     None),
    ("SPORT", TEAL, "Youngest ever world title duel begins",
     "Gukesh v Sindarov, Game 1 in Geneva: 14 games, $2.5m prize at stake.",
     "chess"),
    ("ASIA", NAVY, "Modi opens AI hub at IIT Patna",
     "PM inaugurates AI centre and a Rs 400-crore research park project.",
     "chip"),
    ("TECH", TEAL, "Huang returns to Nvidia HQ to applause",
     "Chief welcomed back as shares surge; AI rally powers the stock higher.",
     "graph"),
    ("EUROPE", NAVY, "Moscow may launch nuclear-armed craft",
     "Germany's space command warns of a possible December orbital launch.",
     "rocket"),
    ("EUROPE", RED, "12,000 evacuated from UK concert",
     "Police clear venue after an 'unknown substance' is released in the crowd.",
     "crowd"),
    ("MIDDLE EAST", RED, "Houthi strike on Taiz kills two",
     "Attack in Yemen leaves two civilians dead and eight wounded.",
     None),
    ("ASIA", NAVY, "Search goes on at burnt candy factory",
     "Cikande, Indonesia: ~30 still missing after Saturday's blaze (update).",
     "factory"),
    ("EUROPE", NAVY, "Le Pen lists three Ukraine war paths",
     "French leader warns scenarios include a third world war.",
     None),
    ("EUROPE", RED, "Bomb threats hit 450 German schools",
     "Schools across Germany receive emailed threats in a single day.",
     None),
]

TICKER = [
    "Ukraine SBU claims ship strikes off Libya, near Benghazi",
    "Taliban erase women's names from official papers in Balkh",
    "WSJ: Kim Jong Un snubs Trump's bid to rebuild dialogue",
    "Haaretz: 23 Israeli soldiers died by suicide in 2026",
    "Russian strikes kill 4, incl. a child, wound 19 in Ukraine",
    "Russia hits oil sites in Tatarstan, Perm and Rostov",
    "Ukrainian troops make small gains in Kursk region",
    "Rutte: Russia's pre-1997 NATO demand 'unacceptable'",
    "Khodorkovsky: Russian subversion could drag Europe to war",
    "Iraq's leader arrives in Egypt on first official visit",
    "Litvinenko widow hopes for major trial, 20 years on",
    "India, China hold military talks in Arunachal Pradesh",
    "SCO: Pakistan invites India to culture ministers' meet",
    "Lahore tops world pollution list as AQI passes 500",
    "M4.0 quake shakes Pakistan near Afghan border",
    "Bangladesh: Yunus blames 'higher level' for Grameen attacks",
    "King Charles calls Meghan after her father's arrest",
    "Dutch trans activist Jason Bhugwandass dies at 28",
    "China: official sentenced to death for leaking 100 reports",
    "Kim Jong Un receives credentials from new India envoy",
    "O'Hare ground stop briefly amid Thanksgiving travel rush",
    "Mossad foiled ISIS plot on Taylor Swift's Vienna show",
]

NUMBERS = [
    ("12,000", "evacuated from UK concert"),
    ("450", "German schools threatened"),
    ("~30", "still missing in Cikande"),
    ("23", "IDF suicides in 2026"),
    ("$2.5m", "world chess prize"),
    ("500+", "Lahore AQI peak"),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 24
    right = W - mx

    # ---- masthead
    d.text((W // 2, 12), "THE WORLD TODAY", font=font(SERIF, 56),
           fill=INK, anchor="ma")
    d.text((W // 2, 74), "THE WORLD IN ONE PAGE  •  ALL STORIES DATED 24 NOVEMBER 2026",
           font=font(SANS_B, 12), fill=FAINT, anchor="ma")
    rule(d, mx, 96, right, 3)
    # ---- date bar
    d.text((W // 2, 106), "TUESDAY, 24 NOVEMBER 2026",
           font=font(SERIF, 34), fill=RED, anchor="ma")
    rule(d, mx, 150, right, 3)
    d.text((W // 2, 158), "35 STORIES  •  7 REGIONS  •  EUROPE  •  MIDDLE EAST  •  ASIA  •  AMERICAS  •  AFRICA  •  SPORT & SCIENCE  •  MARKETS & TECH",
           font=font(SANS_B, 11), fill=NAVY, anchor="ma")

    # ---- lead story
    ly, lh = 178, 118
    d.rectangle([mx, ly, right, ly + lh], fill=CARD_BG, outline=INK, width=2)
    d.text((mx + 14, ly + 8), "LEAD  •  EUROPE", font=font(SANS_B, 12), fill=RED)
    head = "Russian drone breaches Polish airspace in night raid on Ukraine"
    hl = wrap(d, head, font(SERIF, 25), 600)
    y = draw_lines(d, hl, mx + 14, ly + 26, font(SERIF, 25), INK, 27)
    deck = ("Warsaw briefly authorised shooting it down, then stood down, "
            "as Moscow struck western Ukraine overnight.")
    dl = wrap(d, deck, font(SANS, 13), 600)
    draw_lines(d, dl, mx + 14, y + 2, font(SANS, 13), FAINT, 16)
    icon_drone_map(d, right - 330, ly + 10, 316, lh - 20)

    # ---- featured grid: 3 cols x 4 rows
    gy, gh, gap = 304, 112, 7
    cw = (W - 2 * mx - 2 * gap) // 3
    icons = {"plane": icon_plane, "chess": icon_chess, "chip": icon_chip,
             "graph": icon_graph, "rocket": icon_rocket,
             "crowd": icon_crowd, "factory": icon_factory}
    for i, (kick, col, head, deck, ic) in enumerate(FEATURED):
        r, c = divmod(i, 3)
        x = mx + c * (cw + gap)
        y0 = gy + r * (gh + gap)
        d.rectangle([x, y0, x + cw, y0 + gh], fill=CARD_BG, outline=RULE, width=1)
        d.line([(x, y0), (x + cw, y0)], fill=col, width=3)
        tx = x + 10
        tw = cw - 20
        if ic:
            icons[ic](d, x + cw - 62, y0 + 34, 52)
            tw = cw - 20 - 62
        d.text((tx, y0 + 8), kick, font=font(SANS_B, 10), fill=col)
        hl = wrap(d, head, font(SERIF, 15), tw)[:2]
        y = draw_lines(d, hl, tx, y0 + 26, font(SERIF, 15), INK, 18)
        dl = wrap(d, deck, font(SANS, 11), tw)[:2]
        draw_lines(d, dl, tx, y + 3, font(SANS, 11), FAINT, 14)

    # ---- ticker
    ty = gy + 4 * gh + 3 * gap + 8
    d.text((mx, ty), "THE DAY IN BRIEF — 22 MORE STORIES",
           font=font(SANS_B, 12), fill=RED)
    rule(d, mx, ty + 18, right, 2)
    colw = (W - 2 * mx - 16) // 2
    f_t = font(SANS, 11)
    for i, item in enumerate(TICKER):
        col, row = divmod(i, 11)
        x = mx + col * (colw + 16)
        y = ty + 26 + row * 11
        d.text((x, y), "•  " + item, font=f_t, fill=INK)

    # ---- footer: day in numbers (single-line labels, sources at very bottom)
    fy = ty + 26 + 11 * 11 + 6
    rule(d, mx, fy, right, 3)
    d.text((mx, fy + 7), "DAY IN NUMBERS", font=font(SANS_B, 12), fill=RED)
    bw = (W - 2 * mx) // 6
    for i, (num, lab) in enumerate(NUMBERS):
        x = mx + i * bw
        d.text((x + bw // 2, fy + 24), num, font=font(SERIF, 20),
               fill=NAVY, anchor="ma")
        d.text((x + bw // 2, fy + 48), lab, font=font(SANS, 10),
               fill=FAINT, anchor="ma")
    d.text((W // 2, H - 18), "Sources: Reuters, KCNA, Oxfam, CEOBS, TOI, WSJ, Haaretz — all dated Tuesday 24 November 2026",
           font=font(SANS, 9), fill=FAINT, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, img.size)


if __name__ == "__main__":
    main()
