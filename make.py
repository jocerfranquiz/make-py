import yaml
import os

def process(entries): #TODO fix recursion over directories
  for entry in entries:
    if entry["type"] == "directory":
      os.makedirs(entry["name"], exist_ok=True) # Thanks @pLumo
      os.chdir(entry["name"])
      process(entry.get("contents", []))
      os.chdir('..')
    if entry["type"] == "file":
      with open(entry["name"], "w"): pass
   #if entry["type"] == "link":
    #  os.symlink(entry["name"], entry["target"])

if __name__ == '__main__':
  with open("structure.yaml", "r") as f:
    structure = yaml.load(f, Loader=yaml.FullLoader)

    process(structure['structure'][0])


  
