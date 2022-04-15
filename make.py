import yaml
import os

def make_directory(entries): 
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



  # d = {'a':1,'b':2,'c':[{'d':4,'f':6,'c':[{'g':8},{'h':9},{'i':10}]},{'e':5}]}

  # def func(s):
  #   if isinstance(s,dict):
  #     for i in s:
  #       print(i)
  #       if i == 'c':
  #         func(s['c'])
  #   elif isinstance(s,list):
  #     for i in s:
  #       print(i,type(i))
  #       func(i)
  
  # func(d)



