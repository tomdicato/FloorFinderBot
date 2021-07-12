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
                create_choice(
                    name="Digital Represenation of a physical cryptocurrency aka the Manzcoin NFTz",
                    value="manzcoin-nftz",
                ),
                create_choice(name="Aliens", value="thealienboy"),
                create_choice(name="BAYC", value="boredapeyachtclub"),
                create_choice(name="Blob Mob", value="blobmob"),
                create_choice(name="BoringBananas", value="boring-bananas-company"),
                create_choice(name="Bulls", value="bullsontheblock"),
                create_choice(name="Cool Cats", value="cool-cats-nft"),
                create_choice(name="Craniums", value="thewickedcraniums"),
                create_choice(name="Deadheads", value="deadheads"),
                create_choice(name="Degenz", value="degenz"),
                create_choice(name="Divine Order Of the Zodiac", value="divine-zodiac"),
                create_choice(name="Goatz", value="maisondegoat"),
                create_choice(name="Gutter Cats", value="guttercatgang"),
                create_choice(name="Hash Demons", value="hashdemons"),
                create_choice(name="Huas", value="chihuahua-gang-revenge"),
                create_choice(name="Lucky Maneki", value="luckymaneki"),
                create_choice(name="Meebits", value="meebits"),
                create_choice(name="MisfitU", value="misfit-university-official"),
                create_choice(name="Punks Comic", value="punks-comic"),
                create_choice(name="Slacker Ducks", value="slacker-duck-pond"),
                create_choice(name="Svins", value="svinsfarm"),
                create_choice(name="Theos", value="theo-nft"),
                create_choice(name="Top Dog Beach Club", value="topdogbeachclub"),
                create_choice(name="Untamed Elephants", value="untamed-elephants"),
                create_choice(name="Wizards", value="forgottenruneswizardscult")
                # 25 choices
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
