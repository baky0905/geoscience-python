# geoscience-python

https://baky0905.github.io/geoscience-python/

## Purpose

Create practical data analysis and data science online reproducible sphinx booklet for common Geoscience and Petroleum Engineering problems. Key is to enable people to solve their own problems.

What kind of code will we be using?
* Personal automation
* Consistent ways of writing code
* Code that you are writing for yourself and you are the only person who is going to be using it
* <del>Professional code<del>
* <del>Checked in code<del>
* <del>Reviewed code<del>
  
You can some cut corners, write some crappy code and do some things that questionable but all of it is just fine -
no one will ever see it and no one will ever know.

**Main goal - solve your problem!**

**Motivate you to maybe dive in deeper and become semi-professional one day!**



## Authors

Kristijan Bakaric
Peyman Kor
...

## Licence

The course material is licensed under a Creative Commons BY-NC-SA 4.0 license.

## Usage:

### Building html pages locally
The libraries needed in these Jupyter notebooks are listed in file requirements.txt. In addition, to compile the *.ipynb and *.rst files to html pages, the following libraries are needed:

* nbsphinx (conda install -c conda-forge nbsphinx)
* sphinx_rtd_theme (conda install sphinx_rtd_theme)

After all has been installed and enabled do the following:

1) clone this repository

tree is looking like this:

```
├───docs
│   ├───.doctrees
│   │   ├───additional
│   │   ├───nbsphinx
│   │   └───notebooks
│   │       └───.ipynb_checkpoints
│   ├───additional
│   ├───notebooks
│   │   └───.ipynb_checkpoints
│   ├───_images
│   ├───_sources
│   │   ├───additional
│   │   └───notebooks
│   │       └───.ipynb_checkpoints
│   └───_static
│       ├───css
│       ├───fonts
│       │   ├───Lato
│       │   └───RobotoSlab
│       └───js
└───source
    ├───additional
    ├───data
    ├───notebooks
    │   └───.ipynb_checkpoints
    ├───_static
    └───_templates
```

2) Make a contribution by creating an:
  * *.rst file and putting it to source/additional folder
  * jupyter notebbok and putting it to source/notebook folder

3) we need to discuss wether to put data in the data folder or url sourcing is also ok (could disseaper one day and then it is not reproducible)

4) After you have created rst and jupyter notebok, you need to reference them in the index.rst file

Example:

```
.. toctree::
   :maxdepth: 2
   :caption: Introduction:

   additional/welcome.rst
   notebooks/quick_introduction.ipynb
```

5) while in the root folder in anaconda prompt run a command `sphinx-build -b html source\ docs\` 
which will compile the *.ipynb and *.rst files to html pages and create a sphinx website.
In the command line source is the source\ folder where your files live and docs\ will be the folder where
htmls and the tree will be compiled.

\docs folder will be the folder that will be rendered on github pages as a static website.

6) Go to your git bash 

```
git pull
git add .
git commit -m "Add ..."
git push
```

7) Voila: https://baky0905.github.io/geoscience-python/


