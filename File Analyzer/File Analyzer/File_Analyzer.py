import glob

# Get all .txt files in the directory

files = glob.glob("server_dump/*.txt") 

print(files)