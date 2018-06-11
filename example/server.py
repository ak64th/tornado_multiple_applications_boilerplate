import os

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.options import parse_config_file, parse_command_line

from example import settings
from example.router import router

define('port', default=8080, type=int)
define('process', default=0, type=int)  # one process per cpu


def parse_config():
    if os.path.exists(settings.CONFIG_PATH):
        parse_config_file(
            settings.CONFIG_PATH,
            final=False
        )
    parse_command_line()


def main():
    parse_config()
    print('')
    print('----------------------------------------------')
    print('- serve on 127.0.0.1:%s...                 -' % (options.port,))
    print('----------------------------------------------')
    print('- Conception Proof Only                      -')
    print('----------------------------------------------')
    print('')

    server = HTTPServer(router)
    server.bind(options.port)
    # Auto-reloading is enabled when DEBUG == True and it is incompatible with
    # multi-processing mode
    server.start(1 if settings.DEBUG else options.process)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
