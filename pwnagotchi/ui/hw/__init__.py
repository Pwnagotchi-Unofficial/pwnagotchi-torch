from pwnagotchi.ui.hw.inky import Inky
from pwnagotchi.ui.hw.papirus import Papirus
from pwnagotchi.ui.hw.oledhat import OledHat
from pwnagotchi.ui.hw.lcdhat import LcdHat
from pwnagotchi.ui.hw.dfrobot1 import DFRobotV1
from pwnagotchi.ui.hw.dfrobot2 import DFRobotV2
from pwnagotchi.ui.hw.waveshare213inV1 import WaveshareV1
from pwnagotchi.ui.hw.waveshare213inV2 import WaveshareV2
from pwnagotchi.ui.hw.waveshare213inV3 import WaveshareV3
from pwnagotchi.ui.hw.waveshare213inV4 import WaveshareV4
from pwnagotchi.ui.hw.waveshare27inV1 import Waveshare27inch
from pwnagotchi.ui.hw.waveshare27inV2 import Waveshare27inchV2
from pwnagotchi.ui.hw.waveshare29inV1 import Waveshare29inch
from pwnagotchi.ui.hw.waveshare29inV2 import Waveshare29inchV2
from pwnagotchi.ui.hw.waveshare144inlcd import Waveshare144lcd
from pwnagotchi.ui.hw.waveshare154inb import Waveshare154inchb
from pwnagotchi.ui.hw.waveshare213inbc import Waveshare213bc
from pwnagotchi.ui.hw.waveshare213ind import Waveshare213d
from pwnagotchi.ui.hw.waveshare213inb_v4 import Waveshare213bV4
from pwnagotchi.ui.hw.waveshare35inlcd import Waveshare35lcd
from pwnagotchi.ui.hw.spotpear24in import Spotpear24inch
from pwnagotchi.ui.hw.displayhatmini import DisplayHatMini


def display_for(config):
    # config has been normalized already in utils.load_config
    if config['ui']['display']['type'] == 'inky':
        return Inky(config)

    elif config['ui']['display']['type'] == 'papirus':
        return Papirus(config)

    if config['ui']['display']['type'] == 'oledhat':
        return OledHat(config)

    if config['ui']['display']['type'] == 'lcdhat':
        return LcdHat(config)

    if config['ui']['display']['type'] == 'dfrobot_1':
        return DFRobotV1(config)

    if config['ui']['display']['type'] == 'dfrobot_2':
        return DFRobotV2(config)

    elif config['ui']['display']['type'] == 'waveshare_1':
        return WaveshareV1(config)

    elif config['ui']['display']['type'] == 'waveshare_2':
        return WaveshareV2(config)

    elif config['ui']['display']['type'] == 'waveshare_3':
        return WaveshareV3(config)

    elif config['ui']['display']['type'] == 'waveshare_4':
        return WaveshareV4(config)

    elif config['ui']['display']['type'] == 'waveshare27inch':
        return Waveshare27inch(config)

    elif config['ui']['display']['type'] == 'waveshare27inchv2':
        return Waveshare27inchV2(config)

    elif config['ui']['display']['type'] == 'waveshare29inch':
        return Waveshare29inch(config)

    elif config['ui']['display']['type'] == 'waveshare29inchv2':
        return Waveshare29inchV2(config)

    elif config['ui']['display']['type'] == 'waveshare144lcd':
        return Waveshare144lcd(config)

    elif config['ui']['display']['type'] == 'waveshare154inchb':
        return Waveshare154inchb(config)

    elif config['ui']['display']['type'] == 'waveshare213bc':
        return Waveshare213bc(config)

    elif config['ui']['display']['type'] == 'waveshare213d':
        return Waveshare213d(config)

    elif config['ui']['display']['type'] == 'waveshare213inb_v4':
        return Waveshare213bV4(config)

    elif config['ui']['display']['type'] == 'waveshare35lcd':
        return Waveshare35lcd(config)

    elif config['ui']['display']['type'] == 'spotpear24inch':
        return Spotpear24inch(config)

    elif config['ui']['display']['type'] == 'displayhatmini':
        return DisplayHatMini(config)
