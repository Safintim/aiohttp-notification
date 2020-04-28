from setuptools import setup

setup(
    name='aiohttp_notification',
    version='0.1',
    author='Timur Safin',
    author_email='timurtlt96@mail.ru',
    packages=['notification'],
    url='https://github.com/Safintim/aiohttp-notification',
    license='MIT',
    description='Aiohttp firebase service',
    install_requires=[
        'aiohttp',
        'aiopg',
        'aiohttp-validate',
        'SQLAlchemy',
        'psycopg2',
        'psycopg2-binary',
        'pyfcm',
        'PyYAML',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Aiohttp',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
        'Natural Language :: Russian',
    ],
)
