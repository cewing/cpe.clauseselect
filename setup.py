from setuptools import setup, find_packages

version = '1.0-dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='cpe.clauseselect',
      version=version,
      description="Interface and form elements for sentence-based filtering in Django",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
        "Framework :: Django",
        ],
      keywords='django, jquery',
      author='Cris Ewing',
      author_email='cris@crisewing.com',
      url='https://github.com/cewing/cpe.clauseselect',
      license='gpl',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['cpe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'django',
      ],
      )
