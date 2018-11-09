# -*- coding: utf-8 -*-

from plone import api
from plone.api.content import get_uuid

import logging
import transaction

logger = logging.getLogger(__name__)


def fix_internal_link_field(context):
    """ Parte della migrazione collective.smartlink to version 1100.
    Serve per togliere il contenuto del campo 'internal_link' e metterlo
    nel campo standard 'remoteUrl'.

    Si spazzola tutti i link del sito e li corregge.
    """
    logger.info('Fixing the internal_link field for all the Link objects.')

    site = api.portal.get()
    print u"Getting all the Link objects in the site..."
    link_brains = site.portal_catalog.unrestrictedSearchResults(
        portal_type=["Link"],
    )

    objects_changed = 0

    for brain in link_brains:
        link_obj = brain.getObject()
        # Facciamo un controllo che dovrebbe essere inutile ma stiamo dalla
        # parte dei bottoni. Se un oggetto ha un link interno NON può avere
        # anche un link esterno.
        if link_obj.internal_link and not link_obj.remoteUrl:
            logger.info('---\nLink: {}\n'.format(link_obj.absolute_url_path()))

            linked_obj = link_obj.internal_link.to_object
            uuid = get_uuid(linked_obj)
            link_obj.remoteUrl = u'${}/resolveuid/{}'.format(
                '{portal_url}',
                uuid,
            )
            link_obj.internal_link = None

            objects_changed += 1
            if objects_changed > 10:
                try:
                    print "Partial Commit..."
                    transaction.commit()
                    print "Partial Commit: OK"
                except Exception as e:
                    logger.error(
                        u"Error while committing transaction.")
                    logger.error(u"{}".format(e))
                objects_changed = 0

    transaction.commit()
