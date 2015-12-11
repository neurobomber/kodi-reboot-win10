import xbmcaddon
import xbmcgui
import subprocess

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

xbmcgui.Dialog().ok(addonname, "Restarting machine to Windows 10")

subprocess.call(["sudo","grub-reboot","1"])
subprocess.call(["sudo","reboot"])
