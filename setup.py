from distutils.core import setup


setup(
    name='twpy',
    version='1.0',
    install_requires=[],
    entry_points={
        'console_scripts': 'twpy = twpy.__main__:main'
    },
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
    ],
)
