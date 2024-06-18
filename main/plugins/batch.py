"""
Plugin for both public & private channels and groups!
"""

import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot
from main.plugins.pyroplug import get_bulk_msg
from main.plugins.helpers import get_link, screenshot, extract_message_range, batch_lock

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait
from ethon.pyfunc import video_metadata
batch = []

@Drone.on(events.NewMessage(incoming=True, pattern='/cancel'))
async def cancel(event):
    if not event.sender_id in batch:
        return await event.reply("No batch active.")
    batch.clear()
    await event.reply("Done.")

@Drone.on(events.NewMessage(incoming=True, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    async with Drone.conversation(event.chat_id) as conv:
        if not batch_lock.acquire(blocking=False):
            return await conv.send_message("Another user is batching at the same time. Please wait.")
        try:
            # Only start a new batch if none is active
            if not batch:  # Check if batch list is empty
                batch.append(event.sender_id)
                # Initiate conversation to get message links
                await conv.send_message("Send me the first message link you want to start saving from, as a reply to this message. ignore the reply as video", buttons=Button.force_reply())
                try:
                    first_link = await conv.get_reply()
                    try:
                        _first_link = get_link(first_link.text)
                    except Exception:
                        await conv.send_message("No valid first link found.")
                        return conv.cancel()
                except Exception as e:
                    print(e)
                    await conv.send_message("Cannot wait more for your response bye!")
                    return conv.cancel()
                await conv.send_message("Send me the last message link you want to save from, as a reply to this message.", buttons=Button.force_reply())
                try:
                    last_link = await conv.get_reply()
                    try:
                        _last_link = get_link(last_link.text)
                    except Exception:
                        await conv.send_message("No valid last link found.")
                        return conv.cancel()
                except Exception as e:
                    print(e)
                    await conv.send_message("Cannot wait more for your response bye!")
                    return conv.cancel()
                try:
                    message_range = await extract_message_range(_first_link, _last_link)
                except ValueError as e:
                    await conv.send_message(f"Invalid message range: {e}")
                    return conv.cancel()
                except Exception as e:
                    print(e)
                    await conv.send_message("Failed to extract message range.")
                    return conv.cancel()
                await run_batch(userbot, Bot, event.sender_id, _first_link, message_range)
            else:
                await conv.send_message("A batch is already running. Please wait or use /cancel to stop it.")
        finally:
            batch_lock.release()
            batch.clear()



async def run_batch(userbot, client, sender, link, _range):

    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try: 
            if not sender in batch:
                await client.send_message(sender, "Batch completed.")
                break
        except Exception as e:
            print(e)
            await client.send_message(sender, "Batch completed.")
            break
        try:
            await get_bulk_msg(userbot, client, sender, link, i) 
        except FloodWait as fw:
            if int(fw.x) > 299:
                await client.send_message(sender, "Cancelling batch since you have floodwait more than 5 minutes.")
                break
            await asyncio.sleep(fw.x + 5)
            await get_bulk_msg(userbot, client, sender, link, i)
        protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
        await asyncio.sleep(timer)
        await protection.delete()
            
