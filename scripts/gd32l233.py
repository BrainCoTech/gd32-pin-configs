import yaml
from pin_definitions import parse_pin_definitions, parse_pin_af_summary
from pin_configs import generate_pin_configs

gd32_pin_definitions = {}

# Change GD32L233Kx-QFN32 pincode to 'Q', avoid pincode conflict with GD32F233Kx-LQFP32
gd32_pin_definitions['Q'] = parse_pin_definitions('./data/GD32L233/GD32L233Kx-QFN32-pin-definitions.xlsx')

gd32_pin_definitions['K'] = parse_pin_definitions('./data/GD32L233/GD32L233Kx-LQFP32-pin-definitions.xlsx')

gd32_pin_definitions['C'] = parse_pin_definitions('./data/GD32L233/GD32L233Cx-LQFP48-pin-definitions.xlsx')

gd32_pin_definitions['R'] = parse_pin_definitions('./data/GD32L233/GD32L233Rx-LQFP64-pin-definitions.xlsx')

summary = parse_pin_af_summary('./data/GD32L233/pin-alternate-functions-summary.xlsx')

signal_configs, pins = generate_pin_configs(gd32_pin_definitions, summary)

pin_configs_prefix = """
# GD32L233XX pin definitions
#
# Sources:
# - GD32L233XX Datasheet (Revision 1.2)
#
# Pin codes:
#
# - 32 pins: Q (GD32L233Kx-QFN32)
# - 32 pins: K (GD32L233Kx-LQFP32)
# - 48 pins: C
# - 64 pins: R
#
# Memory codes:
#
# - 64Kb   Flash, 16Kb  SRAM: 8
# - 128Kb  Flash, 24Kb  SRAM: B
# - 256Kb  Flash, 32Kb  SRAM: C
#
# Copyright (c) 2021 BrainCo Inc.
# SPDX-License-Identifier: Apache 2.0

model: af

series: gd32l233

variants:
  - pincode: Q
    memories: [8, B]
  - pincode: K
    memories: [8, B]
  - pincode: C
    memories: [8]
  - pincode: C
    memories: [B, C]
  - pincode: R
    memories: [8]
  - pincode: R
    memories: [B, C]
"""

print(pin_configs_prefix)
print(yaml.dump({"signal-configs":signal_configs}, default_flow_style=False))
print(yaml.dump({"pins":pins}, default_flow_style=False))
