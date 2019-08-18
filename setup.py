from setuptools import setup


def get_requirements():
    with open("requirements.txt") as fh:
        return fh.readlines()


if __name__ == '__main__':
    setup(
        name="juststream",
        version="0.1",
        packages=["juststream"],
        scripts=[],
        install_requires=get_requirements(),
    )
