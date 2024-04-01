from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''Read the requirements file and return the list of requirements'''
    requirements = []
    with open(file_path )as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

# Setup - metadata for the project
setup(
    name = 'Student Performance Prediction',
    version = '0.0.1',
    packages = find_packages(),
    author = 'Iqbal',
    author_email = 'iqbalxply@gmail.com',
    description = 'Student Performance Prediction- Machine Learning Project',
    long_description = open('README.md').read(),
    install_requires = get_requirements('requirements.txt')
)