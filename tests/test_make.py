import src.app.make as make  


def test_transform():
  x = {
    'type': 'directory',
    'name': 'root-dir',
    'contents': [
      {
       'type': 'directory',
       'name': 'empty-dir',
       'contents': [] 
      },
      {
        'type': 'directory',
        'name': 'sub-dir',
        'contents': [
          {
            'type': 'file',
            'name': 'file-1'
          },
          {
            'type': 'file',
            'name': 'file-2'
          }
        ],
      },
      {
        'type': 'file',
        'name': 'root-file'
      }
    ]
  }

  make.transform(x, path = './tmp')

 