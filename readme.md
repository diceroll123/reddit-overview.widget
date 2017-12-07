# reddit-overview
## reddit Overview Desktop Widget for Mac OS (Übersicht).

Keep track of user karma, and have quick-links to subreddits!

I suggest thoroughly reading this readme. This will **_not_** work out-of-the-box.

# Requirements
* Python 3.6+
* ``praw`` library (simply do `pip install praw`) *or `pip3 install praw`* in your terminal
* Basic Python knowledge

# Setup
1. Install [Übersicht](http://tracesof.net/uebersicht/)
2. Download this repo and put the .widget file in your Übersicht widget folder
3. Set up the ``client_id`` and ``client_secret`` for PRAW [(how-to)](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#script-application)
  - Get the codes from reddit as shown, then put them in config.py, respectively.
4. Change the ``usernames`` and ``subreddits`` comma-separated lists in ``config.py`` for the users and subreddits you'd like to follow, and save!

How to install widgets: [link](http://tracesof.net/uebersicht-widgets/#installation)

# Customization
- Step 4 of [Setup](#setup), rather crucial in making this your own.
- In ``index.coffee`` there's a ``settings`` object with a ``columns`` variable. Feel free to change this to your liking. 
  - *A positive integer is suggested.*

# Various FYIs
- To have a reddit avatar of your own, you'll need to enter their [beta](https://www.reddit.com/r/beta/).
  - I don't think you can leave the beta, *and if you can it's probably not easy*.
- The usernames and subreddits are all clickable if you have the ``Interaction Shortcut`` setting enabled on Übersicht.
  - *This is mostly the reason this widget has subreddits available, so this is suggested.*
- You may or may not need to change the ``command`` (first line) in ``index.coffee`` to have the direct path to your python3 location.
  - To find that, just open your terminal and put in ``which python3``.

# Screenshot
![Screenshot](https://github.com/diceroll123/reddit-overview.widget/blob/master/screenshot.png?raw=true)

# License
WTFPL
