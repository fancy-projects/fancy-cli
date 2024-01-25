set -e

cd /usr/local/share
git clone https://github.com/pythonkid90/fancy-cli.git
pip3 install ./fancy-cli

cp -r fancy-cli/build/lib/fancy .
rm -rf fancy-cli  # Clean up the temporary directory

pyinstaller fancy-cli  # Create standalone executable


echo "✨ fancy-cli installed! Use: fancy --help"