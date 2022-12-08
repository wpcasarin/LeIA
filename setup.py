import codecs
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setup(
    name='LeIA',
    # packages = ['vaderSentiment'], # this must be the same as the name above
    # a better way to do it than the line above -- this way no typo/transpo errors
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    version='0.0.1',
    description='LeIA (Léxico para Inferência Adaptada) é um fork do léxico e ferramenta para análise de sentimentos VADER (Valence Aware Dictionary and sEntiment Reasoner) adaptado para textos em português.',
    long_description=read("README.md"),
    long_description_content_type='text/x-rst',
    author='C.J. Hutto',
    author_email='cjhutto@gatech.edu',
    license='MIT License: http://opensource.org/licenses/MIT',
    url='https://github.com/wpcasarin/LeIA',  # use the URL to the github repo
    # download_url='https://github.com/cjhutto/vaderSentiment/archive/master.zip',
    install_requires=['requests'],
    keywords=['vader', 'sentiment', 'analysis', 'opinion', 'mining', 'nlp', 'text', 'data',
              'text analysis', 'opinion analysis', 'sentiment analysis', 'text mining', 'twitter sentiment',
              'opinion mining', 'social media', 'twitter', 'social', 'media'],  # arbitrary keywords
    classifiers=['Development Status :: 4 - Beta', 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License', 'Natural Language :: English',
                 'Programming Language :: Python :: 3.5', 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Information Analysis', 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Text Processing :: General'],
)
