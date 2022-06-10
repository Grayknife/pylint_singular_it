## repository for pylint configurations and plugins

Extensions in pylint are not implemented so as a workaround the extensions are implemented as pylint plugins. 

The following extensions exists in this repo:

1. pylint_sit (pylint extension)
2. pylint_sit_django (pylint extension django)

Every extension has its own directory with the following subdirectories and files:

- `src` Directory
- an extension file inside `src`, for example ``src/pylint_sit.py``
- a virtual environment, we are using ``venv``
- a requirements file: ``requirements.txt``
- a `README.md` as long description for the extension
- a `LICENSE` for the extension
- a `setup.cfg` for the extension
- a `setup.py` for the extension

The ``dist`` directory will automatically be created.

### Create a new extension

We created an example directory ``example_extension`` with all its necessary files.
1. copy ``example_extension`` as a new extension and name it correctly.
2. ``cd`` into it and create a virtual environment: `virtualenv venv`
3. Install the packages from ``requirements.txt``: `pip install -r requirements.txt`
4. Rename ``src/example_extension.py`` and modify it to your needs.
5. Run ``python -m build``. A `dist` directory will be created with your packaged extension
7. Verify extension reading the paragraph **Verify extension**


### Update existing extension

- Update the extension .py file to your needs
- Update the ``setup.cfg`` file:
  - increase build version
  - optional: update ``install_requires``
  - optional: update ``README.md``

### Verify extension
1. Install it locally: 
   - ``cd`` into extension root directory
   - Run ``pip install -e .``
2. Create an Error test file:
   - Create an example file `test.py` and insert a failure in that file you want to check. 
3. Run ``pylint test.py --load-plugins <EXTENSION_NAME>``

### Build a package extension

- Create a new ``.wheel`` and ``.tar.gz``
  - ``cd`` into the root directory of the extension and create a virtual environment: `virtualenv venv`
  - Install the packages from ``requirements.txt``: `pip install -r requirements.txt`
  - Rename ``src/example_extension.py`` and modify it to your needs.
  - Run ``python -m build``. A `dist` directory will be created with your packaged extension
- Optional: Upload the extension to ``pypi``
  - Run ``twine upload dist/pylint_sit-<NEW_BUILD_VERSION>*`` & username and password are required


### Contribute
TODO