# -*- coding: utf-8 -*-
"""Generate a polished CV PDF from _data/cv.yml.

Layout conventions (resume-style):
- Title left, dates right, on the SAME row (no overlap).
- Organization / subtitle in gray italics below the title row.
- Hanging-indent bullets aligned under the text column.
- Accent-colored section rules, generous vertical rhythm.
- Footer with name + page number on page 2+.
"""
import yaml
from pathlib import Path
from fpdf import FPDF

ROOT = Path(r"D:\Projects\Ilya-Jahed.github.io")
data = yaml.safe_load((ROOT / "_data" / "cv.yml").read_text(encoding="utf-8"))["cv"]

ACCENT = (23, 105, 125)
DARK = (30, 30, 30)
GRAY = (105, 105, 105)
LIGHT = (150, 150, 150)

M_L = 15.0
M_R = 15.0
CONTENT_W = 210.0 - M_L - M_R  # A4 width


def clean(s):
    return (
        " ".join(str(s).split())
        .replace("\u2014", "-")
        .replace("\u2019", "'")
        .replace("\u2013", "-")
        .replace("\u00a0", " ")
    )


def fmt_date(value):
    value = clean(value or "")
    if value.lower() == "present":
        return "present"
    # Keep source data ISO-8601, but render compact human-readable dates in PDF.
    try:
        from datetime import date
        parts = value.split("-")
        if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            return f"{months[int(parts[1]) - 1]} {parts[0]}"
    except (ValueError, IndexError):
        pass
    return value


def fmt_dates(start, end):
    start = fmt_date(start)
    end = fmt_date(end or "present")
    return f"{start} - {end}"


class CV(FPDF):
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-13)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*LIGHT)
            self.cell(0, 5, clean(data["name"]), align="L")
            self.cell(0, 5, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="TOP")

    def section(self, title):
        if self.get_y() > self.h - 40:
            self.add_page()
        self.ln(3.0)
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*ACCENT)
        self.cell(0, 5, clean(title).upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.5)
        self.line(M_L, self.get_y() + 0.6, 210 - M_R, self.get_y() + 0.6)
        self.set_line_width(0.2)
        self.ln(3.4)
        self.set_text_color(*DARK)

    def entry_row(self, title, dates, url=None):
        """Title on the left, dates on the right, same row."""
        if self.get_y() > self.h - 30:
            self.add_page()
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*DARK)
        date_w = self.get_string_width(dates) + 4
        title_w = CONTENT_W - date_w
        x0 = self.get_x()
        y0 = self.get_y()
        # dates first (right, fixed width, top-aligned)
        self.set_xy(210 - M_R - date_w, y0)
        self.set_font("Helvetica", "", 8.5)
        self.set_text_color(*GRAY)
        self.cell(date_w, 5, dates, align="R")
        # title (left, may wrap into the remaining width)
        self.set_xy(x0, y0)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*DARK)
        self.multi_cell(title_w, 5, clean(title), new_x="LMARGIN", new_y="NEXT")

    def sub(self, text, italic=True):
        self.set_font("Helvetica", "I" if italic else "", 9)
        self.set_text_color(*GRAY)
        self.multi_cell(CONTENT_W, 4.4, clean(text), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*DARK)

    def body(self, text):
        self.ln(0.6)
        self.set_font("Helvetica", "", 9)
        self.set_text_color((60, 60, 60))
        self.multi_cell(CONTENT_W, 4.5, clean(text), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*DARK)

    def bullets(self, items):
        indent = 4.0
        bullet_w = 3.0
        text_w = CONTENT_W - indent - bullet_w
        for it in items:
            y = self.get_y()
            if y > self.h - 25:
                self.add_page()
            self.set_xy(M_L + indent, self.get_y())
            self.set_font("Helvetica", "", 9)
            self.set_text_color(*ACCENT)
            self.cell(bullet_w, 4.5, "-")
            self.set_text_color((60, 60, 60))
            self.multi_cell(text_w, 4.5, clean(it), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*DARK)

    def kv(self, label, value, label_w=None):
        """Bold label + gray value on one flowing line (skills/languages)."""
        if self.get_y() > self.h - 20:
            self.add_page()
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*DARK)
        lw = label_w or (self.get_string_width(clean(label)) + 2)
        x0 = self.get_x()
        self.set_x(M_L + 4.0)
        self.cell(lw, 4.6, clean(label))
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*GRAY)
        self.multi_cell(CONTENT_W - 4.0 - lw, 4.6, clean(value), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*DARK)


pdf = CV(format="A4")
pdf.set_auto_page_break(auto=True, margin=16)
pdf.set_margins(M_L, 13, M_R)
pdf.add_page()

# ---------------------------------------------------------------- header
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(*DARK)
pdf.cell(0, 10, clean(data["name"]), new_x="LMARGIN", new_y="NEXT")

pdf.set_font("Helvetica", "", 10.5)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 5.5, clean(data["label"]), new_x="LMARGIN", new_y="NEXT")

gh = data["social_networks"][0]["username"]
li = data["social_networks"][1]["username"]
contact = (
    f"{clean(data['location'])}   |   {clean(data['email'])}   |   "
    f"github.com/{gh}   |   linkedin.com/in/{li}   |   ilya-jahed.github.io"
)
pdf.set_font("Helvetica", "", 8.5)
pdf.set_text_color(*GRAY)
pdf.multi_cell(0, 4.4, contact, new_x="LMARGIN", new_y="NEXT")

pdf.set_draw_color(*ACCENT)
pdf.set_line_width(0.7)
pdf.line(M_L, pdf.get_y() + 1.5, 210 - M_R, pdf.get_y() + 1.5)
pdf.set_line_width(0.2)

sections = data["sections"]

# ---------------------------------------------------------------- summary
pdf.section("Profile")
pdf.body(data["summary"])

# ---------------------------------------------------------------- education
pdf.section("Education")
for it in sections["Education"]:
    dates = fmt_dates(it.get("start_date"), it.get("end_date"))
    pdf.entry_row(f"{clean(it['studyType'])} in {clean(it['area'])}", dates)
    pdf.sub(f"{clean(it['institution'])}, {clean(it['location'])}   |   GPA: {clean(it.get('score', ''))}")
    if it.get("highlights"):
        pdf.bullets(it["highlights"])
    pdf.ln(1.6)

# ---------------------------------------------------------------- experience
pdf.section("Research Experience")
for it in sections["Experience"]:
    dates = fmt_dates(it.get("start_date"), it.get("end_date"))
    pdf.entry_row(clean(it["position"]), dates)
    org = clean(it["company"])
    if it.get("location"):
        org += f", {clean(it['location'])}"
    pdf.sub(org)
    if it.get("summary"):
        pdf.body(it["summary"])
    if it.get("highlights"):
        pdf.bullets(it["highlights"])
    pdf.ln(1.6)

# ---------------------------------------------------------------- projects
pdf.section("Selected Projects")
for it in sections["Projects"]:
    dates = fmt_dates(it.get("start_date"), it.get("end_date"))
    pdf.entry_row(clean(it["name"]), dates)
    if it.get("url"):
        pdf.sub(clean(it["url"]))
    if it.get("summary"):
        pdf.body(it["summary"])
    if it.get("highlights"):
        pdf.bullets(it["highlights"])
    pdf.ln(1.6)

# ---------------------------------------------------------------- skills
pdf.section("Skills")
for it in sections["Skills"]:
    label = f"{clean(it['name'])} ({clean(it.get('level', ''))}):"
    pdf.kv(label, it.get("keywords", ""))
pdf.ln(1.0)

# ---------------------------------------------------------------- languages
pdf.section("Languages")
for it in sections["Languages"]:
    pdf.kv(clean(it["name"]) + ":", it.get("summary", ""))
pdf.ln(1.0)

# ---------------------------------------------------------------- interests
if sections.get("Interests"):
    pdf.section("Research Interests")
    for it in sections["Interests"]:
        pdf.kv(clean(it["name"]) + ":", it.get("keywords", ""))

out = ROOT / "assets" / "pdf" / "cv.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
pdf.output(str(out))
print(f"written: {out} ({out.stat().st_size} bytes, {pdf.page_no()} pages)")
