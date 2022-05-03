import tempfile
import os
from src.app.hasher import hash_directory, hash_file

class TestHasher:

  def test_hash_file(self):
    with tempfile.TemporaryDirectory() as tmpdir:
      with open(str(tmpdir)+'test.txt', mode = 'w') as f:
        f.write(
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
          'sed do eiusmod tempor incididunt ut labore et dolore magna '
          'aliqua. Sit amet nulla facilisi morbi tempus iaculis. Risus '
          'viverra adipiscing at in tellus integer feugiat scelerisque. '
          'Eget est lorem ipsum dolor sit amet. Sagittis aliquam malesuada '
          'bibendum arcu vitae elementum curabitur vitae nunc.'
        )
      md5 = hash_file('test.txt', path = tempfile.tempdir, mode = 'MD5')

      assert md5 == '8ed161509301c5c373c7fa12e1b08277'


  def test_hash_directory(self):
      #tmpdir = 'tmp'
      #os.mkdir(tmpdir)
    with tempfile.TemporaryDirectory() as tmpdir:
      with open(os.path.join(tmpdir,'test.txt'), mode = 'w') as f:
        f.write(
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
          'sed do eiusmod tempor incididunt ut labore et dolore magna '
          'aliqua. Sit amet nulla facilisi morbi tempus iaculis. Risus '
          'viverra adipiscing at in tellus integer feugiat scelerisque. '
          'Eget est lorem ipsum dolor sit amet. Sagittis aliquam malesuada '
          'bibendum arcu vitae elementum curabitur vitae nunc.'
        )
      os.mkdir(os.path.join(tmpdir,'dir-a'), mode = 0o777)
      os.chdir(os.path.join(tmpdir,'dir-a'))
      with open('test-a.txt', mode = 'w') as f:
        f.write(
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
          'sed do eiusmod tempor incididunt ut labore et dolore magna '
          'aliqua. Sit amet nulla facilisi morbi tempus iaculis.'
        )
      os.chdir('..')
      md5 = hash_directory(tmpdir, path = os.path.abspath('..'), mode = 'MD5')
      print(md5)
      assert md5 == '71afeb6a9963f25cbdd91cee9392170d'