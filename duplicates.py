# If you want to create a multiple file or duplicates of file. These two line code work for you.
import shutil

# Change the number in bracket. Number of copies you wants.
for i in range (15):

# Change the working directory (XXX) and file_name with the file format (.pdb).
shutil.copy2 ('xxx/file_name.pdb', 'xxx/file_name{}.pdb'.format(i))
print(f"Created duplicate file {i+1}")
