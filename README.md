# Web development: домашние задание 9 (Python)

## Проект "Менеджер задач" — продолжение

Цель:

Добавить строковое представление (str) и метаданные (Meta) к моделям менеджера задач, а также настроить административную панель для удобного управления этими моделями.

1. Реализуйте изменения в моделях:
   - Модель **Task**:
     - Добавить метод str, который возвращает название задачи. 
     - Добавить класс Meta с настройками:
       - Имя таблицы в базе данных: 'task_manager_task'.
       - Сортировка по убыванию даты создания. 
       - Человекочитаемое имя модели: 'Task'.
       - Уникальность по полю 'title'. 
   - Модель **SubTask**:
     - Добавить метод str, который возвращает название подзадачи. 
     - Добавить класс Meta с настройками:
       - Имя таблицы в базе данных: 'task_manager_subtask'.
       - Сортировка по убыванию даты создания.
       - Человекочитаемое имя модели: 'SubTask'. 
       - Уникальность по полю 'title'. 
   - Модель **Category**:
     - Добавить метод str, который возвращает название категории. 
     - Добавить класс Meta с настройками:
       - Имя таблицы в базе данных: 'task_manager_category'. 
       - Человекочитаемое имя модели: 'Category'. 
       - Уникальность по полю 'name'.


2. Настройте отображение моделей в админке:
   - В файле admin.py вашего приложения добавьте классы администратора для настройки отображения моделей Task, SubTask и Category.


3. Зафиксируйте изменения в гит:
   - Создайте новый коммит и запушьте его в ваш гит.


4. Создайте записи через админку:
   1. Создайте суперпользователя. 
   2. Перейдите в административную панель Django. 
   3. Добавьте несколько объектов для каждой модели.


5. Оформите ответ:
   - Прикрепите ссылку на гит и скриншоты, где видны созданные объекты к ответу на домашнее задание.

---

superuser:

user name: admin

password: admin

---

Для установки mysqlclient на MacOS:

https://pypi.org/project/mysqlclient/

mac os global environment run: ->

```
brew install mysql-client pkg-config
```

in your virtualenv or other environment ->

```
export PKG_CONFIG_PATH="$(brew --prefix)/opt/mysql-client/lib/pkgconfig"
```

```
pip install -r requirements.txt
```
