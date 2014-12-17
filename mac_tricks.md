* Set pip install target directory

> nano ~/.pip/pip.conf

> [global]

> target=/Library/Python/2.7/site-packages

* List all listening ports

> sudo lsof -nP -iTCP:$PORT -sTCP:LISTEN
