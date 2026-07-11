"""vox_scenes.py — Why Two Qubits Live in a Space That Multiplies, Not Adds
(vox-tensor-product, slate cut, 16:9).

One Scene per GRAPHIC beat whose source is 'own'.
B01, B04, B05, B08, B10, B12 are CARD beats — rendered by the pipeline.

Color law: teal #1F6F5C = product state / rank-1 / separable / direct sum structure;
           crimson #BF3339 = entangled state / rank-2 / Bell state / cross-terms present.
Never swap mid-film.

Exclusions: NO Schmidt decomposition derivation, NO SVD algebra,
            NO entanglement entropy, NO LOCC framework.
"""
import sys, json, pathlib

sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *   # noqa: F401,F403
import numpy as np

DUR = {
    "B01": 10.0, "B02": 13.0, "B03": 13.0, "B04":  9.0,
    "B05":  4.0, "B06": 13.0, "B07": 13.0, "B08":  4.0,
    "B09": 14.0, "B10":  4.0, "B11": 14.0, "B12": 10.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or
                                    b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ─── helpers ──────────────────────────────────────────────────────────────────

def matrix_cell(val, cx, cy, color=INK, fs=26, bold=False):
    """A single matrix entry positioned at (cx, cy)."""
    t = Text(val, font=MONO, color=color, font_size=fs)
    t.move_to([cx, cy, 0])
    return t

def matrix_brackets(cx, cy, w=1.2, h=1.2):
    """Left and right brackets for a 2×2 matrix centered at (cx, cy)."""
    lx = cx - w / 2
    rx = cx + w / 2
    top = cy + h / 2
    bot = cy - h / 2
    # Each bracket: three-segment path (top, side, bottom)
    left_top  = Line([lx + 0.15, top, 0], [lx, top, 0], color=INK, stroke_width=2)
    left_side = Line([lx, top, 0], [lx, bot, 0], color=INK, stroke_width=2)
    left_bot  = Line([lx, bot, 0], [lx + 0.15, bot, 0], color=INK, stroke_width=2)
    right_top  = Line([rx - 0.15, top, 0], [rx, top, 0], color=INK, stroke_width=2)
    right_side = Line([rx, top, 0], [rx, bot, 0], color=INK, stroke_width=2)
    right_bot  = Line([rx, bot, 0], [rx - 0.15, bot, 0], color=INK, stroke_width=2)
    return VGroup(left_top, left_side, left_bot, right_top, right_side, right_bot)


# =============================================================================
# B02 — direct sum: two independent planes, no connection
# =============================================================================

class B02_DirectSum(Scene):
    def construct(self):
        total = DUR["B02"]

        title = Text("direct sum", font=SANS, color=INK, font_size=26)
        title.move_to([0, 3.2, 0])
        underline = Line(LEFT * 1.5 + UP * 2.85, RIGHT * 1.5 + UP * 2.85,
                         color=INK, stroke_width=2)

        # Left plane (system A)
        plane_a = Rectangle(width=3.5, height=2.2, color=TEAL, stroke_width=2)
        plane_a.move_to([-2.8, 0.4, 0])
        lbl_a = Text("system A", font=SANS, color=TEAL, font_size=22)
        lbl_a.move_to([-2.8, 1.8, 0])
        basis_a = VGroup(
            Text("|0⟩", font=MONO, color=INK, font_size=22).move_to([-3.4, 0.4, 0]),
            Text("|1⟩", font=MONO, color=INK, font_size=22).move_to([-2.2, 0.4, 0]),
        )

        # Right plane (system B)
        plane_b = Rectangle(width=3.5, height=2.2, color=TEAL, stroke_width=2)
        plane_b.move_to([2.8, 0.4, 0])
        lbl_b = Text("system B", font=SANS, color=TEAL, font_size=22)
        lbl_b.move_to([2.8, 1.8, 0])
        basis_b = VGroup(
            Text("|0⟩", font=MONO, color=INK, font_size=22).move_to([2.2, 0.4, 0]),
            Text("|1⟩", font=MONO, color=INK, font_size=22).move_to([3.4, 0.4, 0]),
        )

        # "No bridge" marker between the two planes (label above cross lines)
        no_bridge = Text("no connection", font=SANS, color=SLATE, font_size=19)
        no_bridge.move_to([0, 1.3, 0])

        # Cross placed below the label (y-range [−0.3, 0.5] — clear of label above)
        cross1 = Line([-0.35, 0.5, 0], [0.35, -0.1, 0], color=SLATE, stroke_width=2)
        cross2 = Line([-0.35, -0.1, 0], [0.35, 0.5, 0], color=SLATE, stroke_width=2)

        # Dimension label
        dim_lbl = Text("2 + 2 = 4", font=MONO, color=TEAL, font_size=26)
        dim_lbl.move_to([0, -1.8, 0])

        cap = Text("independent planes — no joint states possible",
                   font=SANS, color=SLATE, font_size=21)
        cap.move_to([0, -2.8, 0])

        self.play(FadeIn(title), Create(underline), run_time=0.5)
        self.play(
            Create(plane_a), FadeIn(lbl_a), FadeIn(basis_a),
            Create(plane_b), FadeIn(lbl_b), FadeIn(basis_b),
            run_time=0.8,
        )
        self.play(
            Create(VGroup(cross1, cross2)), FadeIn(no_bridge),
            run_time=0.5,
        )
        self.play(FadeIn(dim_lbl), run_time=0.4)
        self.play(FadeIn(cap), run_time=0.4)
        remaining = total - 2.6
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B03 — tensor product: 2×2 grid of all four basis states
# =============================================================================

class B03_TensorBasis(Scene):
    def construct(self):
        total = DUR["B03"]

        title = Text("tensor product", font=SANS, color=INK, font_size=26)
        title.move_to([0, 3.2, 0])
        underline = Line(LEFT * 2.0 + UP * 2.85, RIGHT * 2.0 + UP * 2.85,
                         color=INK, stroke_width=2)

        # 2×2 grid of basis states
        # Columns = system B (|0⟩, |1⟩); Rows = system A (|0⟩, |1⟩)
        col_x = [-1.6, 1.6]
        row_y = [1.0, -0.6]

        # Header labels
        hdr_A = Text("A", font=SANS, color=TEAL, font_size=22).move_to([-3.0, 0.2, 0])
        hdr_B = Text("B", font=SANS, color=TEAL, font_size=22).move_to([0.0, 2.2, 0])

        col_lbl0 = Text("|0⟩", font=MONO, color=TEAL, font_size=22).move_to([col_x[0], 2.2, 0])
        col_lbl1 = Text("|1⟩", font=MONO, color=TEAL, font_size=22).move_to([col_x[1], 2.2, 0])
        row_lbl0 = Text("|0⟩", font=MONO, color=TEAL, font_size=22).move_to([-3.0, row_y[0], 0])
        row_lbl1 = Text("|1⟩", font=MONO, color=TEAL, font_size=22).move_to([-3.0, row_y[1], 0])

        # Grid cells
        cells = {}
        labels = {"00": "|00⟩", "01": "|01⟩", "10": "|10⟩", "11": "|11⟩"}
        colors = {"00": INK, "01": INK, "10": INK, "11": INK}
        cell_boxes = []
        cell_texts = []
        for i, ri in enumerate(["0", "1"]):
            for j, ci in enumerate(["0", "1"]):
                key = ri + ci
                box = Rectangle(width=2.2, height=1.1, color=TEAL, stroke_width=1.5)
                box.move_to([col_x[j], row_y[i], 0])
                lbl = Text(labels[key], font=MONO, color=INK, font_size=26)
                lbl.move_to([col_x[j], row_y[i], 0])
                cell_boxes.append(box)
                cell_texts.append(lbl)

        # Dimension label
        dim_lbl = Text("2 × 2 = 4", font=MONO, color=TEAL, font_size=26)
        dim_lbl.move_to([0, -2.0, 0])

        cap = Text("all combinations — joint states exist",
                   font=SANS, color=TEAL, font_size=21)
        cap.move_to([0, -2.8, 0])

        self.play(FadeIn(title), Create(underline), run_time=0.5)
        self.play(
            FadeIn(VGroup(hdr_B, col_lbl0, col_lbl1)),
            FadeIn(VGroup(hdr_A, row_lbl0, row_lbl1)),
            run_time=0.5,
        )
        for box, lbl in zip(cell_boxes, cell_texts):
            self.play(Create(box), FadeIn(lbl), run_time=0.25)
        self.play(FadeIn(dim_lbl), run_time=0.4)
        self.play(FadeIn(cap), run_time=0.4)
        remaining = total - 2.8
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B06 — rank-1 product state coefficient matrix
# =============================================================================

class B06_Rank1Matrix(Scene):
    def construct(self):
        total = DUR["B06"]

        title = Text("product state", font=SANS, color=TEAL, font_size=26)
        title.move_to([0, 3.2, 0])
        underline = Line(LEFT * 1.8 + UP * 2.85, RIGHT * 1.8 + UP * 2.85,
                         color=TEAL, stroke_width=2)

        # State label
        state_lbl = Text("|ψ⟩ = |a⟩ ⊗ |b⟩", font=MONO, color=INK, font_size=26)
        state_lbl.move_to([0, 2.2, 0])

        # Coefficient matrix: C = [[αγ, αδ], [βγ, βδ]]
        cx, cy = -1.0, 0.3
        brk = matrix_brackets(cx, cy, w=2.8, h=1.8)
        c00 = matrix_cell("αγ", cx - 0.7, cy + 0.45, color=TEAL, fs=26)
        c01 = matrix_cell("αδ", cx + 0.7, cy + 0.45, color=TEAL, fs=26)
        c10 = matrix_cell("βγ", cx - 0.7, cy - 0.45, color=TEAL, fs=26)
        c11 = matrix_cell("βδ", cx + 0.7, cy - 0.45, color=TEAL, fs=26)

        c_label = Text("C =", font=MONO, color=INK, font_size=26)
        c_label.move_to([-2.9, cy, 0])

        # Rank annotation
        rank_lbl = Text("rank 1", font=SANS, color=TEAL, font_size=24)
        rank_lbl.move_to([2.8, 0.8, 0])

        det_lbl = Text("det(C) = 0", font=MONO, color=TEAL, font_size=22)
        det_lbl.move_to([2.8, 0.1, 0])

        sep_note = Text("(outer product of two vectors)",
                        font=SANS, color=SLATE, font_size=20)
        sep_note.move_to([0, -1.4, 0])

        cap = Text("no cross-qubit information — subsystems independent",
                   font=SANS, color=TEAL, font_size=20)
        cap.move_to([0, -2.8, 0])

        self.play(FadeIn(title), Create(underline), run_time=0.5)
        self.play(FadeIn(state_lbl), run_time=0.4)
        self.play(FadeIn(c_label), Create(brk), run_time=0.5)
        self.play(
            FadeIn(VGroup(c00, c01, c10, c11)),
            run_time=0.5,
        )
        self.play(FadeIn(rank_lbl), FadeIn(det_lbl), run_time=0.5)
        self.play(FadeIn(sep_note), run_time=0.4)
        self.play(FadeIn(cap), run_time=0.4)
        remaining = total - 3.2
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B07 — rank-2 Bell state coefficient matrix
# =============================================================================

class B07_Rank2Bell(Scene):
    def construct(self):
        total = DUR["B07"]

        title = Text("Bell state", font=SANS, color=CRIMSON, font_size=26)
        title.move_to([0, 3.2, 0])
        underline = Line(LEFT * 1.3 + UP * 2.85, RIGHT * 1.3 + UP * 2.85,
                         color=CRIMSON, stroke_width=2)

        # State label
        state_lbl = Text("|Φ⁺⟩ = (|00⟩ + |11⟩) / √2", font=MONO, color=INK, font_size=24)
        state_lbl.move_to([0, 2.2, 0])

        # Coefficient matrix: C = (1/√2) [[1, 0], [0, 1]]
        cx, cy = -1.0, 0.3
        brk = matrix_brackets(cx, cy, w=2.8, h=1.8)
        c00 = matrix_cell("1", cx - 0.7, cy + 0.45, color=CRIMSON, fs=28)
        c01 = matrix_cell("0", cx + 0.7, cy + 0.45, color=INK, fs=28)
        c10 = matrix_cell("0", cx - 0.7, cy - 0.45, color=INK, fs=28)
        c11 = matrix_cell("1", cx + 0.7, cy - 0.45, color=CRIMSON, fs=28)

        prefactor = Text("1/√2 ·", font=MONO, color=INK, font_size=24)
        prefactor.move_to([-3.4, cy, 0])

        c_label = Text("C =", font=MONO, color=INK, font_size=26)
        c_label.move_to([-4.4, cy, 0])

        # Rank annotation
        rank_lbl = Text("rank 2", font=SANS, color=CRIMSON, font_size=24)
        rank_lbl.move_to([2.8, 0.8, 0])

        det_lbl = Text("det(C) = ½", font=MONO, color=CRIMSON, font_size=22)
        det_lbl.move_to([2.8, 0.1, 0])

        entangled_lbl = Text("entangled", font=SANS, color=CRIMSON, font_size=24)
        entangled_lbl.move_to([2.8, -0.7, 0])

        cap = Text("rank 2 = cannot be written as a product — entangled",
                   font=SANS, color=CRIMSON, font_size=20)
        cap.move_to([0, -2.8, 0])

        self.play(FadeIn(title), Create(underline), run_time=0.5)
        self.play(FadeIn(state_lbl), run_time=0.4)
        self.play(FadeIn(c_label), FadeIn(prefactor), Create(brk), run_time=0.5)
        self.play(
            FadeIn(VGroup(c00, c01, c10, c11)),
            run_time=0.5,
        )
        self.play(FadeIn(rank_lbl), FadeIn(det_lbl), run_time=0.5)
        self.play(FadeIn(entangled_lbl), run_time=0.4)
        self.play(FadeIn(cap), run_time=0.4)
        remaining = total - 3.2
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B09 — structure compare: direct sum (rank-1 only) vs tensor product
# =============================================================================

class B09_StructureCompare(Scene):
    def construct(self):
        total = DUR["B09"]

        # Vertical divider
        divider = Line(UP * 3.2, DOWN * 2.2, color=SLATE, stroke_width=1.5)

        # Left column: direct sum
        ds_title = Text("DIRECT SUM", font=SANS, color=TEAL, font_size=22)
        ds_title.move_to([-3.0, 3.0, 0])

        ds_lbl = Text("rank-1 states only", font=SANS, color=TEAL, font_size=20)
        ds_lbl.move_to([-3.0, 2.1, 0])

        ds_eg = Text("all states factor:", font=SANS, color=INK, font_size=19)
        ds_eg.move_to([-3.0, 1.3, 0])
        ds_state = Text("|ψ⟩ = |a⟩⊗|b⟩  always", font=MONO, color=TEAL, font_size=19)
        ds_state.move_to([-3.0, 0.7, 0])

        ds_no_bell = Text("Bell state:", font=SANS, color=INK, font_size=19)
        ds_no_bell.move_to([-3.2, -0.2, 0])
        ds_cross1 = Line([-2.3, 0.1, 0], [-1.5, -0.5, 0], color=CRIMSON, stroke_width=2.5)
        ds_cross2 = Line([-2.3, -0.5, 0], [-1.5, 0.1, 0], color=CRIMSON, stroke_width=2.5)
        ds_no_lbl = Text("no analog", font=SANS, color=CRIMSON, font_size=19)
        ds_no_lbl.move_to([-3.0, -1.1, 0])

        # Right column: tensor product
        tp_title = Text("TENSOR PRODUCT", font=SANS, color=CRIMSON, font_size=22)
        tp_title.move_to([3.0, 3.0, 0])

        tp_lbl1 = Text("rank-1 states", font=SANS, color=TEAL, font_size=20)
        tp_lbl1.move_to([3.0, 2.1, 0])
        tp_lbl2 = Text("+ rank-2 states", font=SANS, color=CRIMSON, font_size=20)
        tp_lbl2.move_to([3.0, 1.5, 0])

        tp_prod = Text("product states ✓", font=SANS, color=TEAL, font_size=19)
        tp_prod.move_to([3.0, 0.6, 0])

        tp_bell = Text("Bell states ✓", font=SANS, color=CRIMSON, font_size=19)
        tp_bell.move_to([3.0, 0.0, 0])

        tp_extra = Text("entanglement lives here",
                        font=SANS, color=CRIMSON, font_size=19)
        tp_extra.move_to([3.0, -1.0, 0])

        self.play(Create(divider), run_time=0.4)
        self.play(FadeIn(ds_title), FadeIn(tp_title), run_time=0.5)
        self.play(FadeIn(ds_lbl), FadeIn(VGroup(tp_lbl1, tp_lbl2)), run_time=0.5)
        self.play(FadeIn(ds_eg), FadeIn(ds_state), run_time=0.4)
        self.play(FadeIn(tp_prod), run_time=0.3)
        self.play(
            FadeIn(ds_no_bell),
            Create(VGroup(ds_cross1, ds_cross2)),
            FadeIn(ds_no_lbl),
            FadeIn(tp_bell),
            run_time=0.6,
        )
        self.play(FadeIn(tp_extra), run_time=0.4)
        remaining = total - 3.6
        if remaining > 0:
            self.wait(remaining)


# =============================================================================
# B11 — dimension count: 2^3=8 vs 2+2+2=6
# =============================================================================

class B11_DimensionCount(Scene):
    def construct(self):
        total = DUR["B11"]

        title = Text("3-qubit error code", font=SANS, color=INK, font_size=26)
        title.move_to([0, 3.2, 0])
        underline = Line(LEFT * 2.8 + UP * 2.85, RIGHT * 2.8 + UP * 2.85,
                         color=INK, stroke_width=2)

        # Left: direct sum count
        ds_header = Text("direct sum", font=SANS, color=SLATE, font_size=22)
        ds_header.move_to([-3.0, 2.2, 0])

        ds_math = Text("2 + 2 + 2 = 6", font=MONO, color=SLATE, font_size=28)
        ds_math.move_to([-3.0, 1.2, 0])

        ds_note = Text("no cross-qubit states", font=SANS, color=SLATE, font_size=20)
        ds_note.move_to([-3.0, 0.3, 0])

        ds_fail = Text("encoding state cannot exist", font=SANS, color=CRIMSON, font_size=19)
        ds_fail.move_to([-3.0, -0.5, 0])

        # Divider
        divider = Line(UP * 2.8, DOWN * 2.2, color=SLATE, stroke_width=1.5)

        # Right: tensor product count
        tp_header = Text("tensor product", font=SANS, color=TEAL, font_size=22)
        tp_header.move_to([3.0, 2.2, 0])

        tp_math = Text("2 × 2 × 2 = 8", font=MONO, color=CRIMSON, font_size=28)
        tp_math.move_to([3.0, 1.2, 0])

        tp_note = Text("cross-qubit states exist", font=SANS, color=TEAL, font_size=20)
        tp_note.move_to([3.0, 0.3, 0])

        # Encoding state: α|000⟩ + β|111⟩
        enc_state = Text("α|000⟩ + β|111⟩", font=MONO, color=CRIMSON, font_size=22)
        enc_state.move_to([3.0, -0.5, 0])

        enc_note = Text("entangled encoding state", font=SANS, color=CRIMSON, font_size=18)
        enc_note.move_to([3.0, -1.2, 0])

        extra_note = Text("extra 2 dims = entangled states the code uses",
                          font=SANS, color=CRIMSON, font_size=19)
        extra_note.move_to([0, -2.5, 0])

        self.play(FadeIn(title), Create(underline), run_time=0.5)
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(ds_header), FadeIn(tp_header), run_time=0.4)
        self.play(FadeIn(ds_math), FadeIn(tp_math), run_time=0.5)
        self.play(FadeIn(ds_note), FadeIn(tp_note), run_time=0.4)
        self.play(FadeIn(ds_fail), FadeIn(enc_state), run_time=0.5)
        self.play(FadeIn(enc_note), run_time=0.3)
        self.play(FadeIn(extra_note), run_time=0.5)
        remaining = total - 3.4
        if remaining > 0:
            self.wait(remaining)
