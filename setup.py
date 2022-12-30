from setuptools import setup, find_packages
from glob import glob
from os.path import isfile

files = []
for path in [i for i in glob('tests/**/*', recursive=True) if isfile(i)]:
    files.append((("{}{}".format("share/dockingfactory/", path.rsplit("/", 1)[0]), [path])))
    
setup(name='DockingFactory',
      version='0.0.1',
      install_requires=[],
      packages=['DockingCluster'],
      scripts=['dockingfactory.py'],
      data_files=files
)	
