import json
import requests

from tasks.services import set_contact_payload
from celery.utils.log import get_task_logger
from tasks import celery

logger = get_task_logger(__name__)


@celery.task
def create_contact():
    """
    Task creating a random contact.
    :return:
    """
    logger.info('-- Task create contact launched --')


@celery.task
def delete_contacts():
    """
    Task deleting contacts.
    :return:
    """
    logger.info('-- Task delete contact launched --')
