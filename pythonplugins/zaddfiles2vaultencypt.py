#!/usr/bin/python
import sys, os

VAULTCMD="/usr/bin/ansible-vault"
os.putenv("ANSIBLE_VAULT_PASSWORD_FILE", "/etc/ansible/autoconfig-jumbo/.vault_pass")

os.system("clear")

if len(sys.argv) == 2:
  FILEPATH=sys.argv[1]
  if os.path.isdir(FILEPATH):
      all_files = sorted([os.path.join(FILEPATH, file) for file in os.listdir(FILEPATH)], key=os.path.getctime) 
      for filename in all_files:
        os.system("%s encrypt %s" % (VAULTCMD, filename))

      print "##################################################################################################"
      print "Ansible Vault Encrypted all files under the directory: %s"   %  (FILEPATH)
      print "##################################################################################################"
  elif os.path.isfile(FILEPATH):  
      filename=FILEPATH
      os.system("%s encrypt %s" % (VAULTCMD, filename))
      print "##################################################################################################"
      print "Ansible Vault Encrypted file: %s"   % (filename)
      print "##################################################################################################"
  else:  
      print("Please enter valid file or directory path")
else:
  print("Please enter valid input (First argument: file or directory path)")
