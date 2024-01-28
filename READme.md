<h2>Система автоматизации рабочего места товароведа</h2>

Закинуть файл credentials.json – от сервисного аккаунта Google Cloud Console для доступа к API Google Sheets:
`/Users/user_name/.config/gspread/credentials.json`


Запускаем бота с помощью команды nohup и символа & в конце строки (эта команда позволяет боту работать в фоновом режиме):
`nohup python3 telegrambro.py &;`
`nohup python3 telegrambro.py > /dev/null 2>&1 &`

Stop
`pkill python3`