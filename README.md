# fetching_fools_gold
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Table of Contents
* [Description](#description)
* [Installations](#installations)
* [Functionality](#functionality)
* [Commands](#commands)
* [Technologies Used](#technologies-used)
* [Demo](#demo)
* [Future Ideas](#future-ideas)
* [Sources](#sources)


## Description
A Selenium-Python based algorithm to find the fake gold bar in the minimum number of weighings.
* **GitHub:** https://github.com/JXIong15/fetching_fools_gold
* **Tested Website:** http://sdetchallenge.fetchrewards.com/
<p><img src="" width="100%"  stylealt="tested website page"/></p>
<p align="center">(The SDET Challenge webpage to be tested using Selenium)</p>


## Installations
* **ChromeDriver** Installation
    * To check/update Chrome, go to the menu and select `Help > About Google Chrome` or download and install it: https://www.google.com/chrome/
    * Next, download the matching version of ChromeDriver: https://sites.google.com/chromium.org/driver/
    * Lastly, add it to your system path
        * You can figure out your PATH by typing `echo $PATH` in your `command line`
    * To make sure chromedriver is working, type `chromedriver` in your `command line`. You should receive the same message in the image below:
<p><img src="" width="100%"  stylealt="successful chromedriver installation"/></p>
<p align="center">(Success ChromeDriver Installation Verification)</p>

* Clone *this* repo in *command line*: `git clone` and one of the links below
  * **HTTPS:** https://github.com/JXIong15/fetching_fools_gold.git
  * **SSH:** git@github.com:JXIong15/fetching_fools_gold.git
* `cd` into the project and install in your command line:
  * *python*: https://www.python.org/downloads/
  * *pip*: should automatically be installed with python above
  * *pipenv*: https://pipenv.pypa.io/en/latest/install/
    * run `pipenv install` to download provided packages to pipfile and project
    * run `pipenv shell` to enter the virtual environment


## Functionality
* For the purpose of this project, the environmental variables are given in `.env.EXAMPLE`. 
Delete the **.EXAMPLE** part to use the **.env** file
* It is recommended that you create your own superuser to access the Django Admin: `python manage.py createsuperuser`
* To start the app locally, run `python manage.py runserver` and go to `http://localhost:8000/admin`
  * there is currently no Frontend, so you will just see the Django Admin panel with its built-in forms
* Using **Postman** (or any similar application):
  * GET *http://localhost:8000/balance/* : returns a list of the current payer balances
  * GET *http://localhost:8000/payer/* : returns a list of the current payers
  * GET *http://localhost:8000/transaction/* : returns a list of the transactions from oldest timestamp
  * POST *http://localhost:8000/payer/* : data = `{'name'='NAME'}` will return the new payer's information
  * POST *http://localhost:8000/transaction/* : data = `{'name'='NAME', 'points'=int, timestamp=time}` will add the 
new points to the specified payer
  * POST *http://localhost:8000/spend/* : data = `{'points'=int}` will return a receipt of which payer(s) spent points 
and how many points each payer spent
    * points are spent in order of oldest transaction timestamp
  * DELETE *http://localhost:8000/payer/{payer_id}* : will delete the payer and all associated transactions to them


## Commands
* In the *virtual environment*, run:
  * Server: `python manage.py runserver`
  * Tests: `python manage.py test`
  * Webclient Requests: `python points/client.py`


## Technologies Used
* **Django** and **Django REST Framework**
* **Postman** to test API routes: https://www.postman.com/downloads/
* **environ** for secret keys
* **requests** for Python web client


## Results
* **Webclient Results**:
<p><img src="https://i.imgur.com/ht6eSnv.png" width="100%" height="100%" stylealt="webclient results"/></p>

* **Test Results**:
<p><img src="https://i.imgur.com/72YEB2F.png" width="100%" height="100%" stylealt="tests results"/></p>


## Future Ideas
* In *tests*, get `object.create()` to work so that the code efficiently runs
  * right now it makes API calls to `post` new objects
* Figure out how to connect Transaction and Payer models by Payer name rather than foreign key
* Get Django forms and Django Admin to function properly when transactions are ran. Currently, calling the API routes is the only way transaction points are applied to payers.


## Sources
* Django Docs: https://docs.djangoproject.com/en/4.0/
* Python HTTP Requests: https://docs.python-requests.org/en/latest/


## License
Licensed under the [MIT License](LICENSE).

<p align="center">© 2022 Jou Xiong</p>


Download selebium
Make sure to download chromedriver for your version of chrome
download chromedriver (I used Homebrew) and add to PATH 
can find PATH using "echo $PATH" in terminal
check chromedriver works by running "chromedriver" in terminal
if getting an Apple error for chromedriver, go to directory where chromedriver is and run "xattr -d com.apple.quarantine chromedriver"

CD into directory of project and type python3 main.py