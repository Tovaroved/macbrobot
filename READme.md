<h2>Система автоматизации рабочего места товароведа</h2>

Закинуть файл credentials.json – от сервисного аккаунта Google Cloud Console для доступа к API Google Sheets:
`/Users/user_name/.config/gspread/credentials.json`


Запускаем бота с помощью команды nohup и символа & в конце строки (эта команда позволяет боту работать в фоновом режиме):
`nohup python3 telegrambro.py &;`
`nohup python3 telegrambro.py > /dev/null 2>&1 &`

Stop
`pkill python3`

Команда для запуска независимо от сервера
`sudo systemctl start tgbot.service`

Команда для просмотра статуса бота
`sudo systemctl status tgbot.service`


Команды ниже исключительно для понимания)
`sudo cp tgbot.service /etc/systemd/system/`
`(sudo ln -s ./tgbot.service /etc/systemd/system/tgbot.service)`

`sudo journalctl -u tgbot.service`

`sudo systemctl daemon-reload`