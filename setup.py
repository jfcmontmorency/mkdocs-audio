from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='mkdocs-audio',
    version='0.0.1',
    author='Jean-Francois Cartier',
    author_email='jfcartier@cmontmorency.qc.ca',
    url='https://github.com/jfcmontmorency/mkdocs-audio',
    description='MkDocs plugin to embed audio files',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'mkdocs>=1.4.2', 
        'lxml>=4.7.0'
    ],
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-audio = mkdocs_audio.plugin:Plugin',
        ]
    }
)
