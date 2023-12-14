import subprocess
import paramiko
import time
import re
import ping3
import json
import sys
from paramiko import SSHClient
from scp import SCPClient

def is_pingable(ip):
    if ping3.ping(ip) is not None:
        print(f"Ping {ip} successful")
        return True
    else:
        print(f"Ping {ip} failed")
        return False

class SSHClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp = None  

    def connect(self):
        try:
            self.client.connect(self.host, username=self.username, password=self.password)
            print(f"SSH connection to {self.host} successful")
            self.sftp = self.client.open_sftp()
            return True 
        except paramiko.AuthenticationException:
            print(f"Failed to authenticate to {self.host}")
        except paramiko.SSHException as e:
            print(f"SSH connection to {self.host} failed: {str(e)}")
        return False 

    def download_file(self, remote_path, local_path):
        try:
            with SCPClient(self.client.get_transport(), progress=self.progress) as scp:
                scp.get(remote_path, local_path)
            print(f"Downloaded file from {remote_path} to {local_path}")
        except Exception as e:
            print(f"Error downloading file: {str(e)}")
            
    def upload_file(self, local_path, remote_path):
        try:
            with SCPClient(self.client.get_transport(), progress=self.progress) as scp:
                scp.put(local_path, remote_path)
            print(f"Uploaded file from {local_path} to {remote_path}")
        except Exception as e:
            print(f"Error uploading file: {str(e)}")
            
    def progress(self, filename, size, sent):
        sys.stdout.write(f"\rTransferring {filename}: {sent}/{size} bytes ({int(sent / size * 100)}%)\n")
        sys.stdout.flush()

    def send_command(self, command):
        output = ""
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode()
            # print(f"Command Output:\n{output}")
            error_output = stderr.read().decode()
            if error_output:
                print(f"Command Error Output:\n{error_output}")
        except paramiko.SSHException as ssh_exception:
            print(f"SSH Exception: {str(ssh_exception)}")
        except Exception as e:
            print(f"An error occurred while executing command: {str(e)}")
        return output

    def disconnect(self):
        if self.sftp:
            self.sftp.close()
        self.client.close()
        print(f"SSH connection to {self.host} closed")

    def getMac(self):
        command = [
            ". /lib/functions.sh",
            ". /lib/functions/system.sh",
            "mac=`mtd_get_mac_binary factory 4116 |tr -d ':'`",
            "echo $mac"
        ]
        # command = [
        #     ". /lib/functions.sh",
        #     ". /lib/functions/system.sh",
        #     "mac=`mtd_get_mac_binary '0:ART' 4116 |tr -d ':'`",
        #     "echo $mac"
        # ]
        result = self.send_command(" && ".join(command)).strip()
        if result is not None:
            print(f"Device Mac Address:{result}")

    def getModel(self):
        result = self.send_command("cat /tmp/sysinfo/model").strip()  
        print(f"Device Model:{result}")
    
    def getFirmwareVersion(self):
        result = self.send_command('cat /etc/openwrt_release | grep DISTRIB_BULDTIME | awk -F"\'" \'{print $2}\'').strip()
        print(f"Device Firmware Version: {result}")
    
    def loopBackUart(self, uartTool, tty):
        msg = "loopBackUart test:iyunlink2014"
        # command = f"{uartTool} '{msg}' -b {tty}"
        command = f"{uartTool} '{msg}'"
        result = self.send_command(command)
        if result != msg:
            print(f"{tty} send msg: '{msg}' receiver: '{result}',loopBack test fail")
        else:
            print(f"{tty} loopBack test success")   
        
    def getWifiAP(self):
        # result = self.send_command("iwinfo | awk '/ESSID/ && $3 != \"unknown\" {print \"SSID: \" $3} /Access Point/ && $3 != \"00:00:00:00:00:00\" {print \"MAC Address: \" $3}'|tr -d '\n'")
        result = self.send_command("uci show wireless | awk -F'.' '/mode='"'"\'ap\'"'"'/ && !seen[$2]++ {print $2;}' | while read -r config_name; do uci get wireless.\"$config_name\".ssid; done").strip()
        print(result)
        return
        
    def getModemInfo(self,uartTool):

        return 
    
    def initModem(self, uartTool, tty, options):
        
        return
    
    def setMac(self, mac):
        mac = mac.replace(":", "").replace("-", "")
        mac_pattern = re.compile(r'^([0-9A-Fa-f]{12})$')
        is_valid_mac = bool(mac_pattern.match(mac))
        if is_valid_mac:
            print(f"{mac} is a valid MAC address.")
 
            command = [
            ". /lib/functions.sh",
            "mtd_factory=/dev/mtd$(find_mtd_index Factory)",
            f"echo -ne '\\x{mac[0:2]}\\x{mac[2:4]}\\x{mac[4:6]}\\x{mac[6:8]}\\x{mac[8:10]}\\x{mac[10:12]}' > /tmp/mac",
            "dd if=$mtd_factory of=/tmp/factory.bin 2>/dev/null",
            "dd if=/tmp/mac of=/tmp/factory.bin bs=1 seek=4 count=6  conv=notrunc 2>/dev/null",
            "dd if=/tmp/mac of=/tmp/factory.bin bs=1 seek=40 count=6  conv=notrunc 2>/dev/null",
            "dd if=/tmp/mac of=/tmp/factory.bin bs=1 seek=46 count=6  conv=notrunc 2>/dev/null",
            "mtd erase $mtd_factory  2>/dev/null",
            "dd if=/tmp/factory.bin of=$mtd_factory 2>/dev/null",
            ]
            result = self.send_command(" && ".join(command))
            self.getMac()
        else:
            print(f"{mac} is not a valid MAC address.")

if __name__ == "__main__":
    with open("config.json", "r") as file:
        config_data = json.load(file)

    target_ip = config_data["target_ip"]
    ssh_username = config_data["ssh_username"]
    ssh_password = config_data["ssh_password"]
    local_file_path = "local_file.txt"
    remote_file_path = "/tmp/file.txt"

    ssh = SSHClient(target_ip, ssh_username, ssh_password)
    while True:
        if is_pingable(target_ip):
            pause = 1
            ssh.connect()
            ssh.upload_file(local_file_path, remote_file_path)
            ssh.getModel()
            ssh.getMac()
            ssh.getFirmwareVersion()
            # ssh.setMac("18c3f4a200e6")
            # ssh.getWifiAP()
            ssh.loopBackUart('at_tool', '/dev/ttyUSB2')
            # for command in config_data["commands_to_run"]:
            #     result = ssh.send_command(command)
            #     print(f"Command Output for '{command}': {result}")
            ssh.disconnect()
            # break
            while(1):
                time.sleep(1)
        else:
            print(f"Waiting for {target_ip} to respond...")
            time.sleep(1)