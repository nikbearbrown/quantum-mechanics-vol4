"""vox_scenes.py — Two Different Labs, the Same Quantum State
(vox-same-density-matrix, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B01, B03, B06, B09, B11, B14 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = z-axis pair / the center / indistinguishable;
           crimson #BF3339 = x-axis pair / the "different" preparation.
Never swap mid-film.

Exclusions: NO partial-trace computation, NO purity/Tr(rho^2), NO Schmidt, NO entanglement.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 9.0,  "B02": 12.0, "B03": 10.0, "B04": 13.0,
    "B05": 13.0, "B06": 5.0,  "B07": 14.0, "B08": 14.0,
    "B09": 5.0,  "B10": 13.0, "B11": 5.0,  "B12": 12.0,
    "B13": 14.0, "B14": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- helpers ----------------------------------------------------------------

def _bloch_circle(radius=2.0, color=INK, cx=0.0, cy=0.0):
    """2D Bloch cross-section circle centered at (cx, cy)."""
    circ = Circle(radius=radius)
    circ.set_stroke(color, 2.5).set_fill(GROUND, 0)
    circ.move_to([cx, cy, 0])
    return circ


def _matrix_2x2(a, b, c, d, label="", accent=TEAL):
    """A 2x2 matrix display as a VGroup."""
    bracket_l = Text("[", font=MONO, color=INK, font_size=42)
    bracket_r = Text("]", font=MONO, color=INK, font_size=42)
    entry_00 = Text(str(a), font=MONO, color=accent, font_size=28)
    entry_01 = Text(str(b), font=MONO, color=INK, font_size=28)
    entry_10 = Text(str(c), font=MONO, color=INK, font_size=28)
    entry_11 = Text(str(d), font=MONO, color=accent, font_size=28)
    # Arrange in grid
    entry_00.move_to([-0.6, 0.32, 0])
    entry_01.move_to([0.6, 0.32, 0])
    entry_10.move_to([-0.6, -0.32, 0])
    entry_11.move_to([0.6, -0.32, 0])
    bracket_l.move_to([-1.1, 0.0, 0])
    bracket_r.move_to([1.1, 0.0, 0])
    grp = VGroup(bracket_l, entry_00, entry_01, entry_10, entry_11, bracket_r)
    if label:
        lbl = Text(label, font=SERIF, color=INK, font_size=22, slant=ITALIC)
        lbl.next_to(grp, LEFT, buff=0.3)
        grp.add(lbl)
    return grp


# =============================================================================
# B02 — Measurement result: every axis gives 50/50 from both labs
# =============================================================================

class B02_MeasurementResults(Scene):
    def construct(self):
        total = DUR["B02"]

        header_a = LabelChip("Lab A", accent=TEAL, size=24)
        header_a.move_to(LEFT * 3.5 + UP * 2.8)
        header_b = LabelChip("Lab B", accent=CRIMSON, size=24)
        header_b.move_to(RIGHT * 3.5 + UP * 2.8)

        # Separator (stops at DOWN*1.8 so same_lbl at DOWN*2.4 clears it)
        mid_line = Line(UP * 3.2, DOWN * 1.8, color=INK, stroke_width=1)
        mid_line.set_opacity(0.3)

        axes = ["Z-axis", "X-axis", "Y-axis"]
        y_pos = [1.2, 0.0, -1.2]

        rows_a = []
        rows_b = []
        for ax, y in zip(axes, y_pos):
            ax_lbl = Text(ax, font=SERIF, color=SLATE, font_size=24, slant=ITALIC)
            ax_lbl.move_to([0.0, y, 0])
            result_a = Text("50 / 50", font=MONO, color=TEAL, font_size=26)
            result_a.move_to([-3.5, y, 0])
            result_b = Text("50 / 50", font=MONO, color=CRIMSON, font_size=26)
            result_b.move_to([3.5, y, 0])
            rows_a.append((ax_lbl, result_a, result_b))

        self.play(FadeIn(header_a), FadeIn(header_b), Create(mid_line), run_time=0.5)
        for (ax_lbl, result_a, result_b) in rows_a:
            self.play(FadeIn(ax_lbl), FadeIn(result_a), FadeIn(result_b), run_time=0.4)

        same_lbl = SerifLabel("identical from both", accent=SLATE, size=22)
        same_lbl.move_to(DOWN * 2.4)
        self.play(FadeIn(same_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.5))


# =============================================================================
# B04 — Lab A density matrix: (1/2)|0><0| + (1/2)|1><1| = I/2
# =============================================================================

class B04_LabAMatrix(Scene):
    def construct(self):
        total = DUR["B04"]

        title = Text("Lab A", font=SERIF, color=TEAL, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.0)

        mix_lbl = Text("1/2  |0><0|  +  1/2  |1><1|", font=MONO, color=INK, font_size=26)
        mix_lbl.move_to(UP * 1.6)

        arrow = Text("=", font=MONO, color=INK, font_size=32)
        arrow.move_to(UP * 0.4)

        mat = _matrix_2x2("1/2", "0", "0", "1/2", accent=TEAL)
        mat.move_to(DOWN * 0.6)

        result_lbl = Text("=  I/2", font=MONO, color=TEAL, font_size=30)
        result_lbl.move_to(DOWN * 2.0)

        # Teal accent underline for result (gives the gate a shape to track)
        underline = Line(LEFT * 1.1 + DOWN * 2.35, RIGHT * 1.1 + DOWN * 2.35,
                         color=TEAL, stroke_width=3)

        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(mix_lbl, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(arrow), FadeIn(mat), run_time=0.5)
        self.play(FadeIn(result_lbl), run_time=0.3)
        self.play(Create(underline), run_time=0.3)
        self.wait(max(0.5, total - 2.1))


# =============================================================================
# B05 — Lab B density matrix: (1/2)|+><+| + (1/2)|-><-| = I/2
# =============================================================================

class B05_LabBMatrix(Scene):
    def construct(self):
        total = DUR["B05"]

        title = Text("Lab B", font=SERIF, color=CRIMSON, font_size=28, slant=ITALIC)
        title.move_to(UP * 3.0)

        mix_lbl = Text("1/2  |+><+|  +  1/2  |-><-|", font=MONO, color=INK, font_size=26)
        mix_lbl.move_to(UP * 1.6)

        arrow = Text("=", font=MONO, color=INK, font_size=32)
        arrow.move_to(UP * 0.4)

        mat = _matrix_2x2("1/2", "0", "0", "1/2", accent=CRIMSON)
        mat.move_to(DOWN * 0.6)

        result_lbl = Text("=  I/2", font=MONO, color=CRIMSON, font_size=30)
        result_lbl.move_to(DOWN * 2.0)

        same_box = SerifLabel("same matrix as Lab A", accent=SLATE, size=22)
        same_box.move_to(DOWN * 3.0)

        # Crimson accent underline (gives the gate a shape to track)
        underline = Line(LEFT * 1.1 + DOWN * 2.35, RIGHT * 1.1 + DOWN * 2.35,
                         color=CRIMSON, stroke_width=3)

        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(mix_lbl, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(arrow), FadeIn(mat), run_time=0.5)
        self.play(FadeIn(result_lbl, shift=UP * 0.1), run_time=0.4)
        self.play(Create(underline), run_time=0.3)
        self.play(FadeIn(same_box, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 2.5))


# =============================================================================
# B07 — Bloch ball: pure states on surface, mixed inside, center at I/2
# =============================================================================

class B07_BlochBall(Scene):
    def construct(self):
        total = DUR["B07"]

        circ = _bloch_circle(radius=2.8, color=SLATE)
        circ.move_to([0.0, 0.0, 0])

        # Cardinal points
        north = Dot(radius=0.12, color=TEAL).move_to([0.0, 2.8, 0])
        south = Dot(radius=0.12, color=TEAL).move_to([0.0, -2.8, 0])
        east  = Dot(radius=0.12, color=CRIMSON).move_to([2.8, 0.0, 0])
        west  = Dot(radius=0.12, color=CRIMSON).move_to([-2.8, 0.0, 0])
        center = Dot(radius=0.18, color=GOLD).move_to([0.0, 0.0, 0])

        north_lbl = Text("|0>", font=MONO, color=TEAL, font_size=22)
        north_lbl.move_to([0.55, 3.0, 0])
        south_lbl = Text("|1>", font=MONO, color=TEAL, font_size=22)
        south_lbl.move_to([0.55, -3.0, 0])
        east_lbl = Text("|+>", font=MONO, color=CRIMSON, font_size=22)
        east_lbl.move_to([3.3, 0.0, 0])
        west_lbl = Text("|->", font=MONO, color=CRIMSON, font_size=22)
        west_lbl.move_to([-3.3, 0.0, 0])
        center_lbl = Text("I/2", font=MONO, color=INK, font_size=22)
        center_lbl.move_to([0.55, 0.25, 0])

        surface_note = SerifLabel("pure states: surface", accent=SLATE, size=20)
        surface_note.move_to(LEFT * 3.5 + UP * 2.5)
        center_note = SerifLabel("maximally mixed: center", accent=SLATE, size=20)
        center_note.move_to(RIGHT * 3.0 + DOWN * 2.5)

        self.play(Create(circ), run_time=0.5)
        self.play(FadeIn(north), FadeIn(south), FadeIn(north_lbl), FadeIn(south_lbl), run_time=0.4)
        self.play(FadeIn(east), FadeIn(west), FadeIn(east_lbl), FadeIn(west_lbl), run_time=0.4)
        self.play(FadeIn(center), FadeIn(center_lbl), run_time=0.3)
        self.play(FadeIn(surface_note), FadeIn(center_note), run_time=0.4)
        self.wait(max(0.5, total - 2.2))


# =============================================================================
# B08 — Two pairs of arrows converge to center: z-pair (teal) and x-pair (crimson)
# =============================================================================

class B08_TwoPairsOneCenter(Scene):
    def construct(self):
        total = DUR["B08"]

        circ = _bloch_circle(radius=2.4, color=SLATE)
        center = Dot(radius=0.18, color=GOLD).move_to([0.0, 0.0, 0])

        # North and south poles (Lab A / z-axis pair)
        north = Dot(radius=0.12, color=TEAL).move_to([0.0, 2.4, 0])
        south = Dot(radius=0.12, color=TEAL).move_to([0.0, -2.4, 0])
        north_lbl = Text("|0>", font=MONO, color=TEAL, font_size=22)
        north_lbl.move_to([0.55, 2.6, 0])
        south_lbl = Text("|1>", font=MONO, color=TEAL, font_size=22)
        south_lbl.move_to([0.55, -2.6, 0])

        # East and west poles (Lab B / x-axis pair)
        east = Dot(radius=0.12, color=CRIMSON).move_to([2.4, 0.0, 0])
        west = Dot(radius=0.12, color=CRIMSON).move_to([-2.4, 0.0, 0])
        east_lbl = Text("|+>", font=MONO, color=CRIMSON, font_size=22)
        east_lbl.move_to([2.85, 0.25, 0])
        west_lbl = Text("|->", font=MONO, color=CRIMSON, font_size=22)
        west_lbl.move_to([-2.85, 0.25, 0])

        # Arrows: poles → center
        arr_n = Arrow([0.0, 2.4, 0], [0.0, 0.22, 0], color=TEAL,
                      stroke_width=3, buff=0, tip_length=0.2)
        arr_s = Arrow([0.0, -2.4, 0], [0.0, -0.22, 0], color=TEAL,
                      stroke_width=3, buff=0, tip_length=0.2)
        arr_e = Arrow([2.4, 0.0, 0], [0.22, 0.0, 0], color=CRIMSON,
                      stroke_width=3, buff=0, tip_length=0.2)
        arr_w = Arrow([-2.4, 0.0, 0], [-0.22, 0.0, 0], color=CRIMSON,
                      stroke_width=3, buff=0, tip_length=0.2)

        lab_a_note = LabelChip("Lab A: midpoint", accent=TEAL, size=20)
        lab_a_note.move_to(LEFT * 4.2 + UP * 2.4)
        lab_b_note = LabelChip("Lab B: midpoint", accent=CRIMSON, size=20)
        lab_b_note.move_to(RIGHT * 3.8 + DOWN * 2.4)

        self.play(Create(circ), FadeIn(center), run_time=0.4)
        self.play(FadeIn(north), FadeIn(south), FadeIn(north_lbl), FadeIn(south_lbl),
                  FadeIn(east), FadeIn(west), FadeIn(east_lbl), FadeIn(west_lbl), run_time=0.4)
        self.play(Create(arr_n), Create(arr_s), FadeIn(lab_a_note), run_time=0.5)
        self.play(Create(arr_e), Create(arr_w), FadeIn(lab_b_note), run_time=0.5)
        self.wait(max(0.5, total - 2.1))


# =============================================================================
# B10 — Many antipodal pairs all converge to the same center
# =============================================================================

class B10_ManyPairs(Scene):
    def construct(self):
        total = DUR["B10"]

        circ = _bloch_circle(radius=2.6, color=SLATE)
        center = Dot(radius=0.20, color=GOLD).move_to([0.0, 0.0, 0])

        # Four antipodal pairs at different angles
        angles = [90, 0, 45, 135]  # degrees
        pair_dots = VGroup()
        arrows = VGroup()
        for deg in angles:
            rad = deg * PI / 180
            px, py = 2.6 * np.cos(rad), 2.6 * np.sin(rad)
            d1 = Dot(radius=0.10, color=TEAL).move_to([px, py, 0])
            d2 = Dot(radius=0.10, color=TEAL).move_to([-px, -py, 0])
            a1 = Arrow([px, py, 0], [px * 0.10, py * 0.10, 0],
                       color=TEAL, stroke_width=2, buff=0, tip_length=0.18)
            a2 = Arrow([-px, -py, 0], [-px * 0.10, -py * 0.10, 0],
                       color=TEAL, stroke_width=2, buff=0, tip_length=0.18)
            pair_dots.add(d1, d2)
            arrows.add(a1, a2)

        note = SerifLabel("any axis — same center", accent=SLATE, size=22)
        note.move_to(DOWN * 3.1)
        center_lbl = Text("I/2", font=MONO, color=INK, font_size=24)
        center_lbl.move_to([0.6, 0.3, 0])

        self.play(Create(circ), FadeIn(center), FadeIn(center_lbl), run_time=0.4)
        self.play(FadeIn(pair_dots), run_time=0.4)
        self.play(Create(arrows), run_time=0.6)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 1.9))


# =============================================================================
# B12 — Density matrix is a prediction machine, not a history record
# =============================================================================

class B12_PredictionMachine(Scene):
    def construct(self):
        total = DUR["B12"]

        header = Text("What the density matrix encodes:", font=SERIF,
                      color=INK, font_size=26, slant=ITALIC)
        header.move_to(UP * 2.6)

        pred_box = RoundedRectangle(corner_radius=0.18, width=7.5, height=1.4)
        pred_box.set_stroke(TEAL, 2.5).set_fill(GROUND, 0)
        pred_box.move_to(UP * 1.0)
        pred_txt = Text("measurement predictions", font=SERIF, color=TEAL,
                        font_size=26, slant=ITALIC)
        pred_txt.move_to(UP * 1.0)

        not_box = RoundedRectangle(corner_radius=0.18, width=7.5, height=1.4)
        not_box.set_stroke(CRIMSON, 2.5).set_fill(GROUND, 0)
        not_box.move_to(DOWN * 0.6)
        not_txt = Text("preparation history", font=SERIF, color=CRIMSON,
                       font_size=26, slant=ITALIC)
        not_txt.move_to(DOWN * 0.6)
        cross = Line(not_box.get_left() + RIGHT * 0.3, not_box.get_right() + LEFT * 0.3,
                     color=CRIMSON, stroke_width=3)

        conclusion = SerifLabel("same predictions = same state", accent=TEAL, size=22)
        conclusion.move_to(DOWN * 2.2)

        self.play(FadeIn(header), run_time=0.3)
        self.play(Create(pred_box), FadeIn(pred_txt), run_time=0.5)
        self.play(Create(not_box), FadeIn(not_txt), run_time=0.4)
        self.play(Create(cross), run_time=0.3)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 2.1))


# =============================================================================
# B13 — QKD example: two stations → same ρ → same security treatment
# =============================================================================

class B13_QKDExample(Scene):
    def construct(self):
        total = DUR["B13"]

        # Station Z box
        box_z = RoundedRectangle(corner_radius=0.15, width=3.0, height=1.4)
        box_z.set_stroke(TEAL, 2.5).set_fill(GROUND, 0)
        box_z.move_to(LEFT * 4.5 + UP * 0.8)
        lbl_z = Text("Station Z", font=SERIF, color=TEAL, font_size=24, slant=ITALIC)
        lbl_z.move_to(LEFT * 4.5 + UP * 1.1)
        sub_z = Text("|0>,|1> mix", font=MONO, color=TEAL, font_size=18)
        sub_z.move_to(LEFT * 4.5 + UP * 0.5)

        # Station X box
        box_x = RoundedRectangle(corner_radius=0.15, width=3.0, height=1.4)
        box_x.set_stroke(CRIMSON, 2.5).set_fill(GROUND, 0)
        box_x.move_to(LEFT * 4.5 + DOWN * 0.8)
        lbl_x = Text("Station X", font=SERIF, color=CRIMSON, font_size=24, slant=ITALIC)
        lbl_x.move_to(LEFT * 4.5 + DOWN * 0.5)
        sub_x = Text("|+>,|-> mix", font=MONO, color=CRIMSON, font_size=18)
        sub_x.move_to(LEFT * 4.5 + DOWN * 1.1)

        # Arrows to rho box
        arr_z = Arrow(LEFT * 3.0 + UP * 0.8, LEFT * 1.2 + UP * 0.15,
                      color=TEAL, stroke_width=2, buff=0, tip_length=0.2)
        arr_x = Arrow(LEFT * 3.0 + DOWN * 0.8, LEFT * 1.2 + DOWN * 0.15,
                      color=CRIMSON, stroke_width=2, buff=0, tip_length=0.2)

        # rho = I/2 box
        rho_box = RoundedRectangle(corner_radius=0.18, width=2.4, height=1.6)
        rho_box.set_stroke(SLATE, 2.5).set_fill(GROUND, 0)
        rho_box.move_to(ORIGIN)
        rho_lbl = Text("rho = I/2", font=MONO, color=INK, font_size=26)
        rho_lbl.move_to(ORIGIN)

        # Arrow to result
        arr_r = Arrow(RIGHT * 1.2, RIGHT * 2.6,
                      color=SLATE, stroke_width=2, buff=0, tip_length=0.2)

        # Result box
        result_box = RoundedRectangle(corner_radius=0.15, width=3.0, height=1.6)
        result_box.set_stroke(SLATE, 2).set_fill(GROUND, 0)
        result_box.move_to(RIGHT * 4.1)
        result_lbl = Text("same security", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        result_lbl.move_to(RIGHT * 4.1 + UP * 0.25)
        result_sub = Text("treatment", font=SERIF, color=SLATE, font_size=22, slant=ITALIC)
        result_sub.move_to(RIGHT * 4.1 + DOWN * 0.25)

        illustrative = SerifLabel("illustrative example", accent=SLATE, size=18)
        illustrative.move_to(DOWN * 2.8)

        self.play(Create(box_z), FadeIn(lbl_z), FadeIn(sub_z),
                  Create(box_x), FadeIn(lbl_x), FadeIn(sub_x), run_time=0.5)
        self.play(Create(arr_z), Create(arr_x), run_time=0.4)
        self.play(Create(rho_box), FadeIn(rho_lbl), run_time=0.4)
        self.play(Create(arr_r),
                  Create(result_box), FadeIn(result_lbl), FadeIn(result_sub), run_time=0.4)
        self.play(FadeIn(illustrative, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 2.3))
