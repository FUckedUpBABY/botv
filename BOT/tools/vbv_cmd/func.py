from .gate import *
from FUNC.defs import *

async def massvbvfunc(fullcc,bearer_token, session):
    try:
        result = await vbvcheck(fullcc,bearer_token, session)

        return f"<code>{fullcc}</code>\n<b>Result - {result[1]}</b>\n"

    except:
        import traceback
        await error_log(traceback.format_exc())
        return f"<code>{fullcc}</code>\n<b>Result - API Error 🚫</b>\n"


