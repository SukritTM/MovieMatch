# MovieMatch
## Run Instructions
These instructions assume you have a working installation of python 3.9 which is added to PATH on a machine running Windows 10.

Fork this repository, then clone it to your local machine.

Although it is not required, it is reccommended to start a python virtual environment in which to install your dependencies. To do so, navigate to the root folder of this repository with `cd moviematch`, and type

`python -m venv <your-env-name>`

Replace `<your-env-name>` with a name of your choice (I recommend something like `.venv`)
To activate your virtual environment, from the root folder, type

`<your-env-name>\scripts\activate.bat`

From this point forward, all commands are to be run from within the virtual environment

Now, we can install our dependencies. To do so, type 
`python -m pip install -r requirements.txt`

Once the dependencies have been installed, we can run the app. To do so, first run

`set FLASK_APP=src`

And then,

`flask run --port=80`

Now open a browser. In the address bar, type `http://localhost`. Enjoy! 😃

**Important:** Currently, the project does not run on chrome canary. Please use a different browser

*Note:* If you have any other service running on port 80, you will have to either stop it, or run this application on a different port. To do so, type `flask run --port=<port>`

Replace `<port>` with a port number of your choice. In the browser, visit `http://localhost:<port>`
