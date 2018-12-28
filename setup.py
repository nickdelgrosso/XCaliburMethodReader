from setuptools import setup

setup(
    name='XCaliburMethodReader',
    py_modules=['XCaliburMethodReader'],
    version='0.1',
    url='https://github.com/nickdelgrosso/XCaliburMethodReader',
    license='GNU',
    author='Nicholas A. Del Grosso',
    author_email='delgrosso.nick@gmail.com',
    description='A command-line program for mass spectrometry researchers that extracts and converts data from Thermo XCalibur Method (.meth) files.',
    entry_points="""
        [console_scripts]
        XCaliburMethodReader=XCaliburMethodReader:main
    """
)
