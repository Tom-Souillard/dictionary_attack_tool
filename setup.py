from setuptools import setup, find_packages

setup(
    name='dictionary_attack_tool',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest>=6.0.0',
    ],
    entry_points={
        'console_scripts': [
            'generate_wordlist=scripts.generate_wordlist:generate_wordlist',
            'run_dictionary_attack=scripts.run_dictionary_attack:run_dictionary_attack',
        ],
    },
    author='Tom Souillard',
    author_email='tom.souillard@gmail.com',
    description='A robust Python tool for performing dictionary attacks using Hashcat.',
    license='Apache License 2.0',
    keywords='dictionary attack security pentest hashcat',
    url='https://github.com/Tom-Souillard/dictionary_attack_tool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Security',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
