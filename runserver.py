# Import your application as:
# from app import application
# Example:

from app import app
import os
'''
from cherrypy import wsgiserver

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 5000), d)

if __name__ == '__main__':
   try:
      server.start()
   except KeyboardInterrupt:
      server.stop()
'''
app.run(debug=True)
