import ast
import codecs
import os

from pip.req import parse_requirements

from setuptools import find_packages, setup


# CONFIGURATION

package_name = 'elokenz_twote'
long_doc_file = 'README.md'
classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 1.10',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: AGPL License',  # example license
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]


# CONFIGURATION CODE - DO NOT TOUCH

# The session argument for the parse_requirements function is available (but
# optional) in pip 1.5, and mandatory in next versions
try:
    from pip.download import PipSession
except ImportError:
    parse_args = {}
else:
    parse_args = {'session': PipSession()}


def get_requirements(source):
    install_reqs = parse_requirements(source, **parse_args)
    return set([str(ir.req) for ir in install_reqs])


class MetaDataFinder(ast.NodeVisitor):
    def __init__(self):
        self.data = {}

    def visit_Assign(self, node):
        if node.targets[0].id in (
                '__version__',
                '__author__',
                '__contact__',
                '__homepage__',
                '__license__',
        ):
            self.data[node.targets[0].id[2:-2]] = node.value.s


def read(*path_parts):
    filename = os.path.join(os.path.dirname(__file__), *path_parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_info(*path_parts):
    finder = MetaDataFinder()
    node = ast.parse(read(*path_parts).encode('utf-8'))
    finder.visit(node)
    info = finder.data
    info['docstring'] = ast.get_docstring(node)
    return info


package_info = find_info(package_name, '__init__.py')


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name=package_name,
    version=package_info['version'],
    packages=find_packages(),
    include_package_data=True,
    description=package_info['docstring'],
    long_description=read(long_doc_file),
    url=package_info['homepage'],
    author=package_info['author'],
    author_email=package_info['contact'],
    install_requires=get_requirements('requirements.txt'),
    license=package_info['license'],
    classifiers=classifiers,
)
