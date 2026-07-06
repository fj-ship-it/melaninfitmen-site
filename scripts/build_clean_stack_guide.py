"""
SUPPS Lead Magnet — The Clean Stack Guide
Branded PDF for @melaninfitmen. Delivered via Beehiiv welcome email
(website signup) and ManyChat keyword SUPPS.

Style constants and flowable helpers match the house system in the
meal-prep-pdf skill (build_mealprep_pdf.py). Every ParagraphStyle has
explicit leading — see the skill's HR-overlap warning.

Run:  python scripts/build_clean_stack_guide.py
Out:  lead_magnets/The-Clean-Stack-Guide.pdf
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, PageBreak,
                                Table, TableStyle, Image, Flowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

GOLD = HexColor("#BA7517")
BLACK = HexColor("#000000")
DARK_BG = HexColor("#1A1A1A")
DARK_GRAY = HexColor("#333333")
WHITE = HexColor("#FFFFFF")
LIGHT_GOLD = HexColor("#F5E6CC")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(REPO, "public", "assets", "img", "mfm-chevron-mark.png")
OUT_DIR = os.path.join(REPO, "lead_magnets")
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "The-Clean-Stack-Guide.pdf")

styles = {
    "cover_title": ParagraphStyle("ct", fontName="Helvetica-Bold", fontSize=28,
        leading=38, textColor=GOLD, alignment=TA_CENTER, spaceAfter=24),
    "cover_sub": ParagraphStyle("cs", fontName="Helvetica", fontSize=14,
        leading=20, textColor=DARK_GRAY, alignment=TA_CENTER, spaceAfter=4),
    "cover_tag": ParagraphStyle("ctag", fontName="Helvetica-Oblique", fontSize=11,
        leading=16, textColor=DARK_GRAY, alignment=TA_CENTER, spaceAfter=20),
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=18,
        leading=24, textColor=GOLD, spaceBefore=16, spaceAfter=20),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=14,
        leading=19, textColor=BLACK, spaceBefore=8, spaceAfter=6),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=11,
        leading=16, textColor=DARK_GRAY, spaceBefore=8, spaceAfter=8),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5,
        textColor=DARK_GRAY, spaceAfter=5, leading=14),
    "bold_body": ParagraphStyle("bb", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=BLACK, spaceAfter=6, leading=14),
    "bullet": ParagraphStyle("bul", fontName="Helvetica", fontSize=10.5,
        textColor=DARK_GRAY, spaceAfter=6, leading=14, leftIndent=20,
        bulletFontName="Helvetica-Bold", bulletFontSize=10, bulletColor=GOLD),
    "check": ParagraphStyle("chk", fontName="Helvetica", fontSize=11,
        textColor=DARK_GRAY, spaceAfter=10, leading=15, leftIndent=24,
        bulletFontName="ZapfDingbats", bulletFontSize=10, bulletColor=GOLD),
    "small": ParagraphStyle("sm", fontName="Helvetica", fontSize=9,
        leading=13, textColor=DARK_GRAY, spaceAfter=4),
    "footer": ParagraphStyle("ft", fontName="Helvetica-Oblique", fontSize=8,
        leading=12, textColor=DARK_GRAY, alignment=TA_CENTER),
    "gold_callout": ParagraphStyle("gc", fontName="Helvetica-Bold", fontSize=11,
        leading=16, textColor=GOLD, spaceBefore=8, spaceAfter=12, leftIndent=10),
    "table_header": ParagraphStyle("th", fontName="Helvetica-Bold", fontSize=9,
        leading=13, textColor=WHITE, alignment=TA_CENTER),
    "table_cell": ParagraphStyle("tc", fontName="Helvetica", fontSize=9,
        leading=13, textColor=DARK_GRAY, alignment=TA_CENTER),
    "table_cell_left": ParagraphStyle("tcl", fontName="Helvetica", fontSize=9,
        leading=13, textColor=DARK_GRAY, alignment=TA_LEFT),
    "supp_number": ParagraphStyle("sn2", fontName="Helvetica-Bold", fontSize=22,
        leading=30, textColor=GOLD, spaceBefore=2, spaceAfter=2),
    "supp_title": ParagraphStyle("st", fontName="Helvetica-Bold", fontSize=16,
        leading=22, textColor=BLACK, spaceAfter=4),
    "supp_tagline": ParagraphStyle("stag", fontName="Helvetica-Oblique", fontSize=10,
        leading=14, textColor=DARK_GRAY, spaceAfter=14),
    "step_num": ParagraphStyle("sn", fontName="Helvetica-Bold", fontSize=10.5,
        textColor=GOLD, spaceAfter=4, leading=14),
    "center_body": ParagraphStyle("cb", fontName="Helvetica", fontSize=10.5,
        textColor=DARK_GRAY, spaceAfter=6, leading=14, alignment=TA_CENTER),
    "center_bold": ParagraphStyle("cbb", fontName="Helvetica-Bold", fontSize=12,
        textColor=BLACK, spaceAfter=6, leading=16, alignment=TA_CENTER),
}


class PaddedHR(Flowable):
    """HR line with padding baked into reported height (no margin collapse)."""
    def __init__(self, width, thickness, color, pad_top=34, pad_bottom=16):
        Flowable.__init__(self)
        self._width = width
        self.thickness = thickness
        self.color = color
        self.pad_top = pad_top
        self.pad_bottom = pad_bottom

    def wrap(self, availWidth, availHeight):
        return (self._width, self.pad_top + self.thickness + self.pad_bottom)

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, self.pad_bottom, self._width, self.pad_bottom)


def gold_hr():
    return PaddedHR(7.0 * inch, 2, GOLD, pad_top=26, pad_bottom=12)


def p(style_key, text):
    return Paragraph(text, styles[style_key])


def bullet(text):
    return Paragraph(text, styles["bullet"], bulletText="•")


def checkbox(text):
    # ZapfDingbats 'o' = empty square outline (real checkbox glyph)
    return Paragraph(text, styles["check"], bulletText="o")


def essential(number, title, tagline, dose, timing, why, buy, avoid):
    items = [
        p("supp_number", number),
        p("supp_title", title),
        p("supp_tagline", tagline),
        p("step_num", "THE DOSE"),
        p("body", dose),
        p("step_num", "WHEN TO TAKE IT"),
        p("body", timing),
        p("step_num", "WHY IT MATTERS FOR US"),
        p("body", why),
        p("step_num", "WHAT TO BUY"),
        p("body", buy),
        p("step_num", "RED FLAG TO AVOID"),
        p("body", avoid),
        Spacer(1, 0.18 * inch),
    ]
    # Never split a supplement block across pages
    return [KeepTogether(items)]


story = []

# ── COVER ────────────────────────────────────────────────
story.append(Spacer(1, 0.9 * inch))
story.append(Image(LOGO, width=1.3 * inch, height=1.3 * inch))
story.append(Spacer(1, 0.35 * inch))
story.append(p("cover_title", "THE CLEAN STACK<br/>GUIDE"))
story.append(gold_hr())
story.append(p("cover_sub", "The No-BS Supplement Checklist for Black Men."))
story.append(Spacer(1, 0.3 * inch))
story.append(p("cover_tag",
    "5 label red flags • The 5 essentials • What to skip • The store checklist"))
story.append(Spacer(1, 0.5 * inch))
story.append(p("center_body", "From @melaninfitmen"))
story.append(p("center_body", "Melanin Fit Men | Health &amp; Fitness"))
story.append(Spacer(1, 0.7 * inch))
story.append(p("footer",
    "FREE RESOURCE — NOT FOR RESALE. This guide is for educational purposes and is not medical advice. "
    "Consult a physician before starting any supplement, especially if you take prescription medication."))
story.append(PageBreak())

# ── WHY THIS GUIDE EXISTS ────────────────────────────────
story.append(p("h1", "WHY THIS GUIDE EXISTS"))
story.append(gold_hr())
story.append(p("body",
    "I've spent 15 years inside the supplement manufacturing industry. I've seen how the sausage "
    "gets made — what goes into the bottle, what the label hides, and how products get designed "
    "to sell instead of to work."))
story.append(p("body",
    "Here's the truth nobody at the supplement counter will tell you: the FDA does not approve "
    "supplements before they hit the shelf. The label is your only line of defense — and most "
    "labels are written to beat you, not inform you."))
story.append(Spacer(1, 0.08 * inch))
story.append(p("bold_body", "And for Black men, the stakes are higher:"))
story.append(bullet(
    "<b>76% of Black Americans are Vitamin D deficient</b> — melanin reduces Vitamin D synthesis "
    "from sunlight, and almost nobody is telling us."))
story.append(bullet(
    "<b>56% of Black men have high blood pressure</b> — the highest rate of any group in the world, "
    "which makes minerals like magnesium worth understanding."))
story.append(bullet(
    "<b>Heart disease is our #1 killer</b> — so the quality of your omega-3 isn't a detail. "
    "It's the whole point."))
story.append(Spacer(1, 0.08 * inch))
story.append(p("body",
    "Most supplements are overpriced, underdosed, and dressed up in marketing. But the right "
    "supplements, at the right doses, in the right forms, from brands that prove what's in the "
    "bottle — those can genuinely support your health."))
story.append(p("body",
    "This guide is the insider filter. Five label rules that expose the games. Five essentials "
    "that earn their spot. The junk to skip. And a checklist you can pull up in any store aisle."))
story.append(p("gold_callout", "READ THE LABEL, KING. THIS GUIDE TEACHES YOU HOW."))
story.append(PageBreak())

# ── THE 5 LABEL RULES ────────────────────────────────────
story.append(p("h1", "THE 5 LABEL RULES"))
story.append(gold_hr())
story.append(p("body",
    "Every trick in the industry shows up on the label — if you know where to look. "
    "Run every product through these five rules before your money leaves your pocket."))
story.append(Spacer(1, 0.08 * inch))

story.append(p("step_num", "RULE 1 — NO PROPRIETARY BLENDS. EVER."))
story.append(p("body",
    "A \"proprietary blend\" lists ingredients without exact doses. That's not protecting a secret "
    "formula — it's hiding that the expensive ingredients are in there at doses too small to matter. "
    "If you can't see exact amounts, you can't trust it. Walk away."))

story.append(p("step_num", "RULE 2 — WATCH FOR FAIRY DUSTING"))
story.append(p("body",
    "A label with 30 impressive ingredients usually means 30 useless doses. Brands sprinkle in a "
    "pinch of a trendy ingredient just to print it on the front of the bottle. Fewer ingredients "
    "at full clinical doses beats a kitchen-sink formula every time."))

story.append(p("step_num", "RULE 3 — THE FORM IS THE PRODUCT"))
story.append(p("body",
    "Two bottles can say \"Magnesium 400mg\" and be completely different products. Magnesium "
    "<b>oxide</b> is poorly absorbed — it's in the bottle because it's cheap. Magnesium "
    "<b>glycinate</b> is what you actually want. Same story with fish oil (triglyceride form beats "
    "ethyl ester) and zinc (picolinate beats oxide). The form tells you if the brand cut corners."))

story.append(p("step_num", "RULE 4 — DEMAND THIRD-PARTY TESTING"))
story.append(p("body",
    "Anyone can print \"lab tested\" on a label — that phrase is legally meaningless. Look for "
    "independent certification seals: <b>NSF Certified for Sport, Informed Choice, or USP "
    "Verified</b>. These mean an outside lab confirmed what's in the bottle matches the label."))

story.append(p("step_num", "RULE 5 — MEGADOSES ARE MARKETING, NOT MEDICINE"))
story.append(p("body",
    "\"50,000% Daily Value!\" is a red flag, not a feature. More is not better — zinc over 40mg "
    "a day depletes copper, and megadosed cheap B-vitamins mostly produce expensive urine. "
    "Clinical doses, not circus numbers."))
story.append(PageBreak())

# ── THE 5 ESSENTIALS (pages 4-5) ─────────────────────────
story.append(p("h1", "THE 5 ESSENTIALS FOR BLACK MEN"))
story.append(gold_hr())
story.append(p("body",
    "If you take nothing else from this guide: these five, at these doses, in these forms, cover "
    "the gaps that hit Black men hardest. This is the clean stack."))
story.append(Spacer(1, 0.1 * inch))

story.extend(essential(
    "01", "Vitamin D3", "The non-negotiable",
    "4,000–5,000 IU daily.",
    "With your biggest meal — D3 is fat-soluble and needs dietary fat to absorb.",
    "76% of Black Americans are deficient. Melanin reduces Vitamin D synthesis from sunlight, "
    "so we need more than the standard advice assumes. Supports bone health, immune function, "
    "and mood.",
    "D3 (cholecalciferol), softgel in an oil base. Pair with Vitamin K2 if you can find a clean combo.",
    "D2 (ergocalciferol) — the cheaper, weaker form. And dry tablets with no fat source."))

story.extend(essential(
    "02", "Magnesium Glycinate", "The sleep and pressure mineral",
    "200–400mg daily (elemental magnesium).",
    "30–60 minutes before bed. The glycinate form is calming, not stimulating.",
    "With 56% of Black men dealing with high blood pressure, magnesium is a mineral we cannot "
    "afford to be low on. Supports healthy blood pressure, sleep quality, and muscle recovery.",
    "Magnesium glycinate (also sold as bisglycinate). Check the ELEMENTAL magnesium number on the label.",
    "Magnesium oxide — poorly absorbed, mostly a laxative. It's in the bottle because it costs pennies."))

story.extend(essential(
    "03", "Omega-3 Fish Oil", "The heart defender",
    "2,000–3,000mg combined EPA + DHA daily (read the EPA/DHA line, not the \"fish oil\" line).",
    "With meals, split morning and evening if it repeats on you.",
    "Heart disease is the #1 killer of Black men. Omega-3s are anti-inflammatory and support "
    "heart and prostate health — this is the one to never cheap out on.",
    "Triglyceride-form fish oil, third-party tested for purity. Dark bottle, refrigerate after opening.",
    "Ethyl ester form hidden behind a big \"1,000mg Fish Oil!\" front label that's only 300mg EPA+DHA."))

story.extend(essential(
    "04", "Creatine Monohydrate", "The most proven supplement in history",
    "5g daily. No loading phase needed. Consistency is the whole game.",
    "Any time of day — timing doesn't matter, the daily habit does.",
    "Decades of research. Supports muscle, strength, brain function, and cardiovascular health. "
    "For men training after 35, it's the closest thing to a sure bet on the shelf.",
    "Plain creatine monohydrate powder — Creapure if you want the gold standard. One ingredient on the label.",
    "\"Advanced\" creatine blends (HCL, esters, liquid creatine) — more money for less evidence."))

story.extend(essential(
    "05", "Zinc Picolinate", "The testosterone and immune mineral",
    "15–30mg daily. DO NOT exceed 40mg — excess zinc depletes copper.",
    "With food to avoid nausea. Away from your magnesium dose if possible.",
    "Supports immune function, prostate health, and healthy testosterone levels — three things "
    "every man over 35 should be paying attention to.",
    "Zinc picolinate. If you take it long-term, choose a version with 1–2mg copper.",
    "Megadosed 50mg+ zinc products, and zinc oxide — the sunscreen ingredient, barely absorbed."))
story.append(PageBreak())

# ── SKIP THESE ───────────────────────────────────────────
story.append(p("h1", "SKIP THESE — THE MONEY BURNERS"))
story.append(gold_hr())
story.append(p("body",
    "The industry makes its margin on hope. These categories are where your money goes to die:"))
story.append(Spacer(1, 0.08 * inch))
story.append(p("step_num", "\"TEST BOOSTERS\""))
story.append(p("body",
    "Herb blends with heroic names and proprietary doses. If your testosterone is genuinely low, "
    "that's a conversation with your doctor and a blood panel — not a $60 bottle. Sleep, lifting, "
    "zinc, and body composition move the needle more than any booster on the shelf."))
story.append(p("step_num", "FAT BURNERS"))
story.append(p("body",
    "Mostly caffeine in a costume. The \"thermogenic matrix\" is a proprietary blend (Rule 1) "
    "wrapped around stimulants. A calorie deficit and your 4-day training split do the job for free."))
story.append(p("step_num", "BCAAs (IF YOU EAT ENOUGH PROTEIN)"))
story.append(p("body",
    "If you're hitting your protein target from food or a quality protein powder, BCAAs add "
    "nothing — you already ate them. They're amino acids sold twice."))
story.append(p("step_num", "GREENS POWDERS AS A VEGETABLE REPLACEMENT"))
story.append(p("body",
    "A scoop of dried powder is not a plate of vegetables — the fiber is gone and the doses are "
    "fairy-dusted (Rule 2). Fine as insurance on travel weeks; a scam as a lifestyle."))
story.append(p("step_num", "DETOX AND CLEANSE PRODUCTS"))
story.append(p("body",
    "You have a liver and two kidneys. They are the detox. Anything promising to \"flush toxins\" "
    "is selling you your own biology back at $40 a bottle."))
story.append(p("gold_callout",
    "EVERY DOLLAR YOU DON'T BURN HERE FUNDS THE STACK THAT WORKS."))
story.append(PageBreak())

# ── THE STORE CHECKLIST + DOSING CHART ───────────────────
story.append(p("h1", "THE CLEAN STACK CHECKLIST"))
story.append(gold_hr())
story.append(p("body",
    "Pull this up in the aisle or before you hit \"add to cart.\" A clean product passes ALL of these:"))
story.append(Spacer(1, 0.08 * inch))
story.append(checkbox("<b>Exact doses listed</b> — zero proprietary blends anywhere on the label"))
story.append(checkbox("<b>Clinical doses</b> — matches the numbers in this guide, not a sprinkle"))
story.append(checkbox("<b>The right form</b> — glycinate, picolinate, triglyceride, monohydrate"))
story.append(checkbox("<b>Third-party seal</b> — NSF, Informed Choice, or USP on the bottle"))
story.append(checkbox("<b>Short ingredient list</b> — the fewer the ingredients, the fewer the hiding places"))
story.append(checkbox("<b>No miracle language</b> — \"melts fat,\" \"boosts T by 300%\" = put it back"))
story.append(checkbox("<b>Lot number + expiration date</b> — basic accountability from a real facility"))
story.append(Spacer(1, 0.15 * inch))

story.append(p("h2", "The Stack at a Glance"))
header = [Paragraph(t, styles["table_header"]) for t in
          ["Supplement", "Daily Dose", "Best Time", "Form to Buy"]]
rows = [
    ["Vitamin D3", "4,000–5,000 IU", "With biggest meal", "D3 softgel (oil base)"],
    ["Magnesium", "200–400mg", "Before bed", "Glycinate"],
    ["Omega-3", "2,000–3,000mg EPA+DHA", "With meals", "Triglyceride form"],
    ["Creatine", "5g", "Any time, daily", "Plain monohydrate"],
    ["Zinc", "15–30mg", "With food", "Picolinate"],
]
data = [header] + [
    [Paragraph(c, styles["table_cell_left"] if i == 0 else styles["table_cell"])
     for i, c in enumerate(r)] for r in rows
]
t = Table(data, colWidths=[1.5 * inch, 1.9 * inch, 1.6 * inch, 2.0 * inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), DARK_BG),
    ("BACKGROUND", (0, 1), (-1, -1), LIGHT_GOLD),
    ("GRID", (0, 0), (-1, -1), 0.5, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(t)
story.append(Spacer(1, 0.12 * inch))
story.append(p("small",
    "Start one supplement at a time, a week apart, so you know what's doing what. "
    "If you take prescription medication — especially for blood pressure — clear the stack "
    "with your doctor first."))
story.append(PageBreak())

# ── CLOSING ──────────────────────────────────────────────
story.append(Spacer(1, 1.2 * inch))
story.append(Image(LOGO, width=1.0 * inch, height=1.0 * inch))
story.append(Spacer(1, 0.25 * inch))
story.append(p("cover_title", "READ THE LABEL, KING."))
story.append(gold_hr())
story.append(p("center_body",
    "You now know more about reading a supplement label than 95% of the men in any gym. "
    "Use it. Teach it. And never buy a proprietary blend again."))
story.append(Spacer(1, 0.3 * inch))
story.append(p("center_bold", "KEEP LEVELING UP"))
story.append(p("center_body",
    "<b>The King's Drop</b> — supplement truth in your inbox, one email a week, no fluff. "
    "You're already in if this guide came from melaninfitmen.com."))
story.append(p("center_body",
    "Comment <b>FUEL</b> on any @melaninfitmen post for the 5-Meal Prep Blueprint."))
story.append(p("center_body",
    "Comment <b>KING</b> for the Black Men's Health Starter Guide — all five pillars in one."))
story.append(p("center_body",
    "Watch the breakdowns on YouTube: <b>@MelaninFitMen</b>"))
story.append(Spacer(1, 0.5 * inch))
story.append(p("footer",
    "This guide is for educational purposes only and is not medical advice, diagnosis, or treatment. "
    "Statements about supplements have not been evaluated by the Food and Drug Administration. "
    "These products are not intended to diagnose, treat, cure, or prevent any disease. "
    "Consult a physician before beginning any supplement regimen."))
story.append(p("footer", "© 2026 Melanin Fit Men. Train hard. Eat right. Live long."))

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
                        topMargin=0.75 * inch, bottomMargin=0.75 * inch,
                        title="The Clean Stack Guide — Melanin Fit Men",
                        author="Melanin Fit Men")
doc.build(story)
print("built:", OUT)
