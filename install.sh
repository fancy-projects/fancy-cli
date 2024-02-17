rm /usr/local/share/fancy ; cp -r ~/PycharmProjects/fancy/scripts/fancy /usr/local/share/fancy
rm /usr/local/bin/fancy ; ln -s /usr/local/share/fancy /usr/local/bin/fancy
echo 'done'
