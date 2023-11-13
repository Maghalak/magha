import setuptools

setuptools.setup(
    include_package_data=True,
    name='math_quiz',
    version='0.0.1',
    description='Maghalak python module',
    url='https://github.com/Maghalak/magha.git',
    author='Maghalak',
    author_email='contact@Maghalak.com',
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'pytest'
    ],
    long_description='Maghalak python module',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)
