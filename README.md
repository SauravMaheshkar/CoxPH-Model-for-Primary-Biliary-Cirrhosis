![Banner](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/Banner.png)

# CoxPH Model for Primary Biliary Cirrhosis

**Proportional hazards** models are a class of survival models in statistics. Survival models relate the time that passes, before some event occurs, to one or more covariates that may be associated with that quantity of time. In a proportional hazards model, the unique effect of a unit increase in a covariate is multiplicative with respect to the hazard rate. For example, taking a drug may halve one's hazard rate for a stroke occurring, or, changing the material from which a manufactured component is constructed may double its hazard rate for failure. Other types of survival models such as accelerated failure time models do not exhibit proportional hazards. The accelerated failure time model describes a situation where the biological or mechanical life history of an event is accelerated (or decelerated).

**Cox regression** (or **proportional hazards regression**) is method for investigating the effect of several variables upon the time a specified event takes to happen. In the context of an outcome such as death this is known as Cox regression for survival analysis. The method does not assume any particular "survival model" but it is not truly nonparametric because it does assume that the effects of the predictor variables upon survival are constant over time and are additive in one scale.

Provided that the assumptions of Cox regression are met, this function will provide better estimates of survival probabilities and cumulative hazard than those provided by the Kaplan-Meier function.


# Table of contents

- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Stack](#stack)
- [Usage](#usage)
- [Development](#development)
- [Directory tree](#directory-tree)
- [Request](#request)
    -[Bug](#bug)
- [Contribute](#contribute)
- [License](#license)
- [Credits](#credits)

# Installation
[(Back to top)](#table-of-contents)

To use this project, first clone the repo on your device using the command below:

```git init```

```https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis.git``` 

You'll also need to run the ```requirements.txt``` file to download all the dependencies. Then you can run the app by running ```python3 app.py```. This will open a web app where you'll need to put in the values in the ```input``` boxes.

# Stack

[(Back to top)](#table-of-contents)

The following libraries and modules were used in this software:

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [sklearn](https://scikit-learn.org/stable/)
- [matplotlib](https://matplotlib.org/)
- [lifelines](https://lifelines.readthedocs.io/en/latest/)
- [flask](https://flask.palletsprojects.com/en/1.1.x/)

# Usage
[(Back to top)](#table-of-contents)

To run the program just run the following command on the terminal
```python
python3 app.py
```

# Development
[(Back to top)](#table-of-contents)

This entire project is based on the [lifeline](https://lifelines.readthedocs.io/en/latest/index.html) package specifically on the [CoxPH Survival Regression Model](https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html#cox-s-proportional-hazard-model). If want to develop on the project start from mastering this package and all it's [prediction](https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html#prediction) functions. 

There are two main files in the project 
- [main.py](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/main.py)
- [app.py](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/app.py)

You'll be making all the changes in the [main.py](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/main.py) file. If you have a different dataset, edit the ```input_path``` variable. Make sure that the sex column is filled with categorical variables. For instance, my dataset didn't had the variables as categorical they were of the form "f" and "m". If you want to encode different columns edit the ```to_encode``` variable. Also, if you want to change the duration column for the regression model change the ```duration_col``` parameter in the ```fit()``` function. Same goes for the ```event_col``` variable. 

In the [app.py](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/app.py) file , you can change the input data for the prediction. In this project I've made a simple Flask Web-Application for any user to input the data. The user will input the variables in the ```input``` tag of the [index.html](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/templates/index.html) file. If you instead want the user to give as input a .csv file you'll need to add some code to convert that .csv file to a dataframe and then edit the [main.py](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/main.py) file as well.

# Directory Tree
[(Back to top)](#table-of-contents)

```bash
├── __pycache__
│   ├── main.cpython-38.pyc
│   └── process_data.cpython-38.pyc
├── app.py
├── input
│   └── pbc.csv
├── main.py
├── requirements.txt
├── static
│   ├── css
│   └── js
└── templates
    ├── index.html
    └── result.html
```

# Request
[(Back to top)](#table-of-contents)

### Bug 
[(Back to top)](#table-of-contents)

If you spot a bug in the program kindly raise a issue. Instructions for raising an issue can be found [here](https://docs.github.com/en/enterprise/2.15/user/articles/creating-an-issue)

# Contribute
[(Back to top)](#table-of-contents)

If you want to contribute to the project kindly mail me at `sauravvmaheshkar@gmail.com`.

### Step 1
 - **Option 1**
   🍴 Fork it!  
 - **Option 2**
    👯‍♂️ Clone this repo to your local machine using `https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis.git`
### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using `https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/compare/`


# License
[(Back to top)](#table-of-contents)

[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

The data for this project was taken from kaggle datasets. The owner of the dataset is [student zero](https://www.kaggle.com/jixing475). You can find the dataset [here](https://www.kaggle.com/jixing475/mayo-clinic-primary-biliary-cirrhosis-data).

- Copyright 2020 @[Saurav Maheshkar](https://sauravmaheshkar.github.io/)
- [MIT License](https://opensource.org/licenses/MIT)


# Credits

The inspiration for this readme file came from
- [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46#license)
- [Navendu Pottekkat](https://github.com/navendu-pottekkat/awesome-readme/blob/master/README-template.md)

Description of the CoxPH came froom
- [Wikipedia](https://en.wikipedia.org/wiki/Proportional_hazards_model)
- [Statsdirect](https://www.statsdirect.com/help/survival_analysis/cox_regression.htm)
