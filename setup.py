from setuptools import setup, find_packages
from typing import List

HYPEN_DOT_E = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirement = []
    with open(file_path, 'r') as file_obj:
        requirement = file_obj.readlines()
        requirement = [line.replace('\n', '') for line in requirement ]
    
    if HYPEN_DOT_E in requirement:
        requirement.remove(HYPEN_DOT_E)
    return requirement
        

setup(
    
    author='Onkar',
    author_email='onkarrajambatwar@gmail.com',
    name='ML_Project',
    requires=['Pandas', 'seaborn', 'numpy'],
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)