# SecureJournal
A Python library for encrypting a journal

To get started, clone the repo using `git clone`  or otherwise. 

There are a couple of meta-dependencies.

`python` is one of those, `^3.8.5` is recommended. 

`pip` is the second meta-dependency.

On Ubuntu (Focal Fossa):

`sudo apt-get install python3 python3-pip`

Now using pip:


`pip install -r requirements.txt` 

That _should_ do it. 

To get started with a new or existing journal, run:

`python script.py`

When you are ready to encrypt your journal, again run:

`python script.py`

And the script figures out the rest.

If you forget your decryption password and need to restart, run:

`rm -f encrypted && touch plaintext && python script.py`

Your encrypted backups will be kept in the `backup` directory in case you need them.

Side Notes
= 

This is a hobby project. 

It is not guaranteed to be invulnerable to attacks executed by sophisticated actors.

This program is intended for use on Ubuntu or Mac OS. 

If you want it to work on Windows, WSL2 is recommended.
