from setuptools import find_packages,setup
from typing import List

HYPHEN_N_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of reuirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n") for req in requirements]
        
        if HYPHEN_N_DOT in requirements:
            requirements.remove(HYPHEN_N_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ranjith',
    author_email='ranjithkr118@gmail.com',
    packages=find_packages(),
    requires=['pandas','numpy','seaborn']
)