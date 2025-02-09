'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup   ##find_packages -> will see where __init__.py in present and make that root folder as package
from typing import List

def get_requirements()->List[str]:
  '''
  This function will return the List of requirements
  '''
  requirement_lst:List[str] = []
  try:
    with open('requirements.txt','r') as file:
      ##Read line from file
      lines = file.readlines()
      ##Process each line
      for line in lines:
        requirement = line.strip()
        ##Ignore empty line and -e .
        if requirement and requirement!="-e .":
          requirement_lst.append(requirement)
  except FileNotFoundError:
    print("requirements.txt file not found")


  return requirement_lst

setup(
  name="NetworkSecurity",
  version="0.0.1",
  author="AdarshSinghTomar",
  author_email="adarshsinghtomar7909043383@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements()
)
