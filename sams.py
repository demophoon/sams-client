""" Sams Client

Usage:
    sams config (set|delete|print) <config> [<value>]
    sams check <url>
    sams register
    sams (-h | --help)
    sams --version

Options:
    -h --help           Show this help screen.
    --version           Display client version.
    --noop              Test the action before actually running.
"""

from docopt import docopt

import client


def main():
    args = docopt(__doc__, version=client.full_version_string)
    actions = {
        #'config': client.config.cli_handler,
        #'register': client.register.register,
        'check': client.check.cli_handler,
    }
    client.cli.parser(args, actions)

if __name__ == '__main__':
    main()
