#!/usr/bin/python3
# coding=utf-8

import json
import sys, os, codecs, shutil
from optparse import OptionParser
from collections import OrderedDict

import data_converter
from utils import list_filter, list_map, is_app_rules


VERSION = '0.1.0'
USAGE = '%prog [options] arg0 arg1'
GITHUB_URL = 'https://github.com/RikkaApps/StorageRedirect-assets'


def main():
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
    opt_parser.add_option('--merge',
                          action='store_true', dest='merge', default=False,
                          help='merge converted configs to current ' \
                          '(latest) rules')
    opt_parser.add_option('--make-verified-list',
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

    (options, _) = opt_parser.parse_args()
    if options.convert:
        convert(options.convert)
    elif options.merge:
        merge(input=options.input, output=options.output)
    elif options.make_verified_list:
        make_verfied_list(options.make_verified_list)
        if options.merge_verified_list:
            merge_verified_list(options.make_verified_list)
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

    output_path = input + os.sep + 'output'
    if os.path.isfile(output_path):
        os.remove(output_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    print('Output to ' + output_path)

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

    with codecs.open(path + os.sep + 'verified_apps.json',
        mode='r',
        encoding='utf-8') as f:
        app_list = list_map(
            lambda item: item['package_name'],
            json.loads(f.read())
        )
        f.close()
    print('Origin data count: %d' % (len(app_list)))

    with codecs.open(path + os.sep + 'verified_apps.output.json',
        mode='r',
        encoding='utf-8') as f:
        added_count = 0
        for new_item in list_map(
            lambda item: item['package_name'],
            json.loads(f.read())):
            if not new_item in app_list:
                app_list.append(new_item)
                added_count += 1
        f.close()
    print('Added %d items from verified_apps.output.json.' \
    ' Now it will be deleted.' % (added_count))
    os.remove(path + os.sep + 'verified_apps.output.json')

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


if __name__ == '__main__':
    main()