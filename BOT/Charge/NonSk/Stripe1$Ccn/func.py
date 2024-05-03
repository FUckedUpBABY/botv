from .response import *
from .gate import *
from FUNC.defs import *

async def mass_charge_func(fullz , proxy , data , user_id):
    try:
        result = await create_cvv_charge(fullz , data , proxy)
        getresp = await uhq_charge_resp(result, user_id, fullz)

        return f"<code>{fullz}</code>\n<b>Result - {getresp[1]}</b>\n"

    except:
        import traceback
        await error_log(traceback.format_exc())
        return f"<code>{fullz}</code>\n<b>Result - Card Declined 🚫</b>\n"


