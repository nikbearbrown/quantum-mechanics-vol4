"""vox_scenes.py — The Hidden Rule Behind the Classical Limit of 2
(vox-chsh-arithmetic, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B01, B03, B05, B07, B10, B12, B15 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = arithmetic fact / always-zero column / bound as theorem;
           crimson #BF3339 = quantum violation / 2root2 / gap above classical limit.
Never swap mid-film.

Exclusions: NO quantum correlation formula, NO Tsirelson bound proof, NO loopholes, NO attribution.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 12.0, "B03": 10.0, "B04": 12.0,
    "B05": 5.0,  "B06": 13.0, "B07": 5.0,  "B08": 14.0,
    "B09": 12.0, "B10": 5.0,  "B11": 12.0, "B12": 5.0,
    "B13": 12.0, "B14": 14.0, "B15": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# =============================================================================
# B02 — S axis: classical bound 2 (teal) vs quantum 2root2 (crimson)
# =============================================================================

class B02_SAxis(Scene):
    def construct(self):
        total = DUR["B02"]

        # Horizontal axis
        ax = Line(LEFT * 5.5 + DOWN * 0.5, RIGHT * 5.5 + DOWN * 0.5,
                  color=INK, stroke_width=2)
        ax_lbl = Text("|S|", font=MONO, color=INK, font_size=24)
        ax_lbl.next_to(ax.get_right(), RIGHT, buff=0.15)

        # Scale: 0 at x=-5.5, 4 at x=5.5 → 1 unit = 2.75 px
        def sx(val): return -5.5 + val * 2.75

        zero_tick = Line([sx(0), -0.7, 0], [sx(0), -0.3, 0], color=INK, stroke_width=2)
        zero_lbl = Text("0", font=MONO, color=INK, font_size=20)
        zero_lbl.move_to([sx(0), -1.0, 0])

        # Classical bound at S=2
        cl_x = sx(2)
        cl_tick = Line([cl_x, -0.7, 0], [cl_x, 0.8, 0], color=TEAL, stroke_width=3)
        cl_chip = LabelChip("classical: 2", accent=TEAL, size=22)
        cl_chip.move_to([cl_x, 1.3, 0])

        # Quantum at S=2root2
        q_val = 2 * np.sqrt(2)
        q_x = sx(q_val)
        q_tick = Line([q_x, -0.7, 0], [q_x, 0.8, 0], color=CRIMSON, stroke_width=3)
        q_chip = LabelChip("quantum: 2root2", accent=CRIMSON, size=22)
        q_chip.move_to([q_x, 1.3, 0])

        # Gap bracket
        gap_line = Line([cl_x, -1.3, 0], [q_x, -1.3, 0],
                        color=CRIMSON, stroke_width=2.5)
        gap_tick_l = Line([cl_x, -1.15, 0], [cl_x, -1.45, 0], color=CRIMSON, stroke_width=2)
        gap_tick_r = Line([q_x, -1.15, 0], [q_x, -1.45, 0], color=CRIMSON, stroke_width=2)
        gap_lbl = Text("violation", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        gap_lbl.move_to([(cl_x + q_x) / 2, -1.75, 0])

        self.play(Create(ax), FadeIn(ax_lbl), FadeIn(zero_tick), FadeIn(zero_lbl), run_time=0.4)
        self.play(Create(cl_tick), FadeIn(cl_chip), run_time=0.4)
        self.play(Create(q_tick), FadeIn(q_chip), run_time=0.4)
        self.play(Create(gap_line), Create(gap_tick_l), Create(gap_tick_r),
                  FadeIn(gap_lbl), run_time=0.4)
        self.wait(max(0.5, total - 1.9))


# =============================================================================
# B04 — Lambda assigns A1,A2,B1,B2 values
# =============================================================================

class B04_LambdaBoxes(Scene):
    def construct(self):
        total = DUR["B04"]

        title = Text("Hidden variable lambda assigns:", font=SERIF,
                     color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 2.8)

        # Alice's settings
        alice_lbl = LabelChip("Alice", accent=TEAL, size=22)
        alice_lbl.move_to(LEFT * 4.0 + UP * 1.5)

        box_a1 = RoundedRectangle(corner_radius=0.12, width=2.0, height=1.0)
        box_a1.set_stroke(TEAL, 2).set_fill(GROUND, 0)
        box_a1.move_to(LEFT * 4.0 + UP * 0.4)
        lbl_a1 = Text("A1 = +1 or -1", font=MONO, color=TEAL, font_size=20)
        lbl_a1.move_to(LEFT * 4.0 + UP * 0.4)

        box_a2 = RoundedRectangle(corner_radius=0.12, width=2.0, height=1.0)
        box_a2.set_stroke(TEAL, 2).set_fill(GROUND, 0)
        box_a2.move_to(LEFT * 4.0 + DOWN * 0.9)
        lbl_a2 = Text("A2 = +1 or -1", font=MONO, color=TEAL, font_size=20)
        lbl_a2.move_to(LEFT * 4.0 + DOWN * 0.9)

        # Bob's settings
        bob_lbl = LabelChip("Bob", accent=CRIMSON, size=22)
        bob_lbl.move_to(RIGHT * 4.0 + UP * 1.5)

        box_b1 = RoundedRectangle(corner_radius=0.12, width=2.0, height=1.0)
        box_b1.set_stroke(CRIMSON, 2).set_fill(GROUND, 0)
        box_b1.move_to(RIGHT * 4.0 + UP * 0.4)
        lbl_b1 = Text("B1 = +1 or -1", font=MONO, color=CRIMSON, font_size=20)
        lbl_b1.move_to(RIGHT * 4.0 + UP * 0.4)

        box_b2 = RoundedRectangle(corner_radius=0.12, width=2.0, height=1.0)
        box_b2.set_stroke(CRIMSON, 2).set_fill(GROUND, 0)
        box_b2.move_to(RIGHT * 4.0 + DOWN * 0.9)
        lbl_b2 = Text("B2 = +1 or -1", font=MONO, color=CRIMSON, font_size=20)
        lbl_b2.move_to(RIGHT * 4.0 + DOWN * 0.9)

        lambda_lbl = SerifLabel("one lambda = one assignment", accent=SLATE, size=20)
        lambda_lbl.move_to(DOWN * 2.4)

        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(alice_lbl), FadeIn(bob_lbl), run_time=0.3)
        self.play(Create(box_a1), FadeIn(lbl_a1), Create(box_b1), FadeIn(lbl_b1), run_time=0.4)
        self.play(Create(box_a2), FadeIn(lbl_a2), Create(box_b2), FadeIn(lbl_b2), run_time=0.4)
        self.play(FadeIn(lambda_lbl), run_time=0.3)
        self.wait(max(0.5, total - 1.9))


# =============================================================================
# B06 — Factored form of S
# =============================================================================

class B06_FactoredS(Scene):
    def construct(self):
        total = DUR["B06"]

        title = Text("For one instruction set lambda:", font=SERIF,
                     color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.0)

        line1 = Text("S = A1 * B1 + A1 * B2 + A2 * B1 - A2 * B2", font=MONO,
                     color=INK, font_size=22)
        line1.move_to(UP * 1.8)

        # Factored form on one line: "S = A1(B1+B2)  +  A2(B1-B2)"
        s_eq = Text("S =", font=MONO, color=INK, font_size=26)
        s_eq.move_to(LEFT * 5.2 + UP * 0.6)

        term1 = Text("A1", font=MONO, color=TEAL, font_size=26)
        term1.move_to(LEFT * 3.8 + UP * 0.6)
        bracket1a = Text("(", font=MONO, color=INK, font_size=30)
        bracket1a.move_to(LEFT * 3.1 + UP * 0.6)
        b1_plus_b2 = Text("B1+B2", font=MONO, color=TEAL, font_size=26)
        b1_plus_b2.move_to(LEFT * 2.0 + UP * 0.6)
        bracket1b = Text(")", font=MONO, color=INK, font_size=30)
        bracket1b.move_to(LEFT * 0.9 + UP * 0.6)

        plus = Text("+", font=MONO, color=INK, font_size=28)
        plus.move_to(LEFT * 0.2 + UP * 0.6)

        term2 = Text("A2", font=MONO, color=TEAL, font_size=26)
        term2.move_to(RIGHT * 0.8 + UP * 0.6)
        bracket2a = Text("(", font=MONO, color=INK, font_size=30)
        bracket2a.move_to(RIGHT * 1.5 + UP * 0.6)
        b1_minus_b2 = Text("B1-B2", font=MONO, color=TEAL, font_size=26)
        b1_minus_b2.move_to(RIGHT * 2.6 + UP * 0.6)
        bracket2b = Text(")", font=MONO, color=INK, font_size=30)
        bracket2b.move_to(RIGHT * 3.7 + UP * 0.6)

        note = SerifLabel("B1,B2 each +1 or -1: 4 possible pairs", accent=SLATE, size=20)
        note.move_to(DOWN * 0.8)

        underline = Line(LEFT * 4.5 + UP * 0.28, RIGHT * 4.5 + UP * 0.28,
                         color=TEAL, stroke_width=2)

        self.play(FadeIn(title), run_time=0.3)
        self.play(FadeIn(line1, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(s_eq), run_time=0.2)
        self.play(FadeIn(term1), FadeIn(bracket1a), FadeIn(b1_plus_b2), FadeIn(bracket1b),
                  FadeIn(plus), FadeIn(term2), FadeIn(bracket2a),
                  FadeIn(b1_minus_b2), FadeIn(bracket2b), run_time=0.5)
        self.play(Create(underline), run_time=0.3)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 2.3))


# =============================================================================
# B08 — Four-row table building row by row
# =============================================================================

class B08_FourRowTable(Scene):
    def construct(self):
        total = DUR["B08"]

        # Table header
        col_positions = [-4.5, -2.0, 0.5, 3.0]
        headers = ["B1", "B2", "B1+B2", "B1-B2"]
        header_colors = [CRIMSON, CRIMSON, TEAL, TEAL]

        for x, h, c in zip(col_positions, headers, header_colors):
            lbl = Text(h, font=MONO, color=c, font_size=24)
            lbl.move_to([x, 2.8, 0])
            self.add(lbl)

        sep = Line(LEFT * 5.5 + UP * 2.4, RIGHT * 5.5 + UP * 2.4,
                   color=INK, stroke_width=1)
        self.add(sep)

        # Row data: (B1, B2, B1+B2, B1-B2)
        rows_data = [
            ("+1", "+1", "+2", "0"),
            ("+1", "-1", "0", "+2"),
            ("-1", "+1", "0", "-2"),
            ("-1", "-1", "-2", "0"),
        ]
        y_rows = [1.6, 0.6, -0.4, -1.4]

        for (b1, b2, bsum, bdiff), y in zip(rows_data, y_rows):
            row_grp = VGroup()
            vals = [b1, b2, bsum, bdiff]
            cols = [CRIMSON, CRIMSON, TEAL, TEAL]
            for x, v, c in zip(col_positions, vals, cols):
                t = Text(v, font=MONO, color=c, font_size=24)
                t.move_to([x, y, 0])
                row_grp.add(t)
            self.play(FadeIn(row_grp), run_time=0.5)

        # Observation note
        obs = SerifLabel("one column +/-2, the other 0", accent=TEAL, size=20)
        obs.move_to(DOWN * 2.6)
        self.play(FadeIn(obs, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 3.0))


# =============================================================================
# B09 — Same table with |S(lambda)|=2 column added
# =============================================================================

class B09_TableWithS(Scene):
    def construct(self):
        total = DUR["B09"]

        col_positions = [-5.0, -3.0, -1.0, 1.0, 3.5]
        headers = ["B1", "B2", "B1+B2", "B1-B2", "|S(l)|"]
        header_colors = [CRIMSON, CRIMSON, TEAL, TEAL, TEAL]

        for x, h, c in zip(col_positions, headers, header_colors):
            lbl = Text(h, font=MONO, color=c, font_size=22)
            lbl.move_to([x, 2.8, 0])
            self.add(lbl)

        sep = Line(LEFT * 6.0 + UP * 2.4, RIGHT * 5.5 + UP * 2.4,
                   color=INK, stroke_width=1)
        self.add(sep)

        rows_data = [
            ("+1", "+1", "+2", "0"),
            ("+1", "-1", "0", "+2"),
            ("-1", "+1", "0", "-2"),
            ("-1", "-1", "-2", "0"),
        ]
        y_rows = [1.6, 0.6, -0.4, -1.4]

        for (b1, b2, bsum, bdiff), y in zip(rows_data, y_rows):
            vals = [b1, b2, bsum, bdiff]
            cols_v = [CRIMSON, CRIMSON, TEAL, TEAL]
            for x, v, c in zip(col_positions[:4], vals, cols_v):
                t = Text(v, font=MONO, color=c, font_size=22)
                t.move_to([x, y, 0])
                self.add(t)
            # S column — highlight box
            s_box = RoundedRectangle(corner_radius=0.08, width=1.2, height=0.6)
            s_box.set_stroke(TEAL, 2).set_fill(GROUND, 0)
            s_box.move_to([col_positions[4], y, 0])
            s_lbl = Text("2", font=MONO, color=TEAL, font_size=22)
            s_lbl.move_to([col_positions[4], y, 0])
            self.add(s_box, s_lbl)

        # Animate: highlight all S column boxes
        highlight = SurroundingRectangle(
            VGroup(*[Text("2", font=MONO, color=TEAL, font_size=22).move_to([col_positions[4], y, 0])
                     for y in y_rows]),
            color=TEAL, buff=0.1
        )
        result_lbl = LabelChip("|S(lambda)| = 2 always", accent=TEAL, size=22)
        result_lbl.move_to(DOWN * 2.8)

        self.play(Create(highlight), run_time=0.5)
        self.play(FadeIn(result_lbl, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 1.1))


# =============================================================================
# B11 — All lambda arrows bounded by |S|=2 line
# =============================================================================

class B11_AllLambdas(Scene):
    def construct(self):
        total = DUR["B11"]

        # S axis
        ax = Line(LEFT * 5.5 + DOWN * 0.5, RIGHT * 5.5 + DOWN * 0.5,
                  color=INK, stroke_width=2)
        ax_lbl = Text("|S|", font=MONO, color=INK, font_size=24)
        ax_lbl.next_to(ax.get_right(), RIGHT, buff=0.12)

        def sx(val): return -5.5 + val * 2.75

        bound_tick = Line([sx(2), -0.7, 0], [sx(2), 1.5, 0], color=TEAL, stroke_width=3)
        bound_lbl = LabelChip("|S| = 2", accent=TEAL, size=22)
        bound_lbl.move_to([sx(2), 2.0, 0])

        # Many arrows from various y-levels, all stopping at x=sx(2)
        arrow_ys = [1.5, 0.8, 0.2, -0.1, -0.5, -0.8, -1.5]
        import random
        random.seed(42)
        arrows = VGroup()
        for y in arrow_ys:
            end_x = sx(2) * (1 if y > 0 else -1)
            arr = Arrow([sx(0), y, 0], [end_x, y, 0], color=SLATE,
                        stroke_width=2, buff=0, tip_length=0.15)
            arrows.add(arr)

        theorem_lbl = SerifLabel("not an average — every lambda exactly 2", accent=TEAL, size=20)
        theorem_lbl.move_to(DOWN * 2.8)

        self.play(Create(ax), FadeIn(ax_lbl), run_time=0.3)
        self.play(Create(bound_tick), FadeIn(bound_lbl), run_time=0.4)
        self.play(Create(arrows), run_time=0.6)
        self.play(FadeIn(theorem_lbl, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 1.8))


# =============================================================================
# B13 — Quantum violation: S axis comparison, gap labeled
# =============================================================================

class B13_QuantumGap(Scene):
    def construct(self):
        total = DUR["B13"]

        ax = Line(LEFT * 5.5 + DOWN * 0.5, RIGHT * 5.5 + DOWN * 0.5,
                  color=INK, stroke_width=2)
        ax_lbl = Text("|S|", font=MONO, color=INK, font_size=24)
        ax_lbl.next_to(ax.get_right(), RIGHT, buff=0.12)

        def sx(val): return -5.5 + val * 2.75

        zero_tick = Line([sx(0), -0.7, 0], [sx(0), -0.3, 0], color=INK, stroke_width=2)
        zero_lbl = Text("0", font=MONO, color=INK, font_size=20)
        zero_lbl.move_to([sx(0), -1.0, 0])

        cl_x = sx(2)
        cl_tick = Line([cl_x, -0.7, 0], [cl_x, 0.9, 0], color=TEAL, stroke_width=3)
        cl_chip = LabelChip("classical: 2", accent=TEAL, size=22)
        cl_chip.move_to([cl_x, 1.4, 0])

        q_val = 2 * np.sqrt(2)
        q_x = sx(q_val)
        q_tick = Line([q_x, -0.7, 0], [q_x, 0.9, 0], color=CRIMSON, stroke_width=3)
        q_chip = LabelChip("quantum: 2root2", accent=CRIMSON, size=22)
        q_chip.move_to([q_x, 1.4, 0])

        gap_line = Line([cl_x, -1.3, 0], [q_x, -1.3, 0], color=CRIMSON, stroke_width=2.5)
        gap_tick_l = Line([cl_x, -1.15, 0], [cl_x, -1.45, 0], color=CRIMSON, stroke_width=2)
        gap_tick_r = Line([q_x, -1.15, 0], [q_x, -1.45, 0], color=CRIMSON, stroke_width=2)
        gap_pct = Text("41% above classical", font=SERIF, color=CRIMSON, font_size=20, slant=ITALIC)
        gap_pct.move_to([(cl_x + q_x) / 2, -1.85, 0])

        # Conclusion
        conclusion = SerifLabel("quantum outcomes not pre-assigned +/-1 numbers", accent=CRIMSON, size=20)
        conclusion.move_to(DOWN * 3.0)

        self.play(Create(ax), FadeIn(ax_lbl), FadeIn(zero_tick), FadeIn(zero_lbl), run_time=0.4)
        self.play(Create(cl_tick), FadeIn(cl_chip), run_time=0.3)
        self.play(Create(q_tick), FadeIn(q_chip), run_time=0.3)
        self.play(Create(gap_line), Create(gap_tick_l), Create(gap_tick_r), run_time=0.3)
        self.play(FadeIn(gap_pct, shift=UP * 0.1), run_time=0.3)
        self.play(FadeIn(conclusion, shift=UP * 0.1), run_time=0.3)
        self.wait(max(0.5, total - 2.2))


# =============================================================================
# B14 — Worked example: A1=+1, A2=-1, all four B rows
# =============================================================================

class B14_WorkedExample(Scene):
    def construct(self):
        total = DUR["B14"]

        title = Text("Example: A1 = +1, A2 = -1", font=SERIF,
                     color=INK, font_size=24, slant=ITALIC)
        title.move_to(UP * 3.0)

        col_x = [-5.0, -3.2, -1.2, 0.8, 2.8, 4.8]
        headers = ["B1", "B2", "A1(B1+B2)", "A2(B1-B2)", "S", "|S|"]
        header_colors = [CRIMSON, CRIMSON, TEAL, TEAL, INK, TEAL]
        for x, h, c in zip(col_x, headers, header_colors):
            t = Text(h, font=MONO, color=c, font_size=18)
            t.move_to([x, 2.2, 0])
            self.add(t)
        sep = Line(LEFT * 6.0 + UP * 1.8, RIGHT * 6.0 + UP * 1.8, color=INK, stroke_width=1)
        self.add(sep)

        # A1=+1, A2=-1
        rows = [
            ("+1", "+1", "+2", "0", "+2", "2"),
            ("+1", "-1", "0", "-2", "-2", "2"),
            ("-1", "+1", "0", "+2", "+2", "2"),
            ("-1", "-1", "-2", "0", "-2", "2"),
        ]
        y_rows = [1.1, 0.1, -0.9, -1.9]

        for row_vals, y in zip(rows, y_rows):
            row_grp = VGroup()
            for x, v, c in zip(col_x, row_vals, header_colors):
                t = Text(v, font=MONO, color=c, font_size=18)
                t.move_to([x, y, 0])
                row_grp.add(t)
            self.play(FadeIn(row_grp), run_time=0.4)

        # Highlight last column
        constant_lbl = LabelChip("always 2", accent=TEAL, size=22)
        constant_lbl.move_to(RIGHT * 4.8 + DOWN * 2.7)

        illustrative = SerifLabel("illustrative example", accent=SLATE, size=18)
        illustrative.move_to(DOWN * 3.2)

        self.play(FadeIn(constant_lbl, shift=UP * 0.1), run_time=0.3)
        self.play(FadeIn(illustrative), run_time=0.3)
        self.wait(max(0.5, total - 2.7))
