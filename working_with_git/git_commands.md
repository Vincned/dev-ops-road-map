## Main GitHub commands
* rm -rf .git - удаление папки гит
* git status - проверка статуса гит
* git init - создание чистого репозитория
* git branch -M main - создание * главной ветки main 
* git add . - добавление текущей папки в гит
* git commit -m "Initial commit" - коммит файлов с комментом
* git remote add origin https://github.com/Vincned/dev-ops-road-map.git - связываем локальный гит с репозиторием
* git push -u origin main - выполняем перенос на репозиторий
* git branch - посмотреть в какой ветке я нахожусь сейчас (активная будет отмечена звездочкой *)
* git checkout main - переключение на main ветку
* git pull origin main - подтянуть свежие изменения
* it switch -c feature/my-new-feature - создание новой ветки с понятным названием

## Tag's commands
* git tag -a v1.0.0 -m "Релиз версии 1.0.0" - аннотированный тег - создание полноценного
объекта Git содержащие имя, email, дата создания, подпись и сообщение к тегу
* git tag v1.0.0 - легковесный тег
* Git tag - список всех тегов 
* git tag -a v1.0.0 9fceb02 -m "Релиз версии 1.0.0" - Тег для старого коммита: (укажите хэш коммита в конце)

Отправка тегов на GitHub
Отправить конкретный тег:
* git tag -a v1.0.0 -m "Release 1.0.0"
* git push origin v1.0.0
* git push origin --tags - отправить все локальные теги
* git tag -d v1.0.0 - удалить тег локально
* git push origin --delete v1.0.0 - удаление на гитхабе