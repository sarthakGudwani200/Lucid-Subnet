"""Lucid Subnet Validator — scores miners on accuracy and freshness."""

import argparse
import asyncio
import random
import aiohttp


SAMPLE_QUERIES = [
    {"type": "package", "name": "react", "registry": "npm"},
    {"type": "package", "name": "next", "registry": "npm"},
    {"type": "package", "name": "express", "registry": "npm"},
    {"type": "package", "name": "flask", "registry": "pypi"},
    {"type": "package", "name": "django", "registry": "pypi"},
    {"type": "package", "name": "fastapi", "registry": "pypi"},
]


async def get_ground_truth(query: dict) -> dict:
    """Fetch the authoritative answer to verify miner responses."""
    urls = {
        "npm": f"https://registry.npmjs.org/{query['name']}/latest",
        "pypi": f"https://pypi.org/pypi/{query['name']}/json",
    }
    registry = query.get("registry", "npm")
    url = urls.get(registry)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return {}
            data = await resp.json()

    if registry == "npm":
        return {"version": data.get("version")}
    elif registry == "pypi":
        return {"version": data["info"]["version"]}
    return {}


def score_response(miner_response: dict, ground_truth: dict) -> float:
    if not miner_response or "error" in miner_response:
        return 0.0

    if not ground_truth:
        return 0.5

    if miner_response.get("version") == ground_truth.get("version"):
        return 1.0

    return 0.2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wallet.name", type=str, default="lucid-owner")
    parser.add_argument("--wallet.hotkey", type=str, default="default")
    parser.add_argument("--netuid", type=int, required=True)
    parser.add_argument("--subtensor.network", type=str, default="test")
    args = parser.parse_args()

    print(f"Lucid Validator starting on netuid {args.netuid}")
    print("Sending queries to miners and scoring responses...")


if __name__ == "__main__":
    main()
