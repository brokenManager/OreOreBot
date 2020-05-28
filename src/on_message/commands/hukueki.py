import discord
from src.on_message.commands.util.command_base import CommandBase


class Hukueki(CommandBase):
    COMMAND = "hukueki"
    COMMAND_TEMPLATE = "{{prefix}}{command} <message>".format(command=COMMAND)
    HELP = "{}\n".format(COMMAND) +\
           "「S(任意の文字列)はしてないといいね」形式の文字列を返します\n" +\
           "コマンド:{}".format(COMMAND_TEMPLATE)

    MESSAGE_TEMPLATE = \
        "```" +\
        "ねぇ、将来何してるだろうね\n" +\
        "{}はしてないと良いね" +\
        "困らないでよ{}はしてないといいね" +\
        "```"

    async def execute(self, params: discord.Message):
        messages = params.content.split(" ")
        send_message = " ".join(messages[1:]) if len(messages) >= 2 else ""
        await params.channel(Hukueki.MESSAGE_TEMPLATE.format(send_message))