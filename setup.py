from setuptools import setup
import pypandoc

try:
    long_description = pypandoc.convert_file('README.md', 'rst')
    long_description = long_description.replace('\r', '')

except OSError:
    import io
    
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup(
    name='letters',
    version='1.9',
    license='GPLv3+',
    authors=['zelow'],
    url='https://github.com/zeloww/letters',
    install_requires=['numpy', 'pillow'],
    description='A simple method to customize your programs to infinity!',
    long_description=long_description,
    keywords=['python', 'py', 'letter', 'letters', 'font', 'ascii', 'color', 'colors', 'gradient', 'gradients', 'fade' 'text'],
    packages=['letters'],
)
