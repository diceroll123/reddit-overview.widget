# this file doesn't need touching, unless you know what you're doing.
import json
import sys
import config

def throw_error(error):
  print(json.dumps({'error': error}))
  sys.exit(1)

PY36 = sys.version_info >= (3, 6)

if not PY36:
  throw_error('You need at least Python3.6<br>for reddit-overview.<br>You must change the command<br>path to a python3.6+ binary.')

try:
  import praw
except ModuleNotFoundError as e:
  throw_error('Please refer to the<br>requirements section in<br>the reddit-overview readme<br>to continue.')

if config.client_id == '' or config.client_secret == '':
  throw_error('Please refer to step 3 in<br>the reddit-overview setup<br>to continue.')

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent='macOS:reddit-overview widget for Übersicht:v1.0.0 (by u/diceroll123)')
VECTOR_ICON = './reddit-karma.widget/reddit.svg' # for unassigned icons

colors = {
  'reddit_orange': '#FF5700',
  'reddit_green':  '#25B79F',
}

output = {}
output['users'] = {}
output['subs'] = {}

for username in config.usernames:
  user = reddit.redditor(username)
  image = VECTOR_ICON
  background = colors['reddit_orange']
  try:
    karma = f'{user.link_karma + user.comment_karma:,}' # this line fails if the username is bad
    output['users'][username] = {}
    output['users'][username]['karma'] = karma

    if user.subreddit:
      # this means they've got an avatar!
      image = user.subreddit['icon_img']
      background = 'transparent'
    output['users'][username]['image'] = image
    output['users'][username]['key_color'] = background
  except:
    # silently ignore bad/deleted/etc usernames
    pass

for subreddit in config.subreddits:
  sub = reddit.subreddit(subreddit)
  try:
    if sub.created > 0:
      # honestly this is just to load the lazy subreddit object.
      # this would be the reason the try fails, if the subreddit is invalid.
      pass
    key_color = 'transparent'
    image = VECTOR_ICON
    background = colors['reddit_green']

    output['subs'][subreddit] = {}
    if not sub.icon_img:
      # if there's no subreddit image, then use svg icon with bgcolor
      if sub.key_color:
        background = sub.key_color
    else:
      image = sub.icon_img
      background = 'transparent'

    output['subs'][subreddit]['image'] = image
    output['subs'][subreddit]['key_color'] = background
  except:
    # silently ignore bad/private/etc subreddits
    pass

print(json.dumps(output))
