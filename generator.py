from openpyxl import load_workbook

# Remove white space from workbook
def remove_whilespace(s):
	for i in range(1, s.max_row + 1):
		for j in range(1, s.max_column + 1):
			c = s.cell(row = i, column = j)
			if c.value:
				c.value = ''.join(str(c.value).split())

# Load workbook wrapper
def load_af_summary(fn):
	wb = load_workbook(fn)
	remove_whilespace(wb.worksheets[0])
	return wb

'''
Format alternate functions summary and pin definitions to get pinctrl config.

return format: 
{
	'PA0': {
		'pincodes': ['A', 'B', 'C']
		'afs': {
			'modex': 0,
			'modey': 1
		}
	},
	'PA0': {
		'pincodes': ['B', 'C']
		'afs': {
			'modey': 0,
			'modez': 1
		}
	}
}
'''
def pins_config_construct(af_summary, package_pins):
	cfg = {}
	s = af_summary.worksheets[0]
	for i in range(2, s.max_row + 1):
		pin_name = s.cell(row = i, column = 1)

		afs = {}
		for j in range(2, s.max_column + 1):
			c = s.cell(row = i, column = j)
			if not c.value:
				continue
			modes = str(c.value).replace(')', ')/')
			for mode in modes.split('/'):
				if mode:
					afs[mode] = j - 2
	
		# No af defined for this pin
		if not afs:
			continue

		pincodes = []
		for package in package_pins:
			if pin_name.value in package_pins[package]:
				pincodes.append(package)

		cfg[pin_name.value] = {'pincodes': pincodes, 'afs': afs}

	return cfg
	
def __pin_config_format(pin_config, tab):
		pincodes = '  ' * tab + 'pincodes: ['
		for package in pin_config['pincodes']:
			pincodes += package + ', '
		pincodes = pincodes[:-2] + ']' + '\n'
		pin_yaml = pincodes
		
		afs = '  ' * tab + 'afs:' + '\n'
		for mode in pin_config['afs']:
			afs += '  ' * (tab + 1) + mode + ': ' + str(pin_config['afs'][mode]) + '\n'
		pin_yaml += afs

		return pin_yaml

# Generate pinctrl pins config
def pinctrl_pins_config_format(pins_config):
	pins_yaml = 'pins:' + '\n'
	for pin in pins_config:
		tab = 1
		pins_yaml += '  ' * tab + pin + ':\n'
		pins_yaml += __pin_config_format(pins_config[pin], tab+1)
	return pins_yaml
