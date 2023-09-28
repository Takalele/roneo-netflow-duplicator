from setuptools import setup, find_packages
setup(
    name='roneo',
    version='0.1.0',
    install_requires=[
        'scapy',
        'pyyaml'
    ],
    packages=find_packages(include=['roneo']),
    include_package_data=True,
        entry_points={
        'console_scripts': ['roneo=roneo.main:main']
    }
)