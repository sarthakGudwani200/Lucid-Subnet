# Lucid Subnet

A Bittensor subnet for real-time knowledge verification and grounding. Miners serve verified, up-to-date information about packages, APIs, documentation, and technical facts. Validators score responses based on accuracy, freshness, and completeness.

## Overview

Lucid brings real-time knowledge to the Bittensor network. Instead of relying on static training data, miners in this subnet provide live-verified answers about:

- **Package versions** — npm, PyPI, crates.io, and more
- **API documentation** — current endpoints, parameters, and responses
- **Framework changes** — breaking changes, migration guides, deprecations
- **Technical facts** — grounded in live data, not hallucinated

Validators independently verify miner responses against authoritative sources and score them on accuracy, freshness, and response time.

## Architecture

```
Validator                          Miner
   |                                 |
   |--- Query (package/api/doc) ---->|
   |                                 |--- Fetch live data
   |                                 |--- Verify & format
   |<------ Response ----------------|
   |
   |--- Score (accuracy, freshness)
   |--- Set weights on-chain
```

## Getting Started

### Prerequisites

- Python 3.10+
- [Bittensor CLI](https://docs.bittensor.com/getting-started/install-btcli)

### Installation

```bash
git clone https://github.com/get-Lucid/Lucid-Subnet.git
cd Lucid-Subnet
pip install -r requirements.txt
```

### Running a Miner

```bash
python neurons/miner.py --wallet.name <wallet> --wallet.hotkey <hotkey> --netuid <netuid> --subtensor.network test
```

### Running a Validator

```bash
python neurons/validator.py --wallet.name <wallet> --wallet.hotkey <hotkey> --netuid <netuid> --subtensor.network test
```

## Incentive Mechanism

Miners are scored on three dimensions:

1. **Accuracy** — Does the response match the ground truth from authoritative sources?
2. **Freshness** — Is the data current, not stale or outdated?
3. **Speed** — How quickly does the miner respond?

Validators send queries to miners, independently verify the responses, and set weights accordingly through Yuma Consensus.

## Links

- Website: [getlucid.tech](https://getlucid.tech)
- Twitter: [@getlucid_](https://x.com/getlucid_)
- GitHub: [get-Lucid](https://github.com/get-Lucid)

## License

MIT
