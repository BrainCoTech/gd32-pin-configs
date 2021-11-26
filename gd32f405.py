from generator import *

data_path = "./data/"
gd32f405_af_fn = data_path + "GD32F405 alternate functions summary.xlsx"
gd32f405rx_pins_fn = data_path + "GD32F405Rx_LQFP64_pins.txt"			
gd32f405vx_pins_fn = data_path + "GD32F405Vx_LQFP100_pins.txt"	
gd32f405zx_pins_fn = data_path + "GD32F405Zx_LQFP144_pins.txt"	

package_pins = {}

# Load GD32F405Rx pin definitions
rx_pins = open(gd32f405rx_pins_fn, 'r')
package_pins['R'] = rx_pins.read().split()
rx_pins.close()

# Load GD32F405Vx pin definitions
vx_pins = open(gd32f405vx_pins_fn, 'r')
package_pins['V'] = vx_pins.read().split()
vx_pins.close()

# Load GD32F405Zx pin definitions
zx_pins = open(gd32f405zx_pins_fn, 'r')
package_pins['Z'] = zx_pins.read().split()
zx_pins.close()

# Load gd32f405 alternate functions summary from excel
af_summary = load_af_summary(gd32f405_af_fn)

# Construct the pins config
pins_config = pins_config_construct(af_summary, package_pins)

af_summary.close()

# Format pinctrl config from pins config 
pinctrl_pins_config = pinctrl_pins_config_format(pins_config)

print(pinctrl_pins_config)
