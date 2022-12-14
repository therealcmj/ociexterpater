#!/usr/bin/env python3

import importlib
import oci
import logging

__requires__ = 'oci==2.78.0'

if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(levelname)7s %(module)s:%(funcName)s -> %(message)s', level=logging.INFO)
    logging.info("Starting up")

    from ociexterpater.config import config
    cfg = config()

    # at this point we should have a signer and some other stuff in the cfg object

    clients = cfg.categories_to_delete

    for client in clients:
        logging.debug( "Importing {}".format(client))
        my_module = importlib.import_module("ociexterpater.ociclients.%s" % client)
        logging.debug( "Module name: {}".format( my_module.__name__ ))

        logging.debug( "Getting {}".format( client ) )
        cls = getattr( importlib.import_module("ociexterpater.ociclients.%s" % client), client )
        logging.debug( "Name for {} is {}".format( client, cls.service_name ) )

        logging.debug( "Instantiating" )
        o = cls( cfg )
        logging.debug("Instantiated OK")

        o.findAndDeleteAllInCompartment()
