#!/bin/env python

import sys
import os
import subprocess

if len(sys.argv) < 3:
	print("You're missing a file path to the zip files")
	print("./bkcrack_auto.py <path_to_bkcrack> <path_to_zips>")
elif len(sys.argv) > 3:
	print("You have too many arguments")
	print("./bkcrack_auto.py <path_to_bkcrack> <path_to_zips>")

bkcrack_path = sys.argv[1]
zip_path = sys.argv[2]
ext = ('.zip', '.ZIP')

for files_name in os.listdir(zip_path):
	if files_name.endswith(ext):
		# Getting output of zip with 'unzip -Z <zipfile>
		unzip_command = 'unzip -Z %s/%s' % (zip_path, files_name)
		lines = subprocess.check_output(unzip_command, shell=True).split('\n')
		jpg_array = []
		png_array = []
		svg_array = []

		for line in lines:
			split_line = line.split(" ")
			exf_name = split_line[-1]
			if 'jpg' in line:
				store_level = split_line[-4]
				if store_level == 'stor':
					print("Found JPG %s" % split_line[-1])
					jpg_array.append(exf_name)
			elif 'png' in line:
				store_level = split_line[-4]
				if store_level == 'stor':
					print("Found exploitable PNG %s in %s" % (exf_name, files_name))
					png_array.append(exf_name)

			if 'svg' in line:
				store_level = split_line[-4]
				if store_level == 'stor':
					print("Found exploitable SVG %s in %s" % (exf_name, files_name))
					svg_array.append(exf_name)

		# In order of speed to crack
		for svg_item in svg_array:
			print("Finding key for svg %s in %s" % (svg_item, files_name))
			exp_command = '%s/bkcrack -C %s/%s -c %s -p %s' % (bkcrack_path, zip_path, files_name, svg_item, 'file_search/svg.txt')
			key_lines = subprocess.check_output(exp_command, shell=True).split('\n')
			key = key_lines[-2]
			if 'could' not in key:
				print("Found key %s, attempting to find the password up to 12 char" % key)
				pwd_command = '%s/bkcrack -k %s -r 12 ?a' % (bkcrack_path, key)
				pwd_lines = subprocess.check_output(pwd_command, shell=True).split('\n')
				pwd = pwd_lines[-2]
				if 'Could' not in pwd:
					print("Password %s" % pwd)
				else:
					print("Could not find password changing the zip password to 'password'")
					new_filename = "%s/%s.%s.zip" % (zip_path, files_name, key.replace(" ", "_"))
					change_command = '%s/bkcrack -C %s -k %s -U %s password' % (bkcrack_path, files_Name, key, new_filename)
					subprocess.check_output(change_command, shell=True).split('\n')					
					
			else:
				print("Couldn't find the key!")

		for jpg_item in jpg_array:
			print("Finding key for jpg %s in %s" % (jpg_item, files_name))
			exp_command = '%s/bkcrack -C %s/%s -c %s -p %s' % (bkcrack_path, zip_path, files_name, jpg_item, 'file_search/jpg.txt')
			key_lines = subprocess.check_output(exp_command, shell=True).split('\n')
			key = key_lines[-2]
			if 'could' not in key:
				print("Found key %s, attempting to find the password up to 12 char" % key)
				pwd_command = '%s/bkcrack -k %s -r 12 ?a' % (bkcrack_path, key)
				pwd_lines = subprocess.check_output(pwd_command, shell=True).split('\n')
				pwd = pwd_lines[-2]
				if 'Could' not in pwd:
					print("Password %s" % pwd)
				else:
					print("Could not find password changing the zip password to 'password'")
					new_filename = "%s/%s.%s.zip" % (zip_path, files_name, key.replace(" ", "_"))
					change_command = '%s/bkcrack -C %s -k %s -U %s password' % (bkcrack_path, files_Name, key, new_filename)
					subprocess.check_output(change_command, shell=True).split('\n')					
					
			else:
				print("Couldn't find the key!")

		for png_item in png_array:
			print("Finding key for png %s in %s" % (png_item, files_name))
			exp_command = '%s/bkcrack -C %s/%s -c %s -p %s' % (bkcrack_path, zip_path, files_name, png_item, 'file_search/png.txt')
			key_lines = subprocess.check_output(exp_command, shell=True).split('\n')
			key = key_lines[-2]
			if 'could' not in key:
				print("Found key %s, attempting to find the password up to 12 char" % key)
				pwd_command = '%s/bkcrack -k %s -r 12 ?a' % (bkcrack_path, key)
				pwd_lines = subprocess.check_output(pwd_command, shell=True).split('\n')
				pwd = pwd_lines[-2]
				if 'Could' not in pwd:
					print("Password %s" % pwd)
				else:
					print("Could not find password changing the zip password to 'password'")
					new_filename = "%s/%s.%s.zip" % (zip_path, files_name, key.replace(" ", "_"))
					change_command = '%s/bkcrack -C %s -k %s -U %s password' % (bkcrack_path, files_Name, key, new_filename)
					subprocess.check_output(change_command, shell=True).split('\n')					
					
			else:
				print("Couldn't find the key!")

	else:
		continue
