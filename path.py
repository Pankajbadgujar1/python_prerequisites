import os 

# new_dir = "path_domo"
# os.mkdir(new_dir)
# print(f'Directry {new_dir} created successfully...')


# items = os.listdir('.')
# print(items)


# dir_name = "path_domo"
# file_name = "example.txt"
# full_path = os.path.join(dir_name,file_name)
# print(full_path)


# check the file is exist or not
# path='sample.txt'
# if os.path.exists(path):
#     print(f"The path {path} is exists..")
# else:
#     print(f"The path {path} is not exists..")


#Getting the absolute path
relative_path = 'sample.txt'
absulute_path = os.path.abspath(relative_path)
print(absulute_path)