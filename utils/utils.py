# TODO Create a function for traverse the whole directory, with an argument to pass a function
# TODO Create another function to calculate the sha256 of files and directories for testing
# TODO Use the traverse function to calculate all the sha256.
# Do I need to add those sha in another structure or in the YAML file?
# TODO replace in make.py the function for create the ditedtory with the new one here
# TODO create the test function

import os

def create_file(fname, mode = 'w'):
  '''Create new files 
  Args:
      fname (str): Name of the file
      mode (str): Mode to open the file. Default is `w` (write mode)
        More info in [Python's official documentation](https://docs.python.org/3/library/functions.html#open)
  '''
  with open(fname, mode):
    #TODO write data from template in file
    pass

def create_directory(dirname, path, permits):
  '''Create new directories
  Args:
      dirname (str): Name of the directory
      path (str): Path to the directory to be created
      permits (str): Directory permits
  '''

def traverse(obj, transform = None):
  '''Traverse dictionary and apply a funct to keys and values
  Args:
      obj (dict): Dictionary with a valid project structure
      funct (function): function to apply to keys and values in `obj`
  '''
  if isinstance(obj, dict):
    type_file = None
    type_directory = None

    for key in obj:
      if key == 'contents':
        traverse(obj[key])
        os.chdir('..')
      elif key == 'type' and obj[key] == 'directory':
        type_directory = True
        type_file == False
      elif key == 'type' and obj[key] == 'file':
        type_directory = False
        type_file = True
      elif type_directory == True and key == 'name':
        os.makedirs(obj[key], exist_ok=True)
        os.chdir(obj[key])
        type_directory = False
      elif type_file == True and key == 'name':
        with open(obj['name'], 'w'):
          pass
        type_file = False

  elif isinstance(obj,list) and len(obj)>0:
    for key in obj:
      traverse(key)

def transform(x):

  if x['type'] == 'directory':

    print(f"directory: {x['name']}")

    if len(x['contents']) > 0:
      traverse(x['contents'], transform)

  if x['type'] == 'file':

    print(f"file: {x['name']}")


def traverse(x, f):

  if isinstance(x, dict):

    f(x)

  if isinstance(x, list):

    for l in x:
      traverse(l, f)


if __name__ == '__main__':

  x = {
       'type':'directory',
       'name':'dir-a',
       'contents':[
             {'type':'file','name':'f-1'},
             {'type':'file','name':'f-2'},
             {'type':'directory',
              'name':'dir-b',
              'contents':[]
             }
           ]
      }

  traverse(x, transform)
