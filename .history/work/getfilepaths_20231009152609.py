import os

path = 'D:/DEV/MISC/b9d/work'
path = '\\NOS\Data\Bca_SafeCert21_QualityGrp\06_Compliance Oversight\04_Data Strategy\03_ODA Independence\'
directory = os.listdir(path)
print(directory)
output_file = path+'output.txt'
print(output_file)
# Function to recursively list files and folders and write their paths to a text file
def list_files_and_folders(directory, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                print(file_path)
                file.write(file_path + '\n')
            for folder in dirs:
                folder_path = os.path.join(root, folder)
                print(folder_path)
                file.write(folder_path + '\n')

# Replace 'your_directory_path' with the directory you want to start from
directory_to_search = '\\NOS\Data\Bca_SafeCert21_QualityGrp\06_Compliance Oversight\04_Data Strategy\03_ODA Independence\'

# Replace 'output.txt' with the desired output file name
output_file_name = 'Bca_SafeCert21_QualityGrp__06_Compliance Oversight__04_Data Strategy__03_ODA Independence.txt'

list_files_and_folders(directory_to_search, output_file_name)
print(f'Paths have been written to {output_file_name}')

# Write main
def main():
    list_files_and_folders(directory_to_search, output_file_name)

# Call main
main()

