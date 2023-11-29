from setuptools import setup, find_packages

setup(
    name='mltoolbox',
    version='0.1.1',
    author='Techno Absurdist',
    author_email='andere.emi@gmail.com',
    description='A python package for out-of-the-box ML solutions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/technoabsurdist/ml-api',
    packages=find_packages(),
    install_requires=[
        'openai',             # For chat functionalities with GPT models
        'sieve',              # If used for various ML functionalities
        'langchain',          # For language processing utilities
        'python-dotenv',      # For loading environment variables
        'Flask',              # If you're using Flask for any web functionalities
        'requests',           # Commonly used for making HTTP requests
        'numpy',              # If your package performs numerical computations
        'scipy',              # If used in any audio processing or scientific computations
        'librosa',            # For audio analysis, if used in your audio module
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', # Minimum Python version your package supports
    include_package_data=True,
    keywords='common-ml-functions, language processing, youtube downloader, text-to-speech', # Add relevant keywords
)
