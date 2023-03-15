from setuptools import find_packages, setup

setup(name='sftp_downloader',
      version='0.1',
      packages=find_packages(),
      install_requires=['argparse', 'csv', 'pysftp'],
      entry_points={
          'console_scripts': ['sftp_downloader=sftp_downloader.main:main']
      })
