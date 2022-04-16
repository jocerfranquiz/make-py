import yaml
import os

def make_directory(entries):
  '''
  This function creates the directory structure and files
   specified in structure.yaml
  ''' 
  if isinstance(entries, dict):
    type_file = None
    type_directory = None

    for key in entries:
      if key == 'contents':
        make_directory(entries[key])
        os.chdir('..')
      elif key == 'type' and entries[key] == 'directory':
        type_directory = True
        type_file == False
      elif key == 'type' and entries[key] == 'file':
        type_directory = False
        type_file = True
      elif type_directory == True and key == 'name':
        os.makedirs(entries[key], exist_ok=True)
        os.chdir(entries[key])
        type_directory = False
      elif type_file == True and key == 'name':
        with open(entries['name'], 'w'):
          pass
        type_file = False

  elif isinstance(entries,list) and len(entries)>0:
    for key in entries:
      make_directory(key)

if __name__ == '__main__':
  with open("structure.yaml", "r") as f:
    structure = yaml.load(f, Loader=yaml.FullLoader)
    make_directory(structure['structure'])







