import pytest
from src.app.utils import traverse

def test_create_file():
  assert False

def test_create_directory():
  assert False

def test_traverse():

  def f(x: dict):
    if (isinstance(x, dict) or isinstance(x,list)) and len(x):
      traverse(x,f)
      assert True
    else:
      assert False

  with pytest.raises(Exception):
    traverse(1,f)
    traverse([],f)
    traverse({2},f)
    traverse({'a':1,'b':2,'c':{}},f)
    traverse({'a':1,'b':2,'c':[10,20,30]},f)
    traverse({'a':1,'b':2,'c':[{'d':3},{'e':4}]},f)
