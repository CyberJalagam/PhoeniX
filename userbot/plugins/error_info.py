# Exclusive for PhoeniX Userbot.
# By @Techy05 (DON'T REMOVE THESE LINES)
## Don't modify this module

from sql.global_variables_sql import SYNTAX, MODULE_LIST, ERROR, ERRORS

MODULE_LIST.append("errors")
SYNTAX.update({
    "errors": "\
**Getting errors/problems while using PhoeniX? Or a module isn't working?**\
\nDon't worry, Let's fix them\
\n\n• `.errors`\
\nUsage: __Shows the list of known errors in Userbots__\
\n\n• `.error <error_name>`\
\nUsage: __Shows the solution for the requested error/problem__\
"
})

ERRORS.append("updater not working")
ERROR.update({
    "updater not working": "\
**So, you're having problems with updater. PhoeniX Service will fix it.**\
\n\nERROR: `Unfortunately, the directory /app does not seem to be a git repository.`\
\nSolution: __Use “.update now” and check again if it works.__\
\n__If it still doesn't work, then use “.chl” once.\
\n\nERROR: `[UPDATER]: Looks like you are using your own custom branch (master). in that case, Updater is unable to identify which branch is to be merged. please checkout to any official branch`\
\nSolution: __Delete PhoeniX repo from your account. Refork__ [PhoeniX](https://github.com/Techy05/PhoeniX). __Then Manual Deploy from Heroku to fix__\
\nIf you use custom fork, then please don't mess with branches.\
"
})
