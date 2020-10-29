# ez meme sys

@client.command(pass_context=True)
async def meme(ctx):
    embed = discord.Embed(title="meme", description="Ez meme sys by L4xus")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
