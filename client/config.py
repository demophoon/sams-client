"""
Configuration utilities
"""

from client.cli import parser


def cli_handler(**args):
    import pprint
    pprint.pprint(args)
    config = args.get('<config>')
    value = args.get('<value>')
    actions = {
        'print': lambda **args: conf_print(config),
        'set': lambda **args: conf_set(config, value),
        'delete': lambda **args: conf_delete(config),
    }
    parser(args, actions)
    pass


def conf_print(config):
    print "Printing %s" % config


def conf_set(config, value):
    print "Setting %s to %s" % (config, value)


def conf_delete(config):
    print "Deleting %s"
