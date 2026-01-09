# import os
# import shutil

# src_path = os.path.join(os.path.dirname(__file__), 'example.bin')
# dst_path = os.path.join(os.path.dirname(__file__), 'destination.bin')

# if not os.path.exists(src_path):
#     raise FileNotFoundError(f"Source file not found: {src_path}")

# # Small, clear copy using shutil (handles large files efficiently)
# shutil.copyfile(src_path, dst_path)


import os
import shutil

src = os.path.join(os.path.dirname(__file__), "example.bin")
dst = os.path.join(os.path.dirname(__file__), "destination.bin")

shutil.copyfile(src, dst)

with open(dst, 'r') as file:
    for line in file:
        print(line)
