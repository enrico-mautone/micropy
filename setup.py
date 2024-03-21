from setuptools import setup, find_packages

setup(
    name='Micropy',
    version='0.1.0',
    author='Enrico Mautone',
    author_email='enrico.mautone@gmail.com',
    description='A Python framework to speed-up microservices creation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/enrico-mautone/micropy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi',
        'uvicorn'
    ],
    entry_points={
        'console_scripts': [
            'micropy=micropy_launcher.launcher:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
