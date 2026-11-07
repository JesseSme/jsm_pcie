# jsm_pcie

PCIe Gen1 x1 endpoint on the SkyWater SKY130 process: digital core plus on-chip PHY. Planning and specification workspace.

- [Specification chapters](specification/INDEX.md): verbatim text, summaries and extracted requirement candidates.
- [Extraction method and validation](specification/README.md).
- [Endpoint profile](docs/endpoint-profile.md).
- [SKY130 implementation target](docs/asic-target.md), [on-chip PHY architecture](docs/phy-architecture.md) and [fabrication routes](docs/fabrication-routes.md).
- [Implementation tickets](tickets/INDEX.md) and [agent workflow](tickets/README.md).

The backlog targets synthesizable SystemVerilog hardened with OpenLane/OpenROAD, pyuvm digital verification, and transistor-level PHY design verified in ngspice with SKY130 models. Endpoint RTL and circuits are not implemented yet.

Edit to test.
