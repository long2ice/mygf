import re

from setuptools import setup, find_packages


def version():
    ver_str_line = open('mygf/__init__.py', 'rt').read()
    mob = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", ver_str_line, re.M)
    if not mob:
        raise RuntimeError('Unable to find version string')
    return mob.group(1)


def requirements():
    return open('requirements.txt', 'rt').read().splitlines()


setup(
    name='mygf',
    author='long2ice',
    url='https://github.com/long2ice/mygf',
    author_email='long2ice@gamil.com',
    zip_safe=True,
    include_package_data=True,
    version=version(),
    packages=find_packages(include=['mygf*']),
    description='Girlfriend of MySQL(Clean up cache with MySQL binlog,based on the framework cache ring).',
    long_description_content_type='text/x-rst',
    long_description=open('README.rst', 'r').read(),
    keywords=('mysql cache redis',),
    install_requires=requirements(),
)
