from setuptools import find_packages, setup

import django_fire


setup(
    name='django-fire',
    version=django_fire.__version__,
    packages=find_packages(exclude=['*.tests']),
    scripts=[],

    install_requires=['Django'],

    author='lordpeara',
    author_email='lordpeara@gmail.com',
    description='vulnerable password cleanser for django',
    license='MIT',
    keywords='django password password-remover password-cleanser',
    url='http://github.com/lordpeara/django-fire',

    zip_safe=False,
    include_package_data=True,

    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
)
