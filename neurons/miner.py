"""Lucid Subnet Miner — serves real-time knowledge queries."""

import argparse
import asyncio
import aiohttp


async def fetch_package_info(name: str, registry: str = "npm") -> dict:
    urls = {
        "npm": f"https://registry.npmjs.org/{name}/latest",
        "pypi": f"https://pypi.org/pypi/{name}/json",
    }
    url = urls.get(registry)
    if not url:
        return {"error": f"unsupported registry: {registry}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return {"error": f"package not found: {name}"}
            data = await resp.json()

    if registry == "npm":
        return {
            "name": data.get("name"),
            "version": data.get("version"),
            "description": data.get("description", ""),
        }
    elif registry == "pypi":
        info = data.get("info", {})
        return {
            "name": info.get("name"),
            "version": info.get("version"),
            "description": info.get("summary", ""),
        }


async def handle_query(query: dict) -> dict:
    query_type = query.get("type", "package")

    if query_type == "package":
        return await fetch_package_info(
            query.get("name", ""),
            query.get("registry", "npm"),
        )

    return {"error": f"unsupported query type: {query_type}"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wallet.name", type=str, default="lucid-owner")
    parser.add_argument("--wallet.hotkey", type=str, default="default")
    parser.add_argument("--netuid", type=int, required=True)
    parser.add_argument("--subtensor.network", type=str, default="test")
    args = parser.parse_args()

    print(f"Lucid Miner starting on netuid {args.netuid}")
    print("Waiting for validator queries...")


if __name__ == "__main__":
    main()
