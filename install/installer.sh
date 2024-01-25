export ANSI_COLORS=1

deactivate

echo -e "\e[34mNavigating to installation directory...\e[0m"
cd /usr/local/share

echo -e "\e[32mCloning fancy-cli repository...\e[0m"
rm -rf fancy-cli ; git clone https://github.com/pythonkid90/fancy-cli.git

echo -e "\e[33mInstalling dependencies...\e[0m"
pip3 install ./fancy-cli

echo -e "\e[32mCopying executable file...\e[0m"
cp ./fancy-cli/fancy-exe fancy

echo -e "\e[31mRemoving temporary directory...\e[0m"
rm -rf ./fancy-cli

ls

echo -e "\e[36mCreating symbolic link in /usr/local/bin...\e[0m"
rm /usr/local/bin/fancy
ln -s /usr/local/share/fancy /usr/local/bin/fancy

echo -e "\e[1mfancy-cli installed successfully!\e[0m \e[32mUse: fancy --help for documentation.\e[0m"