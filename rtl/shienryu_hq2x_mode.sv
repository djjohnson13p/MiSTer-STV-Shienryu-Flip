// Hold the HQ2x raster mode for a complete input frame.  The blanking signal
// must accompany the RGB presented to video_mixer (cofi_vbl in this core).
// Native mode changes are qualified at the next blanking edge; the video
// pipeline/scaler may reacquire for multiple frames after a mode transition.
module shienryu_hq2x_mode (
    input  wire clk,
    input  wire reset,
    input  wire request,
    input  wire vblank,
    input  wire interlaced,
    input  wire hires,
    output reg  enabled = 1'b0
);
    reg previous_vblank = 1'b0;

    always @(posedge clk) begin
        previous_vblank <= vblank;
        if (reset)
            enabled <= 1'b0;
        else if (vblank && !previous_vblank)
            enabled <= request && !interlaced && !hires;
    end
endmodule
