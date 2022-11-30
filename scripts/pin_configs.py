
def  generate_pin_configs(gd32_pin_definitions, summary):
    '''
    Generate pin configs.
    Input: dict paired with pincode and pin_definitions.
    Output: signal_configs and pins for pin configs.
    '''
    pins = {}
    signal_configs = {}

    # Generate pins
    for pin, functions in summary.items():
        pins[pin] = {}

        pins_pincodes = []
        for key, value in gd32_pin_definitions.items():
            if pin in value:
                pins_pincodes.append(key)

        pins[pin]["pincodes"] = pins_pincodes
        
        pins_afs = {}
        for i in range(0, len(functions)):
            if functions[i] == '':
                continue

            for f in functions[i].split('/'):
                pins_afs[f] = i

                if f not in signal_configs:
                    signal_configs[f] = {}

        pins[pin]["afs"] = pins_afs

    # Generate signal_configs
    for pincode, pin_definitions in gd32_pin_definitions.items():
        functions = set()
        for pin, alternate in pin_definitions.items():
            for func in alternate.split(','):
                # Extract ADC and DAC from alternate
                if "ADC" in func or "DAC" in func:
                    pins[pin]["afs"][func] = "ANALOG"
                if func not in functions:
                    functions.add(func)

        for func, config in signal_configs.items():
            if func not in functions:
                if "exclude-pincodes" in config:
                    config["exclude-pincodes"].append(pincode)
                else:
                    config["exclude-pincodes"] = [pincode]

    signal_configs = {k: v for k, v in signal_configs.items() if v}

    return signal_configs, pins
