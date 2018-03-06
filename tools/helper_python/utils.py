# coding=utf-8

import os
from github import Github

def list_map(f, source):
    return list(map(f, source))

def list_filter(f, source):
    return list(filter(f, source))

def is_app_rules(abs_path):
    return os.path.isfile(abs_path) and abs_path.endswith('.json')

def login_github(arg):
    if '+' in arg:
        username = arg[:arg.index('+')]
        passwd = arg[arg.index('+') + 1:]
        return Github(username, passwd)
    else:
        return Github(arg)