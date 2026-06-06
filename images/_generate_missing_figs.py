"""
Generate all 11 missing figures for quantum-mechanics-vol4.
Run from: books/quantum-mechanics-vol4/images/
  python3 _generate_missing_figs.py
House style: figsize=(7, 3.6), dpi=200 → 1400×720 px, white background,
  spines top/right off, mathtext labels, descriptive title at top.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc, FancyBboxPatch, Circle, Rectangle, Wedge
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe
import os, sys

OUT = os.path.dirname(os.path.abspath(__file__))

STYLE = dict(figsize=(7, 3.6), dpi=200)
TAB = plt.rcParams['axes.prop_cycle'].by_key()['color']

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  wrote {name}")

# ──────────────────────────────────────────────────────────────────────────────
# Fig 2.1 — Direct sum vs. tensor product for two qubits
# ──────────────────────────────────────────────────────────────────────────────
def fig_02_01():
    fig, (ax1, ax2) = plt.subplots(1, 2, **STYLE)
    fig.patch.set_facecolor('white')

    # Left: ℂ² ⊕ ℂ² — two separate planes, no cross-terms
    ax1.set_xlim(-0.2, 2.2)
    ax1.set_ylim(-0.3, 2.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title(r'$\mathbb{C}^2 \oplus \mathbb{C}^2$ (direct sum)', fontsize=10)

    # Plane A
    pA = plt.Polygon([[0,1.4],[0,2.4],[1,2.4],[1,1.4]], closed=True,
                      facecolor=TAB[0], alpha=0.18, edgecolor=TAB[0], linewidth=1.5)
    ax1.add_patch(pA)
    ax1.text(0.5, 1.9, r'$\mathbb{C}^2_A$', ha='center', va='center', fontsize=11, color=TAB[0], fontweight='bold')
    ax1.annotate('', xy=(0.5, 2.42), xytext=(0.5, 2.42+0.0))
    ax1.arrow(0.0, 1.4, 0.85, 0, head_width=0.07, head_length=0.08,
              fc=TAB[0], ec=TAB[0], length_includes_head=True)
    ax1.arrow(0.0, 1.4, 0, 0.85, head_width=0.07, head_length=0.08,
              fc=TAB[0], ec=TAB[0], length_includes_head=True)
    ax1.text(0.95, 1.38, r'$|0\rangle_A$', fontsize=8.5, color=TAB[0])
    ax1.text(-0.02, 2.3, r'$|1\rangle_A$', fontsize=8.5, color=TAB[0], ha='right')

    # Plane B
    pB = plt.Polygon([[0,0],[0,1],[1,1],[1,0]], closed=True,
                      facecolor=TAB[1], alpha=0.18, edgecolor=TAB[1], linewidth=1.5)
    ax1.add_patch(pB)
    ax1.text(0.5, 0.5, r'$\mathbb{C}^2_B$', ha='center', va='center', fontsize=11, color=TAB[1], fontweight='bold')
    ax1.arrow(0.0, 0.0, 0.85, 0, head_width=0.07, head_length=0.08,
              fc=TAB[1], ec=TAB[1], length_includes_head=True)
    ax1.arrow(0.0, 0.0, 0, 0.85, head_width=0.07, head_length=0.08,
              fc=TAB[1], ec=TAB[1], length_includes_head=True)
    ax1.text(0.95, -0.03, r'$|0\rangle_B$', fontsize=8.5, color=TAB[1])
    ax1.text(-0.02, 0.9, r'$|1\rangle_B$', fontsize=8.5, color=TAB[1], ha='right')

    ax1.text(1.15, 1.2, r'$\oplus$', fontsize=20, ha='center', va='center', color='#555')
    ax1.text(0.5, -0.25, 'dim = 2+2 = 4\n(no cross-terms)', ha='center', va='top',
             fontsize=8, color='#444', style='italic')

    # Right: ℂ² ⊗ ℂ² — four-dimensional joint space
    ax2.set_xlim(-0.3, 2.2)
    ax2.set_ylim(-0.3, 2.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title(r'$\mathbb{C}^2 \otimes \mathbb{C}^2$ (tensor product)', fontsize=10)

    # Full 2×2 grid of basis states
    basis = [(r'$|00\rangle$', 0, 0), (r'$|01\rangle$', 1, 0),
             (r'$|10\rangle$', 0, 1), (r'$|11\rangle$', 1, 1)]
    colors4 = [TAB[2], TAB[3], TAB[4], TAB[5]]
    for (lbl, col, row), c in zip(basis, colors4):
        x = col * 0.85 + 0.1
        y = row * 0.85 + 0.1
        circ = Circle((x, y), 0.32, facecolor=c, alpha=0.25, edgecolor=c, linewidth=1.5)
        ax2.add_patch(circ)
        ax2.text(x, y, lbl, ha='center', va='center', fontsize=10, color=c, fontweight='bold')

    # Entanglement arrow showing correlations are possible
    ax2.annotate('', xy=(0.95, 0.10), xytext=(0.10, 0.10),
                 arrowprops=dict(arrowstyle='<->', color='#888', lw=1.2, connectionstyle='arc3,rad=-0.35'))
    ax2.annotate('', xy=(0.95, 0.95), xytext=(0.10, 0.95),
                 arrowprops=dict(arrowstyle='<->', color='#888', lw=1.2, connectionstyle='arc3,rad=0.35'))

    ax2.text(0.95, -0.25, 'dim = 2×2 = 4\n(correlations allowed)', ha='center', va='top',
             fontsize=8, color='#444', style='italic')
    ax2.text(0.52, 1.55, 'entanglement\npossible', ha='center', va='center',
             fontsize=7.5, color='#666',
             bbox=dict(boxstyle='round,pad=0.2', facecolor='#f0f0f0', edgecolor='#bbb'))

    fig.suptitle('Direct Sum vs. Tensor Product for Two Qubits', fontsize=11, fontweight='bold', y=1.01)
    fig.tight_layout()
    save(fig, '02-composite-systems-and-entanglement-fig-01.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 2.2 — Bell state preparation circuit + coefficient matrices
# ──────────────────────────────────────────────────────────────────────────────
def fig_02_02():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 3.8)
    ax.axis('off')
    ax.set_title('Bell State Preparation Circuit: $|00\\rangle \\to |\\Phi^+\\rangle$',
                 fontsize=11, fontweight='bold')

    # Wire y positions
    yA, yB = 2.8, 1.6
    wire_color = '#222'
    lw = 1.8

    # ── Wires ──
    ax.plot([0.5, 9.5], [yA, yA], color=wire_color, lw=lw, zorder=1)
    ax.plot([0.5, 9.5], [yB, yB], color=wire_color, lw=lw, zorder=1)

    # Wire labels
    ax.text(0.2, yA, r'$A$', fontsize=11, va='center', ha='right', fontweight='bold', color=TAB[0])
    ax.text(0.2, yB, r'$B$', fontsize=11, va='center', ha='right', fontweight='bold', color=TAB[1])

    # Input states
    ax.text(0.55, yA+0.25, r'$|0\rangle$', fontsize=10, va='bottom', ha='left', color=TAB[0])
    ax.text(0.55, yB+0.25, r'$|0\rangle$', fontsize=10, va='bottom', ha='left', color=TAB[1])

    # ── Stage 1: H gate on qubit A at x=2.5 ──
    hbox = FancyBboxPatch((2.1, yA-0.35), 0.8, 0.7,
                           boxstyle='round,pad=0.05', facecolor='#d4e6f1',
                           edgecolor=TAB[0], linewidth=1.5, zorder=3)
    ax.add_patch(hbox)
    ax.text(2.5, yA, r'$H$', ha='center', va='center', fontsize=12, fontweight='bold',
            color=TAB[0], zorder=4)

    # State label after H
    ax.text(3.5, yA+0.28, r'$|+\rangle_A \otimes |0\rangle_B$', fontsize=9,
            ha='center', va='bottom', color='#555', style='italic')

    # Dashed divider
    ax.axvline(x=4.5, ymin=0.35, ymax=0.92, color='#bbb', lw=1, linestyle='--')

    # ── Stage 2: CNOT at x=6.0 ──
    # Control dot on A
    ax.plot(6.0, yA, 'o', ms=10, color=TAB[0], zorder=4)
    # Vertical connection line
    ax.plot([6.0, 6.0], [yA, yB], color=wire_color, lw=lw, zorder=2)
    # Target circle on B
    circ_cx, circ_cy, circ_r = 6.0, yB, 0.28
    cnot_circle = Circle((circ_cx, circ_cy), circ_r,
                          facecolor='white', edgecolor=TAB[1], linewidth=1.8, zorder=3)
    ax.add_patch(cnot_circle)
    ax.plot([circ_cx-circ_r, circ_cx+circ_r], [circ_cy, circ_cy],
            color=TAB[1], lw=1.5, zorder=4)
    ax.plot([circ_cx, circ_cx], [circ_cy-circ_r, circ_cy+circ_r],
            color=TAB[1], lw=1.5, zorder=4)

    # State label after CNOT
    ax.text(7.3, yA+0.28, r'$|\Phi^+\rangle = \frac{|00\rangle+|11\rangle}{\sqrt{2}}$',
            fontsize=9, ha='center', va='bottom', color='#333', style='italic')

    # ── Coefficient matrices below the circuit ──
    # Stage 0: |00⟩
    def draw_matrix(ax, cx, cy, entries, label, color):
        """Draw a tiny 2x2 matrix with bracket-like boxes."""
        dx, dy = 0.28, 0.22
        ax.text(cx, cy+0.55, label, ha='center', va='bottom', fontsize=7.5,
                color=color, style='italic')
        for r in range(2):
            for c2 in range(2):
                bx = cx - dx + c2*dx
                by = cy - dy + (1-r)*dy
                ax.text(bx+dx/2, by+dy/2, entries[r][c2],
                        ha='center', va='center', fontsize=8, color=color)
        # bracket
        rect = FancyBboxPatch((cx-dx-0.08, cy-dy-0.08), 2*dx+0.16, 2*dy+0.16,
                               boxstyle='round,pad=0.04',
                               facecolor='none', edgecolor=color, linewidth=1.0, alpha=0.5)
        ax.add_patch(rect)

    y_mat = 0.3
    draw_matrix(ax, 1.2, y_mat,
                [['1','0'],['0','0']], r'$C$ at $|00\rangle$', '#666')
    ax.annotate('', xy=(3.2, y_mat+0.2), xytext=(2.0, y_mat+0.2),
                arrowprops=dict(arrowstyle='->', color='#aaa', lw=1))
    draw_matrix(ax, 3.8, y_mat,
                [[r'$\frac{1}{\sqrt{2}}$','0'],[r'$\frac{1}{\sqrt{2}}$','0']],
                r'after $H$: rank 1', TAB[0])
    ax.annotate('', xy=(5.6, y_mat+0.2), xytext=(4.9, y_mat+0.2),
                arrowprops=dict(arrowstyle='->', color='#aaa', lw=1))
    draw_matrix(ax, 6.5, y_mat,
                [[r'$\frac{1}{\sqrt{2}}$','0'],['0',r'$\frac{1}{\sqrt{2}}$']],
                r'after CNOT: rank 2', TAB[1])
    ax.text(8.2, y_mat+0.3, 'entangled!\n' + r'$\det(C)=\frac{1}{2}\neq 0$',
            ha='center', va='center', fontsize=8, color=TAB[2],
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff3cd', edgecolor=TAB[2], alpha=0.9))

    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 3.8)
    fig.tight_layout()
    save(fig, '02-composite-systems-and-entanglement-fig-02.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 2.3 — SVD of C and Schmidt decomposition
# ──────────────────────────────────────────────────────────────────────────────
def fig_02_03():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')
    ax.set_title(r'SVD of Coefficient Matrix $C$ and Schmidt Decomposition',
                 fontsize=11, fontweight='bold')

    def matrix_block(ax, x, y, w, h, title, rows, color, bg='#f0f0f0'):
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                               facecolor=bg, edgecolor=color, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y+h+0.15, title, ha='center', va='bottom',
                fontsize=9, color=color, fontweight='bold')
        row_h = h / len(rows)
        for i, row in enumerate(rows):
            col_w = w / len(row)
            for j, entry in enumerate(row):
                ax.text(x + col_w*(j+0.5), y + h - row_h*(i+0.5),
                        entry, ha='center', va='center', fontsize=9, color='#222')

    # C matrix
    matrix_block(ax, 0.3, 1.5, 1.5, 1.5,
                 r'$C$ (2×2 complex)',
                 [[r'$c_{00}$', r'$c_{01}$'],
                  [r'$c_{10}$', r'$c_{11}$']],
                 '#555', bg='#f8f8f8')

    # = sign
    ax.text(2.05, 2.25, r'$=$', ha='center', va='center', fontsize=16, color='#333')

    # U matrix
    matrix_block(ax, 2.3, 1.5, 1.3, 1.5,
                 r'$U$ (unitary)',
                 [[r'$|u_1\rangle$', r'$|u_2\rangle$'],
                  ['', '']],
                 TAB[0], bg='#eaf4fb')
    # Column labels for U
    ax.text(2.3+0.325, 1.35, r'Schmidt', ha='center', va='top', fontsize=7.5, color=TAB[0])
    ax.text(2.3+0.975, 1.35, r'states $A$', ha='center', va='top', fontsize=7.5, color=TAB[0])

    # · sign
    ax.text(3.75, 2.25, r'$\cdot$', ha='center', va='center', fontsize=20, color='#333')

    # Σ matrix
    matrix_block(ax, 4.0, 1.5, 1.5, 1.5,
                 r'$\Sigma$ (diagonal)',
                 [[r'$\sqrt{\lambda_1}$', r'$0$'],
                  [r'$0$', r'$\sqrt{\lambda_2}$']],
                 TAB[2], bg='#fef9e7')

    # · sign
    ax.text(5.65, 2.25, r'$\cdot$', ha='center', va='center', fontsize=20, color='#333')

    # V† matrix
    matrix_block(ax, 5.9, 1.5, 1.5, 1.5,
                 r'$V^\dagger$',
                 [[r'$\langle v_1|$', ''],
                  [r'$\langle v_2|$', '']],
                 TAB[1], bg='#eafaf1')
    ax.text(5.9+0.375, 1.35, r'Schmidt', ha='center', va='top', fontsize=7.5, color=TAB[1])
    ax.text(5.9+0.375, 1.08, r'states $B$', ha='center', va='top', fontsize=7.5, color=TAB[1])

    # Schmidt decomposition formula at bottom
    ax.text(5.0, 0.65,
            r'$|\psi_{AB}\rangle = \sqrt{\lambda_1}\,|u_1\rangle_A|v_1\rangle_B \;+\; \sqrt{\lambda_2}\,|u_2\rangle_A|v_2\rangle_B$',
            ha='center', va='center', fontsize=10.5,
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff3cd', edgecolor='#e6ac00', linewidth=1.5))

    # Entanglement annotation
    ax.annotate('Schmidt rank = 1\n→ product state',
                xy=(4.75, 1.75), xytext=(7.7, 2.8),
                fontsize=8, color=TAB[2], ha='center',
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=1),
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#fef9e7', edgecolor=TAB[2], alpha=0.8))
    ax.text(7.7, 3.25, 'Schmidt rank ≥ 2\n→ entangled', ha='center', va='center',
            fontsize=8, color=TAB[1],
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#eafaf1', edgecolor=TAB[1], alpha=0.8))

    fig.tight_layout()
    save(fig, '02-composite-systems-and-entanglement-fig-03.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 3.1 — Four-quadrant CHSH table: B₁, B₂ values, |S(λ)|=2 annotated
# ──────────────────────────────────────────────────────────────────────────────
def fig_03_01():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis('off')
    ax.set_title(r'CHSH Bound: $|S(\lambda)| = 2$ in Every Row', fontsize=11, fontweight='bold')

    # Table layout
    # Columns: A₁B₁, A₁B₂, A₂B₁, A₂B₂, B₁, B₂, |S(λ)|
    col_x = [0.5, 1.7, 2.9, 4.1, 5.5, 6.9, 8.3]
    col_labels = [r'$A_1 B_1$', r'$A_1 B_2$', r'$A_2 B_1$', r'$A_2 B_2$',
                  r'$B_1 = A_1B_1 + A_2B_1$' + '\n' + r'$+ A_1B_2 + A_2B_2$ (wait)',
                  '', r'$|S(\lambda)|$']

    # Header row
    headers = [r'$A_1B_1$', r'$A_1B_2$', r'$A_2B_1$', r'$A_2B_2$',
               r'$B_1 = A_1B_1+A_2B_1$', r'$B_2 = A_1B_2-A_2B_2$', r'$|S|$']
    # Simpler headers
    hdrs = [r'$A_1B_1$', r'$A_1B_2$', r'$A_2B_1$', r'$A_2B_2$',
            r'$B_1$', r'$B_2$', r'$|S(\lambda)|$']
    hx = [0.9, 2.0, 3.1, 4.2, 5.6, 6.9, 8.2]
    for h, x in zip(hdrs, hx):
        ax.text(x, 4.15, h, ha='center', va='center', fontsize=9, fontweight='bold', color='#222')
    ax.axhline(3.85, xmin=0.05, xmax=0.97, color='#444', lw=1.2)

    # B₁ = A₁B₁ + A₁B₂ + A₂B₁ - A₂B₂
    # B₂ = A₁B₁ - A₁B₂ + A₂B₁ + A₂B₂
    # S(λ) = B₁ + B₂ ... actually S = A₁B₁ + A₁B₂ + A₂B₁ - A₂B₂
    # Here B₁ and B₂ as used in the chapter:
    # S(λ) = A₁(B₁+B₂) + A₂(B₁-B₂)
    # If B₁=B₂: S=2A₁B₁ → |S|=2
    # If B₁=-B₂: S=2A₂B₁ → |S|=2
    # The four cases from the chapter (A₁,A₂,B₁,B₂ each ±1):
    rows_data = [
        # (A1, A2, B1, B2)
        (+1, +1, +1, +1),
        (+1, +1, +1, -1),
        (+1, +1, -1, +1),
        (+1, +1, -1, -1),
        (+1, -1, +1, +1),
        (+1, -1, +1, -1),
        (+1, -1, -1, +1),
        (+1, -1, -1, -1),
    ]
    # S = A1*B1 + A1*B2 + A2*B1 - A2*B2
    row_ys = [3.45, 3.0, 2.55, 2.1, 1.65, 1.2, 0.75, 0.35]

    bg_colors = ['#f8f8f8', 'white'] * 4
    for i, ((a1, a2, b1, b2), ry) in enumerate(zip(rows_data, row_ys)):
        S = a1*b1 + a1*b2 + a2*b1 - a2*b2
        bx = [0.9, 2.0, 3.1, 4.2, 5.6, 6.9, 8.2]
        vals = [a1*b1, a1*b2, a2*b1, a2*b2,
                a1*b1 + a1*b2 + a2*b1,  # placeholder — not B1 alone
                a2*b2,                   # placeholder
                abs(S)]
        # Recompute properly
        # B1 = b1, B2 = b2 per hidden variable λ
        # S(λ) = A1(B1+B2) + A2(B1-B2)
        S_val = a1*(b1+b2) + a2*(b1-b2)
        display_vals = [f'{a1*b1:+d}', f'{a1*b2:+d}', f'{a2*b1:+d}', f'{a2*b2:+d}',
                        f'{b1:+d}', f'{b2:+d}', f'{abs(S_val)}']
        c_S = TAB[2] if abs(S_val) == 2 else TAB[3]
        for j, (v, x) in enumerate(zip(display_vals, bx)):
            color = '#222'
            fw = 'normal'
            if j == 6:
                color = c_S
                fw = 'bold'
            ax.text(x, ry, v, ha='center', va='center', fontsize=9,
                    color=color, fontweight=fw)

    # Annotation box
    ax.text(9.1, 2.1,
            r'In every row:' + '\n' + r'one of $B_1, B_2$' + '\n' + r'equals $\pm 2$,' + '\n' + r'the other $0$' + '\n\n' + r'$\Rightarrow |S(\lambda)|=2$',
            ha='center', va='center', fontsize=8.5, color=TAB[2],
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#eafaf1', edgecolor=TAB[2], linewidth=1.5))

    ax.text(5.0, 0.05,
            r'Classical bound: $|S| = \int |S(\lambda)|\,\rho(\lambda)\,d\lambda \leq 2$',
            ha='center', va='center', fontsize=9, color='#444', style='italic')

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    fig.tight_layout()
    save(fig, '03-bells-theorem-and-chsh-fig-01.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 3.3 — Timeline 1935–2022
# ──────────────────────────────────────────────────────────────────────────────
def fig_03_03():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(1928, 2030)
    ax.set_ylim(-2.5, 3.2)
    ax.axis('off')
    ax.set_title('Bell\'s Theorem — Key Milestones 1935–2022', fontsize=11, fontweight='bold')

    # Timeline axis
    ax.axhline(0, xmin=0.02, xmax=0.98, color='#444', lw=2.5, zorder=1)

    events = [
        (1935, r'EPR paradox' + '\n' + r'(Einstein, Podolsky,' + '\n' + r'Rosen)', -1.8, TAB[0]),
        (1964, "Bell's theorem\n(J.S. Bell)", 1.2, TAB[1]),
        (1972, r'Freedman &' + '\n' + r'Clauser: first' + '\n' + r'Bell test', -1.8, TAB[2]),
        (1982, r'Aspect: locality' + '\n' + r'loophole closed', 1.2, TAB[3]),
        (2015, r'Triple loophole-free' + '\n' + r'tests (Delft, Vienna,' + '\n' + r'NIST)', -1.8, TAB[4]),
        (2022, r'Nobel Prize' + '\n' + r'(Aspect, Clauser,' + '\n' + r'Zeilinger) ★', 1.5, '#c8a900'),
    ]

    for year, label, yoff, color in events:
        # Tick
        ax.plot(year, 0, 'o', ms=9, color=color, zorder=3)
        # Stem
        stem_y = yoff * 0.6
        ax.plot([year, year], [0, stem_y], color=color, lw=1.2, ls='--', alpha=0.7, zorder=2)
        # Label
        va = 'top' if yoff < 0 else 'bottom'
        ax.text(year, stem_y + (0.08 if yoff > 0 else -0.08),
                label, ha='center', va=va, fontsize=7.5, color=color,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor=color, alpha=0.9, linewidth=1.0))
        # Year label on timeline
        ax.text(year, -0.15 if yoff > 0 else 0.15, str(year),
                ha='center', va='top' if yoff > 0 else 'bottom',
                fontsize=7.5, color='#555', fontweight='bold')

    # Arrow tips
    ax.annotate('', xy=(2028, 0), xytext=(2026, 0),
                arrowprops=dict(arrowstyle='->', color='#444', lw=2))

    # CHSH violation range annotation
    ax.annotate('', xy=(2015, 0.08), xytext=(1972, 0.08),
                arrowprops=dict(arrowstyle='<->', color='#aaa', lw=1))
    ax.text(1993.5, 0.18, '43 years of improving experiments', ha='center',
            fontsize=7.5, color='#888', style='italic')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    fig.tight_layout()
    save(fig, '03-bells-theorem-and-chsh-fig-03.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 5.1 — Quantum teleportation circuit
# ──────────────────────────────────────────────────────────────────────────────
def fig_05_01():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.5)
    ax.axis('off')
    ax.set_title('Quantum Teleportation Circuit', fontsize=11, fontweight='bold')

    # Three wires: S (top), A (middle), B (bottom)
    yS, yA, yB = 3.6, 2.2, 0.8
    wire_c = '#222'
    lw = 1.8

    ax.plot([0.5, 10.5], [yS, yS], color=wire_c, lw=lw, zorder=1)
    ax.plot([0.5, 10.5], [yA, yA], color=wire_c, lw=lw, zorder=1)
    ax.plot([0.5, 10.5], [yB, yB], color=wire_c, lw=lw, zorder=1)

    # Labels
    ax.text(0.2, yS, r'$S$', fontsize=11, va='center', ha='right', fontweight='bold', color=TAB[0])
    ax.text(0.2, yA, r'$A$', fontsize=11, va='center', ha='right', fontweight='bold', color=TAB[1])
    ax.text(0.2, yB, r'$B$', fontsize=11, va='center', ha='right', fontweight='bold', color=TAB[2])
    ax.text(0.15, yS+0.35, 'Alice', fontsize=8, color=TAB[0], ha='center')
    ax.text(0.15, yA+0.35, 'Alice', fontsize=8, color=TAB[1], ha='center')
    ax.text(0.15, yB+0.35, 'Bob', fontsize=8, color=TAB[2], ha='center')

    # Input state
    ax.text(0.55, yS+0.28, r'$|\psi\rangle = \alpha|0\rangle+\beta|1\rangle$',
            fontsize=8.5, va='bottom', ha='left', color=TAB[0])

    # Bell pair |Φ+⟩ between A and B — wavy line at x=1.5
    ax.text(1.5, (yA+yB)/2, r'$|\Phi^+\rangle$', ha='center', va='center',
            fontsize=8.5, color='#888',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#f0f0f0', edgecolor='#bbb'))
    # Wavy connector
    t = np.linspace(yB+0.15, yA-0.15, 100)
    wave_x = 1.6 + 0.08*np.sin(t*12)
    ax.plot(wave_x, t, color='#aaa', lw=1.2, ls='-', zorder=1)

    # ── CNOT: control S, target A, x=3.5 ──
    ax.plot(3.5, yS, 'o', ms=10, color=TAB[0], zorder=4)
    ax.plot([3.5, 3.5], [yS, yA], color=wire_c, lw=lw, zorder=2)
    cnot_r = 0.28
    cnot_circ = Circle((3.5, yA), cnot_r, facecolor='white', edgecolor=TAB[1], lw=1.8, zorder=3)
    ax.add_patch(cnot_circ)
    ax.plot([3.5-cnot_r, 3.5+cnot_r], [yA, yA], color=TAB[1], lw=1.5, zorder=4)
    ax.plot([3.5, 3.5], [yA-cnot_r, yA+cnot_r], color=TAB[1], lw=1.5, zorder=4)
    ax.text(3.5, yA-0.55, 'CNOT', ha='center', va='top', fontsize=7.5, color='#555')

    # ── H gate on S, x=5.0 ──
    hbox = FancyBboxPatch((4.65, yS-0.32), 0.7, 0.64,
                           boxstyle='round,pad=0.05', facecolor='#d4e6f1',
                           edgecolor=TAB[0], linewidth=1.5, zorder=3)
    ax.add_patch(hbox)
    ax.text(5.0, yS, r'$H$', ha='center', va='center', fontsize=12,
            fontweight='bold', color=TAB[0], zorder=4)

    # ── Measurement boxes on S and A, x=6.5 ──
    for yw, c in [(yS, TAB[0]), (yA, TAB[1])]:
        mbox = FancyBboxPatch((6.15, yw-0.32), 0.7, 0.64,
                               boxstyle='round,pad=0.05', facecolor='#fdf2e9',
                               edgecolor=c, linewidth=1.5, zorder=3)
        ax.add_patch(mbox)
        # Meter symbol
        arc = Arc((6.5, yw-0.05), 0.38, 0.32, angle=0, theta1=0, theta2=180,
                  color=c, lw=1.5, zorder=4)
        ax.add_patch(arc)
        ax.annotate('', xy=(6.72, yw+0.12), xytext=(6.5, yw-0.05),
                    arrowprops=dict(arrowstyle='->', color=c, lw=1.2), zorder=4)

    ax.text(6.5, yA-0.55, 'Measure', ha='center', va='top', fontsize=7.5, color='#555')

    # ── Classical channel (dashed lines down from S and A to B) ──
    ax.plot([6.8, 7.5, 7.5], [yS, yS, yB+0.35], color='#888', lw=1.2, ls='--', zorder=2)
    ax.plot([6.8, 7.8, 7.8], [yA, yA, yB+0.35], color='#888', lw=1.2, ls='--', zorder=2)
    ax.text(7.2, (yS+yB)/2, '2 classical bits', ha='left', va='center', fontsize=7.5,
            color='#888', style='italic', rotation=270)

    # ── Correction gate on B, x=8.5 ──
    cbox = FancyBboxPatch((8.15, yB-0.32), 0.7, 0.64,
                           boxstyle='round,pad=0.05', facecolor='#eafaf1',
                           edgecolor=TAB[2], linewidth=1.5, zorder=3)
    ax.add_patch(cbox)
    ax.text(8.5, yB, r'$I/X/Z/ZX$', ha='center', va='center', fontsize=8,
            color=TAB[2], fontweight='bold', zorder=4)

    # Output
    ax.text(9.8, yB+0.28, r'$|\psi\rangle$', fontsize=11, va='bottom', ha='left',
            color=TAB[2], fontweight='bold')
    ax.text(9.8, yB-0.1, 'teleported!', fontsize=7.5, va='top', ha='left',
            color=TAB[2], style='italic')

    # Resource accounting
    ax.text(5.5, 0.15,
            r'Resource: 1 ebit ($|\Phi^+\rangle$) + 2 cbits $\;\longrightarrow\;$ transmit 1 qubit',
            ha='center', va='bottom', fontsize=8.5, color='#444',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffde7', edgecolor='#e6b800', lw=1))

    fig.tight_layout()
    save(fig, '05-quantum-teleportation-and-dense-coding-fig-01.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 5.2 — Teleportation vs. Dense Coding side-by-side
# ──────────────────────────────────────────────────────────────────────────────
def fig_05_02():
    fig, (axL, axR) = plt.subplots(1, 2, **STYLE)
    fig.patch.set_facecolor('white')
    fig.suptitle('Teleportation and Dense Coding: The Same Resource, Opposite Directions',
                 fontsize=10, fontweight='bold', y=1.01)

    for ax, title, color in [(axL, 'Teleportation', TAB[0]), (axR, 'Dense Coding', TAB[1])]:
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 4)
        ax.axis('off')
        ax.set_title(title, fontsize=10, fontweight='bold', color=color)

        # Shared Bell pair
        ax.text(2.5, 3.6, r'Shared $|\Phi^+\rangle$ (1 ebit)', ha='center', va='center',
                fontsize=8.5, color='#888',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#f5f5f5', edgecolor='#bbb'))

    # ── LEFT: Teleportation ──
    axL.text(1.0, 2.85, 'Alice', ha='center', fontsize=8, color=TAB[0], fontweight='bold')
    axL.text(4.0, 2.85, 'Bob', ha='center', fontsize=8, color=TAB[2], fontweight='bold')

    # Input qubit
    axL.text(0.2, 2.3, r'$|\psi\rangle$', ha='center', va='center', fontsize=10, color=TAB[0])
    axL.annotate('', xy=(0.8, 2.3), xytext=(0.4, 2.3),
                arrowprops=dict(arrowstyle='->', color=TAB[0], lw=1.3))

    # Bell measurement box
    bm_box = FancyBboxPatch((0.8, 1.85), 1.4, 0.9,
                             boxstyle='round,pad=0.06', facecolor='#d4e6f1',
                             edgecolor=TAB[0], lw=1.5)
    axL.add_patch(bm_box)
    axL.text(1.5, 2.3, 'Bell\nMeasure', ha='center', va='center', fontsize=8, color=TAB[0])

    # Classical channel
    axL.annotate('', xy=(3.2, 2.3), xytext=(2.3, 2.3),
                arrowprops=dict(arrowstyle='->', color='#888', lw=1.2, linestyle='dashed'))
    axL.text(2.75, 2.5, '2 cbits', ha='center', fontsize=7.5, color='#888', style='italic')

    # Correction box
    corr_box = FancyBboxPatch((3.2, 1.85), 1.3, 0.9,
                               boxstyle='round,pad=0.06', facecolor='#eafaf1',
                               edgecolor=TAB[2], lw=1.5)
    axL.add_patch(corr_box)
    axL.text(3.85, 2.3, 'Correct\n$I/X/Z/ZX$', ha='center', va='center', fontsize=8, color=TAB[2])

    # Output
    axL.annotate('', xy=(4.8, 2.3), xytext=(4.5, 2.3),
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=1.3))
    axL.text(4.85, 2.3, r'$|\psi\rangle$', ha='left', va='center', fontsize=10, color=TAB[2])

    # Resource equation
    axL.text(2.5, 0.9,
             r'$1\ \text{ebit} + 2\ \text{cbits}$' + '\n' + r'$\longrightarrow 1\ \text{qubit}$',
             ha='center', va='center', fontsize=9, color='#333',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffde7', edgecolor='#e6b800', lw=1.2))

    # ── RIGHT: Dense Coding ──
    axR.text(1.0, 2.85, 'Alice', ha='center', fontsize=8, color=TAB[1], fontweight='bold')
    axR.text(4.0, 2.85, 'Bob', ha='center', fontsize=8, color=TAB[2], fontweight='bold')

    # 2-bit message
    axR.text(0.2, 2.3, r'$m \in \{00,01,10,11\}$', ha='left', va='center', fontsize=7.5, color=TAB[1])

    # Pauli encode box
    enc_box = FancyBboxPatch((0.3, 1.85), 1.6, 0.9,
                              boxstyle='round,pad=0.06', facecolor='#d4e6f1',
                              edgecolor=TAB[1], lw=1.5)
    axR.add_patch(enc_box)
    axR.text(1.1, 2.3, r'Pauli Encode' + '\n' + r'$I/X/Z/iY$', ha='center', va='center',
             fontsize=8, color=TAB[1])

    # Quantum channel (single qubit) arrow
    axR.annotate('', xy=(3.0, 2.3), xytext=(1.95, 2.3),
                arrowprops=dict(arrowstyle='->', color=TAB[3], lw=1.6))
    axR.text(2.45, 2.5, '1 qubit', ha='center', fontsize=7.5, color=TAB[3], style='italic')

    # Bell decode box
    dec_box = FancyBboxPatch((3.0, 1.85), 1.5, 0.9,
                              boxstyle='round,pad=0.06', facecolor='#eafaf1',
                              edgecolor=TAB[2], lw=1.5)
    axR.add_patch(dec_box)
    axR.text(3.75, 2.3, 'Bell\nDecode', ha='center', va='center', fontsize=8, color=TAB[2])

    # Output 2 bits
    axR.annotate('', xy=(4.8, 2.3), xytext=(4.5, 2.3),
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=1.3))
    axR.text(4.82, 2.3, r'$m$', ha='left', va='center', fontsize=10, color=TAB[2])

    # Resource equation
    axR.text(2.5, 0.9,
             r'$1\ \text{ebit} + 1\ \text{qubit channel}$' + '\n' + r'$\longrightarrow 2\ \text{cbits}$',
             ha='center', va='center', fontsize=9, color='#333',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#fffde7', edgecolor='#e6b800', lw=1.2))

    # Duality label
    fig.text(0.5, -0.02, 'Same entanglement resource — opposite direction of information flow',
             ha='center', va='top', fontsize=9, color='#555', style='italic')
    fig.tight_layout()
    save(fig, '05-quantum-teleportation-and-dense-coding-fig-02.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 6.1 — Branching-world decoherence diagram
# ──────────────────────────────────────────────────────────────────────────────
def fig_06_01():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis('off')
    ax.set_title('Decoherence: System–Environment Entanglement', fontsize=11, fontweight='bold')

    # Initial state (left)
    ax.text(0.8, 2.25,
            r'$|\psi_0\rangle|e_0\rangle$' + '\n' + r'$= (\alpha|0\rangle + \beta|1\rangle)|e_0\rangle$',
            ha='center', va='center', fontsize=9, color='#333',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0', edgecolor='#888', lw=1.2))

    ax.annotate('', xy=(2.2, 2.25), xytext=(1.6, 2.25),
                arrowprops=dict(arrowstyle='->', color='#666', lw=1.5))
    ax.text(2.0, 2.55, r'$\hat{H}_{SE}$', ha='center', fontsize=9, color='#666')

    # Fork point
    ax.plot(2.5, 2.25, 'o', ms=7, color='#555', zorder=3)

    # Upper branch: |0⟩ with |e₀(t)⟩
    ax.annotate('', xy=(5.2, 3.5), xytext=(2.6, 2.4),
                arrowprops=dict(arrowstyle='->', color=TAB[0], lw=1.8,
                                connectionstyle='arc3,rad=-0.2'))
    ax.text(5.4, 3.5, r'$\alpha|0\rangle|e_0(t)\rangle$', ha='left', va='center',
            fontsize=10, color=TAB[0],
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#eaf4fb', edgecolor=TAB[0], lw=1.3))

    # Lower branch: |1⟩ with |e₁(t)⟩
    ax.annotate('', xy=(5.2, 1.0), xytext=(2.6, 2.1),
                arrowprops=dict(arrowstyle='->', color=TAB[1], lw=1.8,
                                connectionstyle='arc3,rad=0.2'))
    ax.text(5.4, 1.0, r'$\beta|1\rangle|e_1(t)\rangle$', ha='left', va='center',
            fontsize=10, color=TAB[1],
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#fef9e7', edgecolor=TAB[1], lw=1.3))

    # Overlap bracket
    ax.annotate('', xy=(6.8, 1.0), xytext=(6.8, 3.5),
                arrowprops=dict(arrowstyle='<->', color='#888', lw=1.5))
    ax.text(7.05, 2.25, r'$\langle e_0(t)|e_1(t)\rangle$' + '\n' + r'$\to 0$ as branches diverge',
            ha='left', va='center', fontsize=9, color='#555')

    # Final reduced state
    ax.text(4.5, 0.3,
            r'$\hat\rho_S(t) = |\alpha|^2|0\rangle\langle 0|$' +
            r'$+ \langle e_1|e_0\rangle\alpha\beta^*|0\rangle\langle 1|$' +
            r'$+ \ldots \;\to\; |\alpha|^2|0\rangle\langle 0| + |\beta|^2|1\rangle\langle 1|$',
            ha='center', va='center', fontsize=8.5, color='#333',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef9e7', edgecolor='#c8a900', lw=1.2))

    ax.text(2.5, -0.25, 'Off-diagonals suppressed\nas branches diverge:', ha='center', va='top',
            fontsize=8, color='#888')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    fig.tight_layout()
    save(fig, '06-open-systems-and-lindblad-fig-01.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 6.2 — Annotated Bloch sphere with T₁, T₂ processes
# ──────────────────────────────────────────────────────────────────────────────
def fig_06_02():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(-1.8, 3.2)
    ax.set_ylim(-2.0, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Bloch Sphere: Precession ($\omega_0$), Dephasing ($T_2$), Relaxation ($T_1$)',
                 fontsize=10, fontweight='bold')

    # Draw sphere (ellipse for projection)
    sphere = plt.matplotlib.patches.Ellipse((0, 0), 2.0, 2.0,
                                             facecolor='#f8fafc', edgecolor='#b0c4d8',
                                             linewidth=1.5, zorder=1)
    ax.add_patch(sphere)
    # Equator (dashed ellipse)
    equator = matplotlib.patches.Ellipse((0, 0), 2.0, 0.5,
                                          facecolor='none', edgecolor='#c0c0c0',
                                          linewidth=1.0, linestyle='--', zorder=2)
    ax.add_patch(equator)

    # z-axis
    ax.annotate('', xy=(0, 1.3), xytext=(0, -1.3),
                arrowprops=dict(arrowstyle='->', color='#555', lw=1.5))
    ax.text(0.06, 1.35, r'$z$', fontsize=10, color='#555')

    # North / South pole labels
    ax.text(0, 1.05, r'$|0\rangle$', ha='center', va='bottom', fontsize=9,
            color='#333', fontweight='bold')
    ax.text(0, -1.15, r'$|1\rangle$', ha='center', va='top', fontsize=9,
            color='#333', fontweight='bold')
    ax.plot(0, 1.0, 'o', ms=5, color='#333', zorder=4)
    ax.plot(0, -1.0, 'o', ms=5, color='#333', zorder=4)

    # Sample Bloch vector (starting point)
    rx, ry = 0.55, 0.45
    ax.annotate('', xy=(rx, ry), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=TAB[3], lw=2.0), zorder=5)
    ax.text(rx+0.08, ry+0.08, r'$\vec{r}(t)$', fontsize=9, color=TAB[3])

    # ── Process 1: Precession (orange circular arrow around z) ──
    theta_pre = np.linspace(np.pi*0.1, np.pi*1.5, 60)
    prec_r = 0.65
    prec_x = prec_r * np.cos(theta_pre)
    prec_y = 0.22 * np.sin(theta_pre)  # flattened equatorial ellipse
    ax.plot(prec_x, prec_y, color=TAB[5], lw=1.8, zorder=3)
    # Arrow tip
    ax.annotate('', xy=(prec_x[-1], prec_y[-1]),
                xytext=(prec_x[-2], prec_y[-2]),
                arrowprops=dict(arrowstyle='->', color=TAB[5], lw=1.8))
    ax.text(-0.85, 0.35, r'precession $\omega_0$', ha='center', fontsize=8, color=TAB[5],
            bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=TAB[5], alpha=0.85, lw=1))

    # ── Process 2: Transverse shrinkage toward z-axis (T₂) ──
    ax.annotate('', xy=(0.0, ry), xytext=(rx*1.25, ry),
                arrowprops=dict(arrowstyle='->', color=TAB[0], lw=1.5,
                                connectionstyle='arc3,rad=0'))
    ax.text(1.3, ry+0.18, r'$T_2$: transverse decay', ha='left', fontsize=8, color=TAB[0])
    ax.text(1.3, ry, r'(shrink toward $z$-axis)', ha='left', fontsize=7.5, color=TAB[0])

    # ── Process 3: Longitudinal decay toward ground state (T₁) ──
    ax.annotate('', xy=(0.0, -0.85), xytext=(0.0, ry*0.5),
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=1.8,
                                connectionstyle='arc3,rad=-0.3'))
    ax.text(0.25, -0.35, r'$T_1$: relax to $|0\rangle$', ha='left', fontsize=8, color=TAB[2])

    # Constraint box
    ax.text(2.7, -1.4,
            r'$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$' + '\n' + r'$T_2 \leq 2T_1$',
            ha='center', va='center', fontsize=9.5,
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#fff3cd', edgecolor='#c8a900', lw=1.5))

    fig.tight_layout()
    save(fig, '06-open-systems-and-lindblad-fig-02.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 8.1 — NV center vs. transmon energy level diagrams
# ──────────────────────────────────────────────────────────────────────────────
def fig_08_01():
    fig, (axL, axR) = plt.subplots(1, 2, **STYLE)
    fig.patch.set_facecolor('white')
    fig.suptitle('NV Center and Transmon: Different Physics, Same Two-Level Structure',
                 fontsize=10, fontweight='bold', y=1.01)

    # ── LEFT: NV center (spin-1) ──
    axL.set_xlim(0, 4)
    axL.set_ylim(-0.5, 5.5)
    axL.axis('off')
    axL.set_title('NV Center (spin-1)', fontsize=9.5, fontweight='bold', color=TAB[0])

    # Energy levels (schematic, not to scale)
    # ms=0 (ground), ms=±1 (split by D + Zeeman)
    # Level positions
    e_ms0 = 0.8
    e_msm1 = 2.4   # ms=-1
    e_msp1 = 3.5   # ms=+1
    e_exc = 4.8    # excited state (not labeled in detail)

    lw_lvl = 2.0
    # Ground state triplet
    axL.plot([0.5, 2.0], [e_ms0, e_ms0], color=TAB[0], lw=lw_lvl)
    axL.text(2.1, e_ms0, r'$|m_s=0\rangle$', va='center', fontsize=8.5, color=TAB[0])

    axL.plot([0.5, 2.0], [e_msm1, e_msm1], color=TAB[1], lw=lw_lvl)
    axL.text(2.1, e_msm1, r'$|m_s=-1\rangle$', va='center', fontsize=8.5, color=TAB[1])

    axL.plot([0.5, 2.0], [e_msp1, e_msp1], color='#aaa', lw=lw_lvl, ls='--')
    axL.text(2.1, e_msp1, r'$|m_s=+1\rangle$', va='center', fontsize=8.5, color='#aaa')

    # D splitting bracket
    axL.annotate('', xy=(0.3, e_msp1), xytext=(0.3, e_ms0),
                arrowprops=dict(arrowstyle='<->', color='#888', lw=1.2))
    axL.text(0.15, (e_ms0+e_msp1)/2, r'$D \approx 2.87$' + '\nGHz',
             ha='center', va='center', fontsize=7.5, color='#666', rotation=90)

    # Zeeman splitting bracket
    axL.annotate('', xy=(2.1+1.7, e_msp1), xytext=(2.1+1.7, e_msm1),
                arrowprops=dict(arrowstyle='<->', color='#666', lw=1.0))
    axL.text(3.95, (e_msm1+e_msp1)/2, r'$2g_e\mu_B B$', ha='center', va='center',
             fontsize=7.5, color='#666')

    # Qubit subspace highlight
    qs_rect = FancyBboxPatch((0.4, e_ms0-0.18), 1.7, e_msm1-e_ms0+0.36,
                              boxstyle='round,pad=0.05',
                              facecolor='#d4e6f1', edgecolor=TAB[0], lw=1.5, alpha=0.4)
    axL.add_patch(qs_rect)
    axL.text(1.25, (e_ms0+e_msm1)/2, r'qubit $\{|0\rangle,|1\rangle\}$',
             ha='center', va='center', fontsize=7.5, color=TAB[0], fontweight='bold')

    # Transition arrow
    axL.annotate('', xy=(1.9, e_msm1-0.05), xytext=(1.9, e_ms0+0.05),
                arrowprops=dict(arrowstyle='<->', color=TAB[1], lw=1.5))
    axL.text(1.72, (e_ms0+e_msm1)/2+0.5, r'$\nu_{0,-1}$', ha='right',
             fontsize=8.5, color=TAB[1])

    axL.set_ylim(-0.5, 5.5)

    # ── RIGHT: Transmon ──
    axR.set_xlim(0, 4)
    axR.set_ylim(-0.5, 5.5)
    axR.axis('off')
    axR.set_title('Transmon (Josephson circuit)', fontsize=9.5, fontweight='bold', color=TAB[2])

    # Harmonic oscillator levels + anharmonicity (energy levels)
    # En = n*ω - n(n-1)/2 * |α| with α ≈ -0.3 GHz
    omega = 1.0   # in units
    anharmonicity = -0.22  # relative units

    levels = []
    for n in range(5):
        E = n * omega + n*(n-1)/2 * anharmonicity
        levels.append(E)

    # Normalize: set |0⟩ at 0.5, scale
    E0 = levels[0]
    scale = 0.9
    offset = 0.5
    y_levels = [offset + (E - E0)*scale for E in levels]

    colors_t = [TAB[2], TAB[3], '#aaa', '#bbb', '#ccc']
    labels_t = [r'$|0\rangle$ ($n=0$)', r'$|1\rangle$ ($n=1$)', r'$|2\rangle$ ($n=2$)',
                r'$|3\rangle$', r'$|4\rangle$']
    for i, (y_lvl, c, lbl) in enumerate(zip(y_levels[:4], colors_t[:4], labels_t[:4])):
        ls = '--' if i >= 2 else '-'
        axR.plot([0.5, 2.2], [y_lvl, y_lvl], color=c, lw=lw_lvl, ls=ls)
        axR.text(2.3, y_lvl, lbl, va='center', fontsize=8.5, color=c)

    # Qubit subspace highlight
    qs_rect2 = FancyBboxPatch((0.4, y_levels[0]-0.18), 1.9, y_levels[1]-y_levels[0]+0.36,
                               boxstyle='round,pad=0.05',
                               facecolor='#fdebd0', edgecolor=TAB[2], lw=1.5, alpha=0.4)
    axR.add_patch(qs_rect2)
    axR.text(1.35, (y_levels[0]+y_levels[1])/2, r'qubit $\{|0\rangle,|1\rangle\}$',
             ha='center', va='center', fontsize=7.5, color=TAB[2], fontweight='bold')

    # ω₀ transition
    axR.annotate('', xy=(2.15, y_levels[1]-0.05), xytext=(2.15, y_levels[0]+0.05),
                arrowprops=dict(arrowstyle='<->', color=TAB[3], lw=1.5))
    axR.text(1.98, (y_levels[0]+y_levels[1])/2 + 0.3, r'$\omega_0$', ha='right',
             fontsize=9, color=TAB[3])

    # Anharmonicity bracket
    axR.annotate('', xy=(0.35, y_levels[2]), xytext=(0.35, y_levels[1]),
                arrowprops=dict(arrowstyle='<->', color='#888', lw=1.0))
    axR.text(0.2, (y_levels[1]+y_levels[2])/2, r'$\alpha$', ha='center', va='center',
             fontsize=8.5, color='#888')
    axR.text(0.2, (y_levels[1]+y_levels[2])/2-0.3, r'$\approx -300$' + '\nMHz',
             ha='center', va='top', fontsize=7, color='#888')

    # Shared conclusion at bottom
    fig.text(0.5, -0.04,
             r'Both reduce to $\hat H = (\hbar\omega_0/2)\hat\sigma_z$ in the $\{|0\rangle,|1\rangle\}$ subspace',
             ha='center', fontsize=9, color='#444', style='italic')

    fig.tight_layout()
    save(fig, '08-quantum-hardware-fig-01.png')


# ──────────────────────────────────────────────────────────────────────────────
# Fig 9.1 — Surface code d=3 geometry
# ──────────────────────────────────────────────────────────────────────────────
def fig_09_01():
    fig, ax = plt.subplots(**STYLE)
    fig.patch.set_facecolor('white')
    ax.set_xlim(-0.8, 5.0)
    ax.set_ylim(-0.8, 3.8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Surface Code ($d=3$): Data Qubits, $X$-Plaquettes, $Z$-Stars',
                 fontsize=10, fontweight='bold')

    d = 3
    # Data qubit positions on a 3×3 grid
    data_pos = [(col, row) for row in range(d) for col in range(d)]
    # X stabilizers: plaquette centers (between 4 data qubits)
    # For d=3, plaquettes at half-integer positions inside the grid
    x_stab_pos = [(col+0.5, row+0.5) for row in range(d-1) for col in range(d-1)]  # 4 plaquettes
    # Z stabilizers: star centers (between 4 data qubits — at same positions but different topology)
    # Stars sit on edge-shared positions; for simplicity, interleave
    # In standard surface code layout, X and Z stabilizers alternate in a checkerboard
    # Use the rotated square lattice arrangement:
    # X-stabilizers (blue squares) at (0.5,0.5),(1.5,0.5),(0.5,1.5),(1.5,1.5)
    # Z-stabilizers (red stars) at (0.5,0.5+1),(1.5,0.5+1)... — need to offset

    # Simpler: draw on a tilted lattice
    # Actually use the standard unrotated picture with 9 data + 4 X + 4 Z
    # Place X-stabilizers and Z-stabilizers in checkerboard of face/edge
    # Standard picture: alternating plaquettes
    x_plaq = [(0.5, 0.5), (1.5, 1.5)]  # 2 X plaquettes (blue)
    z_star = [(1.5, 0.5), (0.5, 1.5)]  # 2 Z stars (red) — interior

    # Also boundary stabilizers (weight-2): edges of boundary
    # For clarity, draw the 4 interior stabilizers and note boundaries
    x_plaq_all = [(0.5, 0.5), (1.5, 0.5), (0.5, 1.5), (1.5, 1.5)]  # all 4 in 3x3

    # Actually for d=3 standard surface code (rotated):
    # 9 data qubits, 4 X-stabilizers (plaquettes), 4 Z-stabilizers (vertices)
    # Use the simple square lattice where:
    # X-stabilizers = faces at (col+0.5, row+0.5) for (col,row) in {(0,0),(1,0),(0,1),(1,1)}
    # Z-stabilizers = vertex positions but shifted to avoid overlap
    # => use checkerboard: X at even-sum faces, Z at odd-sum faces

    # Draw grid edges
    for row in range(d):
        for col in range(d):
            if col < d-1:
                ax.plot([col, col+1], [row, row], color='#ccc', lw=1.0, zorder=1)
            if row < d-1:
                ax.plot([col, col], [row, row+1], color='#ccc', lw=1.0, zorder=1)

    # Draw X-stabilizers (blue squares at faces)
    x_plaq_centers = [(0.5, 0.5), (1.5, 1.5)]
    z_plaq_centers = [(1.5, 0.5), (0.5, 1.5)]

    for (cx, cy) in x_plaq_centers:
        sq = plt.Polygon([(cx-0.45, cy-0.45), (cx+0.45, cy-0.45),
                          (cx+0.45, cy+0.45), (cx-0.45, cy+0.45)],
                         closed=True, facecolor=TAB[0], alpha=0.25,
                         edgecolor=TAB[0], linewidth=1.5, zorder=2)
        ax.add_patch(sq)
        ax.text(cx, cy, r'$X$', ha='center', va='center', fontsize=10,
                color=TAB[0], fontweight='bold', zorder=4)

    for (cx, cy) in z_plaq_centers:
        sq = plt.Polygon([(cx-0.45, cy-0.45), (cx+0.45, cy-0.45),
                          (cx+0.45, cy+0.45), (cx-0.45, cy+0.45)],
                         closed=True, facecolor=TAB[3], alpha=0.25,
                         edgecolor=TAB[3], linewidth=1.5, zorder=2)
        ax.add_patch(sq)
        ax.text(cx, cy, r'$Z$', ha='center', va='center', fontsize=10,
                color=TAB[3], fontweight='bold', zorder=4)

    # Draw data qubits
    for (col, row) in data_pos:
        circ = Circle((col, row), 0.22, facecolor='white', edgecolor='#333',
                      linewidth=2.0, zorder=3)
        ax.add_patch(circ)
        ax.text(col, row, f'{row*d+col+1}', ha='center', va='center',
                fontsize=7.5, color='#333', zorder=5)

    # Logical X̄ chain: horizontal, top row, length d=3
    ax.annotate('', xy=(2.25, 2.0+0.35), xytext=(-0.25, 2.0+0.35),
                arrowprops=dict(arrowstyle='->', color=TAB[0], lw=2.0))
    ax.text(1.0, 2.48, r'$\bar{X}$ (length $d=3$)', ha='center', va='bottom',
            fontsize=8.5, color=TAB[0], fontweight='bold')

    # Logical Z̄ chain: vertical, right column, length d=3
    ax.annotate('', xy=(2.0+0.35, 2.25), xytext=(2.0+0.35, -0.25),
                arrowprops=dict(arrowstyle='->', color=TAB[3], lw=2.0))
    ax.text(2.58, 1.0, r'$\bar{Z}$', ha='left', va='center',
            fontsize=8.5, color=TAB[3], fontweight='bold')
    ax.text(2.6, 0.6, r'(length $d=3$)', ha='left', va='center',
            fontsize=7.5, color=TAB[3])

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=TAB[0], alpha=0.4, edgecolor=TAB[0], label=r'$X$-stabilizer (detects $Z$ errors)'),
        mpatches.Patch(facecolor=TAB[3], alpha=0.4, edgecolor=TAB[3], label=r'$Z$-stabilizer (detects $X$ errors)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='white',
               markeredgecolor='#333', markersize=9, label='Data qubit'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=7.5,
              framealpha=0.9, edgecolor='#ccc', bbox_to_anchor=(-0.05, -0.25))

    ax.text(1.0, -0.55,
            r'$[\![9,1,3]\!]$ code: 9 data qubits, 1 logical qubit, distance $d=3$',
            ha='center', va='top', fontsize=8, color='#555', style='italic')

    fig.tight_layout()
    save(fig, '09-error-and-the-threshold-theorem-fig-01.png')


# ──────────────────────────────────────────────────────────────────────────────
# Run all
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("Generating 11 missing figures for quantum-mechanics-vol4...")
    fig_02_01()
    fig_02_02()
    fig_02_03()
    fig_03_01()
    fig_03_03()
    fig_05_01()
    fig_05_02()
    fig_06_01()
    fig_06_02()
    fig_08_01()
    fig_09_01()
    print("Done.")
