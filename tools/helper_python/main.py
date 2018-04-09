#!/usr/bin/python3
# coding=utf-8

import json
import sys, os, codecs, shutil
from optparse import OptionParser
from collections import OrderedDict

from github import Github, GithubObject

import data_converter
from utils import list_filter, list_map, is_app_rules, login_github, \
                  is_issue_need_discussion, list_filter_not


# Constants

# Script version
VERSION = '0.1.1'
# Script usage (help)
USAGE = '%prog [options] arg0 arg1'
# Script repo in github
GITHUB_URL = 'https://github.com/RikkaApps/StorageRedirect-assets'
# Auto rules download source (Github repo required)
ISSUE_REPO = 'RikkaApps/StorageRedirect-assets'


def main():
    # Build opt parser
    description_msg = 'Storage Redirect rules helper ' \
    '(GitHub: {0})'.format(GITHUB_URL)
    version_msg = 'Storage Redirect rules helper {0}\n' \
    'GitHub: {1}'.format(VERSION, GITHUB_URL)

    opt_parser = OptionParser(usage=USAGE,
                              description=description_msg,
                              version=version_msg)
    opt_parser.add_option('--convert',
                          metavar='ORIGIN_RULES_PATH',
                          help='convert old version configs to latest version.')
    opt_parser.add_option('-2', '--merge',
                          action='store_true', dest='merge', default=False,
                          help='merge converted configs to current ' \
                          '(latest) rules')
    opt_parser.add_option('-3', '--make-verified-list',
                          metavar='RULES_PATH',
                          help='make verified apps list from current ' \
                          'repo (Use rules path ([git repo]/rules))')
    opt_parser.add_option('-i', '--input',
                          metavar='INPUT_PATH',
                          help='configs input path ' \
                          '(--merge: Use converted configs (output) path)')
    opt_parser.add_option('-o', '--output',
                          metavar='OUTPUT',
                          help='configs output path ' \
                          '(--merge: Use target rules path ([git repo]/rules))')
    opt_parser.add_option('--merge-verified-list',
                          action='store_true',
                          dest='merge_verified_list', default=False,
                          help='merge output verified apps (when you edited' \
                          ' verified_apps.json maually, you will need this.)' \
                          ' Only use --make-verfied-list can add this arg.')
    opt_parser.add_option('-1', '--download-from-issues',
                          action='store_true', dest='download_issues',
                          default=False,
                          help='Download rules from open issues (only auto ' \
                          'rules supported currently) to a directory')
    opt_parser.add_option('-g', '--login-github',
                          metavar='\'ACCESS_TOKEN\' or \'USERNAME+PASSWD\'',
                          help='Login github by access token or password ' \
                          'when operations need request github api.')
    opt_parser.add_option('-4', '--close-issues-if-existing',
                          metavar='LOCAL_RULES_PATH',
                          help='Close rules issues if existing. Local repo ' \
                          'rules path required.')

    # Get user input and do operations
    (options, _) = opt_parser.parse_args()
    if options.convert:
        convert(options.convert)
    elif options.merge:
        merge(input=options.input, output=options.output)
    elif options.make_verified_list:
        make_verfied_list(options.make_verified_list)
        if options.merge_verified_list:
            merge_verified_list(options.make_verified_list)
    elif options.download_issues:
        if not options.login_github:
            print('Error: you need to login github with \'-g\' or ' \
            '\'--login-github\'. Use \'--help\' or read README.md ' \
            'to learn more')
        else:
            download_issues(login_github(options.login_github))
    elif options.close_issues_if_existing:
        if not options.login_github:
            print('Error: you need to login github with \'-g\' or ' \
            '\'--login-github\'. Use \'--help\' or read README.md ' \
            'to learn more')
        else:
            close_existing_rules_issues(login_github(options.login_github),
                                        options.close_issues_if_existing)
    else:
        opt_parser.print_help()


def convert(input):
    rules_path = input
    rules = list_filter(
        is_app_rules,
        list_map(
            lambda item: rules_path + os.sep + item,
            os.listdir(rules_path)
        )
    )
    print('Found rules count: %d' % (len(rules)))

    # Make output path
    output_path = input + os.sep + 'output'
    if os.path.isfile(output_path):
        os.remove(output_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    print('Output to ' + output_path)

    # Convert and write out results
    for rule in rules:
        with codecs.open(rule, mode='r', encoding='utf-8') as f:
            model = json.loads(f.read(), object_pairs_hook=OrderedDict)
            data_converter.convert_old_data(model)

            with codecs.open(
                output_path + os.sep + model['package'] + '.json',
                mode='w',
                encoding='utf-8') as out:
                out.write(json.dumps(model, indent=2, ensure_ascii=False))
                out.close()
            f.close()
    print('Finished converting.')


def merge(input, output):
    filepath_to_package_name = lambda filepath: filepath[
        filepath.rindex(os.sep) + 1 : filepath.rindex('.json')]

    # List rules
    input_rules = list_filter(
        is_app_rules,
        list_map(
            lambda item: input + os.sep + item,
            os.listdir(input)
        )
    )
    existing_packs = list_map(
        filepath_to_package_name,
        list_filter(
            is_app_rules,
            list_map(
                lambda item: output + os.sep + 'apps' + os.sep + item,
                os.listdir(output + os.sep + 'apps')
            )
        )
    )

    skipped_file = 0
    finished_file = 0
    for input_rule in input_rules:
        package_name = filepath_to_package_name(input_rule)
        # If existing this rules in output path, skip it.
        if (package_name in existing_packs):
            skipped_file += 1
        else:
            shutil.copy(input_rule, output + os.sep
             + 'apps' + os.sep + package_name + '.json')
            finished_file += 1
    print('Finished merging. Skipped %d files.' \
    ' Copied %d files.' % (skipped_file, finished_file))


def make_verfied_list(path):
    rules = list_filter(
        is_app_rules,
        list_map(
            lambda item: path + os.sep + 'apps' + os.sep + item,
            os.listdir(path + os.sep + 'apps')
        )
    )

    # Get all verified apps package name
    verified_apps = []
    for rule in rules:
        with codecs.open(rule, mode='r', encoding='utf-8') as f:
            model = json.loads(f.read())
            if 'verified' in model.keys() and model['verified']:
                verified_apps.append({
                    'package_name': model['package']
                })
            f.close()
    print('Found verified apps count: %d' % (len(verified_apps)))

    # Write to output.json
    with codecs.open(
        path + os.sep + 'verified_apps.output.json',
        mode='w',
        encoding='utf-8') as out:
        print('Output to ' + path + os.sep + 'verified_apps.output.json')
        out.write(json.dumps(verified_apps, indent=2, ensure_ascii=False))
        out.close()
        print('Finished making list.')


def merge_verified_list(path):
    app_list = []

    # Load origin data
    with codecs.open(path + os.sep + 'verified_apps.json',
        mode='r',
        encoding='utf-8') as f:
        app_list = list_map(
            lambda item: item['package_name'],
            json.loads(f.read())
        )
        f.close()
    print('Origin data count: %d' % (len(app_list)))

    # Load new verified apps
    with codecs.open(path + os.sep + 'verified_apps.output.json',
        mode='r',
        encoding='utf-8') as f:
        added_count = 0
        for new_item in list_map(
            lambda item: item['package_name'],
            json.loads(f.read())):
            # Filter out existing items
            if not new_item in app_list:
                app_list.append(new_item)
                added_count += 1
        f.close()
    print('Added %d items from verified_apps.output.json.' \
    ' Now it will be deleted.' % (added_count))
    os.remove(path + os.sep + 'verified_apps.output.json')

    # Sort and output merged data
    app_list.sort()
    with codecs.open(path + os.sep + 'verified_apps.json',
        mode='w',
        encoding='utf-8') as out:
        out.write(json.dumps(
            list_map(
                lambda package_name: {
                    'package_name': package_name
                },
                app_list
            ),
            indent=2,
            ensure_ascii=False
        ))
        out.close()
    print('Finished merge verified_apps.json')


def download_issues(github):
    repo = github.get_repo(ISSUE_REPO)

    # Get issues only created by auto wizard
    issues = list_filter(
        lambda issue: issue.title.startswith( \
            '[New rules request][AUTO]'),
        repo.get_issues(state='open').get_page(0)
    )
    issues = list_filter_not(is_issue_need_discussion, issues)

    # Make output path
    output_path = os.getcwd() + os.sep + 'output'
    if os.path.isfile(output_path):
        os.remove(output_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    print('Output to ' + output_path)

    total = len(issues)
    current = 0
    print_progress = lambda a, b: \
        print('Start downloading rules... %d/%d' % (a, b), end='')
    CODE_BLOCK = '```'

    print_progress(current, total)

    # Download json output from issues
    for issue in issues:
        current += 1

        # Get information from issue
        package_name = issue.title[issue.title.rindex(' ') + 1:]
        print(' Package: ' + package_name, end='\r')

        if (not os.path.isfile(output_path + os.sep + package_name + '.json')):
            body = repo.get_issue(issue.number).body
            content = body[body.index(CODE_BLOCK) + len(CODE_BLOCK) : 
                        body.rindex(CODE_BLOCK)]

            # Try to convert old data
            try:
                content = json.dumps(
                    data_converter.convert_old_data(
                        json.loads(content, object_pairs_hook=OrderedDict)
                    ),
                    indent=2,
                    ensure_ascii=False
                )
            except:
                pass

            # Add to cache
            with codecs.open(
                output_path + os.sep + package_name + '.json',
                mode='w', encoding='utf-8') as f:
                f.write(content)
                f.close()

        print_progress(current, total)

    # Done downloading
    print('\nDownloaded %d rules' % (current))

    print('\nFinished downloading issues. Remember to check if rules are ' \
          'vaild.')


def close_existing_rules_issues(github, rules_path):
    repo = github.get_repo(ISSUE_REPO)

    # Get issues only created by auto wizard
    issues = list_filter(
        lambda issue: issue.title.startswith( \
            '[New rules request][AUTO]'),
        repo.get_issues(state='open').get_page(0)
    )

    # Get existing rules package names
    package_name = list_map(
        lambda item: item[item.rindex(os.sep) + 1:item.rindex('.json')],
        list_filter(
            is_app_rules,
            list_map(
                lambda item: rules_path + os.sep + 'apps' + os.sep + item,
                os.listdir(rules_path + os.sep + 'apps')
            )
        )
    )

    print('Start closing issues...')
    count = 0
    for issue in issues:
        if issue.title[issue.title.rindex(' ') + 1:] in package_name:
            issue.edit(state="closed")
            count += 1
    if count == 0:
        print('No issues to close.')
    else:
        print('Closed %d issues.' % count)


if __name__ == '__main__':
    main()