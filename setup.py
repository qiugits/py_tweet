from setuptools import setup, find_packages


setup(
    name='twpy',
    version='1.0',
    packages=find_packages(),
    install_requires=['requests-oauthlib'],
    # scripts=['twpy/__main__.py'],
    entry_points={'console_scripts': 'twpy = twpy:main'},
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
