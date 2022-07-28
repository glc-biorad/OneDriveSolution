from onedrive import OneDrive
import utility

if __name__ == '__main__':
	#path = "C:\Users\u112958\OneDrive - Bio-Rad Laboratories Inc\Documents\OneDriveSolution" # Need to get it to work with a string like this.
	path = r"C:\Users\u112958\OneDrive - Bio-Rad Laboratories Inc\Documents\OneDriveSolution"
	onedrive = OneDrive(path)
	#onedrive.free_up_space(only_ext='tif')
	onedrive.to_disk(only_ext='tif')