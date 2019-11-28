# Installing the jumpssh module
# pip install jumpssh

# Installing openssh server on Ubuntu Linux
# sudo apt - get install openssh - server - y

# Installing OpenSSH Client on Windows 10
# https: // docs.microsoft.com / en - us / windows - server / administration / openssh / openssh_install_firstuse

# Run remote script on the Arista switch via the Ubuntu remote server
# Open cmd as Administrator before performing SSH from Windows!
# ssh mihai @ 10.10.10.100 "python3 /home/mihai/ping_script.py"

# Run local script on the Arista switch via the Ubuntu remote server
# The dash ( - ) is optional and it means the program reads from stdin
# Open cmd as Administrator before performing SSH from Windows!
# more D:\ping_script.py | ssh mihai @ 10.10.10.100 python3 -

# Executing CLI commands and getting the output via the Ubuntu remote server
from jumpssh import SSHSession

gateway_session = SSHSession('10.10.10.100', 'mihai', password='python').open()

remote_session = gateway_session.get_remote_session('10.10.10.3', 'admin', password='python')

print(remote_session.get_cmd_output('show ip int brief'))

gateway_session.close()
