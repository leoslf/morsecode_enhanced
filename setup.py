from setuptools import setup

setup(
    name='morsecode_enhanced',
    version='1.0.3',
    author='Dany Srour',
    author_email='dany.srour@gmail.com',
    description='A package for encoding and decoding Morse code.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/danysrour/morsecode_enhanced',
    packages=['morsecode_enhanced'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    build_requires=[
        'setuptools',
        'wheel',
    ],
    install_requires=[
        'playsound>=1.2.2',
    ],
    python_requires='>=3.6',
    exclude_package_data={'': ['tests/*']},
)
