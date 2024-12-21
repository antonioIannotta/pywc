from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='pywc',
    version='0.0.10',
    description='A simple CLI program to count the number of lines, words and characters within a file',
    package_dir={"": "wc"},
    packages=find_packages(where="wc"),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/antonioIannotta/pywc',
    author='Antonio Iannotta',
    author_email='antonio.iannotta.ai26@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming language :: Python :: 3.12.3",
        "Operating System :: OS Independent",
    ],
    extras_requires={"dev": "pytest>=7.4.4"},
    python_requires='>=3.12',
)