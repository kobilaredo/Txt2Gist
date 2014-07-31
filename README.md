Txt2Gist - GitHub Gist Creator Service Workflow For Mac OS X
====

A quick hook for Mac OS X to create a GitHub gist from highlighted text

### Application Files 
txt2gist.py: Creates a GitHub Gist from stdin

.gh\_access: Containes your github login and password (one per line)


### Mac OS X Automation Service Workflow Packages
Txt2Gist-Private.workflow: Create a private gist

Txt2Gist-Public.workflow: Create a public gist

###Instructions:
- Install pygithub3
```
pip install pygithub3
```

- Copy application file to ~/

- Install services: In Finder, double click on the workflow packages (Txt2Gist-Private and Txt2Gist-Public. and click Install

- Use it: 

   1. Highlight text

   2. Mouse right click and under _Services_

   * click on **Txt2Gist-Private** to create a private gist

   * or click on **Txt2Gist-Public** to create a  public git

- PROFIT!!!
