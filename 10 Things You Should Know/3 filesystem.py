"""
be able to discuss how you have used python
"""

import glob
import os

os.chdir("/Users/emili/WebstormProjects/Fundamentals JS/07.Functions - Lab")
for file in glob.glob("*.js"):
    print(file)
