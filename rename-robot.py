#!/usr/bin/env python

from __future__ import print_function

import os
import re
import argparse


def get_clean_name(name):
    name = name.lower()
    lower_name = name.replace('-', '_')
    cc_name = ''.join(x.capitalize() or '_' for x in lower_name.split('_'))

    return name, lower_name, cc_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Poppy daemon')
    parser.add_argument('name', type=str, nargs='+',
                        help='name of your robot')
    args = parser.parse_args()
    args.name = '-'.join(args.name)

    wd = os.path.dirname(os.path.realpath(__file__))
    print('Working in directory "{}"...'.format(wd))
    os.chdir(wd)

    old_name, old_lower, old_cc = get_clean_name(os.path.basename(wd))
    new_name, new_lower, new_cc = get_clean_name(os.path.basename(args.name))

    od = os.path.join('software', old_lower)
    nd = os.path.join('software', new_lower)
    print('Rename folder "{}" to "{}"'.format(od, nd))
    os.rename(od, nd)

    od = os.path.join('software', new_lower, '{}.py'.format(old_lower))
    nd = os.path.join('software', new_lower, '{}.py'.format(new_lower))
    print('Rename module "{}" to "{}"'.format(od, nd))
    os.rename(od, nd)

    od = os.path.join('software', new_lower, 'configuration', '{}.json'.format(old_lower))
    nd = os.path.join('software', new_lower, 'configuration', '{}.json'.format(new_lower))
    print('Rename module "{}" to "{}"'.format(od, nd))
    os.rename(od, nd)

    print('Finally, rename root folder from "{}" to "{}"'.format(old_name, args.name))
    os.rename(os.path.join('..', old_name),
              os.path.join('..', new_name))

    print('Start editing python modules...')

    p = os.path.join('software', new_lower, '__init__.py')
    print('Edit {}'.format(p))
    with open(p) as f:
        s = f.read()
    s = re.sub(r'{}'.format(old_lower), '{}'.format(new_lower), s)
    s = re.sub(r'{}'.format(old_cc), '{}'.format(new_cc), s)
    with open(p, 'w') as f:
        f.write(s)

    p = os.path.join('software', new_lower, '{}.py'.format(new_lower))
    print('Edit {}'.format(p))
    with open(p) as f:
        s = f.read()
    s = re.sub(r'{}'.format(old_lower), '{}'.format(new_lower), s)
    s = re.sub(r'{}'.format(old_cc), '{}'.format(new_cc), s)
    with open(p, 'w') as f:
        f.write(s)

    p = os.path.join('software', 'setup.py')
    print('Edit {}'.format(p))
    with open(p) as f:
        s = f.read()
    s = re.sub(r'{}'.format(old_name), '{}'.format(new_name), s)
    with open(p, 'w') as f:
        f.write(s)
