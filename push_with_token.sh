#!/bin/bash
set -e

# Extract just the token value (everything after =)
TOKEN=$(grep GITHUB_TOKEN ~/.hermes/.env | cut -d'=' -f2-)
echo "Token length: ${#TOKEN}"

echo "Pushing to GitHub..."
git push https://jdip1007:${TOKEN}@github.com/jdip1007/Hermes-Playground.git main

echo "Done! GitHub Pages will deploy in 1-2 minutes."