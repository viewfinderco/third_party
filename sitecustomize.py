import imp
import os
import sys

from pkgutil import ImpLoader

class MappingImporter(object):
  def __init__(self, mapping):
    self.mapping = mapping

  def find_module(self, fullname, path=None):
    try:
      real_path = self.mapping[fullname]
      return ImpLoader(fullname, None, real_path, ('', '', imp.PKG_DIRECTORY))
    except KeyError:
      return None

# Walk up the path until we find a '.git' subdirectory. Add an importer which
# maps the 'viewfinder' module name to that subdirectory. This allows the
# 'viewfinder' module to be found in a directory that is not named
# 'viewfinder'.
path = os.getcwd()
while path != '/':
  try:
    if os.path.isdir(os.path.join(path, '.hg')):
      sys.meta_path.append(MappingImporter({ 'viewfinder': path }))
      break
  except OSError:
    # path is not a dir or does not exist
    pass
  path = os.path.dirname(path)
