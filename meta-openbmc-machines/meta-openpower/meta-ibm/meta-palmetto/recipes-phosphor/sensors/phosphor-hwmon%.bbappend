FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

NAMES = " \
        pwm-tacho-controller@1e786000\
        i2c@1e78a000/i2c-bus@40/nct7717@48\
        i2c@1e78a000/i2c-bus@c0/nct7717@48\
        i2c@1e78a000/i2c-bus@100/occ-hwmon@50\
        i2c@1e78a000/i2c-bus@1c0/occ-hwmon@51\
        i2c@1e78a000/i2c-bus@100/nct7717@48\
        i2c@1e78a000/i2c-bus@140/nct7717@48\
        i2c@1e78a000/i2c-bus@300/nct7717@48\
        i2c@1e78a000/i2c-bus@3c0/nct7717@48\
        i2c@1e78a000/i2c-bus@80/ir35221@70\
        i2c@1e78a000/i2c-bus@80/ir35221@76\
        i2c@1e78a000/i2c-bus@80/ir35221@78\
        i2c@1e78a000/i2c-bus@300/ir35221@73\
        i2c@1e78a000/i2c-bus@300/ir35221@76\
        i2c@1e78a000/i2c-bus@300/ir35221@77\
        i2c@1e78a000/i2c-bus@300/power-supply@59\
        i2c@1e78a000/i2c-bus@300/power-supply@58\
        "
ITEMSFMT = "ahb/apb/{0}.conf"

ITEMS = "${@compose_list(d, 'ITEMSFMT', 'NAMES')}"

ENVS = "obmc/hwmon/{0}"
SYSTEMD_ENVIRONMENT_FILE_${PN} += "${@compose_list(d, 'ENVS', 'ITEMS')}"


SYSTEMD_ENVIRONMENT_FILE_pwmtach-msl += "obmc/hwmon/ahb/apb/pwm-tacho-controller@1e786000.conf"
