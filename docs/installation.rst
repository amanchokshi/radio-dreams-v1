=========================
 Installing Radio Dreams
=========================

*radio-dreams* is designed to install cleanly with a single invocation
of the standard Python package tool

.. code-block:: console

    pip install radio-dreams

*radio-dreams* can also be installed manually from it's github repository

.. code-block:: console

    git clone https://github.com/amanchokshi/radio-dreams.git
    cd radio-dreams
    pip install .

These methods will install *radio-dreams* and the small collection of Python libraries that radio-dreams depends on.
Using a virtual environment is suggested as it prevents errors from conflicting dependancies

The *radio-dreams* package can now be imported with :samp:`import radio_dreams`

Pyenv virtual environment
-------------------------
*radio-dreams* supports Python 3.7+. Using a :samp:`pyenv` environment is the cleanest route to the correct python version. Install pyenv with the instructions at `<https://realpython.com/intro-to-pyenv/>`_. Now, to install the correct version of python and make a virtual environment

.. code-block:: console

    # Install python version 3.8.3
    pyenv install 3.8.3

    # Create a virtual environment called radio-dreams
    # env located at ~/.pyenv/versions/radio-dreams
    pyenv virtualenv 3.8.3 radio-dreams

    # virtual env automatically activated when in radio-dreams
    # Link the radio-dreams dir with the virtual env
    # creates a .python-version file
    python local radio-dreams

    # Install the radio-dreams package & dependancies
    pip install radio-dreams


Conda virtual environment
--------------------------
*radio-dreams* supports Python 3.7+. Using a :samp:`conda` environment is another way to make sure that the correct version of Python is used. Begin by installing either `Anaconda <https://docs.anaconda.com/anaconda/install/>`_ or `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_. A conda environment called *radio-dreams* can be created as follows

.. code-block:: console

    conda create --name radio-dreams python=3.8
    conda activate radio-dreams
    pip install radio-dreams


Python virtual environment
--------------------------
Alternately, if you already have a correct version of Python installed, you can create a `venv <https://docs.python.org/3/library/venv.html/>`_ called radio-dreams within which *radio-dreams* and it's dependancies are cleanly installed

.. code-block:: console

    python -m venv radio-dreams
    source radio-dreams/bin/activate
    pip install radio-dreams



If you find any problems or would like to suggest an improvement,
simply create an issue on the project’s GitHub page:

    https://github.com/amanchokshi/radio-dreams

Good luck!
