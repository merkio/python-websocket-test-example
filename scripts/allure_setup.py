from setuptools import setup


VERSION = '1.0'

install_requires = [
    'pytest>=3.5.1',
    'pytest-rerunfailures>=4.1',
    'allure-pytest>=2.5.0',
    'allure-python-commons>=2.5.0'
]


def main():
    setup(
        name='allure2-pytest',
        version=VERSION,
        description='Allure 2 report for Pytest testing framework',
        author='merkio',
        packages=['tests'],
        url='https://github.com/merkio/python-websocket-test-example',
        install_requires=install_requires
    )


if __name__ == '__main__':
    main()
