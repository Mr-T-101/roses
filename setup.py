from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='Roses',
    version='1.0.0',
    description='Roses are Red, Violets are Blue, this is a random poem generator just for you!',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Tom Eccleston',
    author_email='teccleston77@gmail,com',
    keywords=['python', 'roses', 'poem'],
    url='https://github.com/goodcodebadcode/mymodule',
    download_url='https://pypi.org/project/mymodule/',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
    