# Office microbes
Notebooks and code for our Sloan office microbiome project (pre-print [here](https://peerj.com/preprints/1797/), currently in press at mSystems).

The processed files used in these notebooks are available upon request (due to size, > 120GB). All raw data is publicly accessible in [ERA under accession number ERP014651](http://www.ebi.ac.uk/ena/data/view/ERP014651), and the processed files can all be computed from these raw files using QIIME 1.9.1.
 
## To get started using this code
 1. create a conda enviornment for the project: ``conda create -n office-microbes python=3.4 scikit-bio; source activate office-microbes``
 2. clone the repository: ``git clone git@github.com:gregcaporaso/office-microbes.git``
 3. change to the resulting directory: ``cd office-microbes``
 4. run: ``pip install -e .``
 5. Change to the ``Final`` directory and launch the Jupyter notebook server with the command ``jupyter notebook``
