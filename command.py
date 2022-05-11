import subprocess,sys
import re

def wifipassword():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
    wifi_list = list()
    if len(profile_names) != 0:
        for name in profile_names:
            wifi_profile = dict()
            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name],
                                          capture_output=True).stdout.decode()
            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                wifi_profile["ssid"] = name
                profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                                   capture_output=True).stdout.decode()
                password = re.search("Key Content            : (.*)\r", profile_info_pass)
                if password == None:
                    wifi_profile["password"] = None
                else:
                    wifi_profile["password"] = password[1]
                wifi_list.append(wifi_profile)
    return wifi_list            

def disabelwifi():
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "DISABLED"])    

def enablewifi():
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "ENABLED"])    

     