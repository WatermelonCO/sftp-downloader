from setuptools import find_packages, setup

setup(
    name='sftp-downloader',
    version='0.1.0',
    description='A command-line tool to download files from an SFTP server',
    author='Luke Pearson',
    author_email='luke@watermelonco.es',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['sftp_downloader=sftp_downloader.main:main']
    },
    install_requires=['pysftp', 'click', 'pyyaml'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
