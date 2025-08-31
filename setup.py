# Setup.py is used for packaging and distributing Python projects. It helps with deploying the project to PyPI or other package repositories.
# It helps specify metadata about the project, its dependencies, and other configurations needed for installation on other devices.
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        # "-e ." automatically triggers the setup.py file to install the package
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name="student_performance_indicator",
    version="0.0.1",
    author="Rishbha Singh",
    author_email="rishbhasingh19@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)