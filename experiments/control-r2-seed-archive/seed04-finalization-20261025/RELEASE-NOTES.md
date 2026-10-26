Experimental Shienryu-only, HDMI-only, dual-SDRAM build. This seed4 supersedes the previous install package. Audio, video and180-degree flip were confirmed on a first-generation dual-RAM MiSTer Pi.

## Download and install

Download **MiSTer-STV-Shienryu-Flip-seed04-20261025.zip** below. Extract it and copy the contents of install/ to the SD-card root. Keep the supplied SHYF0004.rbf and SHYF0004.mra names together. Compatible shienryu.zip and stvbios.zip are required separately and are not included.

F12 → Audio & Video → Shienryu180 Flip → On/Off. Fresh settings default Off; use Save settings to retain your choice. Existing settings may retain On. The active HDMI game picture rotates180degrees; OSD orientation is separate. No90-degree or analog/direct-video feature is provided.

## Experimental timing

Full-range timing closure has not been achieved. All conditions below are1.1V; slack is ns. Recovery/removal/minimum pulse width pass all8. Negative setup slack fails.

| Model | C | Setup | Hold | Result |
|---|---:|---:|---:|---|
| Slow | -40 | -0.101 | +0.174 | Fail setup |
| Slow | 0 | -0.038 | +0.172 | Fail setup |
| Slow | 85 | +0.070 | +0.242 | Pass |
| Slow | 100 | +0.014 | +0.235 | Pass |
| Fast | -40 | +3.441 | +0.052 | Pass |
| Fast | 0 | +3.350 | +0.054 | Pass |
| Fast | 85 | +2.972 | +0.089 | Pass |
| Fast | 100 | +2.923 | +0.093 | Pass |

RBF SHA256:99654dbf7a472b610f840f9dbbb0087bc6f508ce3dfdfe2ffbd48e6df5396d11.

The compiled-source ZIP and manifest are attached; source is based on7e987bb9ef0361356be22be13551e4626902f3a7, Quartus25.1 Lite, seed4, fixed build date261025. Exact archived binaries/checkpoints can be restored; identical fresh recompilation is not claimed. The repository README records test scope and inherited timing qualifications. The earlier v1.1 release/tag remains available as historical recovery.
