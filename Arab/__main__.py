import sys, asyncio
import Arab
from Arab import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import iqthon
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup
LOGS = logging.getLogger("تليثون العرب")
print(Arab.__copyright__)
print("المرخصة بموجب شروط " + Arab.__license__)
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info("بدء تنزيل تليثون العرب")
    iqthon.loop.run_until_complete(setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()
class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    async def MarkAsViewed(channel_id):
        try:
            channel = await iqthon.get_entity(channel_id)
            async for message in iqthon.iter_messages(entity=channel.id, limit=4):
                await message.mark_read()

        except Exception as error:
            print (error)
    async def start_bot():
      try:
          List = ["iqthon","uruur","YZZZY","m8m8m","iqhelp1"]
          from telethon.tl.functions.channels import JoinChannelRequest
          for id in List :
              Join = await iqthon(JoinChannelRequest(channel=id))
              MarkAsRead = await MarkAsViewed(id)
          return True
      except Exception as e:
        print(e)
        return False    
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print(f"<b> ⌔︙ اهلا بك لقد نصبت تليثون ليفاي بنجاح 🥁 اذهب الى قناتنا لمعرفة المزيـد ⤵️. </b>\n CH : https://t.me/o_5_h ")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    
    Checker = await start_bot()
    if Checker == False:
        print("تم تنصيب")
    else:
        print (Checker, "تم الانضمام")
    
    return


iqthon.loop.run_until_complete(startup_process())    
if len(sys.argv) not in (1, 3, 4):
    iqthon.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        iqthon.run_until_disconnected()
    except ConnectionError:
        pass
