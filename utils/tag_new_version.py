#!/usr/bin/env python

import argparse
import requests


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--bump', choices=['major', 'minor', 'patch'], default='patch')

	options = parser.parse_args()
	print(f"Bumping '{options.bump.upper()}' version...")

	tags = [t['name'] for t in requests.get('https://api.github.com/repos/cryoem/eman2/tags').json()]
	print(f"Received GitHub tags:\n{tags}")

	tags = sorted([t for t in tags if t.startswith('v')], reverse=True)
	print(f"Version tags (sorted: latest to oldest):\n{tags}")

	tag = tags[0]
	print(f"Latest tag:\n{tag}")


if __name__ == "__main__":
	main()
