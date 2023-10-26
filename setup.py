from setuptools import setup, find_packages

setup(
    name='dicepy',
    version='0.1',
    author='James J. Evans',
    author_email='joesaysahoy@gmail.com',
    description='A dice rolling library for Python.',
    url='https://github.com/primal-coder/dicepy',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    keywords='dice rolling die d20 dnd d&d rpg role playing game',
    python_requires='>=3.6',
    install_requires=['pyglet']
)