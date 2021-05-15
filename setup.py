from setuptools import setup, find_packages

setup(
    name='adbsploit',
    version='0.1',
    author='krish pranav',
    author_email='krisna.pranav@gmail.com',
    description="A python based tool for exploiting and managing android devices via ADB",
    url='https://github.com/krishpranav/adbsploit',
    packages=find_packages(),
    py_modules=['adbsploit'],
    install_requires=[
        'setuptools~=49.2.0',
        'colorama',
        'adbutils',
        'pyfiglet',
        'rich'
    ],
    entry_points={
        'console_scripts': ['adbsploit=adbsploit.adbsploit:main'],
    },
)