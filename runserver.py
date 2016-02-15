#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import pip

from project import app

#pip.main(['install', '-r', 'requirements.txt'])

if __name__ == '__main__':
  app.config['DEBUG'] = True	
  app.run(host='0.0.0.0')
