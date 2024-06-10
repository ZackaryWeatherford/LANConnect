import subprocess


def get_ipaddresses():
    PIPE, STDOUT = subprocess.PIPE, subprocess.STDOUT
    arpA_req = subprocess.Popen(
        ['arp', '-a'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    out, err = arpA_req.communicate()

    out = str(out).replace("\\r\\n", "")
    out = str(out).replace("static", "static\n")
    out = str(out).replace("dynamic", "dynamic\n")
    out = str(out).replace("  ", " ")
    out = str(out).replace("'", "")
    return out

import subprocess



def change_ip_address(interface_name, new_ip, subnet_mask, gateway):
  commands = [
      f"netsh interface ip set address name=\"{interface_name}\" source=static address={new_ip} mask={subnet_mask} gateway={gateway}",
      "netsh interface ip set dnsservers name=\"{interface_name}\" source=static address=8.8.8.8",
  ]
  for command in commands:
    try:
      subprocess.run(command, shell=True, check=True)
      print(f"Successfully changed IP address for {interface_name}")
    except subprocess.CalledProcessError as e:
      print(f"Error changing IP address: {e}")

#Replace Values with your Own
interface_name = "Ethernet"
new_ip = "192.168.1.67"  # Replace with the desired IP within your LAN subnet
subnet_mask = "255.255.255.0"
gateway = "192.168.1.1"  # Replace with your router's IP address





