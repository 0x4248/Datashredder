import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Datashredder',
    url='https://github.com/lewisevans2007/Datashredder/',
    author='Lewis Evans',
    author_email='lewisevans2007@gmail.com',
    packages=['datashredder'],
    install_requires=[''],
    version="0.2.21",
    license='GNU',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='A simple data corruption engine written in python'
)
