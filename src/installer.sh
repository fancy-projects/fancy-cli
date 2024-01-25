#!/usr/bin/env bash

deactivate

set -e

cd /usr/local/share

rm -rf fancy-cli

git clone https://github.com/pythonkid90/fancy-cli.git
pip3 install ./fancy-cli

ls ./fancy-cli
cp ./fancy-cli/fancy-exe .
ls
rm -rf fancy-cli

rm /usr/local/bin/fancy && ln -s ./fancy-exe /usr/local/bin/fancy

echo "✨ fancy-cli installed! Use: fancy --help"