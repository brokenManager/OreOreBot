from typing import Dict, Union
import discord
from src.on_message.commands.util.command_base import CommandBase
from src.on_message.commands.lol import LoL
from src.on_message.commands.role import Role
from src.on_message.commands.typo import Typo
from src.on_message.commands.hukueki import Hukueki
from src.on_message.commands.haracyo import Haracyo
from src.on_message.commands.population import Population
from src.on_message.commands.judge import Judge


class CommandsManager:
    def __init__(
            self,
            client: discord.Client,
            config: Dict[str, Dict[str, Union[str, int]]]
    ):
        """
        全てのコマンドのインスタンスをここでdict[str, command_base]としてselfに渡す
        strにはcommand.get_command_name()の返り値が入る
        """
        base_text_channel_id = config["text_channel"]["base"]
        listen_text_channel_id = config["text_channel"]["listen"]
        base_voice_channel_id = config["voice_channel"]["base"]
        afk_voice_channel_id = config["voice_channel"]["afk"]

        self.base_text_channel = client.get_channel(base_text_channel_id)
        self.listen_text_channel = client.get_channel(listen_text_channel_id)
        self.base_voice_channel = client.get_channel(base_voice_channel_id)
        self.afk_voice_channel = client.get_channel(afk_voice_channel_id)

        AC_id = config["emoji"]["AC"]
        WA_id = config["emoji"]["WA"]
        TLE_id = config["emoji"]["TLE"]
        RE_id = config["emoji"]["RE"]
        CE_id = config["emoji"]["CE"]

        AC = client.get_emoji(AC_id)
        WA = client.get_emoji(WA_id)
        TLE = client.get_emoji(TLE_id)
        RE = client.get_emoji(RE_id)
        CE = client.get_emoji(CE_id)

        self.commands = {
            LoL.COMMAND: LoL(),
            Role.COMMAND: Role(),
            Typo.COMMAND: Typo(),
            Hukueki.COMMAND: Hukueki(),
            Population.COMMAND: Population(),
            Judge.COMMAND: Judge(AC, WA, TLE, RE, CE)
        }

        self.commands[Haracyo.COMMAND] = Haracyo(
            self.commands.keys()
        )

        self.message_command = {
            "lol_count_up": self.commands[LoL.COMMAND].lol_count_up,
            "add_typo": self.commands[Typo.COMMAND].add_typo
        }

    def search_command(self, keyword: str) -> Union[CommandBase, None]:
        """
        コマンドをkeywordから検索する
        ----------
        parameters
        ----------
        keyword: str
            検索に使用する文字列
        """
        if keyword in self.commands.keys():
            return self.commands[keyword]

        return None
