# Service
Сервис для самостоятельной записи на ремонт

Для роли Пользователь

Часть сайта для работы с пользователем.

    • Регистрация, параметры:
        ◦ Ник
        ◦ Пароль
        ◦ Адрес эл. почты
        ◦ Имя
        ◦ Фамилия
        ◦ Отчество
    • Аутентификация

Личный кабинет в который входят стандартный функционал:

    • Редактирование пользовательских данных
    • Смена пароля
    • Добавление личного авто:
        ◦ VIN
        ◦ Госномер
        ◦ Номер стс
        ◦ Дата продажи
        ◦ Пробег
        ◦ Модель автомобиля(выбирает из возможных моделей авто с картинками)
    • Переход на страницу регистрации на ТО(недоступно пока не добавил хотя-бы одно свое авто)

--------------
Страница регистрации на ТО для пользователя

Выбор желаемого дня в календаре, затем таблица с временем для записи (одна запись = полчаса), рабочий день с 8 до 20. 

Пользователь может видеть приемщиков.

Пользователь видит какие ячейки времени занятые, отмененные, свободные. 

С занятыми не может ничего делать, может только занять свободную ячейку (одну в день).

Далее, после того как занял ячейку времени ему предлагается выбрать какое из своих авто он хочет записать,  

тип ремонта (на выбор либо определенное ТО (ТО-1, ТО-2, ТО-3 и т. д.), либо диагностика), тип ремонта выбирает из списка.

Далее пользователь получает предварительную стоимость ремонта/обслуживания и подтверждает запись

(Пока не решил но скорее всего инфа о стоимости будет рассчитана и выведена рядом с типом ремонта во время выбора на предыдущем этапе)

Пользователь может отменить свою запись.

----------------


Для роли Менеджера

Пользовательская часть
Регистрация, аутентификация аналогична простому пользователю. 
Роль менеджера будет выдаваться в админ панели джанго.

Личный кабинет:
    • Редактирование своих данных
    • Смена пароля

Страница регистрации на ТО для Менеджера

Выбор желаемого дня в календаре, затем таблица с временем для записи (одна запись = полчаса), рабочий день с 8 до 20. 

Менеджер может видеть приемщиков.

Менеджер видит какие ячейки времени занятые, отмененные, свободные. 

Менеджер может удалять любые записи (при удалении пользователю отмененной записи отсылается email уведомление)

Менеджер может записывать в свободные ячейки пользователей.

Далее, после того как занял ячейку времени менеджеру предлагается выбрать пользователя.

Далее выбор авто пользователя и далее запись по аналогии с пользователем... 

-------------------

Функционал рассылки email

У менеджера есть возможность инициировать рассылки для уведомления о разных акциях и т. д. 
Для этого нужна отдельная страница где менеджер может ввести текст рассылки и выбирать автомобили или 
клиентов на которые распространяется данная акция (либо все клиенты, если это допустим акция, к примеру, по шиномонтажу).
Также сервис должен отправлять email об удалении записи, напоминания за день до записи что клиент записан на ремонт,
напоминание что подошло время ТО по времени, раз в год

-------------------

Сущности:

Склад расходников:

    • Название расходника (в основном фильтра)
    
    • Цена

Масло:

    • Марка масла
    
    • Вязкость
    
    • Цена за литр

Двигатель:

    • Модель (цифробуквенное обозначение от производителя)
    
    • Ссылка на требуемое масло
    
    • Требуемое количество масла (в литрах)
    
    • Обьём двигателя

Модель автомобиля:

    • Название модели (с названием поколения в скобках)
    
    • Ссылка на изображение с автомобилем
    
    • Ссылка на совместимые двигатели

Тип ремонта:

    • Название операции (Диагностика, ТО-1, ТО-2 и т д)
    
    • Количество нормо-часов
    
    • Ссылка на тип нормочаса
    
    • Ссылка на необходимые запчасти
    
    • Ссылка на Автомобиль 

    • Ссылка на двигатель

    • Предварительная стоимость ремонта (вычисляется автоматически)

Автомобиль:

    • Собственник
    
    • VIN
    
    • Госномер
    
    • Номер СТС
    
    • Дата продажи
    
    • Пробег
    
    • Ссылка на модель автомобиля

    • Ссылка на двигатель

Тип нормочаса:

    • Тип номрмочаса (Диагностика, ТО, установка доп оборудования)
    
    • Цена нормочаса

Приемщик:

    • Фамилия
    
    • Имя
    
    • Отчество

Регистрация на ремонт:

    • День
    
    • Время
    
    • Приемщик
    
    • Ссылка на тип ремонта
    
    • Ссылка на автомобиль


--------------------------------

Комманда для создания дампа

`sudo docker exec -i service_database_1 pg_dump -F t -U dbuser -v -d dbname -f /service/pg_dump/dump_1.tar`


Для запуска сервиса записи необходимо склонировать к себе на локальную машину данный репозиторий.
в окне терминала в локальной директории с проектом "/service" запустить команду:

`sudo docker-compose -f docker-compose.dev.yml up --build`

(При повторном запуске можно без --build)

Находясь в той же локальной директории с проектом открыть новое окно терминала и выполнить команду:

`sudo docker exec -i service_database_1 pg_restore -U dbuser -v -d dbname  /service/pg_dump/dump_1.tar`


После чего в первом окне терминала остановить все запущенные контейнеры: "Ctrl+C" и снова выполнить команду:

`sudo docker-compose -f docker-compose.dev.yml up`


