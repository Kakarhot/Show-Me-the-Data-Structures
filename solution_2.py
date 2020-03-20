import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    paths = []
    
    def find_files_func(suffix, path):
        for filename in os.listdir(path):
            filename_full = os.path.join(path, filename)
            if os.path.isfile(filename_full) and filename.endswith(suffix):
                paths.append(filename_full)
            if os.path.isdir(filename_full):
                find_files_func(suffix, filename_full)
    
    find_files_func(suffix, path)
    
    return paths

print(find_files('.c', '.'))
#expected output: ['./testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c']

print('----------------------------------------')

print(find_files('', '.'))
#expected output: all files in the path
print('----------------------------------------')

print(find_files('.h', '.'))
#expected output: ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']