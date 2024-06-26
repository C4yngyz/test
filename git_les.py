'================================Git====================================='
#Git- это распределенная система контроля версии. Система для отслеживания и введения истории изменения файлов в нашем проекте. При помощи Git можно организовать командную работу
#  Репозиторий - это хранилтище нашего кода и истории его изменений
#  Gidhub - это вебсайт для размещения git - репозиториев для совместной оазработке проектов

'''
 git add . - добавить все файлы в индекс 
 git commit -m 'comment' - зафиксировать изменения
 git log - посмотреть историю коммитов
 git checkout - перемещает между ветками 
 git branch - показывает список всех наших веток
 git branc - M  <name> - меняет название ветки на новое
 git status - показывает состояние всех файлов
 git init - создает репозиторий, в той директории, в которой была прописана команда
 git push - отправляет последний комит на удаленный репозиторий 
 git pull - загружает последний коммит с удаленного репозитория на локальный 
 git remote add origin ссылка_на_уд.репозиторий - связывает удаленный репозиторий с локальнымпше  
 git clone ссылка_на_уд.репозиторий - копирует репозиторий к себе
 git merge - обьединяет ветки 
'''
#file может иметь 4 состояния:
'''

1. неотслеживаемый (untracked)
2. изменяемый (modified)
3. отслеживаемый(staged)
4. Завиксированный(comited)
'''

#Индекс - хранилка, где лежат имена файлов и их изменения , которые должны быть 
в следующем коммите
Ветка - branch