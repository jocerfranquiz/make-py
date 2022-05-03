# TODO create tests and tests everything

import hashlib
import os

BYTE_BLOCK = 64 * 1024 # 4KB
PROJECT_PATH = os.path.relpath('/home/newpaxonian/wsl_projects/make-py')


def hash_file(fname: str, path: str = PROJECT_PATH, mode: str = 'MD5') -> str:
  """ Calculate sha256 for a file
  Args:
      fname (str): name of the file
      path (str): path to location of file
      mode (str): hash mode 'MD5' or 'SHA256'
  """

  if not os.path.exists(os.path.join(path, fname)):
    raise FileNotFoundError()

  hash_function = None
  # TODO add SHA1 and SHA512
  if mode == 'MD5':
    hash_function = hashlib.md5()
  elif mode == 'SHA256':
    hash_function = hashlib.sha256()
    
  with open(os.path.join(path,fname), 'rb') as file:
    while True:
      file_chunk = file.read(BYTE_BLOCK)
      if not file_chunk:
        break  
      else:
        hash_function.update(file_chunk) 

  return hash_function.hexdigest()


def hash_directory(dname: str, path: str = PROJECT_PATH, mode: str = 'MD5', include_paths: bool = False):
  """ Calculate sha256 for a directory

  Args:
      dname (str): name of the file
      path (str): path to location of file
      mode (str): hash mode 'MD5' or 'SHA256'
  """
  hash_function = None
  # TODO add SHA1 and SHA512
  if mode == 'MD5':
    hash_function = hashlib.md5()
  elif mode == 'SHA256':
    hash_function = hashlib.sha256()

  if not os.path.isdir(os.path.join(path,dname)):
    print(path,dname)
    raise TypeError(f'{dname} is not a directory.')

  hashes = []
  for root, dirs, files in os.walk(dname, topdown = True, onerror = None, followlinks = False):

    dirs.sort()
    files.sort()

    for fname in files:
      hashes.append(hash_file(fname, path = root, mode = mode))

      if include_paths:
        #hasher = hash_function()
        path_list = os.path.relpath(os.path.join(root, fname)).split(os.sep)
        hash_function().update(''.join(path_list).encode('utf-8'))
        hashes.append(hash_function.hexdigest())

  hashes.sort()

  for h in hashes:
    hash_function.update(h.encode('utf-8'))

  return hash_function.hexdigest()



