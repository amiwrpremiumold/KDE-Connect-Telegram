# State
Shutdown = "systemctl poweroff"
Reboot = "systemctl reboot"
Suspend = "systemctl suspend"
Hibernate = "systemctl hibernate"
Lock_screen = "loginctl lock-session"
Unlock_screen = "loginctl unlock-session"
Turn_off_screen = "xset dpms force off"
Turn_on_screen = "xset dpms force on"
Lock_keyboard_and_mouse = "pyxtrlock"
Unlock_keyboard_and_mouse = "pkill pyxtrlock"

# Volume
Volume_down = 'qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "decrease_volume"'
Volume_up = 'qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "increase_volume"'
Mute = 'qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "mute"'
Mute_microphone = 'qdbus org.kde.kglobalaccel /component/kmix invokeShortcut "mic_mute"'

# Brightness
Brightness_Up = 'qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/BrightnessControl ' \
                'org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness $(expr ' \
                '$(qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/' \
                'BrightnessControl org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness) + 100)'
Brightness_Down = 'qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/BrightnessControl ' \
                  'org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness $(expr ' \
                  '$(qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/' \
                  'BrightnessControl org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightness) - 100)'

Brightness_Maximum = 'qdbus org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/BrightnessControl ' \
                     'org.kde.Solid.PowerManagement.Actions.BrightnessControl.setBrightness `qdbus ' \
                     'org.kde.Solid.PowerManagement /org/kde/Solid/PowerManagement/Actions/BrightnessControl ' \
                     'org.kde.Solid.PowerManagement.Actions.BrightnessControl.brightnessMax`'

# screen shot
name = 'file=$(date "+%Y%m%d_%H%M%S").png'
file = f'/tmp/$(hostname)_${name}; spectacle -bo "${name}"'

Screen_shot_fullscreen = 'spectacle -b'
Screen_shot_fullscreen_to_phone = 'spectacle -b'
Screen_shot_active_windows_to_phone = 'spectacle -b -a'


# bluetooth
Connect_to_gt1_right = 'bluetoothctl connect E8:EC:A3:10:D2:7B'
disconnect_from_gt1_right = 'bluetoothctl disconnect E8:EC:A3:10:D2:7B'
pair_gt1_right = 'bluetoothctl pair E8:EC:A3:10:D2:7B'
remove_gt1_right = 'bluetoothctl remove E8:EC:A3:10:D2:7B'

# Utilities
Htop = 'konsole --fullscreen -e htop'

