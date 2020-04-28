from notification.db import device


async def get_devices(conn, user_ids):
    device_records = await conn.execute(
        device.select().
        where(device.c.user_id.in_(user_ids)).
        where(device.c.active == True),
    )
    return await device_records.fetchall()
