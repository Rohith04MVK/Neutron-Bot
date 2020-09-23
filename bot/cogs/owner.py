from discord.ext.commands import Cog

from bot.core.bot import Bot


class Owner(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot


def setup(bot: Bot) -> None:
    bot.add_cog(Owner(bot))