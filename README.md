# ThreadTP
A simple multithreaded CLI FTP client. ThreadTP will spawn a number of processes (configured in the config file) and upload the file queue concurrently.

This is a very early version so comments and suggestions are welcomed.

## Requirements
The only current requirements is PyYAML.

    pip install -r requirements.txt

## Use
ThreadTP is very simple to use. Once the CONFIG.yml (CONFIG.json coming soon) is ready you just run:

    python app.py
    or
    ./app.py

ThreadTP will look for it's config file in it's local folder.
Input argument to specify config file location is in the works.

## TODOs
* Put config class in separate file.
* Put main functionality into a ThreadTP module.
* Implement argsparse.
* Allow location of config file to be supplied by user.
* Implement logging correctly.
* Implement JSON parsing for the config class.
* General beautify code.

