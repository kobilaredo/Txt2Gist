#!/usr/bin/env python

'''
Creates a github gist from stdin
'''

from datetime import datetime
from uuid import uuid4
from pygithub3 import Github

import os
import webbrowser
import sys

# configuration
f = open('.gh_access', 'r')
gh_access = f.readlines
[
    gh_username,
    gh_password
] = [
    l.strip() for l in f.readlines()
]

#privacy
if len(sys.argv) == 2 and sys.argv[1].lower() == 'private':
    public = False
else:
    public = True

# other variables
now = datetime.now()
this_month = datetime.strftime(now, '%Y%m')
tstamp = datetime.strftime(datetime.now(), '%d%H%M%S')

filename = tstamp + '_' + str(uuid4())[-4:]


print 'Connecting to GitHub...'
gh = Github(login=gh_username,
            password=gh_password
)

print 'Creating Gist...'
gist = gh.gists.create(dict(description='Auto Uploaded Gist', public=public, 
                            files={filename: {'content': sys.stdin.read()
                                             }
                                  }
                            )
                      )

public_url = gist.html_url

print 'Gist available at:'
print '\t', public_url

print 'Copying url to clipboard...'
os.system('echo "%s" | pbcopy' % public_url)
print 'Opening in browser...'
webbrowser.open_new_tab(public_url)
