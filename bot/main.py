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
                create_choice(name="BAYC", value="boredapeyachtclub"),
                create_choice(name="BoringBananas", value="boring-bananas-company"),
                create_choice(name="bulls", value="bullsontheblock"),
                create_choice(name="craniums", value="thewickedcraniums"),
                create_choice(name="deadheads", value="deadheads"),
                create_choice(name="Gutter Cats", value="guttercatgang"),
                create_choice(name="huas", value="chihuahua-gang-revenge"),
                create_choice(name="luckymaneki", value="luckymaneki"),
                create_choice(name="misfitU", value="misfit-university-official"),
                create_choice(name="Slacker Ducks", value="slacker-duck-pond"),
                create_choice(name="svins", value="svinsfarm"),
                create_choice(name="Theos", value="theo-nft"),
                create_choice(name="Wizards", value="forgottenruneswizardscult")
                # Up to 14 choices
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