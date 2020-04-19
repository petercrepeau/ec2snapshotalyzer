from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    description="SnapshotAlyzer is a tool to manage AWS EC2 snapshots",
    author="Peter Crepeau",
    author_email="peter.crepeau@gmail.com",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/petercrepeau/ec2snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',


)
