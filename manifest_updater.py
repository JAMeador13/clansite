import os
os.environ['DJANGO_SETTINGS_MODULE']='clansite.settings'

import django
django.setup()

import logging, socket, sys
from get_manifest import mani_update

lock_socket = None

def is_lock_free():
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    try:
        lock_id = "jamtime.manifest_updater"
        lock_socket.bind('\0' + lock_id)
        logging.debug("Acquired lock %r" % (lock_id,))
        return True

    except socket.error:
        logging.info("Failed to acquire lock %r" % (lock_id,))
        return False

if not is_lock_free():
    print("lock not free")
    sys.exit()


try:
    mani_update()

except Exception:
    from send_sms import sendSMS
    import traceback, sys
    exc_type, exc_value, exc_traceback = sys.exc_info()
    message = ""

    for i in traceback.format_exception(exc_type, exc_value, exc_traceback):
        message += str(i)

    sendSMS(message)