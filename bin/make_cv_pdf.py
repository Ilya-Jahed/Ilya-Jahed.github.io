# -*- coding: utf-8 -*-
"""Generate a clean one-to-two page CV PDF from _data/cv.yml content."""
import sys
import yaml
from pathlib import Path
from fpdf import FPDF

ROOT = Path(r"D:\Projects\Ilya-Jahed.github.io")
data = yaml.safe_load((ROOT / "_data" / "cv.yml").read_text(encoding="utf-8"))["cv"]

ACCENT = (30, 110, 130)
DARK = (35, 35, 35)
GRAY = (95, 95, 95)

def clean(s):
    # collapse whitespace, strip smart chars unsupported by latin-1 font
    return " ".join(str(s).split()).replace("\u2014", "-").replace("\u2019", "'").replace("\u2013", "-")

class CV(FPDF):
    def section(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*ACCENT)
        self.cell(0, 6, clean(title), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.4)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.set_line_width(0.2)
        self.ln(2)
        self.set_text_color(*DARK)

    def entry_title(self, left, right=""):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*DARK)
        w = self.w - self.l_margin - self.r_margin
        if right:
            self.set_font("Helvetica", "", 9)
            self.set_text_color(*GRAY)
            self.cell(w - 55, 5.5, clean(left))
            self.cell(55, 5.5, clean(right), align="R", new_x="LMARGIN", new_y="NEXT")
            self.set_text_color(*DARK)
        else:
            self.cell(0, 5.5, clean(left), new_x="LMARGIN", new_y="NEXT")

    def sub(self, text):
        self.set_font("Helvetica", "I", 9.5)
        self.set_text_color(*GRAY)
        self.multi_cell(0, 4.8, clean(text), new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*DARK)

    def body(self, text):
        self.set_font("Helvetica", "", 9.5)
        self.multi_cell(0, 4.8, clean(text), new_x="LMARGIN", new_y="NEXT")

    def bullets(self, items):
        self.set_font("Helvetica", "", 9.5)
        for it in items:
            x = self.l_margin + 3
            self.set_x(x)
            self.cell(3.5, 4.8, "-")
            self.multi_cell(self.w - self.l_margin - self.r_margin - 6.5, 4.8,
                            clean(it), new_x="LMARGIN", new_y="NEXT")

pdf = CV()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_margins(16, 14, 16)

# Header
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(*DARK)
pdf.cell(0, 9, clean(data["name"]), new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(*ACCENT)
pdf.cell(0, 5.5, clean(data["label"]), new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(*GRAY)
contact = f"{clean(data['location'])}  |  {clean(data['email'])}  |  github.com/{data['social_networks'][0]['username']}  |  linkedin.com/in/{data['social_networks'][1]['username']}  |  Ilya-Jahed.github.io"
pdf.multi_cell(0, 4.8, contact, new_x="LMARGIN", new_y="NEXT")

sections = data["sections"]

# Summary
pdf.section("Professional Summary")
pdf.body(sections.get("Summary") or clean(data["summary"]))

def render_section(name, key):
    if key not in sections:
        return
    pdf.section(name)
    for item in sections[key]:
        if key == "Education":
            dates = f"{clean(item.get('start_date',''))} - {clean(item.get('end_date',''))}"
            pdf.entry_title(f"{clean(item['area'])}, {clean(item['studyType'])}", dates)
            pdf.sub(f"{clean(item['institution'])} | {clean(item['location'])} | GPA: {clean(item.get('score',''))}")
            if item.get("highlights"):
                pdf.bullets(item["highlights"])
            pdf.ln(1.5)
        elif key == "Experience":
            dates = f"{clean(item.get('start_date',''))} - {clean(item.get('end_date','present'))}"
            pdf.entry_title(clean(item["position"]), dates)
            pdf.sub(f"{clean(item['company'])} | {clean(item.get('location',''))}")
            if item.get("summary"):
                pdf.body(item["summary"])
            if item.get("highlights"):
                pdf.bullets(item["highlights"])
            pdf.ln(1.5)
        elif key == "Projects":
            dates = f"{clean(item.get('start_date',''))} - {clean(item.get('end_date','present'))}"
            pdf.entry_title(clean(item["name"]), dates)
            if item.get("url"):
                pdf.sub(clean(item["url"]))
            if item.get("summary"):
                pdf.body(item["summary"])
            if item.get("highlights"):
                pdf.bullets(item["highlights"])
            pdf.ln(1.5)
        elif key == "Skills":
            pdf.set_font("Helvetica", "B", 9.5)
            pdf.set_text_color(*DARK)
            label = f"{clean(item['name'])} ({clean(item.get('level',''))}): "
            pdf.set_x(pdf.l_margin + 3)
            w_label = pdf.get_string_width(label)
            pdf.cell(w_label, 4.8, label)
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(*GRAY)
            pdf.multi_cell(pdf.w - pdf.l_margin - pdf.r_margin - w_label - 3, 4.8,
                           clean(item.get("keywords", "")), new_x="LMARGIN", new_y="NEXT")
            pdf.set_text_color(*DARK)
        elif key == "Languages":
            pdf.set_font("Helvetica", "B", 9.5)
            w = pdf.get_string_width(clean(item["name"]) + "  ")
            pdf.set_x(pdf.l_margin + 3)
            pdf.cell(w, 4.8, clean(item["name"]))
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(*GRAY)
            pdf.cell(0, 4.8, clean(item.get("summary", "")), new_x="LMARGIN", new_y="NEXT")
            pdf.set_text_color(*DARK)
        elif key == "Interests":
            pdf.set_font("Helvetica", "B", 9.5)
            pdf.set_x(pdf.l_margin + 3)
            pdf.cell(0, 4.8, clean(item["name"]), new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(*GRAY)
            pdf.set_x(pdf.l_margin + 3)
            pdf.multi_cell(0, 4.8, clean(item.get("keywords", "")), new_x="LMARGIN", new_y="NEXT")
            pdf.set_text_color(*DARK)

render_section("Education", "Education")
render_section("Research Experience", "Experience")
render_section("Selected Projects", "Projects")
render_section("Skills", "Skills")
render_section("Languages", "Languages")
render_section("Research Interests", "Interests")

out = ROOT / "assets" / "pdf" / "cv.pdf"
out.parent.mkdir(parents=True, exist_ok=True)
pdf.output(str(out))
print(f"written: {out} ({out.stat().st_size} bytes, {pdf.page_no()} pages)")
