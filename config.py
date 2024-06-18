import os

"""
note : 
use the session string of same account as api_id, api_hash and owner id 
session can be generated with this file https://github.com/ShivangKakkar/StringSessionBot
also dont get logout from the session from your devices list in settings.
and try using alt account as it can join to random groups which you dont even know 
"""
#your bot token
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7141065732:AAGneHDd2_Su3B_T2JBXI4hmsMoFTzbJ_GQ")
#api id
API_ID = int(os.environ.get("API_ID", "22751770"))
#api hash
API_HASH = os.environ.get("API_HASH", "e6ba9518e2539301417c419540acb2e4")
#owner id
OWNER_ID = int(os.environ.get("OWNER_ID", "6130617844"))
#session string
SESSION = os.environ.get("SESSION", "BQFbKhoAw033W1FmE6wyEAqG_U0y4vTB7opMjcppwDGPkjk16yRvI-nFwcIIecOvQ0zH3wRYv2XWiFK-xYuI2zGmoN1VTaBciPuqqeW7o2Z31mriC_VgnjqC7TafVeBKdc-SixW12U7aiLmpW5vTF9oyqgmGjMK7DtGxUX499nO2letQyT69EqYgH4ABdGNBIuP-3W7IvB974BchQKTN1iJ7Z9L5ofv21HjRJFHa_wHwh0izNgJ5oMYAKQ-Fz3SR93aJ2ZbU7jtBtSy_IWzypxTnr1b1QHuSgYAbqktgIcStatTsYgzu2oGP3JOVu2mhkWKUPo6yB1hFIayjtrkVbEHcRfgWDAAAAAFtac30AA")
#for efficiency of bot don't touch it
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
#owner tag
OWNER_TAG = os.environ.get("OWNER_TAG", "askluhfiau")