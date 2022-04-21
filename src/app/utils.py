
import os

# TODO write data from template in file
# TODO add try/except
def create_file(fname, mode = 'w'):
  '''Create new files 
  Args:
      fname (str): Name of the file
      mode (str): Mode to open the file. Default is `w` (write mode)
        More info in [Python's official documentation](https://docs.python.org/3/library/functions.html#open)
  '''
  with open(fname, mode):
    pass

# TODO add try/except
def create_directory(dirname, path = '.', permits = '777'):
  '''Create new directories
  Args:
      dirname (str): Name of the directory
      path (str): Path to the directory to be created
      permits (str): Directory permits
  '''
  os.makedirs(dirname, exist_ok=True)


# TODO add validations to the structure with try/except and logs
def traverse(x, f):
  '''Traverse dictionary and apply a function to keys and values
  Args:
      x (dict): Dictionary with a valid project structure
      f (function): function to apply to keys and values in `obj`
  '''
  if isinstance(x, dict):
    f(x)
  if isinstance(x, list):
    for l in x:
      traverse(l, f)


# TODO transfer this code to tests
# if __name__ == '__main__':

#   x = {
#        'type':'directory',
#        'name':'dir-a',
#        'contents':[
#              {'type':'file','name':'f-1.txt'},
#              {'type':'file','name':'f-2.txt'},
#              {'type':'directory',
#               'name':'dir-b',
#               'contents':[]
#              },
#              {'type':'directory',
#               'name':'dir-c',
#               'contents':[
#                 {'type':'file','name':'f-3.txt'},
#               ]
#              },
#            ]
#       }

#   traverse(x, transform)

# TODO Create another function to calculate the sha256 of files and directories for testing
# TODO Use the traverse function to calculate all the sha256.
# Do I need to add those sha in another structure or in the YAML file?