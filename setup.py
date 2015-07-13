# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup
try:
    from jupyterpip import cmdclass
except:
    import pip, importlib
    pip.main(['install', 'jupyter-pip']); cmdclass = importlib.import_module('jupyterpip').cmdclass

setup(
    name='d3networkx_psctb',
    version='0.1',
    description='Visualize networkx graphs using D3.js in the IPython notebook.',
    author='Jonathan Frederic',
    author_email='jon.freder@gmail.com',
    license='MIT License',
    url='https://github.com/jdfreder/ipython-d3networkx',
    keywords='python ipython javascript d3 networkx d3networkx widget',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'License :: OSI Approved :: MIT License'],
    packages=['d3networkx_psctb'],
    include_package_data=True,
    install_requires=["jupyter-pip","networkx"],
    cmdclass=cmdclass('d3networkx_psctb'),
)
