from setuptools import setup, find_packages

setup(
    name="libbydl",
    version="0.1.0",
    description="A tool for downloading and decrypting books from Libby",
    author="Marek Veselý",
    author_email="me@notmarek.com",
    license="GPLv3",
    packages=find_packages(),
    install_requires=[
        "click==8.0.0",
        "requests==2.25.1",
        "colorama==0.4.4",
        "loguru==0.5.3",
        "tabulate==0.8.9",
        "lxml==4.9.3",
        "pycryptodome==3.10.1",
        "oscrypto==1.2.0",
    ],
    entry_points={
        "console_scripts": [
            "libbydl=libbydl.__main__:main",
        ],
    },
)
