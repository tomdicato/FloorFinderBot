from discord.ext import commands
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
    #    849034764190875669
    # ,
    #    # club-nfts
    #    812365773372129311,
    #    # manzcoin-nftz
    #    826820629260533790,
    # ],
    options=[
        create_option(
            name="projects-a-h",
            description="Projects starting with A-H",
            required=False,
            option_type=3,
            choices=[
                create_choice(
                    name="Digital Represenation of a physical cryptocurrency aka the Manzcoin NFTz",
                    value="manzcoin-nftz",
                ),
                create_choice(name="Aliens", value="thealienboy"),
                create_choice(name="Alphabettys", value="alphabetty-doodles"),
                create_choice(name="Animetas", value="animetas"),
                create_choice(name="Animonkeys", value="animonkeys"),
                create_choice(name="Avastar", value="avastar"),
                create_choice(name="BAYC", value="boredapeyachtclub"),
                create_choice(name="Bears On The Block", value="bearsontheblock"),
                # create_choice(name="Blob Mob", value="blobmob"),
                # create_choice(name="BoringBananas1", value="boring-bananas-company"),
                create_choice(name="Bulls", value="bullsontheblock"),
                create_choice(name="Chickens", value="chicken-derby"),
                create_choice(name="Cool Cats", value="cool-cats-nft"),
                create_choice(name="Craniums", value="thewickedcraniums"),
                create_choice(name="Deadheads", value="deadheads"),
                create_choice(name="Elephants", value="untamed-elephants"),
                create_choice(name="Flufs", value="fluf-world"),
                create_choice(name="FVCK_CRYSTALS", value="fvck-crystal"),
                create_choice(name="Ethlings", value="ethlings"),
                create_choice(name="Fame Lady Squad", value="fameladysquad"),
                create_choice(name="Goblin Goons", value="goblin-goons"),
                create_choice(name="Goatz", value="maisondegoat"),
                create_choice(name="Gutter Cats", value="guttercatgang"),
                create_choice(name="Huas", value="chihuahua-gang-revenge"),
            ],
        ),
        create_option(
            name="projects-l-z",
            description="Projects starting with L-Z",
            required=False,
            option_type=3,
            choices=[
                create_choice(name="Lazy Lions", value="lazy-lions"),
                create_choice(name="Lucky Maneki", value="luckymaneki"),
                create_choice(name="Meebits", value="meebits"),
                create_choice(name="Meebits", value="meebits"),
                create_choice(name="Moon Dogs", value="moondogs-odyssey"),
                create_choice(name="Pudgy Penguins", value="pudgypenguins"),
                create_choice(name="Punks Comic", value="punks-comic"),
                create_choice(name="Purrlinis", value="purrnelopes-country-club"),
                create_choice(name="Rabbits", value="rabbit-college-club"),
                create_choice(name="Robotos", value="robotos-official"),
                create_choice(
                    name="Royal Society of Players (RSOP)",
                    value="royalsocietyofplayers",
                ),
                create_choice(name="Shibas", value="dope-shibas"),
                create_choice(name="Slacker Ducks", value="slacker-duck-pond"),
                create_choice(name="Space Poggers", value="spacepoggers"),
                create_choice(
                    name="SSS - Star Sailor Siblings", value="starsailorsiblings"
                ),
                create_choice(name="Stoner Cats", value="stoner-cats-official"),
                create_choice(name="Strippers", value="stripperville-nfts"),
                create_choice(name="Theos", value="theo-nft"),
                create_choice(name="Top Dog Beach Club", value="topdogbeachclub"),
                create_choice(name="Vogu", value="vogu"),
                create_choice(name="Vox", value="collectvox"),
                create_choice(name="Wizards", value="forgottenruneswizardscult"),
                create_choice(name="World of Women", value="world-of-women-nft"),
                create_choice(name="Zunks", value="zunks"),
            ],
        ),
    ],
)
async def floor_finder(ctx: SlashContext, **kwargs):

    for project in kwargs.values():
        await ctx.defer(hidden=False)

        url = f"https://opensea.io/assets/{ project }?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW"

        try:
            page = requests.get(url)

            soup = BeautifulSoup(page.content, "html.parser")

            price = soup.select_one(".Price--amount")

            price = price.text.strip()

        except:
            print(f"Error getting price for { url }")

        else:

            await ctx.send(f"{ project } floor is: { price }")


client.run(token)