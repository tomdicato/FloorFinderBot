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

def get_activity_section(stats):
     output = "```Range         Volume           Change          Average  \n"
     output = output + "1D".ljust(5, " ") + format_activity_value(stats.get("one_day_volume")) + format_activity_value(stats.get("one_day_change")) + format_activity_value(stats.get("one_day_average_price"))  +"\n"
     output = output + "7D".ljust(5, " ") + format_activity_value(stats.get("seven_day_volume"))  + format_activity_value(stats.get("seven_day_change"))   + format_activity_value(stats.get("seven_day_average_price"))  +"\n"
     output = output + "30D".ljust(5, " ") + format_activity_value(stats.get("thirty_day_volume"))  + format_activity_value(stats.get("thirty_day_change"))  + format_activity_value(stats.get("thirty_day_average_price"))  +"\n"
     output = output + "Total" + format_activity_value(stats.get("total_volume"))  + format_activity_value("") + format_activity_value(stats.get("average_price")) + "```"
     return output

def format_activity_value(value, currency="", padding=17):
    formatted_value="0.0"
    if isinstance(value, float):
      formatted_value = str(round(value, 2))
    else:
        formatted_value = str(value)

    if currency == "DAI":
      formatted_value = formatted_value + " "
    elif currency == "USDC":
      formatted_value = formatted_value + " "
    elif formatted_value != "":
      formatted_value = formatted_value + " ⧫"      
    formatted_value = formatted_value.rjust(padding, " ") 
    
    return formatted_value

def format_int_value(value, padding=17):
    formatted_value="0.0"
    formatted_value = str(int(value)).rjust(padding, " ") 
    return formatted_value


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
        # club-ngmi
        888513307147927612
    ],
    options=[
        create_option(
            name="projects-a-h",
            description="Projects starting with A-H",
            required=False,
            option_type=3,
            choices=[
                create_choice(name="Digital Represenation of a physical cryptocurrency aka the Manzcoin NFTz", value = '0x495f947276749Ce646f68AC8c248420045cb7b5e'),
create_choice(name="Aliens", value = '0x4581649aF66BCCAeE81eebaE3DDc0511FE4C5312'),
create_choice(name="Alphabettys", value = '0x6d05064fe99e40F1C3464E7310A23FFADed56E20'),
create_choice(name="Animetas", value = '0x18Df6C571F6fE9283B87f910E41dc5c8b77b7da5'),
create_choice(name="Animonkeys", value = '0xA32422dfb5bF85B2084EF299992903eb93FF52B0'),
create_choice(name="Avastar", value = '0xF3E778F839934fC819cFA1040AabaCeCBA01e049'),
create_choice(name="BAYC", value = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'),
create_choice(name="Bears On The Block", value = '0x02AA731631c6D7F8241d74F906f5b51724Ab98F8'),
create_choice(name="Bulls", value = '0x3a8778A58993bA4B941f85684D74750043A4bB5f'),
create_choice(name="Chickens", value = '0x8634666bA15AdA4bbC83B9DbF285F73D9e46e4C2'),
create_choice(name="Cool Cats", value = '0x1A92f7381B9F03921564a437210bB9396471050C'),
create_choice(name="Craniums", value = '0x85f740958906b317de6ed79663012859067E745B'),
create_choice(name="Deadheads", value = '0x6fC355D4e0EE44b292E50878F49798ff755A5bbC'),
create_choice(name="Elephants", value = '0x613E5136a22206837D12eF7A85f7de2825De1334'),
create_choice(name="Flufs", value = '0xCcc441ac31f02cD96C153DB6fd5Fe0a2F4e6A68d'),
create_choice(name="FVCK_CRYSTALS", value = '0x7AfEdA4c714e1C0A2a1248332c100924506aC8e6'),
create_choice(name="Ethlings", value = '0x8A1AbD2E227Db543F4228045dd0aCF658601fedE'),
create_choice(name="Fame Lady Squad", value = '0xf3E6DbBE461C6fa492CeA7Cb1f5C5eA660EB1B47'),
create_choice(name="Goblin Goons", value = '0x6322834FE489003512A61662044BcFb5Eeb2A035'),
create_choice(name="Goatz", value = '0x3EAcf2D8ce91b35c048C6Ac6Ec36341aaE002FB9'),
create_choice(name="Gutter Cats", value = '0xEdB61f74B0d09B2558F1eeb79B247c1F363Ae452'),
create_choice(name="Huas", value = '0x495f947276749Ce646f68AC8c248420045cb7b5e'),
create_choice(name="Lazy Lions", value = '0x8943C7bAC1914C9A7ABa750Bf2B6B09Fd21037E0'),
create_choice(name="Lucky Maneki", value = '0x14f03368B43E3a3D27d45F84FabD61Cc07EA5da3'),

            ],
        ),
        create_option(
            name="projects-l-z",
            description="Projects starting with L-Z",
            required=False,
            option_type=3,
            choices=[
                create_choice(name="Meebits", value = '0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7'),
create_choice(name="Moon Dogs", value = '0xfc007068C862E69213Dc7AA817063B1803D4E941'),
create_choice(name="Pudgy Penguins", value = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'),
create_choice(name="Punks Comic", value = '0x5ab21Ec0bfa0B29545230395e3Adaca7d552C948'),
create_choice(name="Purrlinis", value = '0x9759226B2F8ddEFF81583e244Ef3bd13AAA7e4A1'),
create_choice(name="Rabbits", value = '0x91F3114F8818ADe506d0901a44982Dc5c020C99B'),
create_choice(name="Robotos", value = '0x099689220846644F87D1137665CDED7BF3422747'),
create_choice(name="Royal Society of Players (RSOP)", value = '0xB159F1a0920A7f1D336397A52D92da94b1279838'),
create_choice(name="Shibas", value = '0x763864F1A74D748015f45F7c1181B60E62E40804'),
create_choice(name="Slacker Ducks", value = '0xeC516eFECd8276Efc608EcD958a4eAB8618c61e8'),
create_choice(name="Space Poggers", value = '0x4a8B01E437C65FA8612e8b699266c0e0a98FF65c'),
create_choice(name="SSS - Star Sailor Siblings", value = '0x49aC61f2202f6A2f108D59E77535337Ea41F6540'),
create_choice(name="Stoner Cats", value = '0xD4d871419714B778eBec2E22C7c53572b573706e'),
create_choice(name="Strippers", value = '0x9808226ED04e92F9380DA67C5606354FAe5891b0'),
create_choice(name="Theos", value = '0x9E02FFd6643f51aaAFa0f0E2a911Bf25EF2684Cb'),
create_choice(name="Top Dog Beach Club", value = '0x6F0365ca2c1Dd63473F898A60f878A07e0f68A26'),
create_choice(name="Vogu", value = '0x18c7766A10df15Df8c971f6e8c1D2bbA7c7A410b'),
create_choice(name="Vox", value = '0xad9Fd7cB4fC7A0fBCE08d64068f60CbDE22Ed34C'),
create_choice(name="Wizards", value = '0x521f9C7505005CFA19A8E5786a9c3c9c9F5e6f42'),
create_choice(name="World of Women", value = '0xe785E82358879F061BC3dcAC6f0444462D4b5330'),
create_choice(name="Zunks", value = '0x031920cc2D9F5c10B444FD44009cd64F829E7be2'),
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
                
                create_choice(name="Digital Represenation of a physical cryptocurrency aka the Manzcoin NFTz", value = '0x495f947276749Ce646f68AC8c248420045cb7b5e'),
create_choice(name="Aliens", value = '0x4581649aF66BCCAeE81eebaE3DDc0511FE4C5312'),
create_choice(name="Alphabettys", value = '0x6d05064fe99e40F1C3464E7310A23FFADed56E20'),
create_choice(name="Animetas", value = '0x18Df6C571F6fE9283B87f910E41dc5c8b77b7da5'),
create_choice(name="Animonkeys", value = '0xA32422dfb5bF85B2084EF299992903eb93FF52B0'),
create_choice(name="Avastar", value = '0xF3E778F839934fC819cFA1040AabaCeCBA01e049'),
create_choice(name="BAYC", value = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'),
create_choice(name="Bears On The Block", value = '0x02AA731631c6D7F8241d74F906f5b51724Ab98F8'),
create_choice(name="Bulls", value = '0x3a8778A58993bA4B941f85684D74750043A4bB5f'),
create_choice(name="Chickens", value = '0x8634666bA15AdA4bbC83B9DbF285F73D9e46e4C2'),
create_choice(name="Cool Cats", value = '0x1A92f7381B9F03921564a437210bB9396471050C'),
create_choice(name="Craniums", value = '0x85f740958906b317de6ed79663012859067E745B'),
create_choice(name="Deadheads", value = '0x6fC355D4e0EE44b292E50878F49798ff755A5bbC'),
create_choice(name="Elephants", value = '0x613E5136a22206837D12eF7A85f7de2825De1334'),
create_choice(name="Flufs", value = '0xCcc441ac31f02cD96C153DB6fd5Fe0a2F4e6A68d'),
create_choice(name="FVCK_CRYSTALS", value = '0x7AfEdA4c714e1C0A2a1248332c100924506aC8e6'),
create_choice(name="Ethlings", value = '0x8A1AbD2E227Db543F4228045dd0aCF658601fedE'),
create_choice(name="Fame Lady Squad", value = '0xf3E6DbBE461C6fa492CeA7Cb1f5C5eA660EB1B47'),
create_choice(name="Goblin Goons", value = '0x6322834FE489003512A61662044BcFb5Eeb2A035'),
create_choice(name="Goatz", value = '0x3EAcf2D8ce91b35c048C6Ac6Ec36341aaE002FB9'),
create_choice(name="Gutter Cats", value = '0xEdB61f74B0d09B2558F1eeb79B247c1F363Ae452'),
create_choice(name="Huas", value = '0x495f947276749Ce646f68AC8c248420045cb7b5e'),
create_choice(name="Lazy Lions", value = '0x8943C7bAC1914C9A7ABa750Bf2B6B09Fd21037E0'),
create_choice(name="Lucky Maneki", value = '0x14f03368B43E3a3D27d45F84FabD61Cc07EA5da3'),
            ],
        ),
        create_option(
            name="projects-l-z",
            description="Projects starting with L-Z",
            required=False,
            option_type=3,
            choices=[
            create_choice(name="Meebits", value = '0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7'),
create_choice(name="Moon Dogs", value = '0xfc007068C862E69213Dc7AA817063B1803D4E941'),
create_choice(name="Pudgy Penguins", value = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'),
create_choice(name="Punks Comic", value = '0x5ab21Ec0bfa0B29545230395e3Adaca7d552C948'),
create_choice(name="Purrlinis", value = '0x9759226B2F8ddEFF81583e244Ef3bd13AAA7e4A1'),
create_choice(name="Rabbits", value = '0x91F3114F8818ADe506d0901a44982Dc5c020C99B'),
create_choice(name="Robotos", value = '0x099689220846644F87D1137665CDED7BF3422747'),
create_choice(name="Royal Society of Players (RSOP)", value = '0xB159F1a0920A7f1D336397A52D92da94b1279838'),
create_choice(name="Shibas", value = '0x763864F1A74D748015f45F7c1181B60E62E40804'),
create_choice(name="Slacker Ducks", value = '0xeC516eFECd8276Efc608EcD958a4eAB8618c61e8'),
create_choice(name="Space Poggers", value = '0x4a8B01E437C65FA8612e8b699266c0e0a98FF65c'),
create_choice(name="SSS - Star Sailor Siblings", value = '0x49aC61f2202f6A2f108D59E77535337Ea41F6540'),
create_choice(name="Stoner Cats", value = '0xD4d871419714B778eBec2E22C7c53572b573706e'),
create_choice(name="Strippers", value = '0x9808226ED04e92F9380DA67C5606354FAe5891b0'),
create_choice(name="Theos", value = '0x9E02FFd6643f51aaAFa0f0E2a911Bf25EF2684Cb'),
create_choice(name="Top Dog Beach Club", value = '0x6F0365ca2c1Dd63473F898A60f878A07e0f68A26'),
create_choice(name="Vogu", value = '0x18c7766A10df15Df8c971f6e8c1D2bbA7c7A410b'),
create_choice(name="Vox", value = '0xad9Fd7cB4fC7A0fBCE08d64068f60CbDE22Ed34C'),
create_choice(name="Wizards", value = '0x521f9C7505005CFA19A8E5786a9c3c9c9F5e6f42'),
create_choice(name="World of Women", value = '0xe785E82358879F061BC3dcAC6f0444462D4b5330'),
create_choice(name="Zunks", value = '0x031920cc2D9F5c10B444FD44009cd64F829E7be2'),
            ],
        ),
    ],
)
async def floor(ctx: SlashContext, **kwargs):

    for CONTRACT_ADDRESS in kwargs.values():
        await ctx.defer(hidden=False)
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
