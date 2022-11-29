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

print(yaml.dump(signal_configs, default_flow_style=False))
print(yaml.dump(pins, default_flow_style=False))
