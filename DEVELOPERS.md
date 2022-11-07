# Prerequisites:

    # To enable Pypi distribution
    pip install twine

# Update on Pypi

    # Create a source distribution
    rm -rf dist
    python setup.py sdist
    twine upload dist/*



