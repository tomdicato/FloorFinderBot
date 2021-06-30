import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv(".env")

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
token = "FLOOR_BOT_TOKEN"

projects = [
    {"name": "Huas", "value": "chihuahua-gang-revenge"},
    {"name": "manzcoin-nftz", "value": "manzcoin-nftz"},
]


@slash.slash(
    name="floorfinder",
    description="Finds an OpenSea floor per project",
    guild_ids=[849034764190875669],
    options=[
        create_option(
            name="project",
            description="Choose the project",
            required=True,
            option_type=3,
            choices=[
                create_choice(name="manzcoin-nftz", value="manzcoin-nftz"),
                create_choice(name="huas", value="chihuahua-gang-revenge"),
                create_choice(
                    name="boring-bananas-company", value="boring-bananas-company"
                ),
                create_choice(name="deadheads", value="deadheads"),
            ],
        )
    ],
)
async def floor_finder(
    ctx: SlashContext,
    project: str,
):

    url = f"https://opensea.io/assets/{ project }?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.select_one(
        ".AssetsSearchView--assets .dFhPys .dFhPys:nth-child(1) .gPOBwQ .AssetCardFooter--price-amount .Price--amount"
    )

    price = price.text.strip()

    await ctx.send(f"{ project } floor is: { price }")


client.run(token)