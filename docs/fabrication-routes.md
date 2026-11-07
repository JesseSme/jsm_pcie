# SKY130 fabrication routes

Checked **2026-11-07**. Shuttle schedules, prices and terms change; PCIE-057 must re-verify before any commitment, and nothing here commits money or a schedule. No submission happens without explicit user approval.

## Summary

| Route | Status (2026-11-07) | Area and I/O | Deliverables and price | Fit for this design |
|---|---|---|---|---|
| **ChipFoundry chipIgnite** | Scheduled. CI2612 commitment closed 2026-11-04. Next: **CI2705** commit 2027-03-20, tapeout 2027-05-19, delivery 2027-11-03; **CI2709** commit 2027-07-24, tapeout 2027-09-22, delivery 2028-03-08 | Harness with fixed pad ring: Caravel ~10 mm², 38 GPIO; **Caravan** ~10 mm², 27 GPIO + **11 bare pads**; **OpenFrame** ~15 mm², 44 GPIO | $14,950 per tapeout; 100 QFN parts or bare die; evaluation board; private designs allowed; open-source flow (OpenLane) | Best scheduled option. The PHY must use harness pads: Caravan bare pads are the most promising for the PCIe pairs and REFCLK, but their capacitance and ESD are undocumented, and QFN parasitics matter at 2.5 Gb/s |
| **Cadence SKY130 MPW aggregation** | Runs in May 2025 and with a 2026-01-16 deadline; **no later run published** | Full-custom box 3.588 mm × 5.188 mm (~18.6 mm²) with seal ring added; own pad ring allowed | $10,000 per design (2025 terms); 40 bare die; designer packages and tests | Allows custom high-speed pads and short bond wires, which suits the PHY. Requires Cadence Pegasus DRC-clean OASIS, Cadence's PDK variant (registration) and a legal agreement. Contact SKY130MPW@cadence.com for future runs |
| **SkyWater direct MPW** | SkyWater lists S130 shuttles (e.g. #25 cutoff 2026-01-15, #26 cutoff 2026-04-15); later dates not found | Per agreement | Pricing not public; business agreement required | Possible but commercial; not an open-community route |
| **Tiny Tapeout** | SKY26d, SKY26e (and GF26c) listed as open; closing dates not shown on the homepage | Small tiles; analog template available | Priced by tile count; calculator at app.tinytapeout.com | Far too small for the chip. A possible low-cost silicon check of individual PHY cells (bias, divided VCO output), but not for 2.5 Gb/s measurements |

## Context

- **Efabless**, the original open SKY130 shuttle provider, shut down in early 2025. ChipFoundry now runs chipIgnite and also supplies Tiny Tapeout's SKY130 back end; its schedule is thinner than Efabless's old quarterly cadence, and a shuttle below its minimum commitment rolls over or refunds.
- **SkyWater ownership:** IonQ completed its acquisition of SkyWater on 2026-07-31. IonQ says SkyWater remains committed to its foundry customers. No statement was found about the open SKY130 PDK or community shuttles, so treat their continuation as a schedule risk.

## Consequences for the plan

1. **Realistic timing:** with no RTL or circuits yet, CI2705 (commit 2027-03-20) is not realistic for the full chip. The PCIE-060 PHY loopback top is the most plausible first silicon target, on a 2027-2028 shuttle.
2. **Pads decide the route:** PCIE-052 must characterize Caravan bare pads and OpenFrame GPIO pads (capacitance, ESD, series resistance) and model QFN parasitics. If they cannot carry 2.5 Gb/s, only a custom-pad-ring route (Cadence aggregation or SkyWater direct) supports the on-chip PHY.
3. **Area budget:** about 10 mm² (Caravel/Caravan), about 15 mm² (OpenFrame) or about 18.6 mm² (Cadence box). PCIE-003 sizes the chip against these.
4. **Tool compatibility:** ChipFoundry uses the open OpenLane flow and harness templates (PCIE-050). The Cadence route needs Pegasus DRC and OASIS output, which the open flow does not provide; check university Cadence licensing if that route is chosen.

## Sources

- [ChipFoundry home and chipIgnite schedule](https://chipfoundry.io/)
- [ChipFoundry chipIgnite FAQ](https://chipfoundry.io/faqs)
- [Tiny Tapeout: ChipFoundry SKY130 shuttle confirmed (2025-06-26)](https://tinytapeout.com/news/sky130-confirmed/)
- [Tiny Tapeout home (shuttle list)](https://tinytapeout.com/)
- [Tiny Tapeout: Efabless shuts down](https://tinytapeout.com/news/efabless-shutsdown/)
- [SkyWater: Cadence launches MPW aggregation service for SKY130 (2025-05-05)](https://www.skywatertechnology.com/lowering-barriers-to-silicon-cadence-launches-mpw-aggregation-service-for-sky130/)
- [Cadence: Next steps for the Cadence and SkyWater MPW service](https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/next-steps-for-the-cadence-and-skywater-mpw-service)
- [SkyWater MPW programs](https://www.skywatertechnology.com/mpw/)
- [IonQ completes acquisition of SkyWater Technology](https://ionq.com/news/ionq-completes-acquisition-of-skywater-technology)
