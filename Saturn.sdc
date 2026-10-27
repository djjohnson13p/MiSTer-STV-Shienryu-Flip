derive_pll_clocks
derive_clock_uncertainty

# HQ2x is active in this isolated variant.  Its internal clock enable can
# update every two clk_sys cycles in supported low-resolution modes.
# The released, previously pruned setup4/hold3 exception is not valid here.
# Analyze HQ2x conservatively without a blanket multicycle exception.

set_multicycle_path -from [get_clocks { *|pll|pll_inst|altera_pll_i|*[1].*|divclk}] -to {ascal|*} -setup 4
set_multicycle_path -from [get_clocks { *|pll|pll_inst|altera_pll_i|*[1].*|divclk}] -to {ascal|*} -hold 3
