![Banner](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/Banner.png)

# CoxPH Model for Primary Biliary Cirrhosis

**Proportional hazards** models are a class of survival models in statistics. Survival models relate the time that passes, before some event occurs, to one or more covariates that may be associated with that quantity of time. In a proportional hazards model, the unique effect of a unit increase in a covariate is multiplicative with respect to the hazard rate. For example, taking a drug may halve one's hazard rate for a stroke occurring, or, changing the material from which a manufactured component is constructed may double its hazard rate for failure. Other types of survival models such as accelerated failure time models do not exhibit proportional hazards. The accelerated failure time model describes a situation where the biological or mechanical life history of an event is accelerated (or decelerated).

**Cox regression** (or **proportional hazards regression**) is method for investigating the effect of several variables upon the time a specified event takes to happen. In the context of an outcome such as death this is known as Cox regression for survival analysis. The method does not assume any particular "survival model" but it is not truly nonparametric because it does assume that the effects of the predictor variables upon survival are constant over time and are additive in one scale.

Provided that the assumptions of Cox regression are met, this function will provide better estimates of survival probabilities and cumulative hazard than those provided by the Kaplan-Meier function.

**Hazard and hazard-ratios**

Cumulative hazard at a time t is the risk of dying between time 0 and time t, and the survivor function at time t is the probability of surviving to time t 

 

The coefficients in a Cox regression relate to hazard; a positive coefficient indicates a worse prognosis and a negative coefficient indicates a protective effect of the variable with which it is associated.

 

The hazards ratio associated with a predictor variable is given by the exponent of its coefficient; this is given with a confidence interval under the "coefficient details" option in StatsDirect. The hazards ratio may also be thought of as the relative death rate. The interpretation of the hazards ratio depends upon the measurement scale of the predictor variable in question for further information on relative risk of hazards.

 

**Time-dependent and fixed covariates**

In prospective studies, when individuals are followed over time, the values of covariates may change with time. Covariates can thus be divided into fixed and time-dependent. A covariate is time dependent if the difference between its values for two different subjects changes with time; e.g. serum cholesterol. A covariate is fixed if its values can not change with time, e.g. sex or race. Lifestyle factors and physiological measurements such as blood pressure are usually time-dependent. Cumulative exposures such as smoking are also time-dependent but are often forced into an imprecise dichotomy, i.e. "exposed" vs. "not-exposed" instead of the more meaningful "time of exposure". There are no hard and fast rules about the handling of time dependent covariates. 

 

**Model analysis and deviance**
Here the likelihood chi-square statistic is calculated by comparing the deviance (- 2 * log likelihood) of your model, with all of the covariates you have specified, against the model with all covariates dropped. The individual contribution of covariates to the model can be assessed from the significance test given with each coefficient in the main output; this assumes a reasonably large sample size.

 

Deviance is minus twice the log of the likelihood ratio for models fitted by maximum likelihood. The value of adding a parameter to a Cox model is tested by subtracting the deviance of the model with the new parameter from the deviance of the model without the new parameter, the difference is then tested against a chi-square distribution with degrees of freedom equal to the difference between the degrees of freedom of the old and new models. The model analysis option tests the model you specify against a model with only one parameter, the intercept; this tests the combined value of the specified predictors/covariates in the model.

 

Some statistical packages offer stepwise Cox regression that performs systematic tests for different combinations of predictors/covariates. Automatic model building procedures such as these can be misleading as they do not consider the real-world importance of each predictor

 

**Survival and cumulative hazard rates**

The survival/survivorship function and the cumulative hazard function are calculated relative to the baseline (lowest value of covariates) at each time point. Cox regression provides a better estimate of these functions than the Kaplan-Meier method when the assumptions of the Cox model are met and the fit of the model is strong.


# Table of contents

- [Table of contents](#table-of-contents)
- [Aim](#aim)
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

# Aim
[(Back to top)](#table-of-contents)

The aim of this project is to make a Cox Proportional Hazard Model for analysis of Primary Biliary Cirrhosis(pbc) and use that to calculate the predicted life expectancy of a subject

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
