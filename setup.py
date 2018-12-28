from setuptools import setup
import sys

if sys.version_info.major == 2:
    raise SystemError("Only Python 3 supported. (Python Version: {}".format('.'.join(sys.version_info)))

setup(
    name='XCaliburMethodReader',
    py_modules=['XCaliburMethodReader'],
    version='0.1.4',
    url='https://github.com/nickdelgrosso/XCaliburMethodReader',
    license='GNU',
    author='Nicholas A. Del Grosso',
    author_email='delgrosso.nick@gmail.com',
    description='A command-line program for mass spectrometry researchers that extracts and converts data from Thermo XCalibur Method (.meth) files.',
    entry_points="""
        [console_scripts]
        XCaliburMethodReader=XCaliburMethodReader:main
    """,
    install_requires=['olefile', 'xmltodict'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
