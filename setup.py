from setuptools import setup

setup(
    name='not2much',
    version='0.1.0',
    py_modules=['not2much'],
    package_dir={'': 'src'},
    author='Tim Menzies',
    description='Active learning for instance selection; then inference on minimal data',
    install_requires=[],  # Add any dependencies here
)

