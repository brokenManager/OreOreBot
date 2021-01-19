import discord
import os

from src.on_message.root import MessageRoot
from src.config.load import load_config
from src.voice_state_update.change_voice_state import VoiceStateNotifier
from src.message_edit.edit import notify_message_edit
from src.message_delete.delete import notify_message_delete
from src.on_role_created.role import KawaemonRoleAdder


class MainClient(discord.Client):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        super().run(os.environ["TOKEN"])

    async def on_ready(self) -> None:
        if len(self.guilds) == 1:
            pass
        config = load_config()
        self.message_manager = MessageRoot(
            self,
            config
        )
        self.kawae_role_adder = KawaemonRoleAdder(
            self.get_user(config["role"]["user_id"]),
            self.get_channel(config["text_channel"]["base"])
        )
        self.voice_state_notifier = VoiceStateNotifier(self.get_channel(config["text_channel"]["base"]))

    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        await self.message_manager.anarysis_message(message)

    async def on_voice_state_update(
            self,
            member: discord.Member,
            before: discord.VoiceState,
            after: discord.VoiceState
    ) -> None:
        await self.voice_state_notifier.notify(
            member,
            before,
            after
        )

    async def on_message_edit(
            self,
            before: discord.Message,
            after: discord.Message
    ) -> None:
        await notify_message_edit(before, after)

    async def on_message_delete(self, message: discord.Message) -> None:
        await notify_message_delete(message)

    async def on_guild_role_create(self, role):
        await self.kawae_role_adder.add_role(role)