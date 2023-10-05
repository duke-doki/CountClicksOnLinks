# Bitly URL shortener

This project checks if typed URL is already a bitly-link or not. If it is, user will see an
amount of clicks done on this link, if it is not, then user will see a shortened bitly-link variant of the typed link.

### How to install

This project uses env variable `BITLY_TOKEN`, which grants access to the service functional.
The token can be generated at https://app.bitly.com/settings/api/ after registration.
Token must be in `Bearer {token}` format. It must be stored as header in the URL request. For more information: https://dev.bitly.com/.

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).