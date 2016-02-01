import os

from setuptools import find_packages
from setuptools import setup

version = '1.1.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = read('README.rst')

setup(
    name='js.ui_bootstrap',
    version=version,
    description="Fanstatic packaging of Angular UI Bootstrap",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Mikhael Malkov',
    author_email='viruzzz.soft@gmail.com',
    url='https://github.com/Viruzzz-kun/js.ui_bootstrap',
    license='MIT',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.bootstrap',
        'js.angular',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'ui_bootstrap = js.ui_bootstrap:library',
            ],
        },
    )
