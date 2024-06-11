from KatilMusic.core.bot import Hotty
from KatilMusic.core.dir import dirr
from KatilMusic.core.git import git
from KatilMusic.core.userbot import Userbot
from KatilMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "KatilMusicBot"  # connect music api key "Dont change it"
