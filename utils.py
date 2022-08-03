import threading
import time
import os
import logging
from scipy.spatial.distance import euclidean
#import numpy as np
#from CribotMC import BlockTypes


log = logging.getLogger(__name__)


def start_afk_thread(bot):
    def do_afk_thread(bot, pid):
        i = 0
        while True:
            if time.time() - bot.last_keepalive > 20:
                print 'Server disconnected. Exiting'
                os.kill(pid, 0)
                break
            bot.send(bot.proto.PlayServerboundHeldItemChange.id,
                     slot=i
                     )
            i = (i + 1) % 8
            time.sleep(55)

    pid = os.getppid()
    thread = threading.Thread(target=do_afk_thread, name='afk', args=(bot, pid))
    thread.daemon = True
    thread.start()
    return thread


def start_shear_thread(bot):
    def do_shear_thread(bot, pid):
        #shears_id = BlockTypes.get_id('Shears')
        while True:
            for entity in bot.player.iter_entities_in_range('Sheep'):
                is_sheared = entity.metadata.get(16, (0, 0))[1] >= 16
                is_child = entity.metadata.get(12, (0, 0))[1] < 0
                #holding_shears = bot.player.held_item.item_id == shears_id
                if not is_child and not is_sheared:
                    log.debug("Entity metadata: %s", str(entity.metadata))
                    log.info("Sending UseEntity for eid: [%d]", entity.eid)
                    bot.send(bot.proto.PlayServerboundUseEntity.id,
                             target=entity.eid,
                             type=0
                             )
            time.sleep(1)

    time.sleep(5)
    pid = os.getppid()
    thread = threading.Thread(target=do_shear_thread, name='afk', args=(bot, pid))
    thread.daemon = True
    thread.start()
    return thread


def start_chat_interface(bot):
    message = ''
    while message not in ['exit', 'quit']:
        message = raw_input('> ').strip()
        if message not in ['exit', 'quit']:
            bot.send(bot.proto.PlayServerboundChatMessage.id,
                     chat=message
                     )


def start_cmd_interface(bot, handlers):
    cmd = ''
    while cmd not in ['exit', 'quit']:
        args = raw_input('> ').strip().split()
        if not args:
            continue
        if args[0] in handlers:
            handlers[args[0]](bot, *args[1:])
