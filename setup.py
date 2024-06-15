from setuptools import setup, find_packages

setup(
    name='mkdocs-audio',
    version='0.1',
    description='MkDocs plugin to embed audio files',
    long_description='A plugin for MkDocs to embed audio files using a custom syntax.',
    long_description_content_type='text/markdown',
    author='Jean-Francois Cartier',
    author_email='jfcartier@cmontmorency.qc.ca',
    url='https://github.com/yourusername/mkdocs-audio',
    packages=find_packages(),
    install_requires=['mkdocs>=1.0', 'markdown'],
    entry_points={
        'mkdocs.plugins': [
            'audio = mkdocs_audio.plugin:AudioPlugin',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
