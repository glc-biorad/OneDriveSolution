from onedrive import OneDrive

if __name__ == '__main__':
	path = "/Users/glopezca/Documents/Bio-Rad/Programs/OneDriveSolution"
	onedrive = OneDrive(path)
	onedrive.free_up_space(only_ext='png')
	onedrive.to_disk(only_ext='png.icloud')
