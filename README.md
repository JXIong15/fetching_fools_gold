# Fetching Fools Gold
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Table of Contents
* [Description](#description)
* [Installations](#installations)
* [Commands](#commands)
* [Functionality](#functionality)
* [Technologies Used](#technologies-used)
* [Results](#results)
* [Future Ideas](#future-ideas)
* [Sources](#sources)


## Description
A Selenium-Python based algorithm to find the fake gold bar in the minimum number of weighings.
* **GitHub:** https://github.com/JXIong15/fetching_fools_gold
* **Tested Website:** http://sdetchallenge.fetchrewards.com/
<p><img src="https://i.ibb.co/6yyFzJW/Screen-Shot-2022-05-06-at-12-25-03-PM.png" width="100%"  stylealt="tested website page"/></p>
<p align="center">(The SDET Challenge webpage to be tested using Selenium)</p>


## Installations
* **ChromeDriver** Installation
    * To check/update Chrome, go to the menu and select `Help > About Google Chrome` or download and install it: https://www.google.com/chrome/
    * Next, download the matching version of ChromeDriver: https://sites.google.com/chromium.org/driver/
    * Lastly, add it to your system path
        * You can figure out your PATH by typing `echo $PATH` in your `command line`
    * To make sure chromedriver is working, type `chromedriver` in your `command line`. You should receive a similar message to the one in the image below.
    * If you're getting an Apple error for chromedriver, `cd` to the directory where chromedriver is and run `xattr -d com.apple.quarantine chromedriver`
<p><img src="https://i.ibb.co/mvmvcCt/Screen-Shot-2022-05-06-at-12-40-39-PM.png" width="100%"  stylealt="successful chromedriver installation"/></p>
<p align="center">(Success ChromeDriver Installation Verification)</p>

* Clone *this* repo in *command line*: `git clone` and one of the links below
  * **HTTPS:** https://github.com/JXIong15/fetching_fools_gold.git
  * **SSH:** git@github.com:JXIong15/fetching_fools_gold.git
* `$ cd fetching_fools_gold` into the project and install in your command line: 
  * *python*: https://www.python.org/downloads/
  * *pip*: should automatically be installed with python above
  * *pipenv*: https://pipenv.pypa.io/en/latest/install/
    * run `pipenv install` to download provided packages to pipfile and project


## Commands
* Enter the virtual environment: `pipenv shell`
* Next, run `python main.py` to view the results of the algorithm
<p><img src="https://i.ibb.co/dfS01GG/Screen-Shot-2022-05-06-at-1-27-56-PM.png" width="100%"  stylealt="results after installations and running commands"/></p>
<p align="center">(Results after installations and running commands)</p>


## Functionality
* Connects to the webpage using ChromeDriver
* Uses Python to create an algorithm for the least amount of weighings to find the fake gold bar
* Uses Selenium to interact with the webpage and make assertions
* Mathematically, to calculate the fewest amount of weighings needed, a user would weigh an equal half of the gold over and over again until they are weighing one gold bar against one gold bar. Hence, the minimum number of weighings would be `log2(n)` where `n = number-of-gold-bars`, and we round *down*.
    * **Caveat:** In the case that the very first round of weighings are equal and the total number of gold bars is odd, then the extra gold bar that was not weighed is the fake one. Thus, the total number of weighings here would be less than `log2(n)`.


## Technologies Used
* Selenium
* Python
* ChromeDriver


## Results
* **Found Fake Gold Alert Message**:
<p><img src="https://i.ibb.co/PzGQ8fz/Screen-Shot-2022-05-06-at-1-08-25-PM.png" width="100%" height="100%" stylealt="found fake gold alert message"/></p>

* **Found Non-Fake Gold Alert Message**:
<p><img src="https://i.ibb.co/MsQzngj/Screen-Shot-2022-05-06-at-1-08-34-PM.png" width="100%" height="100%" stylealt="found non-fake gold alert message"/></p>


## Future Ideas
* I'd like to run the program on a larger set of gold bars


## Sources
* ChromeDriver Installation Guide: https://blog.testproject.io/2019/07/16/installing-selenium-webdriver-using-python-chrome/
* Python HTTP Requests: https://docs.python-requests.org/en/latest/
* I install everything using Homebrew: https://brew.sh/
    * ChromeDriver using Homebrew: https://formulae.brew.sh/cask/chromedriver


## License
Licensed under the [MIT License](LICENSE).

<p align="center">© 2022 Jou Xiong</p>
