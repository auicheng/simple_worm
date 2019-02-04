ssh_worm
========

An simple auto-propagating ssh worm

## The essentials

This worm use known SSH username and password to attack local machines brutally. 
You can create a dictionary to expand username and password.

## Safeguards 
1. Only scan local network
2. Try SSH with known simple username and password
3. Target path is /tmp/, which will be cleared by Linux automatically

## Compile to executable

Use [Pyinstaller](http://www.pyinstaller.org/) to make a stand alone executable for propagating purpose.

```
./pyinstaller.py --onefile ssh_worm/worm.py 
```


