import yaml
import os
import utils.utils as utils

# TODO add log register
def transform(x):
  '''Apply a function to objrcts in the structure
  Args:
      x (dict): Dictionary with a valid project structure
  '''
  if x['type'] == 'directory':
    print(f"directory: {x['name']}")
    utils.create_directory(x['name'])

    if len(x['contents']) > 0:
      os.chdir(x['name'])
      utils.traverse(x['contents'], transform)
      os.chdir('..')

  if x['type'] == 'file':
    print(f"file: {x['name']}")
    utils.create_file(x['name'])

if __name__ == '__main__':
  with open("structure.yml", "r") as f:
    structure = yaml.load(f, Loader=yaml.FullLoader)
    utils.traverse(structure['structure'],transform)







