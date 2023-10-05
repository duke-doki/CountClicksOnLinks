# Bitly URL shortener

This project checks if typed URL is already a bitly-link or not. If it is, user will see an
amount of clicks done on this link, if it is not, then user will see a shortened bitly-link variant of the typed link.

### How to install

This project uses env variable `BITLY_TOKEN`, which grants access to the service functional. So,
it needs to be defined in `.env` file. The content of `.env` file looks like this:
```
BITLY_TOKEN={your token}
```

The token can be generated at https://app.bitly.com/settings/api/ after registration.
It must be stored as header in the URL request. For more information: https://dev.bitly.com/.


Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to run

The following must be typed in the terminal:
```
python3 main.py {your link}
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).