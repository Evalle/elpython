try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'ex47',
        'author': 'Evgeny Shmarnev',
        'url': 'https://github.com/Evalle/elpython/',
        'download_url': 'https://github.com/Evalle/elpython/ex47/',
        'author_email': 'shmarnev@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'scripts': [],
        'name': 'ex47'
}

setup(**config)
