# PhoeniX UserBot
### All thanks to Raphielgang/Paperplane, UniBorg, X-Tra-Telegram and Hardcore UserBots; which helped me to make PhoeniX UserBot.
## Documentation/Guide, visit [How2Techy](https://how2techy.com/x-tra-userbot-plugin-guide-part1/)
# Installing
Join https://t.me/XtraTgBot for updates and tuts
### The Recommended Way

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


You must have a Heroku Account for this.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Check [Line 111](https://github.com/Total-Noob-69/X-tra-Telegram/blob/master/userbot/uniborgConfig.py#L111) and start adding your vars there.
Fortunately there are no Mandatory vars for the UniBorg Support Config.

