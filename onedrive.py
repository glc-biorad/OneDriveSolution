import subprocess
import os

import utility

class OneDrive():
	def __init__(self, path=None):
		if path != None:
			self.path = utility.create_raw_string(path)
		else:
			self.path = None

	# Free up space
	def free_up_space(self, path=None, fname=None, only_ext=None):
		path = self.path if path == None else utility.create_raw_string(path)
		try:
			fpath = None if fname == None else os.path.join(path, fname)
			fpaths = [fpath] if fname != None else [os.path.join(path, _fname) for _fname in os.listdir(path)]
		except FileNotFoundError:
			sys.exit(f"Error (OneDrive.free_up_space): no such file or directory.")
		for _fpath in fpaths:
			if only_ext != None and _fpath[-len(only_ext):] != only_ext:
				continue
			print(_fpath)
			#subprocess.run('attrib +U -P "' + _fpath + '"')
	
	# To disk
	def to_disk(self, path=None, fname=None, only_ext=None):
		path = self.path if path == None else utility.create_raw_string(path)
		try:
			fpath = None if fname == None else os.path.join(path, fname)
			fpaths = [fpath] if fname != None else [os.path.join(path, _fname) for _fname in os.listdir(path)]
		except FileNotFoundError:
			sys.exit(f"Error (OneDrive.to_disk): no such file or directory.")
		for _fpath in fpaths:
			if only_ext != None and _fpath[-len(only_ext):] != only_ext:
				continue
			print(_fpath)
			with open(_fpath, 'r') as f:
				continue
		

	# Change path.
	def change_path(self, path):
		self.path = utility.create_raw_string(path)
