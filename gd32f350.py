from generator import *

data_path = "./data/"
gd32f350_af_fn = data_path + "GD32F350 alternate functions summary.xlsx"
gd32f350gx_pins_fn = data_path + "GD32F350Gx_QFN28_pins.txt"			
gd32f350kx_pins_fn = data_path + "GD32F350Kx_QFN32_pins.txt"	
gd32f350cx_pins_fn = data_path + "GD32F350Cx_LQFP48_pins.txt"	
gd32f350rx_pins_fn = data_path + "GD32F350Rx_LQFP64_pins.txt"	

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

# Construct the pins config
pins_config = pins_config_construct(af_summary, package_pins)

af_summary.close()

# Format pinctrl config from pins config 
pinctrl_pins_config = pinctrl_pins_config_format(pins_config)

print(pinctrl_pins_config)
