# Checking if a file is empty

# import os
# os.stat(path_to_file).st_size == 0

# or

# import os
# os.path.getsize(path_to_file) > 0

# However, both will throw an exception if the file does not exist. To avoid having to catch such an error, do this:

# import os
# def is_empty_file(fpath):
#     return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

# which will return a bool value.
