"""vox_scenes.py — When Fixing One Qubit Breaks Two
(vox-fault-tolerance, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B01, B04, B05, B08, B10, B12, B14 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = fault-tolerant design / contained error / correctable;
           crimson #BF3339 = error propagation / two data-qubit errors / code failure.
Never swap mid-film.

Exclusions: NO stabilizer group formalism, NO surface-code lattice,
            NO threshold theorem formula, NO magic-state distillation.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 12.0, "B03": 12.0, "B04": 10.0,
    "B05":  5.0, "B06": 14.0, "B07": 12.0, "B08":  5.0,
    "B09": 13.0, "B10":  5.0, "B11": 14.0, "B12":  5.0,
    "B13": 14.0, "B14": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ─── helpers ──────────────────────────────────────────────────────────────────

def wire(y, x_left=-5.5, x_right=5.5, color=INK, sw=2):
    """Horizontal qubit wire."""
    return Line([x_left, y, 0], [x_right, y, 0], color=color, stroke_width=sw)

def cnot_control(cx, cy, radius=0.18):
    """Filled control dot for CNOT."""
    return Dot(point=[cx, cy, 0], radius=radius, color=INK)

def cnot_target(cx, cy, radius=0.30):
    """Open circle with cross for CNOT target."""
    circle = Circle(radius=radius, color=INK, stroke_width=2).move_to([cx, cy, 0])
    hbar = Line([cx - radius, cy, 0], [cx + radius, cy, 0], color=INK, stroke_width=2)
    vbar = Line([cx, cy - radius, 0], [cx, cy + radius, 0], color=INK, stroke_width=2)
    return VGroup(circle, hbar, vbar)

def cnot_vertical(cx, y1, y2, color=INK):
    """Vertical line connecting control to target."""
    return Line([cx, y1, 0], [cx, y2, 0], color=color, stroke_width=2)

def wire_label(text, y, x=-5.8, color=INK, fs=22):
    """Label at left end of qubit wire."""
    lbl = Text(text, font=SANS, color=color, font_size=fs)
    lbl.move_to([x, y, 0])
    return lbl

def x_error_box(cx, cy, size=0.32, color=CRIMSON):
    """X-error marker: filled square with X label."""
    box = Square(side_length=size, color=color, fill_color=color,
                 fill_opacity=1.0, stroke_width=0).move_to([cx, cy, 0])
    lbl = Text("X", font=MONO, color=GROUND, font_size=18).move_to([cx, cy, 0])
    return VGroup(box, lbl)


# =============================================================================
# B02 — clean syndrome circuit: ancilla → CNOT → Q1, CNOT → Q2
# =============================================================================

class B02_SyndromeCktClean(Scene):
    def construct(self):
        total = DUR["B02"]

        # Wire y-positions: ancilla=1.2, Q1=0.0, Q2=-1.4
        y_anc = 1.2
        y_q1  = 0.0
        y_q2  = -1.4

        w_anc = wire(y_anc, x_left=-4.8, x_right=4.8)
        w_q1  = wire(y_q1,  x_left=-4.8, x_right=4.8)
        w_q2  = wire(y_q2,  x_left=-4.8, x_right=4.8)

        lbl_anc = wire_label("ancilla", y_anc, x=-5.5)
        lbl_q1  = wire_label("Q1",      y_q1,  x=-5.5)
        lbl_q2  = wire_label("Q2",      y_q2,  x=-5.5)

        # Gate 1: ancilla controls Q1 at x=-1.5
        g1x = -1.5
        ctrl1 = cnot_control(g1x, y_anc)
        tgt1  = cnot_target(g1x, y_q1)
        vline1 = cnot_vertical(g1x, y_anc, y_q1)

        gate1_lbl = Text("gate 1", font=SANS, color=SLATE, font_size=18)
        gate1_lbl.move_to([g1x, y_anc + 0.55, 0])

        # Gate 2: ancilla controls Q2 at x=1.5
        g2x = 1.5
        ctrl2 = cnot_control(g2x, y_anc)
        tgt2  = cnot_target(g2x, y_q2)
        vline2 = cnot_vertical(g2x, y_anc, y_q2)

        gate2_lbl = Text("gate 2", font=SANS, color=SLATE, font_size=18)
        gate2_lbl.move_to([g2x, y_anc + 0.55, 0])

        # Measure box for ancilla at x=3.8
        mbox = Rectangle(width=0.7, height=0.5, color=INK, stroke_width=2)
        mbox.move_to([3.8, y_anc, 0])
        m_lbl = Text("M", font=MONO, color=INK, font_size=20).move_to([3.8, y_anc, 0])

        # Caption
        cap = Text("one ancilla · two CNOTs · measures parity",
                   font=SANS, color=SLATE, font_size=22)
        cap.move_to([0, -2.8, 0])

        wires = VGroup(w_anc, w_q1, w_q2)
        labels = VGroup(lbl_anc, lbl_q1, lbl_q2)
        gate1_group = VGroup(vline1, ctrl1, tgt1)
        gate2_group = VGroup(vline2, ctrl2, tgt2)
        measure_group = VGroup(mbox, m_lbl)

        self.add(wires, labels)
        self.play(FadeIn(labels), run_time=0.5)
        self.play(Create(gate1_group), FadeIn(gate1_lbl), run_time=0.8)
        self.play(Create(gate2_group), FadeIn(gate2_lbl), run_time=0.8)
        self.play(FadeIn(measure_group), run_time=0.5)
        self.play(FadeIn(cap), run_time=0.5)
        remaining = total - 3.1
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B03 — same circuit with X error on ancilla at gate 1
# =============================================================================

class B03_SyndromeCktError(Scene):
    def construct(self):
        total = DUR["B03"]

        y_anc = 1.2
        y_q1  = 0.0
        y_q2  = -1.4

        w_anc = wire(y_anc, x_left=-4.8, x_right=4.8)
        w_q1  = wire(y_q1,  x_left=-4.8, x_right=4.8)
        w_q2  = wire(y_q2,  x_left=-4.8, x_right=4.8)

        lbl_anc = wire_label("ancilla", y_anc, x=-5.5)
        lbl_q1  = wire_label("Q1",      y_q1,  x=-5.5)
        lbl_q2  = wire_label("Q2",      y_q2,  x=-5.5)

        g1x = -1.5
        ctrl1 = cnot_control(g1x, y_anc)
        tgt1  = cnot_target(g1x, y_q1)
        vline1 = cnot_vertical(g1x, y_anc, y_q1)
        gate1_lbl = Text("gate 1", font=SANS, color=SLATE, font_size=18)
        gate1_lbl.move_to([g1x, y_anc + 0.55, 0])

        g2x = 1.5
        ctrl2 = cnot_control(g2x, y_anc)
        tgt2  = cnot_target(g2x, y_q2)
        vline2 = cnot_vertical(g2x, y_anc, y_q2)
        gate2_lbl = Text("gate 2", font=SANS, color=SLATE, font_size=18)
        gate2_lbl.move_to([g2x, y_anc + 0.55, 0])

        mbox = Rectangle(width=0.7, height=0.5, color=INK, stroke_width=2)
        mbox.move_to([3.8, y_anc, 0])
        m_lbl = Text("M", font=MONO, color=INK, font_size=20).move_to([3.8, y_anc, 0])

        # X error on ancilla wire BEFORE gate 1 (between wire start and g1x)
        err = x_error_box(-3.0, y_anc)

        # Caption
        cap = Text("ancilla error at gate 1 — one gate fails",
                   font=SANS, color=CRIMSON, font_size=22)
        cap.move_to([0, -2.8, 0])

        self.add(wire(y_anc, x_left=-4.8, x_right=4.8),
                 wire(y_q1,  x_left=-4.8, x_right=4.8),
                 wire(y_q2,  x_left=-4.8, x_right=4.8),
                 lbl_anc, lbl_q1, lbl_q2)
        self.play(
            Create(VGroup(vline1, ctrl1, tgt1)),
            FadeIn(gate1_lbl),
            run_time=0.6,
        )
        self.play(
            Create(VGroup(vline2, ctrl2, tgt2)),
            FadeIn(gate2_lbl),
            run_time=0.6,
        )
        self.play(FadeIn(VGroup(mbox, m_lbl)), run_time=0.4)
        self.play(FadeIn(err), run_time=0.5)
        self.play(FadeIn(cap), run_time=0.5)
        remaining = total - 2.6
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B06 — error propagates through gate 2 onto Q2
# =============================================================================

class B06_ErrorPropagation(Scene):
    def construct(self):
        total = DUR["B06"]

        y_anc = 1.2
        y_q1  = 0.0
        y_q2  = -1.4

        w_anc = wire(y_anc, x_left=-4.8, x_right=4.8)
        w_q1  = wire(y_q1,  x_left=-4.8, x_right=4.8)
        w_q2  = wire(y_q2,  x_left=-4.8, x_right=4.8)

        lbl_anc = wire_label("ancilla", y_anc, x=-5.5)
        lbl_q1  = wire_label("Q1",      y_q1,  x=-5.5)
        lbl_q2  = wire_label("Q2",      y_q2,  x=-5.5)

        g1x = -1.5
        ctrl1 = cnot_control(g1x, y_anc)
        tgt1  = cnot_target(g1x, y_q1)
        vline1 = cnot_vertical(g1x, y_anc, y_q1)

        g2x = 1.5
        ctrl2 = cnot_control(g2x, y_anc, radius=0.18)
        tgt2  = cnot_target(g2x, y_q2)
        vline2 = cnot_vertical(g2x, y_anc, y_q2, color=CRIMSON)

        # Error on ancilla before gate 1
        err_anc = x_error_box(-3.0, y_anc)

        # Error on ancilla between gates (shows corrupted state)
        err_anc2 = x_error_box(0.0, y_anc, color=CRIMSON)

        # Error propagated to Q2 after gate 2
        err_q2 = x_error_box(3.0, y_q2, color=CRIMSON)

        # Propagation arrow from ancilla error to Q2 error
        arrow = Arrow(
            start=[g2x, y_anc - 0.3, 0],
            end=[g2x, y_q2 + 0.45, 0],
            color=CRIMSON, stroke_width=3, buff=0.05,
        )

        # Labels
        two_err_lbl = Text("2 data errors", font=SANS, color=CRIMSON, font_size=22)
        two_err_lbl.move_to([3.6, -2.3, 0])

        cap = Text("one ancilla error → copied to Q2 via gate 2",
                   font=SANS, color=CRIMSON, font_size=22)
        cap.move_to([0, -3.0, 0])

        self.add(w_anc, w_q1, w_q2, lbl_anc, lbl_q1, lbl_q2)
        self.play(
            Create(VGroup(vline1, ctrl1, tgt1)),
            Create(VGroup(vline2, ctrl2, tgt2)),
            run_time=0.8,
        )
        self.play(FadeIn(err_anc), run_time=0.5)
        self.play(FadeIn(err_anc2), run_time=0.4)
        self.play(Create(arrow), FadeIn(err_q2), run_time=0.8)
        self.play(FadeIn(two_err_lbl), run_time=0.4)
        self.play(FadeIn(cap), run_time=0.5)
        remaining = total - 3.4
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B07 — syndrome table: 2-qubit flip → wrong correction
# =============================================================================

class B07_WrongCorrection(Scene):
    def construct(self):
        total = DUR["B07"]

        title = Text("syndrome table", font=SANS, color=INK, font_size=26)
        title.move_to([0, 3.0, 0])

        # Underline for shape recording
        underline = Line(LEFT * 2.5 + UP * 2.65, RIGHT * 2.5 + UP * 2.65,
                         color=INK, stroke_width=2)

        # Column headers
        col_x = [-4.0, -1.8,  0.2,  2.2,  4.2]
        hdr_texts = ["syndrome", "Q1 flip", "Q2 flip", "Q3 flip", "correction"]
        hdrs = VGroup(*[
            Text(t, font=SANS, color=SLATE, font_size=20).move_to([col_x[i], 2.0, 0])
            for i, t in enumerate(hdr_texts)
        ])

        # Header divider
        hdr_line = Line(LEFT * 5.5 + UP * 1.6, RIGHT * 5.5 + UP * 1.6,
                        color=SLATE, stroke_width=1.5)

        # Row data: (syndrome, Q1, Q2, Q3, correction)
        rows = [
            ("00", "—", "—", "—", "none"),
            ("01", "✓", "—", "—", "fix Q1"),
            ("10", "—", "✓", "—", "fix Q2"),
            ("11", "—", "—", "✓", "fix Q3"),
            ("10", "✓", "✓", "—", "fix Q2 ✗"),   # the failure row
        ]
        row_colors = [INK, INK, INK, INK, CRIMSON]
        row_y = [1.0, 0.2, -0.6, -1.4, -2.4]

        row_groups = []
        for i, (s, q1, q2, q3, cor) in enumerate(rows):
            c = row_colors[i]
            cells = VGroup(*[
                Text(v, font=MONO, color=c, font_size=20).move_to([col_x[j], row_y[i], 0])
                for j, v in enumerate([s, q1, q2, q3, cor])
            ])
            row_groups.append(cells)

        # Highlight box around failure row
        fail_box = Rectangle(
            width=11.2, height=0.55,
            color=CRIMSON, stroke_width=2.5, fill_color=CRIMSON, fill_opacity=0.08,
        ).move_to([0, row_y[4], 0])

        note = Text("two qubits flipped → syndrome looks like single-qubit error → wrong fix",
                    font=SANS, color=CRIMSON, font_size=19)
        note.move_to([0, -3.2, 0])

        self.play(FadeIn(title), Create(underline), run_time=0.5)
        self.play(FadeIn(hdrs), Create(hdr_line), run_time=0.5)
        for rg in row_groups[:4]:
            self.play(FadeIn(rg), run_time=0.3)
        self.play(Create(fail_box), FadeIn(row_groups[4]), run_time=0.7)
        self.play(FadeIn(note), run_time=0.5)
        remaining = total - 2.8
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B09 — two-column comparison: error correction vs fault tolerance
# =============================================================================

class B09_TwoRequirements(Scene):
    def construct(self):
        total = DUR["B09"]

        # Vertical divider
        divider = Line(UP * 2.8, DOWN * 2.8, color=SLATE, stroke_width=1.5)

        # Left column: error correction
        ec_title = Text("ERROR CORRECTION", font=SANS, color=TEAL, font_size=24)
        ec_title.move_to([-3.0, 2.7, 0])

        ec_lbl1 = Text("handles errors on", font=SANS, color=INK, font_size=21)
        ec_lbl1.move_to([-3.0, 1.8, 0])
        ec_lbl2 = Text("data qubits", font=SANS, color=INK, font_size=21)
        ec_lbl2.move_to([-3.0, 1.2, 0])

        ec_eg = Text("qubit flipped → syndrome\ncatches it → fixed",
                     font=SANS, color=TEAL, font_size=19)
        ec_eg.move_to([-3.0, 0.0, 0])

        ec_check = Text("✓  1 data error → corrected",
                        font=SANS, color=TEAL, font_size=20)
        ec_check.move_to([-3.0, -1.4, 0])

        # Right column: fault tolerance
        ft_title = Text("FAULT TOLERANCE", font=SANS, color=TEAL, font_size=24)
        ft_title.move_to([3.0, 2.7, 0])

        ft_lbl1 = Text("constrains how errors", font=SANS, color=INK, font_size=21)
        ft_lbl1.move_to([3.0, 1.8, 0])
        ft_lbl2 = Text("spread in syndrome circuit", font=SANS, color=INK, font_size=21)
        ft_lbl2.move_to([3.0, 1.2, 0])

        ft_eg = Text("1 gate error anywhere\n→ at most 1 data error",
                     font=SANS, color=TEAL, font_size=19)
        ft_eg.move_to([3.0, 0.0, 0])

        # Violation note (two lines to stay right of divider)
        ft_fail1 = Text("✗  1 ancilla error → 2 data errors",
                        font=SANS, color=CRIMSON, font_size=18)
        ft_fail1.move_to([3.6, -1.4, 0])
        ft_fail2 = Text("(shared ancilla design fails)",
                        font=SANS, color=CRIMSON, font_size=18)
        ft_fail2.move_to([3.6, -1.9, 0])

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(ec_title), FadeIn(ft_title), run_time=0.5)
        self.play(FadeIn(VGroup(ec_lbl1, ec_lbl2)),
                  FadeIn(VGroup(ft_lbl1, ft_lbl2)), run_time=0.5)
        self.play(FadeIn(ec_eg), FadeIn(ft_eg), run_time=0.6)
        self.play(FadeIn(ec_check), run_time=0.4)
        self.play(FadeIn(ft_fail1), FadeIn(ft_fail2), run_time=0.5)
        remaining = total - 2.9
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B11 — fault-tolerant redesign: two ancillas, each touches one data qubit
# =============================================================================

class B11_FaultTolerantCkt(Scene):
    def construct(self):
        total = DUR["B11"]

        # Wire y-positions: ancillaA=2.0, Q1=1.0, ancillaB=-0.2, Q2=-1.2
        y_aa  =  2.0
        y_q1  =  1.0
        y_ab  = -0.2
        y_q2  = -1.2

        w_aa = wire(y_aa, x_left=-4.5, x_right=4.5, color=TEAL)
        w_q1 = wire(y_q1, x_left=-4.5, x_right=4.5)
        w_ab = wire(y_ab, x_left=-4.5, x_right=4.5, color=TEAL)
        w_q2 = wire(y_q2, x_left=-4.5, x_right=4.5)

        lbl_aa = wire_label("ancilla A", y_aa, x=-5.5, color=TEAL)
        lbl_q1 = wire_label("Q1",        y_q1, x=-5.5)
        lbl_ab = wire_label("ancilla B", y_ab, x=-5.5, color=TEAL)
        lbl_q2 = wire_label("Q2",        y_q2, x=-5.5)

        # Ancilla A controls Q1 only at x=-1.5
        g_ax = -1.5
        ctrl_a = cnot_control(g_ax, y_aa)
        tgt_a  = cnot_target(g_ax, y_q1)
        vline_a = cnot_vertical(g_ax, y_aa, y_q1, color=TEAL)

        # Ancilla B controls Q2 only at x=1.5
        g_bx = 1.5
        ctrl_b = cnot_control(g_bx, y_ab)
        tgt_b  = cnot_target(g_bx, y_q2)
        vline_b = cnot_vertical(g_bx, y_ab, y_q2, color=TEAL)

        # Measure boxes
        mbox_a = Rectangle(width=0.7, height=0.5, color=TEAL, stroke_width=2)
        mbox_a.move_to([3.5, y_aa, 0])
        m_a_lbl = Text("M", font=MONO, color=TEAL, font_size=20).move_to([3.5, y_aa, 0])

        mbox_b = Rectangle(width=0.7, height=0.5, color=TEAL, stroke_width=2)
        mbox_b.move_to([3.5, y_ab, 0])
        m_b_lbl = Text("M", font=MONO, color=TEAL, font_size=20).move_to([3.5, y_ab, 0])

        # Separation line between the two pairs
        sep = DashedLine(LEFT * 4.5 + DOWN * 0.0, RIGHT * 4.5 + DOWN * 0.0,
                         color=SLATE, stroke_width=1, dash_length=0.12)

        # Caption
        cap = Text("one ancilla per stabilizer — each error stays local",
                   font=SANS, color=TEAL, font_size=22)
        cap.move_to([0, -2.6, 0])

        self.add(w_aa, w_q1, w_ab, w_q2)
        self.play(
            FadeIn(VGroup(lbl_aa, lbl_q1, lbl_ab, lbl_q2)),
            Create(sep),
            run_time=0.5,
        )
        self.play(
            Create(VGroup(vline_a, ctrl_a, tgt_a)),
            run_time=0.6,
        )
        self.play(
            Create(VGroup(vline_b, ctrl_b, tgt_b)),
            run_time=0.6,
        )
        self.play(
            FadeIn(VGroup(mbox_a, m_a_lbl)),
            FadeIn(VGroup(mbox_b, m_b_lbl)),
            run_time=0.5,
        )
        self.play(FadeIn(cap), run_time=0.5)
        remaining = total - 2.7
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B13 — before/after: one ancilla (CRIMSON) vs two ancillas (TEAL)
# =============================================================================

class B13_BeforeAfter(Scene):
    def construct(self):
        total = DUR["B13"]

        # Vertical divider (shortened to stay above cost_lbl at y=-3.0)
        divider = Line(UP * 3.2, DOWN * 2.5, color=SLATE, stroke_width=1.5)

        # ── LEFT: BEFORE (one shared ancilla) ──
        before_title = Text("BEFORE", font=SANS, color=CRIMSON, font_size=26)
        before_title.move_to([-3.0, 3.1, 0])

        before_sub = Text("one ancilla\nmeasures both stabilizers",
                          font=SANS, color=INK, font_size=21)
        before_sub.move_to([-3.0, 2.0, 0])

        # Small circuit sketch
        w_ba = wire(0.6, x_left=-5.0, x_right=-0.7, color=CRIMSON)
        w_bq1 = wire(-0.2, x_left=-5.0, x_right=-0.7)
        w_bq2 = wire(-1.0, x_left=-5.0, x_right=-0.7)

        ctrl_b1 = cnot_control(-3.8, 0.6)
        tgt_b1  = cnot_target(-3.8, -0.2)
        vl_b1   = cnot_vertical(-3.8, 0.6, -0.2, color=CRIMSON)

        ctrl_b2 = cnot_control(-2.2, 0.6)
        tgt_b2  = cnot_target(-2.2, -1.0)
        vl_b2   = cnot_vertical(-2.2, 0.6, -1.0, color=CRIMSON)

        err_mark = x_error_box(-3.8, 0.6, size=0.28)

        rate_before = Text("3× higher\nlogical error rate",
                           font=SANS, color=CRIMSON, font_size=22)
        rate_before.move_to([-3.0, -2.3, 0])

        # ── RIGHT: AFTER (two ancillas) ──
        after_title = Text("AFTER", font=SANS, color=TEAL, font_size=26)
        after_title.move_to([3.0, 3.1, 0])

        after_sub = Text("one ancilla\nper stabilizer",
                         font=SANS, color=INK, font_size=21)
        after_sub.move_to([3.0, 2.0, 0])

        # Small circuit sketch (two pairs)
        w_aa2 = wire(0.8, x_left=0.7, x_right=5.0, color=TEAL)
        w_aq1 = wire(0.1, x_left=0.7, x_right=5.0)
        w_ab2 = wire(-0.7, x_left=0.7, x_right=5.0, color=TEAL)
        w_aq2 = wire(-1.4, x_left=0.7, x_right=5.0)

        ctrl_a2 = cnot_control(2.0, 0.8)
        tgt_a2  = cnot_target(2.0, 0.1)
        vl_a2   = cnot_vertical(2.0, 0.8, 0.1, color=TEAL)

        ctrl_b3 = cnot_control(3.5, -0.7)
        tgt_b3  = cnot_target(3.5, -1.4)
        vl_b3   = cnot_vertical(3.5, -0.7, -1.4, color=TEAL)

        rate_after = Text("predicted\nlogical error rate",
                          font=SANS, color=TEAL, font_size=22)
        rate_after.move_to([3.0, -2.3, 0])

        cost_lbl = Text("cost: +1 qubit", font=SANS, color=SLATE, font_size=20)
        cost_lbl.move_to([0, -3.0, 0])

        self.play(Create(divider), run_time=0.4)
        self.play(
            FadeIn(before_title), FadeIn(after_title),
            run_time=0.5,
        )
        self.play(
            FadeIn(before_sub), FadeIn(after_sub),
            run_time=0.5,
        )
        self.play(
            Create(VGroup(w_ba, w_bq1, w_bq2)),
            Create(VGroup(w_aa2, w_aq1, w_ab2, w_aq2)),
            run_time=0.5,
        )
        self.play(
            Create(VGroup(vl_b1, ctrl_b1, tgt_b1)),
            Create(VGroup(vl_b2, ctrl_b2, tgt_b2)),
            Create(VGroup(vl_a2, ctrl_a2, tgt_a2)),
            Create(VGroup(vl_b3, ctrl_b3, tgt_b3)),
            run_time=0.7,
        )
        self.play(FadeIn(err_mark), run_time=0.4)
        self.play(
            FadeIn(rate_before), FadeIn(rate_after),
            run_time=0.5,
        )
        self.play(FadeIn(cost_lbl), run_time=0.4)
        remaining = total - 3.9
        if remaining > 0:
            self.wait(remaining)
