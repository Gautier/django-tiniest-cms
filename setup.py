from setuptools import setup

setup(
    name='django-tiniest-cms',
    version='0.9.0',
    description='django-tiniest-cms is an seriously minimalist Django CMS',
    long_description=open('README').read(),
    author='Gautier Hayoun',
    license='MIT',
    packages=['django_tiniest_cms'],
    install_requires=['Markdown==2.4.1']
)
