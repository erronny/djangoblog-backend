import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(
    name="backend", # Replace with your own username
    version="0.0.1",
    author="Sunil Shaw Urf Ronny Dsouza",
    author_email="thehemedia@gmail.com",
    description=(" An demonstration of how to create, document, and publish posts for reader."),
    
    long_description_content_type="text/markdown",
    license = read('LICENSE.txt'),
    url="https://github.com/erronny/django-reusable-posts",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.8"  ,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Django :: Posts",
        "Topic :: Internet :: Blog :: Dynamic Content",

    ],
    python_requires='>=3.6',
)