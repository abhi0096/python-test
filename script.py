import os
import sys
import shutil



# Specify the Jenkins home directory
jenkins_home = '/var/lib/jenkins'

# Get a list of all build folders
build_folders = [f.path for f in os.scandir(f"{jenkins_home}/jobs") if f.is_dir()]

# Loop through each build folder and get its size
for build_folder in build_folders:
    build_size = 0
    for dirpath, dirnames, filenames in os.walk(build_folder):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            build_size += os.path.getsize(fp)
    build_size_in_mb = build_size / (1024*1024)
    print(f"{build_folder} = ({build_size_in_mb:.2f} MB)")
