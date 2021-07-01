import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

load_dotenv(".env")

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
token = os.getenv("FLOOR_BOT_TOKEN")


@slash.slash(
    name="floorbot",
    description="Finds an OpenSea floor per project",
    # guild_ids=[
    #    # Dangywing Test Server
    #    849034764190875669,
    #    # Dangywing Test II
    #    859966516761067532,
    #    # club-nfts
    #    812365773372129311,
    #    # manzcoin-nftz
    #    826820629260533790,
    # ],
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
                create_choice(name="craniums", value="thewickedcraniums"),
            ],
        ),
        create_option(
            name="help",
            description="help me",
            required=False,
            option_type=3,
            choices=[
                create_choice(name="Who are you?", value="@DangyWing and @bohz"),
                create_choice(
                    name="How do projects get added to the bot?",
                    value="https://qjdhqvui1g1.typeform.com/to/r8pjwAJm",
                ),
            ],
        ),
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