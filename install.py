

def main():
  import shutil
  import numpy
  copy_files = ['sharedlibs.py', 'sharedlibs_list.txt']
  numpy_file = numpy.__file__
  site_package_location = numpy_file[:numpy_file.index('numpy')]

  for file in copy_files:
    shutil.copyfile(file, '%s%s' % (site_package_location, file))
  print("Finished.")


if __name__ == '__main__':
  main()
