from setuptools import find_packages, setup


__version__ = "0.0.1"

setup_args = dict(
    name="yarn_exporter",
    version=__version__,
    author="Armadik",
    platforms="Linux",
    description="Platform components for Jupyterhub",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests-kerberos==0.14.0",
        "pyspnego==0.5.1",
        "prometheus-client==0.14.1",
        "yarn-api-client==1.0.3",
    ],
    entry_points={
        'console_scripts': [
            'yarn_exporter = yarn_exporter.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)


def main():
    setup(**setup_args)


if __name__ == '__main__':
    main()
