#!/usr/bin/env python3

import inspect
import importlib
import os
import pkg_resources
import sys
import glob

for dirs in glob.glob('/snap/charm/current/lib/python3*/site-packages'):
    if os.path.isdir(dirs):
        sys.path.append(dirs)

from charmtools import create
from charmtools.generators import CharmGenerator

templates = []
base_path = os.path.dirname(os.path.realpath(__file__))

# Subfolders are considered templates
for root, dirs, files in os.walk(base_path):
    for d in dirs:
        if d.startswith('.'):
            continue
        templates.append(d)
    break

# Add templates to charmtools entry point
for template in templates:
    print("Added custom template: {}".format(template))
    template_path = os.path.join(base_path, template)
    try:
        tplt = importlib.import_module(template)
    except ImportError:
        continue
    for name, obj in inspect.getmembers(tplt):
        if inspect.isclass(obj):
            class_name = name
            break
    distribution = pkg_resources.Distribution(template_path)
    entry_point = pkg_resources.EntryPoint.parse('{} = {}:{}'.format(template,
                                                                     'template',
                                                                     class_name),
                                                 dist=distribution)
    distribution._ep_map = {'charmtools.templates': {template: entry_point}}
    pkg_resources.working_set.add(distribution)


# Home should mean home
def _get_output_path(self):
    if self.opts.charmhome == '.':
        return os.path.join(self.opts.charmhome, self.opts.charmname)
    else:
        return os.path.join(self.opts.charmhome)


CharmGenerator._get_output_path = _get_output_path

# Call charmtools with our new templates available
create.main()
