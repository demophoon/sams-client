"""
    Perform http checks and generate reports
"""

import urllib
import urllib2

from client.cli import parser


class Check(object):

    def __init__(self,
                 url,
                 checkType='http',
                 method='GET',
                 data=None,
                 headers=None,
                 *args, **kwargs):

        self.checkType = checkType
        self.url = url
        self.method = method
        self.data = data
        self.headers = {}
        if headers:
            self.headers = headers

    def run(self):
        req = urllib2.Request(
            self.url,
            self.data,
            self.headers,
        )
        result = {
            'state': ''
        }
        try:
            response = urllib2.urlopen(req)
        except Exception as e:
            return e
        return response


#'close'
#'code'
#'errno'
#'fileno'
#'fp'
#'getcode'
#'geturl'
#'headers'
#'info'
#'msg'
#'next'
#'read'
#'readline'
#'readlines'
#'url']

def run_check(url):
    check = Check(url)
    result = check.run()
    from pprint import pprint
    pprint({
        'code': result.code,
        'headers': result.headers.items(),
        'msg': result.msg,
        'url': result.url,
        'content': result.read(),
    })


def cli_handler(**args):
    url = args.get('<url>')
    run_check(url)
