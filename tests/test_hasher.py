import tempfile
import os
from src.app.hasher import hash_directory, hash_file

DUMMY_TEXT = (
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
          'sed do eiusmod tempor incididunt ut labore et dolore magna '
          'aliqua. Sit amet nulla facilisi morbi tempus iaculis. Risus '
          'viverra adipiscing at in tellus integer feugiat scelerisque. '
          'Eget est lorem ipsum dolor sit amet. Sagittis aliquam malesuada '
          'bibendum arcu vitae elementum curabitur vitae nunc.'
        )

def test_hash_directory(tmpdir):
  f0 = tmpdir.mkdir('dir-a').join('test-a.txt')
  f0.write(DUMMY_TEXT[:-100])
  f1 = tmpdir.join('test.txt')
  f1.write(DUMMY_TEXT)
  md5 = hash_directory(tmpdir, mode = 'MD5')
  assert md5 == '7ba134e525cabaafc586129730023b3a'

def test_hash_file(tmpdir):
  f = tmpdir.join('test.txt')
  f.write(DUMMY_TEXT)
  md5 = hash_file(f, mode = 'MD5')
  assert md5 == '959a18aa7fe84551fe5e1d0cf6495cc4'

# TODO add test for SHA256