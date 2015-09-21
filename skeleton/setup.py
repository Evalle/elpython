try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My project',
        'author': 'Evgeny Shmarnev',
        'url': 'https://github.com/Evalle/',
        'download_url': 'https://github.com/Evalle/',
        'author_email': 'shmarnev@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
}

setup(**config)
