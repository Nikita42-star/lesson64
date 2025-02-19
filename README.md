Бот продажи настольных игр. Часть 1
На сегодняшнем занятии немного отвлечёмся от классического изучения теории и попрактикуемся.
Представим, что вам дали задачу, построенную вокруг того, что нужно сделать небольшого бота, например для магазина настольных игр. На самом деле, вы можете выбрать совершенно любую тему.
Начнём с файла. Нам не нравится название «mail.py». Переименуем его в «main.py» (Рис.1).

Сразу добавим немного структурности в наш проект. Всё, что мы писали до этого, находилось в одном файле, и это не очень удобно для навигации. Мы создадим файл «config», в котором будет храниться конфигурационная информация. Далее создадим файл «keyboards», в котором будет находиться вёрстка наших клавиатур. Также сделаем файл «texts» (Рис.2), который будет выполнять роль простой базы данных для текстов. В начале этого будет вполне достаточно.

В файле «config» мы будем хранить различную информацию, необходимую для работы нашего проекта. Давайте переместим ключ «api» из файла «main.py» в этот новый файл и назовём его «API» (Рис.3).

Поскольку мы занимаемся созданием данных, связанных с настольными играми, давайте добавим следующие элементы в файл «config»: «priceM=1500», «priceL=2000» и «priceXL=3000» (Рис.4).

Почему мы выделили это в отдельный файл? Это сделано для удобства: в файл «config» можно легко зайти и внести изменения, не вникая в общий код. Таким образом, даже не программист сможет настроить необходимые параметры, если ему объяснить, что и где находится. В идеале в будущем мы сможем перенести эту информацию в базу данных.

Теперь перейдём к файлу «texts.py». Чтобы получить доступ к нашим ценам, импортируем всё из файла «config» (Рис.5).

Давайте согласуемся по некоторым элементам. Во-первых, мы создадим сообщение, которое будет отображаться при нажатии на кнопку «start». Также подготовим сообщение «about», в котором расскажем о нашем проекте. Кроме того, у нас будут сообщения, посвящённые играм, такие как «Mgame», «Lgame» и «XLgame» — это будут описания товаров, наши карточки. Для особых случаев добавим кнопку «other». Напишем уникальный текст для каждого из этих сообщений (Рис.6).

Теперь давайте начнём постепенно собирать всё вместе. Возвращаемся в файл «main.py» и импортируем несколько элементов из файлов «config», «keyboards» и «texts» (Рис.7).

Возьмем наш ключ «API» (Рис.8).

Что нам ещё потребуется? Мы можем настроить базовое логирование — никто не запрещает этого делать, и мы непременно это реализуем (Рис.9). Это окажется удобным для работы и проверки всех процессов. В целом, это и есть основа, которую мы на данный момент собрали.

Мы с вами возвращаемся в клавиатуры и начинаем их прописывать. Импортируем из «aiogram.types» «ReplyKeyboardMarkup» и «KeyboardButton» (Рис.10).

Для начала создадим стартовую клавиатуру «start.kb», которая будет использовать «ReplyKeyboardMarkup». Далее определим саму клавиатуру, прописывая кнопки. У нас будут две кнопки: «KeyboardButton(text='стоимость')» и «KeyboardButton(text='О нас')» (Рис.11).

Чтобы активировать автоматическое изменение размера клавиатуры, добавим параметр «resize_keyboard=True» (Рис.12). Итак, первая команда готова.

Далее нам понадобятся три хендлера: один для команды «start», второй для команды «О нас», который будет возвращать информацию и предоставлять возможность вернуться в основное меню, и третий — для команды «стоимость», который будет вызывать меню каталога. Давайте пропишем их (Рис.13).
Новую клавиатуру «catalog_kb», указанную в третьем хендлере, нам ещё предстоит написать.
Мы уже создали конфигурацию, базовую клавиатуру и набор текстов для работы, а также начали писать хендлеры для их обработки. Продолжим в следующем занятии.


Бот продажи настольных игр. Часть 2
Мы остановились на работе со стоимостью и отметили, что у нас будет каталог. Давайте его создадим.
Для этого нам нужно добавить инлайн-кнопки. Импортируем из модуля «aiogram.types» классы «InlineKeyboardMarkup» и «InlineKeyboardButton» (Рис. 1).

Теперь приступим к созданию клавиатуры каталога под названием «catalog_kb». Она будет представлять собой объект класса «InlineKeyboardMarkup» (Рис. 2).

Также мы укажем, что у нашей клавиатуры есть «inlinekeyboard». Как мы будем его строить? Мы создадим 4 кнопки: для маленькой, средней, большой игры и для других предложений (Рис. 3).

Первая кнопка: «InlineKeyboardButton», где мы укажем «text="Средняя Игра", callback_data="medium"», чтобы упростить ориентирование.

Вторая кнопка: «InlineKeyboardButton(text="Большая Игра", callback_data="big")».

Третья кнопка: «InlineKeyboardButton(text="Очень большая игра", callback_data="mega")».

И последняя кнопка: «InlineKeyboardButton(text="Другие предложения", callback_data="other")».

На этом этапе наша клавиатура готова – у нас есть четыре кнопки, каждая из которых отвечает за одну из игр или другие предложения.

Теперь создадим еще одну клавиатуру под названием «buy_kb». Эта клавиатура будет появляться при выборе одной из кнопок на первой клавиатуре и будет предназначена для покупок. Мы добавим кнопку с помощью «InlineKeyboardButton», которая будет содержать «text="Купить!", url="#"» (Рис. 4). Вместо символа ‘#’ можно указать любой адрес. Это одно из свойств: если указать параметр «url», кнопка будет вести на внешний сайт.

Теперь напишем необходимые хендлеры. Они будут достаточно однообразными, поэтому создадим общий шаблон: «async def buy_(call)». В каждой функции будут две основные операции: «await call.message.answer()», в которой будет содержаться набор элементов, и «await call.answer()», чтобы закрыть работу кнопки (Рис. 5).

Нам понадобятся четыре таких хендлера. Разметим их для «medium», «big», «mega» и «other». В названиях хендлеров мы также укажем соответствующие обозначения: «buy_m», «buy_l», «buy_xl» и «buy_other» (Рис. 6).

Теперь пропишем сообщения для каждого хендлера. В случае с «m» мы извлекаем значение «texts.priceM» и вызываем клавиатуру с помощью параметра «reply_markup=buy_kb». Далее, соответственно, для остальных хендлеров мы используем: «texts.priceL, reply_markup=buy_kb» для большого размера, «texts.priceXL, reply_markup=buy_kb» для очень большого размера и «texts.other, reply_markup=buy_kb» для других предложений (Рис. 7).

Чтобы бот заработал корректно, необходимо исправить в хендлерах «О нас» и «Стоимость»т«texts» на «text» (Рис. 8).

Запустим и проверим, как это работает. Напишем команду «/start» (Рис.9).

При нажатии на кнопку «О нас» мы получим сообщение с информацией (Рис. 10).

При нажатии на кнопку «Стоимость» появятся варианты (Рис. 11).

При нажатии на кнопку «Другие предложения» мы получаем ошибку (Рис. 12).

Однако это исправимо. Мы можем написать «url=http://ya.ru» (Рис. 13).

Перезапустим бота. Запустим его снова, выберем «Другие предложения», и он предложит нам ссылку (Рис. 14).

Если нажать на другие кнопки, бот предоставит нам стоимость и ссылку на покупку (Рис. 15).
Однако мы хотели извлечь из текста не стоимость, а названия игр. Давайте это исправим: вместо «priceM», «priceL» и «priceXL» нужно использовать «Mgame», «Lgame» и «XLgame» (Рис. 16).

Снова запустим бота. Теперь, если нажать на кнопки с вариантами, мы получим информацию о каждой из игр и ссылку на покупку (Рис. 17).

Если мы нажмем кнопку «Купить», нам предложат открыть ссылку (Рис. 18).

Мы с вами создали небольшого бота, который уже может предоставлять каталог и рассказывать о чем-либо. В дальнейшем мы сможем улучшить и расширить эту систему. Позже мы изучим это более подробно.
