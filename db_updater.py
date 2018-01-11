import os
os.environ['DJANGO_SETTINGS_MODULE']='clansite.settings'

import django
django.setup()

import logging, socket, sys
import database_updaters
import clan.models as mods

lock_socket = None

def is_lock_free():
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    try:
        lock_id = "jamtime.db_updater"
        lock_socket.bind('\0' + lock_id)
        logging.debug("Acquired lock %r" % (lock_id,))
        return True

    except socket.error:
        logging.info("Failed to acquire lock %r" % (lock_id,))
        return False

if not is_lock_free():
    print("lock not free")
    sys.exit()


if mods.UpdateIndex.objects.filter(pk=1).exists():
    print("Retrieving index...", end=" ")
    update_index = mods.UpdateIndex.objects.get(pk=1)
    print("done!")
else:
    print("Creating index...", end=" ")
    update_index = mods.UpdateIndex.objects.create(weapons=True)
    print("done!")

print(update_index)


def update_db():
    if update_index.activities:
        database_updaters.pgcr_updater()
        update_index.activities = False
        update_index.pgcrs = True
        update_index.save()

    elif update_index.pgcrs:
        database_updaters.team_updater()
        update_index.pgcrs = False
        update_index.teams = True
        update_index.save()

    elif update_index.teams:
        database_updaters.participant_updater()
        update_index.teams = False
        update_index.participants = True
        update_index.save()

    elif update_index.participants:
        database_updaters.weapon_updater()
        update_index.participants = False
        update_index.weapons = True
        update_index.save()

    elif update_index.weapons:
        database_updaters.activity_updater()
        update_index.weapons = False
        update_index.activities = True
        update_index.save()


try:
    update_db()

except Exception:
    from send_sms import sendSMS
    import traceback, sys
    exc_type, exc_value, exc_traceback = sys.exc_info()
    message = ""

    for i in traceback.format_exception(exc_type, exc_value, exc_traceback):
        message += str(i)

    sendSMS(message)

