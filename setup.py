import io

from setuptools import setup, find_packages

with io.open('requirements.txt') as f:
    install_requires = [
        l.strip() for l in f.readlines()
        if l and not l.startswith('#') and not l.startswith('-')
    ]

setup(
    name="example",
    version="0.1.0",
    packages=find_packages(),
    install_requires=install_requires,
    author="Elmer Yu",
    author_email="ak64th@gmail.com",
    description="Tornado multiple applications boilerplate",
    url="github.com/ak64th/tornado_multiple_applications_boilerplate/",
    include_package_data=True
)
