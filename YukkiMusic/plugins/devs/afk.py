from pyrogram import Client
from pyrogram import filters
from YukkiMusic import app


afk_users = {}


@app.on_message(filters.private)
def handle_afk(client, message):
    if message.from_user:
        user_id = message.from_user.id
        if user_id in afk_users:
            # User is AFK
            client.send_message(
                chat_id=message.chat.id,
                text="Sorry, the user is currently AFK. They will respond when available."
            )


@app.on_message(filters.command("afk"))
def set_afk(client, message):
    user_id = message.from_user.id
    afk_users[user_id] = True
    client.send_message(
        chat_id=message.chat.id,
        text="You are now AFK. You will be marked as available when you send a message."
    )


@app.on_message(filters.command("unafk"))
def unset_afk(client, message):
    user_id = message.from_user.id
    if user_id in afk_users:
        del afk_users[user_id]
    client.send_message(
        chat_id=message.chat.id,
        text="Welcome back! You are no longer marked as AFK."
    )
