import logging

from pyfcm import FCMNotification
from pyfcm.errors import AuthenticationError

from notification import settings
from notification.services import get_devices

logger = logging.getLogger(__file__)


def fcm_send_bulk_message(  # noqa WPS211
    registration_ids,
    title=None,
    body=None,
    icon=None,
    data=None,
    sound=None,
    badge=None,
    low_priority=False,
    condition=None,
    time_to_live=None,
    click_action=None,
    collapse_key=None,
    delay_while_idle=False,
    restricted_package_name=None,
    dry_run=False,
    color=None,
    tag=None,
    body_loc_key=None,
    body_loc_args=None,
    title_loc_key=None,
    title_loc_args=None,
    content_available=None,
    extra_kwargs={},
    api_key=None,
    json_encoder=None,
    extra_notification_kwargs=None,
    **kwargs,
):
    
    """
    Copied from https://github.com/olucurious/PyFCM/blob/master/pyfcm/fcm.py:
    """

    if api_key is None:
        api_key = settings.FCM_SERVER_KEY
    push_service = FCMNotification(api_key=api_key, json_encoder=json_encoder)

    return push_service.notify_multiple_devices(
        registration_ids=registration_ids,
        message_title=title,
        message_body=body,
        message_icon=icon,
        data_message=data,
        sound=sound,
        badge=badge,
        collapse_key=collapse_key,
        low_priority=low_priority,
        condition=condition,
        time_to_live=time_to_live,
        click_action=click_action,
        delay_while_idle=delay_while_idle,
        restricted_package_name=restricted_package_name,
        dry_run=dry_run,
        color=color,
        tag=tag,
        body_loc_key=body_loc_key,
        body_loc_args=body_loc_args,
        title_loc_key=title_loc_key,
        title_loc_args=title_loc_args,
        content_available=content_available,
        extra_kwargs=extra_kwargs,
        extra_notification_kwargs=extra_notification_kwargs,
        **kwargs,
    )


async def send_push(conn, user_ids, **kwargs):
    logger.debug(kwargs)
    devices = await get_devices(conn, user_ids)
    registration_ids = [device.registration_id for device in devices]
    try:
        fcm_send_bulk_message(
            registration_ids,
            title=kwargs.pop('title', None),
            body=kwargs.pop('body', None),
            data=kwargs,
        )
    except AuthenticationError:
        logging.error('FCM AuthenticationError')


async def send_push_new_message(
    conn,
    user_ids,
    is_notification=True,
    is_message=True,
    title=None,
    body=None,
    **kwargs,
):
    if is_notification:
        await send_push(conn, user_ids, title=title, body=body, **kwargs)
    if is_message:
        kwargs['data'] = {'title': title, 'body': body}
        await send_push(conn, user_ids, **kwargs)
