# RT 5/6/13 from
#http://lists.osgeo.org/pipermail/tilecache/2010-January/002248.html
#in apache2 site file
#  WSGIScriptAlias /tilecache /var/www/tilecache/tilecache-2.11/tilecache.wsgi

import os, sys
tilecachepath, wsgi_file = os.path.split(__file__)
if not tilecachepath in sys.path:
    sys.path.append(tilecachepath)

from TileCache.Service import Service, wsgiHandler

cfgfiles = (os.path.join(tilecachepath, "tilecache.cfg"))

theService = {}
def wsgiApp (environ, start_response):
    global theService

    cfgs  = cfgfiles
    if not theService:
        theService = Service.load(cfgs)
    return wsgiHandler(environ, start_response, theService)

application = wsgiApp
