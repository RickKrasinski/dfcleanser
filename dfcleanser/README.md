# dfcleanser
Dataframe Cleanser

## Dependencies
The full dataframe Cleanser has dependencies on the following python packages.
1) numpy
2) scipy
3) pandas-sklearn/spark
4) geopy
5) sqlalchemy
6) json
7) specific database driver(MySQL/MsSQLServer/PostGres/Oracle/SQLite)

## Package Installation
It's highly recommended that you install in a virtualenv. The following commands assume you have already done `source activate my-env-name`. After doing so, install both the serverextension and the toolbar button (nbextension) with:

```bash
pip install dfcleanser


## Jupyter Extension(s) 
You can install dfcleanser extensions to the Jupyter Server and Notebook for a permanent implementation of dfcleanser:

## dfcleanser Jupyter Installation

### Automatic Intallation

With the pip install of dfcleanser the Jupyter hooks to run dfcleanser are automatically defined and 
the extensions must be enabled via the dfcleanser Jupyter Extension commands defined below.

#### dfcleanser Jupyter Extension Enable

```bash
jupyter serverextension enable --py dfcleanser --sys-prefix
jupyter nbextension install --py dfcleanser --sys-prefix
jupyter nbextension enable --py dfcleanser --sys-prefix

#### dfcleanser Jupyter Extension Verification

```bash
jupyter nbextension list
jupyter serverextension list

#### Automatic Load/Unload

A new button will appear on your toolbar that looks like this:  
![pizza button](https://github.com/peterskipper/pizzabutton/raw/master/images/button.png "Pizza Delivery Button")

Click the button once to toggle between loading and unloading the dataframe cleanser...

### Manual Installation
If you do not wish to modify the Jupyter server and subsequent notebooks you can manually install the dfcleanser modules for a temporary implementation of dfcleanser:

#### Manual dfcleanser Install/UnInstall
Once the dfcleanser package is installed via pip or conda you need to manually install the dfcleanser functionality to be available in Jupyter.

Open a Jupyter notebook and from a code cell run the following :

from dfcleanser.system.install import install_dfcleanser
install_dfcleanser()

Once the above install completes you can check if the install is good via the following run from a Jupyter code cell:

from dfcleanser.system.install import setup_dfcleanser
setup_dfcleanser()

To remove the dfcleanser module from your Jupyter Server run the following:

from dfcleanser.system.install import uninstall_dfcleanser
uninstall_dfcleanser()

#### Jupyter Notebook dfcleanser Load/Unload
Once you have installed the above components successfully dfcleanser is now available to be dynamically loaded into or unloaded from a Jupyter notebook.

To load dfcleanser into your notebook run the following from a Jupyter code cell:

from dfcleanser.system.load import load_dfcleanser
load_dfcleanser()

The dfcleanser Jupyter cells are now set up in your notebook for you to use independent of any other cells in the notebook.

To unload dfcleanser from your notebook run the following from a Jupyter code cell:

from dfcleanser.system.load import unload_dfcleanser
unload_dfcleanser()


## dfcleanser Data Files

The dfcleanser creates and uses two sets of files while running :

1) dfcleanser Common files
2) Notebook specific files

The dfcleanser Common files are files used by the provided utilities to maintain a server wide set of common functions, lists, dicts ... that are available within any dfcleanser loaded notebook.

The Notebook specific files are files that are tied specifically to a Jupyter notebook that has/had dfcleanser loaded into it.  For every notebook that loads dfcleanser into it a unique cfg an script file is maintained for that notebook.

The notebook specific files are maintained internally by dfcleanser relative to the dfCleasnser package.  The user can manage these files via the System Environment->dfcleanser files button.  If you copy, rename or delete a notebook then use the Environment->dfcleanser files functions to generate proper custom notebook files.

## Datasets/DataSources

dfcleanser allows you to browse through datasets for import or export while running dfcleanser.  To be able to automatically browse and identify datasets you must create a Datasets directory in the tree where the notebook is found.  All datasets in this directory can be browsed and worked with automatically.  

If you do not want to browse you can given the absolute path of your dataset and that will be used.

