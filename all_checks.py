#i/usr/bin/env python3
import os
import sys
import socket


def check_reboot():
	"""Returns True if the computer has a pending reboot."""
	return os.path.exists("/run/reboot-required")

def check_root_full():
	"""Returns True if the root partition is full, False otherwise."""
	return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
	if check_reboot():

		print("Pending Reboot!")
		sys.exit(1)
	if check_root_full():
		print("Root partition full.")
		sys.exit(1)
	
	print("Everything ok.")
	sys.exit(0)

main()
