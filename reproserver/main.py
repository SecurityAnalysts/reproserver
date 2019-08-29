import logging
import tornado.ioloop

from .proxy import make_proxy
#from .web import make_app


logger = logging.getLogger(__name__)


def main():
    logging.root.handlers.clear()
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s: %(message)s")

    #app = make_app()
    #app.listen(8000, address='0.0.0.0', max_buffer_size=1_073_741_824)

    proxy = make_proxy()
    proxy.listen(8001, address='0.0.0.0')

    loop = tornado.ioloop.IOLoop.current()
    print("\n    reproserver is now running: http://localhost:8000/\n")
    loop.start()
