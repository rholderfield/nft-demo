from scripts.helpful_scripts import get_account, SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
