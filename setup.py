from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE = 'requirements.txt'

def get_requirements()->List[str]:  #In function "->return type"
    with open(REQUIREMENT_FILE) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_pckg.replace('\n','') for requirement_pckg in requirement_list]
    if "-e ." in requirement_list:
        requirement_list.remove("-e .")
    return requirement_list

setup(
    name="sensor_KK",
    version="0.0.1",
    author="Kuttralanathan",
    author_email="kuttral99@gmail.com",
    packages=find_packages(), #Run __init__.py from all packages/folders
    install_requires=get_requirements() #Get packages name from requirements.txt
)