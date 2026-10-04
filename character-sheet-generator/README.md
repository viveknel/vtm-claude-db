# V20 Dark Ages character sheet generator

Python that builds an Excel (`.xlsx`) character sheet for *Vampire: The Dark Ages* 20th Anniversary Edition
from the official 4-page interactive PDF sheet, with the rules numbers taken from the `v20-dark-ages` and
`v20-dark-ages-companion` bundles in this library.

The workbook has six sheets: four mirror the PDF pages (dot-track formulas and colour-coded entry cells), plus
a **Character Creation** point-buy checker and an **Experience & Advancement** cost table and log. Neither of
those two is on the PDF; both are built from chapter four of the book.

## Files

| File | Purpose |
|---|---|
| `build_v20_dark_ages_sheet.py` | Builds the workbook. Every sheet, label, rules number and page citation is in here. |
| `xlsx_helpers.py` | Styling and formula helpers (colours, borders, dot-track formula, validations). An unmodified copy of the helper module from the `wod20-character-sheet-builder` skill, kept here so the build runs without it. |
| `verify_recalc.py` | Recalculation test. Fills test characters, has LibreOffice recalculate them, and checks 71 results. |

## Usage

Needs Python 3 and `openpyxl` (`pip install openpyxl`).

```bash
python build_v20_dark_ages_sheet.py                 # writes V20_Dark_Ages_Character_Sheet.xlsx in the current directory
python build_v20_dark_ages_sheet.py my_sheet.xlsx   # or choose the output path
python verify_recalc.py                             # builds a fresh workbook and tests it
python verify_recalc.py my_sheet.xlsx               # or test an existing file
```

`verify_recalc.py` also needs LibreOffice (set the `SOFFICE` environment variable if `soffice` is not on PATH).
openpyxl never evaluates formulas, so this is the check that catches a formula that is present but wrong. The test
characters are Magda, the book's own worked example (Road 7, Willpower 3, Eleventh Generation, max Blood Pool 12,
starting Blood Pool 2, 15 freebie points spent), plus edge cases (Nosferatu, Flaws over the cap, Generation 0 and 5,
bad priority assignment, overspending, negative XP balance).

## Things to know before changing it

- **Page citations are printed pages.** The `v20-dark-ages` chunk database runs one page higher than the printed
  book (the freebie table is DB p.159, printed p.158). Citations in the workbook use printed pages. The Companion's
  database already matches its printed pages.
- **Merit/Flaw freebie rule comes from V20 core.** Dark Ages states the 7-point cap (printed p.156) but not that
  Merits cost freebie points and Flaws add them; that mechanism is V20 core's. The cap is an editable cell on sheet 5.
- **The PDF's "Aura ( )" box** is treated as the Aura difficulty modifier (printed p.114) and calculates from the
  Road rating on the Front Sheet.
- **Sheet 5 does not read sheet 1.** It is a self-contained planning worksheet by design: enter choices there, then
  copy them to the Front Sheet.
- **Blank means blank.** Open-ended tables (Merits, Combat, the XP log) start empty, not full of zeros. Only traits
  with a defined starting state get a value (Attributes 1, Abilities 0, Virtues 1).
- To adapt this for another game, change the data and the palette in the build script (`PAL`) and keep the structure;
  the colour conventions for entry cells (pale yellow) and budget flags (red/green) are deliberately fixed.
