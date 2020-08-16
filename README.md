![Banner](https://github.com/SauravMaheshkar/CoxPH-Model-for-Primary-Biliary-Cirrhosis/blob/master/Banner.png)

# CoxPH Model for Primary Biliary Cirrhosis

<!-- Add buttons here -->

<!-- Describe your project in brief -->

<!-- The project title should be self explanotory and try not to make it a mouthful. (Although exceptions exist- **awesome-readme-writing-guide-for-open-source-projects** - would have been a cool name)

Add a cover/banner image for your README. **Why?** Because it easily **grabs people's attention** and it **looks cool**(*duh!obviously!*).

The best dimensions for the banner is **1280x650px**. You could also use this for social preview of your repo.

I personally use [**Canva**](https://www.canva.com/) for creating the banner images. All the basic stuff is **free**(*you won't need the pro version in most cases*).

There are endless badges that you could use in your projects. And they do depend on the project. Some of the ones that I commonly use in every projects are given below. 

I use [**Shields IO**](https://shields.io/) for making badges. It is a simple and easy to use tool that you can use for almost all your badge cravings. -->

<!-- Some badges that you could use -->

<!-- ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
: This badge shows the version of the current release.

![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
: I think it is self-explanatory. This gives people an idea about how the project is being maintained.

![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
: This is a dynamic badge from [**Shields IO**](https://shields.io/) that tracks issues in your project and gets updated automatically. It gives the user an idea about the issues and they can just click the badge to view the issues.

![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
: This is also a dynamic badge that tracks pull requests. This notifies the maintainers of the project when a new pull request comes.

![GitHub All Releases](https://img.shields.io/github/downloads/navendu-pottekkat/awesome-readme/total): If you are not like me and your project gets a lot of downloads(*I envy you*) then you should have a badge that shows the number of downloads! This lets others know how **Awesome** your project is and is worth contributing to.

![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)
: This shows what kind of open-source license your project uses. This is good idea as it lets people know how they can use your project for themselves.

![Tweet](https://img.shields.io/twitter/url?style=flat-square&logo=twitter&url=https%3A%2F%2Fnavendu.me%2Fnsfw-filter%2Findex.html): This is not essential but it is a cool way to let others know about your project! Clicking this button automatically opens twitter and writes a tweet about your project and link to it. All the user has to do is to click tweet. Isn't that neat? -->

# Demo

<!-- Add a demo for your project -->

<!-- After you have written about your project, it is a good idea to have a demo/preview(**video/gif/screenshots** are good options) of your project so that people can know what to expect in your project. You could also add the demo in the previous section with the product description.

Here is a random GIF as a placeholder.

![Random GIF](https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif) -->

# Table of contents

<!-- After you have introduced your project, it is a good idea to add a **Table of contents** or **TOC** as **cool** people say it. This would make it easier for people to navigate through your README and find exactly what they are looking for.

Here is a sample TOC(*wow! such cool!*) that is actually the TOC for this README. -->

- [Project Title](#project-title)
- [Demo](#demo)
- [Table of contents](#table-of-contents)
- [Overview](#overview)
- [Motivation](#motivation)
- [Stack](#stack)
- [Goals](#goals)
- [Installation](#installation)
- [Directory tree](#directory-tree)
- [Usage](#usage)
- [Development](#development)
- [Request](#request)
    -[Bug](#bug)
- [Contribute](#contribute)
- [License](#license)
- [Credits](#credits)

# Installation
[(Back to top)](#table-of-contents)

<!-- *You might have noticed the **Back to top** button(if not, please notice, it's right there!). This is a good idea because it makes your README **easy to navigate.*** 

The first one should be how to install(how to generally use your project or set-up for editing in their machine).

This should give the users a concrete idea with instructions on how they can use your project repo with all the steps.

Following this steps, **they should be able to run this in their device.**

A method I use is after completing the README, I go through the instructions from scratch and check if it is working. -->

<!-- Here is a sample instruction:

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/navendu-pottekkat/nsfw-filter.git``` -->

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
