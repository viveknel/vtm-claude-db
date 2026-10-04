"""
Build the Vampire: The Dark Ages (V20) Excel character sheet.

Usage:
    python build_v20_dark_ages_sheet.py [output.xlsx]

With no argument the workbook is written to V20_Dark_Ages_Character_Sheet.xlsx in the
current directory. Needs only openpyxl; styling comes from xlsx_helpers.py in
this folder (the wod20-character-sheet-builder skill's helper module).

Rules numbers come from the v20-dark-ages and v20-dark-ages-companion bundles.
Page citations written into the workbook are the book's PRINTED page numbers; the
v20-dark-ages chunk DB runs one page higher than the printed page.
"""
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter as CL
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.pagebreak import Break

import xlsx_helpers as xh

OUT = sys.argv[1] if len(sys.argv) > 1 else "V20_Dark_Ages_Character_Sheet.xlsx"

# Brand trio: blood red -> oxblood -> antique bronze (cover art is red/black on parchment)
PAL = xh.Palette(title_bg="991B1E", section_bg="4A0F12", subheader_bg="8A6A2B")

PRIORITIES = ["Primary", "Secondary", "Tertiary"]
MERIT_TYPES = ["Physical", "Mental", "Social", "Supernatural"]


# ---------------------------------------------------------------------------
# Local helpers (thin wrappers around xlsx_helpers; blank by default)
# ---------------------------------------------------------------------------

def text_entry(ws, r, c, value=None):
    xh.style_entry(ws.cell(row=r, column=c), value, align="left")


def num_entry(ws, r, c, value=None):
    xh.style_entry(ws.cell(row=r, column=c), value, align="center")


def blank_dot_trait(ws, r, lc, ic, dc, max_dots=10):
    """Yellow text label + blank yellow number + dot-track (PDF blank line)."""
    text_entry(ws, r, lc)
    num_entry(ws, r, ic)
    ref = f"{CL(ic)}{r}"
    xh.style_dot_display(ws.cell(row=r, column=dc), xh.dot_formula(ref, max_dots))
    return ref


def label(ws, r, c, text, bold=False, align="left"):
    xh.style_label(ws.cell(row=r, column=c), text, bold=bold, align=align)


def merged_label(ws, r, c1, c2, text, bold=False, align="left"):
    if c1 != c2:
        ws.merge_cells(start_row=r, start_column=c1, end_row=r, end_column=c2)
    xh.style_label(ws.cell(row=r, column=c1), text, bold=bold, align=align)


def caption(ws, r, c, text, c2=None, align="center"):
    """Table column caption: plain label style, wraps. Left-align captions that sit
    over a column of left-aligned row labels."""
    if c2 and c2 != c:
        ws.merge_cells(start_row=r, start_column=c, end_row=r, end_column=c2)
    cell = ws.cell(row=r, column=c)
    xh.style_label(cell, text, bold=False, align=align)
    cell.alignment = Alignment(horizontal=align, vertical="center", wrap_text=True)


def page_break(ws, before_row):
    """Start a new printed page at before_row (keeps tables from splitting)."""
    ws.row_breaks.append(Break(id=before_row - 1))


def note(ws, r, c1, c2, text, lines=1, size=9):
    xh.style_footnote(ws, r, c1, c2, text, size=size)
    xh.set_row_height(ws, r, 12.5 * lines + 3)


def sub_title(ws, r, text, last_col, subtitle_text, subtitle_lines=2):
    xh.style_title(ws, r, 1, last_col, text, PAL)
    xh.set_row_height(ws, r, 25.5)
    xh.style_subtitle(ws, r + 1, 1, last_col, subtitle_text)
    ws.cell(row=r + 1, column=1).alignment = Alignment(
        horizontal="center", vertical="center", wrap_text=True)
    xh.set_row_height(ws, r + 1, 15 * subtitle_lines + 3)


def whole_dv(ws, ranges, minimum, maximum, what):
    """One whole-number validation applied to several ranges."""
    dv = DataValidation(type="whole", operator="between" if maximum is not None
                        else "greaterThanOrEqual",
                        formula1=str(minimum),
                        formula2=str(maximum) if maximum is not None else None,
                        allow_blank=True)
    dv.showErrorMessage = True
    dv.errorTitle = "Whole number needed"
    dv.error = what
    ws.add_data_validation(dv)
    for rg in ranges:
        dv.add(rg)
    return dv


def list_dv(ws, ranges, options=None, formula=None):
    dv = DataValidation(type="list",
                        formula1=formula if formula else '"' + ",".join(options) + '"',
                        allow_blank=True)
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    for rg in ranges:
        dv.add(rg)
    return dv


def finish_sheet(ws, print_area, heights=None):
    """Row-height rhythm: 15pt for every row that holds content, spacers left
    at the default. `heights` overrides specific rows (already-set rows kept)."""
    last = ws.max_row
    for r in range(1, last + 1):
        if ws.row_dimensions[r].height is not None:
            continue
        used = any(c.value is not None or c.has_style for c in ws[r])
        if used:
            ws.row_dimensions[r].height = 15.0
    xh.apply_standard_sheet_setup(ws, print_area=print_area)


# ---------------------------------------------------------------------------
# Sheet 1 - Front Sheet (PDF page 1)
# ---------------------------------------------------------------------------

def build_front(wb):
    ws = wb.active
    ws.title = "1. Front Sheet"
    xh.set_column_widths(ws, {"A": 17, "B": 6.5, "C": 15, "D": 2.2, "E": 17, "F": 6.5,
                              "G": 15, "H": 2.2, "I": 22, "J": 6.5, "K": 15})
    sub_title(ws, 1, "VAMPIRE: THE DARK AGES (V20) \u2014 CHARACTER SHEET", 11,
              "Yellow cells are for your entries. Dot tracks fill in automatically from the "
              "number you type. Sheet 5 checks your character-creation math; sheet 6 tracks experience.")

    # Identity block (3 columns of 3 fields, each a label + 2-cell entry)
    ident = [("Name:", "Nature:", "Clan:"),
             ("Player:", "Demeanor:", "Generation:"),
             ("Chronicle:", "Concept:", "Sire:")]
    for i, row in enumerate(ident):
        r = 4 + i
        for g, lab in enumerate(row):
            lc = [1, 5, 9][g]
            label(ws, r, lc, lab, bold=True)
            xh.add_wide_entry(ws, r, lc + 1, lc + 2, value=None)

    groups = [(1, 2, 3), (5, 6, 7), (9, 10, 11)]

    # ATTRIBUTES
    xh.style_section_header(ws, 8, 1, 11,
                            "ATTRIBUTES (creation: 1 free dot each, then 7 / 5 / 3 dots by priority)", PAL)
    xh.set_row_height(ws, 8, 19.5)
    attrs = [("PHYSICAL", ["Strength", "Dexterity", "Stamina"]),
             ("SOCIAL", ["Charisma", "Manipulation", "Appearance"]),
             ("MENTAL", ["Perception", "Intelligence", "Wits"])]
    for g, (head, names) in enumerate(attrs):
        lc, ic, dc = groups[g]
        xh.style_subheader(ws, 9, lc, dc, head, PAL)
        for i, nm in enumerate(names):
            xh.add_dot_trait(ws, 10 + i, lc, ic, dc, nm, value=1, max_dots=10)

    # ABILITIES
    xh.style_section_header(ws, 14, 1, 11,
                            "ABILITIES (creation: 13 / 9 / 5 dots by priority, no more than 3 in any one Ability)", PAL)
    xh.set_row_height(ws, 14, 19.5)
    abil = [("TALENTS", ["Alertness", "Athletics", "Awareness", "Brawl", "Empathy", "Expression",
                         "Intimidation", "Leadership", "Legerdemain", "Subterfuge"]),
            ("SKILLS", ["Animal Ken", "Archery", "Commerce", "Crafts", "Etiquette", "Melee",
                        "Performance", "Ride", "Stealth", "Survival"]),
            ("KNOWLEDGES", ["Academics", "Enigmas", "Hearth Wisdom", "Investigation", "Law",
                            "Medicine", "Occult", "Politics", "Seneschal", "Theology"])]
    for g, (head, names) in enumerate(abil):
        lc, ic, dc = groups[g]
        xh.style_subheader(ws, 15, lc, dc, head, PAL)
        for i, nm in enumerate(names):
            xh.add_dot_trait(ws, 16 + i, lc, ic, dc, nm, value=0, max_dots=10)
        blank_dot_trait(ws, 26, lc, ic, dc)  # the PDF's blank custom-Ability line

    # ADVANTAGES
    xh.style_section_header(ws, 28, 1, 11,
                            "ADVANTAGES (creation: 4 Discipline dots, 5 Background dots, 7 Virtue dots)", PAL)
    xh.set_row_height(ws, 28, 19.5)
    xh.style_subheader(ws, 29, 1, 3, "DISCIPLINES", PAL)
    xh.style_subheader(ws, 29, 5, 7, "BACKGROUNDS", PAL)
    xh.style_subheader(ws, 29, 9, 11, "VIRTUES", PAL)
    for r in range(30, 35):
        blank_dot_trait(ws, r, 1, 2, 3)
        blank_dot_trait(ws, r, 5, 6, 7)
    for i, nm in enumerate(["Conscience/Conviction", "Self-Control/Instinct", "Courage"]):
        xh.add_dot_trait(ws, 30 + i, 9, 10, 11, nm, value=1, max_dots=5)
    ws.merge_cells("I33:K34")
    c = ws["I33"]
    c.value = ("Each Virtue starts at 1. Road rating = Conscience/Conviction + "
               "Self-Control/Instinct. Starting Willpower = Courage.")
    c.font = Font(name=xh.FONT_NAME, size=8.5, color=xh.NOTE_FONT)
    c.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

    # Bottom block: OTHER TRAITS | ROAD / WILLPOWER / BLOOD POOL | HEALTH / WEAKNESS
    xh.style_section_header(ws, 36, 1, 3, "OTHER TRAITS", PAL)
    xh.style_section_header(ws, 36, 5, 7, "ROAD", PAL)
    xh.style_section_header(ws, 36, 9, 11, "HEALTH", PAL)
    xh.set_row_height(ws, 36, 19.5)

    xh.add_free_text_block(ws, 37, 12, 1, 3)  # 12 ruled lines, as on the PDF

    # Road
    xh.add_wide_entry(ws, 37, 5, 7, value=None)  # Road name
    label(ws, 38, 5, "Road rating")
    num_entry(ws, 38, 6)
    xh.style_dot_display(ws["G38"], xh.dot_formula("F38", 10))
    label(ws, 39, 5, "Aura:")
    xh.add_wide_entry(ws, 39, 6, 7, value=None)
    label(ws, 40, 5, "Aura modifier ( ):")
    ws.merge_cells("F40:G40")
    xh.style_formula(
        ws["F40"],
        '=IF(F38="","",IF(F38>=10,"-2 difficulty",IF(F38>=8,"-1 difficulty",'
        'IF(F38>=4,"No modifier",IF(F38>=2,"+1 difficulty",IF(F38=1,"+2 difficulty",""))))))')
    xh.apply_span_border(ws, 40, 6, 7)

    # Willpower
    xh.style_section_header(ws, 41, 5, 7, "WILLPOWER", PAL)
    xh.set_row_height(ws, 41, 19.5)
    label(ws, 42, 5, "Permanent")
    num_entry(ws, 42, 6)
    label(ws, 43, 5, "Current")
    num_entry(ws, 43, 6)
    note(ws, 42, 7, 7, "Starts = Courage", size=8.5)
    ws.row_dimensions[42].height = 15

    # Blood Pool
    xh.style_section_header(ws, 44, 5, 7, "BLOOD POOL", PAL)
    xh.set_row_height(ws, 44, 19.5)
    label(ws, 45, 5, "Maximum")
    num_entry(ws, 45, 6)
    label(ws, 46, 5, "Current")
    num_entry(ws, 46, 6)
    note(ws, 45, 7, 7, "Max: see sheet 5", size=8.5)
    ws.row_dimensions[45].height = 15

    # Health
    caption(ws, 37, 9, "Level")
    caption(ws, 37, 10, "Penalty")
    caption(ws, 37, 11, "Mark")
    levels = [("Bruised", 0), ("Hurt", -1), ("Injured", -1), ("Wounded", -2),
              ("Mauled", -2), ("Crippled", -5), ("Incapacitated", "\u2014")]
    for i, (nm, pen) in enumerate(levels):
        r = 38 + i
        label(ws, r, 9, nm)
        xh.style_formula(ws.cell(row=r, column=10), pen)
        num_entry(ws, r, 11)
    list_dv(ws, ["K38:K44"], ["/", "X", "*"])
    note(ws, 45, 9, 11, "Mark: / bashing \u2022 X lethal \u2022 * aggravated", size=8.5)
    ws.row_dimensions[45].height = 15
    xh.style_section_header(ws, 46, 9, 11, "WEAKNESS", PAL)
    xh.set_row_height(ws, 46, 19.5)
    xh.add_free_text_block(ws, 47, 2, 9, 11)

    # Consolidated creation-guide footnote
    note(ws, 50, 1, 11,
         "Character Creation Guide (V20 Dark Ages, ch. 4): Attributes 1 free dot each + 7/5/3 \u2022 "
         "Abilities 13/9/5, max 3 each \u2022 Disciplines 4 \u2022 Backgrounds 5 \u2022 Virtues 1 each + 7 "
         "\u2022 Freebie points 15 \u2022 Willpower = Courage \u2022 Road = Conscience/Conviction + "
         "Self-Control/Instinct \u2022 Blood Pool = one die + Domain + Herd (up to your Generation's maximum) "
         "\u2022 Each Ability applies within an Area of Expertise (p.162). See sheet 5.", lines=3)

    # Validation
    whole_dv(ws, ["B10:B12", "F10:F12", "J10:J12", "B16:B26", "F16:F26", "J16:J26",
                  "B30:B34", "F30:F34", "F38", "F42:F43"], 0, 10,
             "Enter a whole number from 0 to 10.")
    whole_dv(ws, ["J30:J32"], 1, 5, "Virtues run from 1 to 5.")
    whole_dv(ws, ["F45:F46"], 0, 50, "Enter a whole number from 0 to 50.")

    page_break(ws, 28)
    finish_sheet(ws, "A1:K50")
    return ws


# ---------------------------------------------------------------------------
# Sheet 2 - Merits, Paths & Combat (PDF page 2)
# ---------------------------------------------------------------------------

def build_page2(wb):
    ws = wb.create_sheet("2. Merits, Paths & Combat")
    xh.set_column_widths(ws, {"A": 21, "B": 11.5, "C": 14, "D": 2.2, "E": 21, "F": 11.5,
                              "G": 14, "H": 2.2, "I": 21, "J": 11.5, "K": 14})
    sub_title(ws, 1, "VAMPIRE: THE DARK AGES (V20) \u2014 MERITS, PATHS & COMBAT", 11,
              "Merits and Flaws, extra traits, Blood Sorcery, experience, derangements, weapons and armor.",
              subtitle_lines=1)

    # MERITS AND FLAWS
    xh.style_section_header(ws, 4, 1, 11, "MERITS AND FLAWS", PAL)
    xh.set_row_height(ws, 4, 19.5)
    for c, t in [(1, "Merit"), (2, "Type"), (3, "Cost"), (5, "Flaw"), (6, "Type"), (7, "Bonus")]:
        caption(ws, 5, c, t)
    for r in range(6, 13):
        text_entry(ws, r, 1)
        num_entry(ws, r, 2)
        num_entry(ws, r, 3)
        text_entry(ws, r, 5)
        num_entry(ws, r, 6)
        num_entry(ws, r, 7)
    label(ws, 13, 2, "Total", bold=True, align="right")
    xh.style_formula(ws["C13"], "=SUM(C6:C12)", bold=True)
    label(ws, 13, 6, "Total", bold=True, align="right")
    xh.style_formula(ws["G13"], "=SUM(G6:G12)", bold=True)
    list_dv(ws, ["B6:B12", "F6:F12"], MERIT_TYPES)
    whole_dv(ws, ["C6:C12", "G6:G12"], 0, None, "Enter a whole number of points.")
    note(ws, 14, 1, 11,
         "Merits cost freebie points; Flaws add freebie points, up to 7 in total (V20 Dark Ages quick "
         "reference, p.156; mechanism per V20 core). Merits and Flaws are optional: the Storyteller may set a "
         "different limit of 5, 7 or 10 points (Appendix A, p.419).", lines=2)

    # OTHER TRAITS
    xh.style_section_header(ws, 16, 1, 11, "OTHER TRAITS", PAL)
    xh.set_row_height(ws, 16, 19.5)
    for r in range(17, 20):
        for lc, ic, dc in [(1, 2, 3), (5, 6, 7), (9, 10, 11)]:
            blank_dot_trait(ws, r, lc, ic, dc)
    whole_dv(ws, [f"{c}{r}" for r in range(17, 20) for c in "BFJ"], 0, 10,
             "Enter a whole number from 0 to 10.")

    # RITUALS | PATHS
    xh.style_section_header(ws, 21, 1, 3, "RITUALS", PAL)
    xh.style_section_header(ws, 21, 5, 7, "PATHS", PAL)
    xh.set_row_height(ws, 21, 19.5)
    caption(ws, 22, 1, "Name", c2=2)
    caption(ws, 22, 3, "Level")
    caption(ws, 22, 5, "Path")
    caption(ws, 22, 6, "Rating")
    for r in range(23, 29):
        xh.add_wide_entry(ws, r, 1, 2, value=None)
        num_entry(ws, r, 3)
    for r in range(23, 30):
        blank_dot_trait(ws, r, 5, 6, 7, max_dots=5)
    whole_dv(ws, ["C23:C28"], 0, 10, "Enter a whole number from 0 to 10.")
    whole_dv(ws, ["F23:F29"], 0, 5, "Paths run from 0 to 5.")

    # EXPERIENCE | DERANGEMENTS
    xh.style_section_header(ws, 31, 1, 3, "EXPERIENCE", PAL)
    xh.style_section_header(ws, 31, 5, 7, "DERANGEMENTS", PAL)
    xh.set_row_height(ws, 31, 19.5)
    label(ws, 32, 1, "Total:")
    num_entry(ws, 32, 2)
    label(ws, 33, 1, "Total Spent:")
    num_entry(ws, 33, 2)
    label(ws, 34, 1, "Spent On:")
    xh.add_free_text_block(ws, 35, 5, 1, 3)
    xh.add_free_text_block(ws, 32, 7, 5, 7)
    note(ws, 34, 2, 3, "(log purchases on sheet 6)", size=8.5)

    # COMBAT
    xh.style_section_header(ws, 41, 1, 11, "COMBAT", PAL)
    xh.set_row_height(ws, 41, 19.5)
    spans = [(1, 3, "Weapon/Attack"), (4, 5, "Diff."), (6, 6, "Damage"), (7, 7, "Range"),
             (8, 9, "Rate"), (10, 10, "Clip"), (11, 11, "Conceal")]
    for c1, c2, t in spans:
        caption(ws, 42, c1, t, c2=c2)
    for r in range(43, 49):
        for c1, c2, t in spans:
            align = "left" if c1 == 1 else "center"
            if c1 == c2:
                xh.style_entry(ws.cell(row=r, column=c1), None, align=align)
            else:
                xh.add_wide_entry(ws, r, c1, c2, value=None, align=align)

    # ARMOR (own full-width section directly below Combat)
    xh.style_section_header(ws, 50, 1, 11, "ARMOR", PAL)
    xh.set_row_height(ws, 50, 19.5)
    for lc, lab in [(1, "Class:"), (5, "Rating:"), (9, "Penalty:")]:
        label(ws, 51, lc, lab)
        xh.add_wide_entry(ws, 51, lc + 1, lc + 2, value=None)
    label(ws, 52, 1, "Description:")
    xh.add_free_text_block(ws, 53, 3, 1, 11)

    page_break(ws, 31)
    finish_sheet(ws, "A1:K55")
    return ws


# ---------------------------------------------------------------------------
# Sheet 3 - Backgrounds & Haven (PDF page 3)
# ---------------------------------------------------------------------------

def build_page3(wb):
    ws = wb.create_sheet("3. Backgrounds & Haven")
    xh.set_column_widths(ws, {"A": 21, "B": 11.5, "C": 14, "D": 2.2, "E": 21, "F": 11.5, "G": 14})
    sub_title(ws, 1, "VAMPIRE: THE DARK AGES (V20) \u2014 BACKGROUNDS & HAVEN", 7,
              "Spell out what each Background dot means for your character, then list gear and your haven.",
              subtitle_lines=1)

    r = 4
    xh.style_section_header(ws, r, 1, 7, "EXPANDED BACKGROUNDS", PAL)
    xh.set_row_height(ws, r, 19.5)
    r += 1
    pairs = [("ALLIES", "MENTOR"), ("CONTACTS", "RESOURCES"), ("FAME", "RETAINERS"),
             ("HERD", "STATUS"), ("INFLUENCE", None)]
    for left, right in pairs:
        xh.style_subheader(ws, r, 1, 3, left, PAL)
        if right:
            xh.style_subheader(ws, r, 5, 7, right, PAL)
        else:  # OTHER( ______ ): name the Background in the entry beside the band
            xh.style_subheader(ws, r, 5, 5, "OTHER", PAL)
            xh.add_wide_entry(ws, r, 6, 7, value=None)
        xh.add_free_text_block(ws, r + 1, 3, 1, 3)
        xh.add_free_text_block(ws, r + 1, 3, 5, 7)
        r += 5  # band + 3 lines + 1 spacer row
    note(ws, r - 1, 1, 7,
         "Core Dark Ages also lists Alternate Identity, Domain and Generation; the Companion adds Servants "
         "(pp.112-113). Use OTHER for any of these. Coteries may pool Allies, Contacts, Domain, Herd, "
         "Influence, Resources and Retainers (p.182).", lines=2)
    r += 1

    xh.style_section_header(ws, r, 1, 7, "POSSESSIONS", PAL)
    xh.set_row_height(ws, r, 19.5)
    page_break(ws, r)
    r += 1
    for (left, right, n) in [("GEAR (CARRIED)", "EQUIPMENT (OWNED)", 5),
                             ("FEEDING GROUNDS", "TRANSPORTATION", 4)]:
        xh.style_subheader(ws, r, 1, 3, left, PAL)
        xh.style_subheader(ws, r, 5, 7, right, PAL)
        xh.add_free_text_block(ws, r + 1, n, 1, 3)
        xh.add_free_text_block(ws, r + 1, n, 5, 7)
        r += n + 2

    xh.style_section_header(ws, r, 1, 7, "HAVEN", PAL)
    xh.set_row_height(ws, r, 19.5)
    r += 1
    caption(ws, r, 1, "Location", c2=2)
    caption(ws, r, 3, "Description", c2=7)
    r += 1
    for i in range(4):
        xh.add_wide_entry(ws, r + i, 1, 2, value=None)
        xh.add_wide_entry(ws, r + i, 3, 7, value=None)
    last = r + 3

    finish_sheet(ws, f"A1:G{last}")
    return ws


# ---------------------------------------------------------------------------
# Sheet 4 - History & Description (PDF page 4)
# ---------------------------------------------------------------------------

def build_page4(wb):
    ws = wb.create_sheet("4. History & Description")
    xh.set_column_widths(ws, {"A": 21, "B": 11.5, "C": 14, "D": 2.2, "E": 21, "F": 11.5, "G": 14})
    sub_title(ws, 1, "VAMPIRE: THE DARK AGES (V20) \u2014 HISTORY & DESCRIPTION", 7,
              "Your character's Prelude, goals, appearance and pictures.", subtitle_lines=1)

    r = 4
    xh.style_section_header(ws, r, 1, 7, "HISTORY", PAL)
    xh.set_row_height(ws, r, 19.5)
    xh.style_subheader(ws, r + 1, 1, 7, "PRELUDE", PAL)
    xh.add_free_text_block(ws, r + 2, 10, 1, 7)
    r += 13
    xh.style_subheader(ws, r, 1, 7, "GOALS", PAL)
    xh.add_free_text_block(ws, r + 1, 3, 1, 7)
    r += 5

    xh.style_section_header(ws, r, 1, 7, "DESCRIPTION", PAL)
    xh.set_row_height(ws, r, 19.5)
    page_break(ws, r)
    r += 1
    fields = ["Age:", "Apparent Age:", "Date of Birth:", "R.I.P.:", "Hair:", "Eyes:", "Race:",
              "Nationality:", "Height:", "Weight:", "Sex:"]
    for i, f in enumerate(fields):
        label(ws, r + i, 1, f)
        xh.add_wide_entry(ws, r + i, 2, 3, value=None)
    xh.add_free_text_block(ws, r, 11, 5, 7)  # the PDF's 11 unlabeled lines beside the fields
    r += len(fields) + 1

    xh.style_section_header(ws, r, 1, 7, "VISUALS", PAL)
    xh.set_row_height(ws, r, 19.5)
    r += 1
    xh.style_subheader(ws, r, 1, 3, "COTERIE CHART", PAL)
    xh.style_subheader(ws, r, 5, 7, "CHARACTER SKETCH", PAL)
    xh.add_image_placeholder(ws, r + 1, r + 12, 1, 3,
                             "(space reserved for a coterie chart \u2014 use Insert > Picture)", PAL)
    xh.add_image_placeholder(ws, r + 1, r + 12, 5, 7,
                             "(space reserved for a character sketch \u2014 use Insert > Picture)", PAL)
    last = r + 12

    finish_sheet(ws, f"A1:G{last}")
    return ws


# ---------------------------------------------------------------------------
# Sheet 5 - Character Creation (not on the PDF)
# ---------------------------------------------------------------------------

def build_creation(wb):
    ws = wb.create_sheet("5. Character Creation")
    LAST = 6
    xh.set_column_widths(ws, {"A": 52, "B": 16, "C": 16, "D": 16, "E": 16, "F": 16})
    sub_title(ws, 1, "VAMPIRE: THE DARK AGES (V20) \u2014 CHARACTER CREATION", LAST,
              "A planning worksheet that checks your arithmetic against Chapter Four. It does not read the "
              "other sheets: enter your choices here, then copy the results onto the Front Sheet. "
              "Page references are to V20 Dark Ages unless noted.")

    def header(r, text):
        xh.style_section_header(ws, r, 1, LAST, text, PAL)
        xh.set_row_height(ws, r, 19.5)

    def budget_formula(prio_ref, a, b, c):
        return f'=IF({prio_ref}="Primary",{a},IF({prio_ref}="Secondary",{b},IF({prio_ref}="Tertiary",{c},"")))'

    # ---- STEP 1 ----------------------------------------------------------
    r = 4
    header(r, "STEP 1 \u2014 CONCEPT")
    r += 1
    note(ws, r, 1, LAST,
         "Choose Concept, Clan, Nature, Demeanor and Road on the Front Sheet (identity block and Road box). "
         "Nosferatu start with 0 dots in Appearance instead of 1 (p.152).", lines=2)
    r += 1
    label(ws, r, 1, "Is the character a Nosferatu?")
    xh.style_entry(ws.cell(row=r, column=2), "No", align="center")
    list_dv(ws, [f"B{r}"], ["No", "Yes"])
    NOS = f"$B${r}"
    r += 2

    # ---- STEP 2: Attributes ---------------------------------------------
    header(r, "STEP 2 \u2014 ATTRIBUTES (1 free dot each, then 7 / 5 / 3 by priority)")
    r += 1
    for c, t in enumerate(["Category", "Priority", "Budget", "Free dots", "Dots spent", "Remaining"], 1):
        caption(ws, r, c, t, align="left" if c == 1 else "center")
    r += 1
    cat_rows = {}
    for cat in ["Physical", "Social", "Mental"]:
        cat_rows[cat] = r
        label(ws, r, 1, cat)
        xh.style_entry(ws.cell(row=r, column=2), None, align="center")
        xh.style_formula(ws.cell(row=r, column=3), budget_formula(f"B{r}", 7, 5, 3))
        r += 1
    att_prio_first, att_prio_last = cat_rows["Physical"], cat_rows["Mental"]
    list_dv(ws, [f"B{att_prio_first}:B{att_prio_last}"], PRIORITIES)
    label(ws, r, 1, "Priorities check")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    rng = f"$B${att_prio_first}:$B${att_prio_last}"
    xh.style_formula(
        ws.cell(row=r, column=2),
        f'=IF(AND(COUNTIF({rng},"Primary")=1,COUNTIF({rng},"Secondary")=1,COUNTIF({rng},"Tertiary")=1),'
        f'"OK","Assign Primary, Secondary and Tertiary exactly once")')
    xh.apply_span_border(ws, r, 2, 4)
    r += 2

    caption(ws, r, 1, "Attribute", align="left")
    caption(ws, r, 2, "Category")
    caption(ws, r, 3, "Dots (start at 1)")
    r += 1
    attr_names = {"Physical": ["Strength", "Dexterity", "Stamina"],
                  "Social": ["Charisma", "Manipulation", "Appearance"],
                  "Mental": ["Perception", "Intelligence", "Wits"]}
    attr_first = {}
    for cat, names in attr_names.items():
        attr_first[cat] = r
        for nm in names:
            label(ws, r, 1, nm)
            label(ws, r, 2, cat, align="center")
            xh.style_entry(ws.cell(row=r, column=3), 1, align="center")
            r += 1
    whole_dv(ws, [f"C{attr_first['Physical']}:C{r - 1}"], 0, 5, "Attributes run from 0 to 5 at creation.")
    for cat in ["Physical", "Social", "Mental"]:
        cr = cat_rows[cat]
        a0 = attr_first[cat]
        free = f'=IF({NOS}="Yes",2,3)' if cat == "Social" else 3
        xh.style_formula(ws.cell(row=cr, column=4), free)
        xh.style_formula(ws.cell(row=cr, column=5), f"=SUM(C{a0}:C{a0 + 2})-D{cr}")
        xh.style_formula(ws.cell(row=cr, column=6), f'=IF(C{cr}="","",C{cr}-E{cr})')
        xh.add_budget_flag(ws, f"F{cr}")
    note(ws, r, 1, LAST,
         "Free dots: every Attribute begins at 1 (a Nosferatu's Appearance at 0), so only dots above that count "
         "against the budget (p.152).", lines=1)
    r += 2

    # ---- STEP 3: Abilities ----------------------------------------------
    page_break(ws, r)
    header(r, "STEP 3 \u2014 ABILITIES (13 / 9 / 5 by priority, no Ability above 3)")
    r += 1
    for c, t in enumerate(["Category", "Priority", "Budget", "Dots on Front Sheet", "Remaining"], 1):
        caption(ws, r, c, t, align="left" if c == 1 else "center")
    ws.row_dimensions[r].height = 28
    r += 1
    ab_first = r
    for cat in ["Talents", "Skills", "Knowledges"]:
        label(ws, r, 1, cat)
        xh.style_entry(ws.cell(row=r, column=2), None, align="center")
        xh.style_formula(ws.cell(row=r, column=3), budget_formula(f"B{r}", 13, 9, 5))
        xh.style_entry(ws.cell(row=r, column=4), None, align="center")
        xh.style_formula(ws.cell(row=r, column=5), f'=IF(C{r}="","",C{r}-N(D{r}))')
        xh.add_budget_flag(ws, f"E{r}")
        r += 1
    ab_last = r - 1
    list_dv(ws, [f"B{ab_first}:B{ab_last}"], PRIORITIES)
    whole_dv(ws, [f"D{ab_first}:D{ab_last}"], 0, 30, "Enter the total dots you assigned in this category.")
    label(ws, r, 1, "Priorities check")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    rng = f"$B${ab_first}:$B${ab_last}"
    xh.style_formula(
        ws.cell(row=r, column=2),
        f'=IF(AND(COUNTIF({rng},"Primary")=1,COUNTIF({rng},"Secondary")=1,COUNTIF({rng},"Tertiary")=1),'
        f'"OK","Assign Primary, Secondary and Tertiary exactly once")')
    xh.apply_span_border(ws, r, 2, 4)
    r += 1
    note(ws, r, 1, LAST,
         "Type in the total dots you gave that category's Abilities on the Front Sheet. Abilities start at 0, "
         "and none may exceed 3 dots at this stage; freebie points can raise them later (p.153). Each Ability "
         "you take also needs an Area of Expertise (p.162).", lines=2)
    r += 2

    # ---- STEP 4: Advantages ---------------------------------------------
    header(r, "STEP 4 \u2014 ADVANTAGES (Disciplines 4, Backgrounds 5, Virtues 7)")
    r += 1

    def dot_pool(r, band, first_caption, rows, budget):
        xh.style_subheader(ws, r, 1, LAST, band, PAL)
        r += 1
        caption(ws, r, 1, first_caption, align="left")
        caption(ws, r, 2, "Dots")
        r += 1
        f = r
        for _ in range(rows):
            text_entry(ws, r, 1)
            num_entry(ws, r, 2)
            r += 1
        l = r - 1
        whole_dv(ws, [f"B{f}:B{l}"], 0, 10, "Enter a whole number from 0 to 10.")
        label(ws, r, 1, "Dots used")
        xh.style_formula(ws.cell(row=r, column=2), f"=SUM(B{f}:B{l})", bold=True)
        used = r
        r += 1
        label(ws, r, 1, "Budget")
        xh.style_formula(ws.cell(row=r, column=2), budget)
        bud = r
        r += 1
        label(ws, r, 1, "Remaining")
        xh.style_formula(ws.cell(row=r, column=2), f"=B{bud}-B{used}", bold=True)
        xh.add_budget_flag(ws, f"B{r}")
        return r + 1

    r = dot_pool(r, "DISCIPLINES \u2014 4 dots among your clan's Disciplines", "Discipline", 4, 4)
    note(ws, r, 1, LAST,
         "Disciplines outside your clan can only be bought with freebie points (p.153). Caitiff may pick any, "
         "with Storyteller approval.", lines=1)
    r += 2
    r = dot_pool(r, "BACKGROUNDS \u2014 5 dots", "Background", 5, 5)
    note(ws, r, 1, LAST,
         "Generation, Domain and Herd count as Backgrounds (Step 5 uses them). Caitiff may not buy Status at "
         "creation (p.183). Coteries may pool Backgrounds (p.182).", lines=2)
    r += 2

    page_break(ws, r)
    xh.style_subheader(ws, r, 1, LAST, "VIRTUES \u2014 each starts at 1, then 7 dots among the three", PAL)
    r += 1
    caption(ws, r, 1, "Virtue", align="left")
    caption(ws, r, 2, "Dots (start at 1)")
    r += 1
    virt = {}
    for key, nm in [("cons", "Conscience / Conviction"), ("sc", "Self-Control / Instinct"), ("cour", "Courage")]:
        label(ws, r, 1, nm)
        xh.style_entry(ws.cell(row=r, column=2), 1, align="center")
        virt[key] = r
        r += 1
    whole_dv(ws, [f"B{virt['cons']}:B{virt['cour']}"], 1, 5, "Virtues run from 1 to 5.")
    label(ws, r, 1, "Dots above the free 3")
    xh.style_formula(ws.cell(row=r, column=2), f"=SUM(B{virt['cons']}:B{virt['cour']})-3", bold=True)
    v_used = r
    r += 1
    label(ws, r, 1, "Budget")
    xh.style_formula(ws.cell(row=r, column=2), 7)
    v_bud = r
    r += 1
    label(ws, r, 1, "Remaining")
    xh.style_formula(ws.cell(row=r, column=2), f"=B{v_bud}-B{v_used}", bold=True)
    xh.add_budget_flag(ws, f"B{r}")
    r += 1
    note(ws, r, 1, LAST,
         "Two Virtues come from your Road (Conscience or Conviction, and Self-Control or Instinct); the third "
         "is Courage (p.154).", lines=1)
    r += 2

    # ---- STEP 5: Finishing touches ----------------------------------------
    header(r, "STEP 5 \u2014 FINISHING TOUCHES (Road, Willpower, Generation, Blood Pool)")
    r += 1
    label(ws, r, 1, "Road rating (Cons./Conv. + Self-Control/Instinct)")
    xh.style_key_output(ws.cell(row=r, column=2), f"=B{virt['cons']}+B{virt['sc']}")
    road_row = r
    r += 1
    label(ws, r, 1, "Aura modifier at that rating")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
    xh.style_formula(
        ws.cell(row=r, column=2),
        f'=IF(B{road_row}>=10,"-2 difficulty",IF(B{road_row}>=8,"-1 difficulty",'
        f'IF(B{road_row}>=4,"No modifier",IF(B{road_row}>=2,"+1 difficulty","+2 difficulty"))))')
    xh.apply_span_border(ws, r, 2, 3)
    r += 1
    label(ws, r, 1, "Starting Willpower (equal to Courage)")
    xh.style_key_output(ws.cell(row=r, column=2), f"=B{virt['cour']}")
    r += 2

    xh.style_subheader(ws, r, 1, LAST, "BLOOD POOL AND GENERATION", PAL)
    r += 1
    label(ws, r, 1, "Generation Background dots (0 = Twelfth Generation)")
    num_entry(ws, r, 2, 0)
    whole_dv(ws, [f"B{r}"], 0, 5, "Generation Background runs from 0 to 5.")
    gen = r
    idx = f"MIN(5,MAX(0,N(B{gen})))+1"
    r += 1
    label(ws, r, 1, "Generation")
    xh.style_formula(ws.cell(row=r, column=2),
                     f'=CHOOSE({idx},"Twelfth","Eleventh","Tenth","Ninth","Eighth","Seventh")')
    r += 1
    label(ws, r, 1, "Maximum Blood Pool")
    xh.style_formula(ws.cell(row=r, column=2), f"=CHOOSE({idx},11,12,13,14,15,20)")
    bp_max = r
    r += 1
    label(ws, r, 1, "Blood points you can spend per turn")
    xh.style_formula(ws.cell(row=r, column=2), f"=CHOOSE({idx},1,1,1,2,3,4)")
    r += 1
    label(ws, r, 1, "Max dots in a Trait at this Generation")
    xh.style_formula(ws.cell(row=r, column=2), f"=CHOOSE({idx},5,5,5,5,5,6)")
    r += 1
    label(ws, r, 1, "Domain Background dots")
    num_entry(ws, r, 2)
    dom = r
    r += 1
    label(ws, r, 1, "Herd Background dots")
    num_entry(ws, r, 2)
    herd = r
    whole_dv(ws, [f"B{dom}:B{herd}"], 0, 10, "Enter a whole number from 0 to 10.")
    r += 1
    label(ws, r, 1, "Starting Blood Pool roll (one die)")
    num_entry(ws, r, 2)
    roll = r
    whole_dv(ws, [f"B{roll}"], 1, 10, "Enter the result of one ten-sided die (1-10).")
    r += 1
    label(ws, r, 1, "Starting Blood Pool (roll + Domain + Herd, capped)")
    xh.style_key_output(ws.cell(row=r, column=2),
                        f'=IF(B{roll}="","",MIN(B{bp_max},B{roll}+N(B{dom})+N(B{herd})))')
    r += 1
    note(ws, r, 1, LAST,
         "Without a Generation Background you begin as a Twelfth Generation vampire; each dot lowers it by one "
         "(Seventh at 5 dots). Starting Blood Pool is random: one die plus your Domain and Herd dots, capped at "
         "your Generation's maximum (p.155). Generation chart: p.181 and p.341. Aura modifier by Road rating: p.114.", lines=2)
    r += 2

    # ---- STEP 6: Freebie points ------------------------------------------
    page_break(ws, r)
    header(r, "STEP 6 \u2014 FREEBIE POINTS (15, plus up to 7 from Flaws)")
    r += 1
    for c, t in enumerate(["Trait", "Cost per dot", "Dots / points bought", "Points spent"], 1):
        caption(ws, r, c, t, align="left" if c == 1 else "center")
    ws.row_dimensions[r].height = 28
    r += 1
    fb_first = r
    costs = [("Attributes", 5), ("Abilities", 2), ("Disciplines", 7), ("Blood Sorcery Paths", 4),
             ("Blood Sorcery Rituals (per ritual level)", 1), ("Backgrounds", 1), ("Virtues", 2),
             ("Road", 2), ("Willpower", 1), ("Merits (points of cost)", 1)]
    for nm, cst in costs:
        label(ws, r, 1, nm)
        xh.style_formula(ws.cell(row=r, column=2), cst)
        num_entry(ws, r, 3)
        xh.style_formula(ws.cell(row=r, column=4), f'=IF(C{r}="","",B{r}*C{r})')
        r += 1
    fb_last = r - 1
    whole_dv(ws, [f"C{fb_first}:C{fb_last}"], 0, 100, "Enter a whole number of dots or points.")
    label(ws, r, 1, "Total freebie points spent", bold=True)
    xh.style_formula(ws.cell(row=r, column=4), f"=SUM(D{fb_first}:D{fb_last})", bold=True)
    spent = r
    r += 2
    label(ws, r, 1, "Base freebie points")
    xh.style_entry(ws.cell(row=r, column=2), 15, align="center")
    base = r
    r += 1
    label(ws, r, 1, "Flaw points taken")
    num_entry(ws, r, 2)
    flaws = r
    r += 1
    label(ws, r, 1, "Flaw points allowed (cap)")
    xh.style_entry(ws.cell(row=r, column=2), 7, align="center")
    cap = r
    whole_dv(ws, [f"B{base}:B{cap}"], 0, 100, "Enter a whole number.")
    r += 1
    label(ws, r, 1, "Freebie budget (base + Flaw points up to the cap)")
    xh.style_formula(ws.cell(row=r, column=2), f"=B{base}+MIN(N(B{flaws}),B{cap})", bold=True)
    budget = r
    r += 1
    label(ws, r, 1, "Remaining freebie points", bold=True)
    xh.style_key_output(ws.cell(row=r, column=2), f"=B{budget}-D{spent}")
    xh.add_budget_flag(ws, f"B{r}", final_tally=True)
    r += 1
    note(ws, r, 1, LAST,
         "Costs per dot: p.158. Rituals cost their level; list them on sheet 2. Merits cost freebie points and "
         "Flaws add them, up to 7 (quick reference p.156; the Merit/Flaw exchange follows V20 core's rule, "
         "which Dark Ages mirrors). The Storyteller may set another limit (Appendix A, p.419). In this edition "
         "a rating of 3 in any Ability already counts as mastery (p.155).", lines=3)
    last = r
    finish_sheet(ws, f"A1:F{last}")
    return ws


# ---------------------------------------------------------------------------
# Sheet 6 - Experience & Advancement (not on the PDF)
# ---------------------------------------------------------------------------

def build_xp(wb):
    ws = wb.create_sheet("6. Experience & Advancement")
    LAST = 9
    xh.set_column_widths(ws, {"A": 18, "B": 12, "C": 38, "D": 26, "E": 8, "F": 8,
                              "G": 11, "H": 11, "I": 50})
    sub_title(ws, 1, "VAMPIRE: THE DARK AGES (V20) \u2014 EXPERIENCE & ADVANCEMENT", LAST,
              "Look up what a purchase costs, then log it. Pick the Trait Type, enter the Old and New rating, and "
              "XP Cost and Balance fill in. Only one point per Trait per story (p.185).")

    xh.style_section_header(ws, 4, 1, LAST, "EXPERIENCE COSTS (V20 Dark Ages, p.184)", PAL)
    xh.set_row_height(ws, 4, 19.5)
    caption(ws, 5, 1, "Trait Type", c2=3)
    caption(ws, 5, 4, "Basis")
    caption(ws, 5, 5, "Multiplier", c2=6)
    caption(ws, 5, 7, "Notes", c2=9)
    costs = [
        ("Area of Expertise", "FLAT", 1, "Each extra field of expertise for an Ability (pp.162, 184)."),
        ("New Ability", "FLAT", 3, "First dot in an Ability you do not yet have (p.184)."),
        ("New Discipline", "FLAT", 10, "First dot in a Discipline you do not yet have (p.184)."),
        ("New Path (Necromancy or Thaumaturgy)", "FLAT", 7, "A first Path in Blood Sorcery (p.184)."),
        ("Secondary Path (Necromancy or Thaumaturgy)", "OLD", 4, "Cost: current Path rating x 4 (p.184)."),
        ("Blood Sorcery Ritual", "NEW", 2, "Cost: ritual level x 2. Enter the ritual's level as New (p.184)."),
        ("Attribute", "OLD", 4, "Cost: current rating x 4 (p.184)."),
        ("Ability", "OLD", 2, "Cost: current rating x 2 (p.184)."),
        ("Clan Discipline", "OLD", 5, "Cost: current rating x 5 (p.184)."),
        ("Other Discipline", "OLD", 7, "Cost: current rating x 7 (p.184)."),
        ("Virtue", "OLD", 2, "Cost: current rating x 2. Does not raise Traits based on that Virtue (p.184)."),
        ("Road Virtues", "OLD", 2, "Conscience/Conviction and Self-Control/Instinct: current rating x 2 (p.184)."),
        ("Willpower", "OLD", 1, "Cost: current rating (p.184)."),
        ("Road", "OLD", 2, "Cost: current Road rating x 2 (p.184)."),
        ("Background (Storyteller approval)", "OLD", 2,
         "Usually earned in play; the Storyteller may allow it at current rating x 2 (p.185)."),
    ]
    first = 6
    for i, (nm, basis, mult, nt) in enumerate(costs):
        r = first + i
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
        label(ws, r, 1, nm)
        xh.apply_span_border(ws, r, 1, 3)
        ws.cell(row=r, column=1).border = xh.RULED_LEFT
        xh.style_formula(ws.cell(row=r, column=4), basis)
        ws.merge_cells(start_row=r, start_column=5, end_row=r, end_column=6)
        xh.style_formula(ws.cell(row=r, column=5), mult)
        xh.apply_span_border(ws, r, 5, 6)
        ws.merge_cells(start_row=r, start_column=7, end_row=r, end_column=9)
        c = ws.cell(row=r, column=7)
        xh.style_label(c, nt)
        c.font = Font(name=xh.FONT_NAME, size=9, color=xh.NOTE_FONT)
        xh.apply_span_border(ws, r, 7, 9)
    last_cost = first + len(costs) - 1
    types = f"$A${first}:$A${last_cost}"
    basis_rng = f"$D${first}:$D${last_cost}"
    mult_rng = f"$E${first}:$E${last_cost}"
    r = last_cost + 1
    note(ws, r, 1, LAST,
         "FLAT: fixed cost per purchase. OLD: multiplier x current (old) rating, so raising a Trait from 3 to 4 "
         "costs 3 x multiplier. NEW: multiplier x the new rating. Multi-step rows add each step's cost.", lines=2)

    # Summary
    r += 2
    xh.style_section_header(ws, r, 1, LAST, "XP BALANCE", PAL)
    xh.set_row_height(ws, r, 19.5)
    r += 1
    sum_first = r
    labels = ["Starting XP (banked before you begin logging)", "Total XP earned", "Total XP spent",
              "Current balance"]
    for i, t in enumerate(labels):
        ws.merge_cells(start_row=r + i, start_column=1, end_row=r + i, end_column=3)
        label(ws, r + i, 1, t, bold=(i == 3))
    START, EARNED, SPENT, BAL = (f"$D${r}", f"$D${r + 1}", f"$D${r + 2}", f"$D${r + 3}")
    num_entry(ws, r, 4, 0)
    start_row = r

    # Advancement log location
    log_hdr = r + 6
    log_first = log_hdr + 2
    n_log = 40
    log_last = log_first + n_log - 1
    xh.style_formula(ws.cell(row=r + 1, column=4), f"={START}+SUM($B${log_first}:$B${log_last})")
    xh.style_formula(ws.cell(row=r + 2, column=4), f"=SUM($G${log_first}:$G${log_last})")
    xh.style_key_output(ws.cell(row=r + 3, column=4), f"={EARNED}-{SPENT}")
    xh.add_budget_flag(ws, f"D{r + 3}")
    whole_dv(ws, [f"D{start_row}"], 0, None, "Enter a whole number of experience points.")
    note(ws, r + 4, 1, LAST,
         "Copy Total XP earned and Total XP spent into the Experience box on sheet 2. Typical awards are 2-5 XP "
         "per session, with 3-5 more for a major arc (p.185).", lines=1)

    r = log_hdr
    xh.style_section_header(ws, r, 1, LAST, "ADVANCEMENT LOG", PAL)
    xh.set_row_height(ws, r, 19.5)
    r += 1
    for c, t in enumerate(["Date / Session", "XP Earned", "Trait Type", "Trait Name", "Old", "New",
                           "XP Cost", "Balance", "Notes"], 1):
        caption(ws, r, c, t)
    for i in range(n_log):
        rr = log_first + i
        text_entry(ws, rr, 1)
        num_entry(ws, rr, 2)
        xh.style_entry(ws.cell(row=rr, column=3), None, align="left")
        text_entry(ws, rr, 4)
        num_entry(ws, rr, 5)
        num_entry(ws, rr, 6)
        m = f"MATCH(C{rr},{types},0)"
        cost = (f'=IF(C{rr}="","",IFERROR(IF(INDEX({basis_rng},{m})="FLAT",INDEX({mult_rng},{m}),'
                f'IF(INDEX({basis_rng},{m})="OLD",INDEX({mult_rng},{m})*(N(F{rr})-N(E{rr}))*(N(E{rr})+N(F{rr})-1)/2,'
                f'INDEX({mult_rng},{m})*N(F{rr}))),""))')
        xh.style_formula(ws.cell(row=rr, column=7), cost)
        xh.style_formula(
            ws.cell(row=rr, column=8),
            f'=IF(AND(B{rr}="",G{rr}=""),"",{START}+SUM($B${log_first}:B{rr})-SUM($G${log_first}:G{rr}))',
            bold=True)
        text_entry(ws, rr, 9)
    list_dv(ws, [f"C{log_first}:C{log_last}"], formula=f"={types}")
    whole_dv(ws, [f"B{log_first}:B{log_last}", f"E{log_first}:F{log_last}"], 0, None,
             "Enter a whole number.")
    xh.add_budget_flag(ws, f"H{log_first}:H{log_last}")
    finish_sheet(ws, f"A1:I{log_last}")
    return ws


def main():
    wb = Workbook()
    build_front(wb)
    build_page2(wb)
    build_page3(wb)
    build_page4(wb)
    build_creation(wb)
    build_xp(wb)
    wb.save(OUT)
    print("saved", OUT)


if __name__ == "__main__":
    main()
