#!/usr/bin/env bash

rm -rf /usr/local/share/fancy-cli
rm /usr/local/bin/fancy

cd /usr/local/share

git clone https://github.com/pythonkid90/fancy-cli/

ln -s /usr/local/share/fancy-cli/dist/fancy-runner-mac/fancy-runner /usr/local/bin/fancy

echo "Install Completed! Type fancy --help for information about how to use the CLI."
