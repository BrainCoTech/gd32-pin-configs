from generator import *
import yaml

data_path = "./data/"
gd32f350_af_fn = data_path + "GD32F350 alternate functions summary.xlsx"
gd32f350gx_pins_fn = data_path + "GD32F350Gx_QFN28_pins.txt"			
gd32f350kx_pins_fn = data_path + "GD32F350Kx_QFN32_pins.txt"	
gd32f350cx_pins_fn = data_path + "GD32F350Cx_LQFP48_pins.txt"	
gd32f350rx_pins_fn = data_path + "GD32F350Rx_LQFP64_pins.txt"	
gd32f350xx_exclude_memories_groups_fn = data_path + "GD32F350_exclude_memories_groups.yml"

package_pins = {}

# Load GD32F350Gx pin definitions
gx_pins = open(gd32f350gx_pins_fn, 'r')
package_pins['G'] = gx_pins.read().split()
gx_pins.close()

# Load GD32F350Kx pin definitions
kx_pins = open(gd32f350kx_pins_fn, 'r')
package_pins['K'] = kx_pins.read().split()
kx_pins.close()

# Load GD32F350Cx pin definitions
cx_pins = open(gd32f350cx_pins_fn, 'r')
package_pins['C'] = cx_pins.read().split()
cx_pins.close()

# Load GD32F350Rx pin definitions
rx_pins = open(gd32f350rx_pins_fn, 'r')
package_pins['R'] = rx_pins.read().split()
rx_pins.close()

# Load GD32F350 alternate functions summary from excel
af_summary = load_af_summary(gd32f350_af_fn)

# Load GD32F350 memory groups
with open(gd32f350xx_exclude_memories_groups_fn, 'r') as mem_cfg:
	exclude_memories_groups_cfg = yaml.safe_load(mem_cfg)

exclude_memories_groups = {}
for group in exclude_memories_groups_cfg['groups'].items():
	exclude_memories_groups[str(group[0])] = group[1]

# Construct the pins config
pinctrl_config = pinctrl_config_construct(af_summary, package_pins, exclude_memories_groups)

af_summary.close()

# Format pinctrl config from pins config 
pinctrl_config_yaml = pinctrl_config_format(pinctrl_config)

print(pinctrl_config_yaml)
