'''
Name:       utitilies.py
Updated:    18-10-2023

This file will contain various QOL functions for setting related to the application windows.
'''

# Not my function.
# Used to detect whether the user on windows used lightmode or darkmode.
def detect_darkmode_in_windows():
    try:
        import winreg
    except ImportError:
        return False
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    reg_keypath = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize'
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError:
        return False
    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == 'AppsUseLightTheme':
                return value == 0
        except OSError:
            break
    return False

# print(detect_darkmode_in_windows())
