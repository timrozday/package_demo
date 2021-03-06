from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='test',
    url='https://github.com/timrozday/package_demo',
    author='Tim Rozday',
    author_email='timrozday@ebi.ac.uk',
    # Needed to actually package something
    packages=['test_package'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='None',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
