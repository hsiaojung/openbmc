## openbmc/build/workspace/sources/palmetto-config/Palmetto.py
## System states
##   state can change to next state in 2 ways:
##   - a process emits a GotoSystemState signal with state name to goto
##   - objects specified in EXIT_STATE_DEPEND have started
SYSTEM_STATES = [
	'BASE_APPS',
	'BMC_STARTING',
	'BMC_READY',
	'HOST_POWERING_ON',
	'HOST_POWERED_ON',
	'HOST_BOOTING',
	'HOST_BOOTED',
	'HOST_POWERED_OFF',
]

EXIT_STATE_DEPEND = {
	'BASE_APPS' : {
		'/org/openbmc/sensors': 0,
	},
	'BMC_STARTING' : {
		'/org/openbmc/control/chassis0': 0,
		'/org/openbmc/control/power0' : 0,
		'/org/openbmc/control/led/identify' : 0,
		'/org/openbmc/control/host0' : 0,
		'/org/openbmc/control/flash/bios' : 0,
	}
}

ID_LOOKUP = {
	'FRU' : {},
	'FRU_STR' : {},
	'SENSOR' : {},
	'GPIO_PRESENT' : {
#		'SLOT0_PRESENT' : '<inventory_root>/system/chassis/motherboard/pciecard_x16',
#		'SLOT1_PRESENT' : '<inventory_root>/system/chassis/motherboard/pciecard_x8',
	}
}

GPIO_CONFIG = {}
GPIO_CONFIG['FSI_CLK']    =   { 'gpio_pin': 'A4', 'direction': 'out' }
GPIO_CONFIG['FSI_DATA']   =   { 'gpio_pin': 'A5', 'direction': 'out' }
GPIO_CONFIG['FSI_ENABLE'] =   { 'gpio_pin': 'A1', 'direction': 'out' }
GPIO_CONFIG['CRONUS_SEL'] =   { 'gpio_pin': 'A6', 'direction': 'out'  }
GPIO_CONFIG['PGOOD']      =   { 'gpio_pin': 'C7', 'direction': 'in'  }
GPIO_CONFIG['BMC_THROTTLE'] = { 'gpio_pin': 'J3', 'direction': 'out' }
#GPIO_CONFIG['IDBTN']       = { 'gpio_pin': 'Q7', 'direction': 'out' }
GPIO_CONFIG['POWER_BUTTON'] = { 'gpio_pin': 'E0', 'direction': 'both' }
GPIO_CONFIG['RESET_BUTTON'] = { 'gpio_pin': 'E2', 'direction': 'both' }
GPIO_CONFIG['UCD9090_RESET']    = { 'gpio_pin': 'F5', 'direction': 'out' }
GPIO_CONFIG['PCIE_RESET']   = { 'gpio_pin': 'B5', 'direction': 'out' }
GPIO_CONFIG['CPU0_NIC_PERST']    = { 'gpio_pin': 'B6', 'direction': 'out' }
GPIO_CONFIG['BMC_CPU_RESET']      =   { 'gpio_pin': 'C1', 'direction': 'out' }
GPIO_CONFIG['BMC_NVME1_PERST']      =   { 'gpio_pin': 'A7', 'direction': 'out' }
GPIO_CONFIG['BMC_NVME2_PERST']      =   { 'gpio_pin': 'A0', 'direction': 'out' }
GPIO_CONFIG['TPCM_I2C_EN']      =   { 'gpio_pin': 'E4', 'direction': 'out' }
GPIO_CONFIG['CPU0_SAS_PERST']      =   { 'gpio_pin': 'G3', 'direction': 'out' }
GPIO_CONFIG['BMC_BMC_PERST']      =   { 'gpio_pin': 'H2', 'direction': 'out' }
GPIO_CONFIG['BMC_CFAM_RESET']      =   { 'gpio_pin': 'J2', 'direction': 'out' }
GPIO_CONFIG['USB_RESET']    = { 'gpio_pin': 'P7', 'direction': 'out' }
#GPIO_CONFIG['PCIE_RESET']   = { 'gpio_pin': 'B5', 'direction': 'out' }
GPIO_CONFIG['CPLD_RESET']    = { 'gpio_pin': 'C6', 'direction': 'out' }
GPIO_CONFIG['CHECKSTOP']      =   { 'gpio_pin': 'P5', 'direction': 'falling' }
#GPIO_CONFIG['HB']      =   { 'gpio_pin': 'R4', 'direction': 'out' }
GPIO_CONFIG['BEEP']      =   { 'gpio_pin': 'N7', 'direction': 'out'  }
GPIO_CONFIGS = {
    'power_config' : {
        'power_good_in' : 'PGOOD',
        'power_up_outs' : [
			('UCD9090_RESET', True),           
	                ('PCIE_RESET', True),
			('CPU0_NIC_PERST', True), 
		        ('BMC_CPU_RESET', True),
			('BMC_NVME1_PERST', True),
			('BMC_NVME2_PERST', True),
			('TPCM_I2C_EN', True),
			('CPU0_SAS_PERST', True),
			('BMC_BMC_PERST', True),
			('BMC_CFAM_RESET', True),
	                ('USB_RESET', True),
                        ('BEEP', False),
        ],
        'reset_outs' : [
            ('CPLD_RESET', True),
            ('CPLD_RESET', False),
        ],
        'pci_reset_outs': [
            # net name, polarity, reset hold
            #('PCIE_RESET', False, False),
        ],
    },
    'hostctl_config' : {
        'fsi_data' : 'FSI_DATA',
        'fsi_clk' : 'FSI_CLK',
        'fsi_enable' : 'FSI_ENABLE',
        'cronus_sel' : 'CRONUS_SEL',
        'optionals' : [
            ('BMC_THROTTLE', True),
 #           ('IDBTN', False),
        ],
    },
}

# Miscellaneous non-poll sensor with system specific properties.
# The sensor id is the same as those defined in ID_LOOKUP['SENSOR'].
MISC_SENSORS = {
	0x09 : { 'class' : 'BootCountSensor' },
	0x05 : { 'class' : 'BootProgressSensor' },
	0x32 : { 'class' : 'OperatingSystemStatusSensor' },
}

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
