Txt2Gist -  Gist Creator Service Workflow For Mac OS X
====================================================

A quick hook for Mac OS X to create a GitHub gist from highlighted text

### Application Files - store in ~
txt2gist.py: Creates a GitHub Gist from stdin

.gh\_access: Containes your github login and password (one per line)


### Mac OS X Automation Service Workflow - Double click to install
Txt2Gist-Private.workflow: Create a private gist

Txt2Gist-Public.workflow: Create a public gist

###Instructions:
1) Install pygithub3
```
pip install pygithub3
```

2) Copy application file to ~/

3) Install services: In Finder, double click on the workflow packages (Txt2Gist-Private and Txt2Gist-Public) and click Install

4) Use it: 

   a) Highlight text

   b) Mouse right click

   c) click on Txt2Gist-Private to create a private gist

   d) or click on Txt2Gist-Public to create a  public git

5) PROFIT
