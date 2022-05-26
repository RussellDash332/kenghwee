from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()
with open('LOG.md') as history_file:
    LOG = history_file.read()

setup_args = dict(
    name='kenghwee',
    version='1.0',
    description='A package where a meme becomes reality.',
    long_description_content_type="text/markdown",
    long_description=f'{README}\n\n{LOG}',
    license='MIT',
    packages=find_packages(),
    author='Russell Saerang',
    author_email='russellsaerang@gmail.com',
    keywords=['Kenghwee', 'Keng Hwee'],
    install_requires = [
        'seaborn',
        'numpy',
        'matplotlib',
        'scipy',
        'pillow',
        'pyglet',
        'cocos2d'
    ],
    url='https://github.com/RussellDash332/kenghwee',
    download_url='https://pypi.org/project/kenghwee/'
)

if __name__ == '__main__':
    setup(**setup_args, include_package_data=True)