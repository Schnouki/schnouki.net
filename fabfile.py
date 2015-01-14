from fabric.api import *
from fabric.context_managers import lcd
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer

import livereload

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'schnouki@ks:22'
dest_path = '/srv/www/schnouki.net/htdocs'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve(port=9090):
    port = int(port)
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(port))
    server.serve_forever()

def reserve(port=9090):
    build()
    serve(port)

def live(port=9090):
    clean()
    build()

    orig_dir = os.getcwd()
    os.chdir(env.deploy_path)

    def live_rebuild():
        with lcd(orig_dir):
            build()
    server = livereload.Server()
    server.watch('../content', live_rebuild)
    server.watch('../my_plugins', live_rebuild)
    server.watch('../plugins', live_rebuild)
    server.watch('../themes', live_rebuild)
    server.watch('*.css')
    server.watch('*.html')
    server.watch('*.js')
    server.serve(liveport=35729, port=int(port))

def preview():
    local('pelican -s publishconf.py')

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
