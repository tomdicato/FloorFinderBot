from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord import Client, Intents, Embed
import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
token = os.getenv("FLOOR_BOT_TOKEN")


@slash.slash(
    name="floorbot2",
    description="Finds an OpenSea floor per project",
    guild_ids=[
        #    # Dangywing Test Server
        849034764190875669,
        # ,
        #    # club-nfts
        812365773372129311,
        #    # manzcoin-nftz
        #    826820629260533790,
    ],
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
                create_choice(name="Alphabettys", value="0x6d05064fe99e40F1C3464E7310A23FFADed56E20"),
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

    for CONTRACT_ADDRESS in kwargs.values():
        await ctx.defer(hidden=False)

        # CONTRACT_ADDRESS = "0x8943c7bac1914c9a7aba750bf2b6b09fd21037e0"

        data_url = "https://api.opensea.io/api/v1/asset/" + str(CONTRACT_ADDRESS) + "/1"
        response = requests.get(data_url)
        json_data = response.json()
        collection_slug = json_data["collection"].get("slug")
        floor_price = json_data["collection"]["stats"].get("floor_price")
        embed = Embed(
            title="View on Opensea ",
            type="rich",
            url="https://opensea.io/assets/" + str(collection_slug),
        )
        embed.set_author(
            name="Floor Price: " + str(floor_price) + " ETH", url="", icon_url=""
        )
        embed.set_footer(
            text="Data provided by OpenSea",
            icon_url="https://storage.googleapis.com/opensea-static/Logomark/Logomark-Blue.png",
        )
        await ctx.send(embed=embed)


@slash.slash(
    name="stats",
    description="Finds an OpenSea floor per project",
    guild_ids=[
        #    # Dangywing Test Server
        849034764190875669
        # ,
        #    # club-nfts
        #    812365773372129311,
        #    # manzcoin-nftz
        #    826820629260533790,
    ],
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
async def floor(ctx: SlashContext, **kwargs):
    data_url = "https://api.opensea.io/api/v1/asset/" + str(CONTRACT_ADDRESS) + "/1"
    response = requests.get(data_url)
    json_data = response.json()

    # print(json_data)
    collection = json_data["collection"]
    collection_slug = collection.get("slug")
    collection_name = collection.get("name")
    stats = collection.get("stats")
    embed = Embed(
        title=str(collection_name) + " Collection (__View__)",
        type="rich",
        url="https://opensea.io/assets/" + str(collection_slug),
    )
    embed.add_field(
        name="__# of Owners__",
        value=format_int_value(stats.get("num_owners")),
        inline="true",
    )
    embed.add_field(
        name="__Total Supply__",
        value=format_int_value(stats.get("total_supply")),
        inline="true",
    )
    embed.add_field(
        name="__Total Sales__",
        value=format_int_value(stats.get("total_sales")),
        inline="true",
    )

    embed.add_field(
        name="__Floor Price__ ",
        value=format_activity_value(stats.get("floor_price")),
        inline="true",
    )
    embed.add_field(
        name="__Average Price__",
        value=format_activity_value(stats.get("average_price")),
        inline="true",
    )
    embed.add_field(
        name="__Total Volumne__",
        value=format_activity_value(stats.get("total_volume")),
        inline="true",
    )

    activity_section = get_activity_section(stats)
    embed.add_field(name="Sales Activity", value=activity_section, inline="false")
    embed.set_footer(
        text="Data provided by OpenSea",
        icon_url="https://storage.googleapis.com/opensea-static/Logomark/Logomark-Blue.png",
    )
    await ctx.send(embed=embed)


client.run(token)
