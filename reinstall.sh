#!/bin/bash
rm -r build/
rm -r dist/
rm -r d3networkx_psctb.egg-info/
rm -r /home/carl/.local/share/jupyter/nbextensions/d3networkx_psctb
pip uninstall d3networkx_psctb -y
pip install .
exit 0