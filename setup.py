from setuptools import setup

setup(name='izzati',
      version='1.1.0',
      description='A simple, multi-language frontend to backend communication library',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3 :: Only'
      ],
      url='http://github.com/kusti8/izzati',
      author='Gustav Hansen',
      author_email='kusti8@gmail.com',
      license='GPL3',
      packages=['izzati'],
      install_requires=[
          'flask',
          'requests',
      ],
      keywords = 'izzati backend frontend communication simple',
      include_package_data=True,
      zip_safe=False)
