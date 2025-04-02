# 🏭 Сетевая структура поставщиков электроники

#### Django REST Framework приложение для управления многоуровневой сетью поставщиков

---

## Основные разделы

1. [🛠 Технологии](#-технологии)
2. [📖 Описание проекта](#-описание-проекта)
3. [🚀 Установка и настройка](#-установка-и-настройка)
4. [🏗 Модель сети](#-модель-сети)
5. [🚀 Функционал](#-функционал)
6. [🔌 API](#-api)
7. [🖥 Админ-панель](#-админ-панель)
8. [📜 Лицензия](#-лицензия)

## 🛠 Технологии

- **Python**: 3.12
- **Poetry**: 2.0.1
- **Django**: 5.1.7
- **Django Rest Framework (DRF)**: 3.15.2
- **PostgreSQL**: 17+
- **Flake8**: 7.1.2

---

## 📖 Описание проекта

Данный проект представляет собой веб-приложение с API-интерфейсом и админ-панелью для управления сетью по продаже
электроники. Приложение реализует иерархическую структуру из трех уровней: завод, розничная сеть и индивидуальный
предприниматель. Каждое звено сети ссылается на одного поставщика оборудования и имеет свои уникальные характеристики.
---

## 🚀 Установка и настройка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/AndyTums/Certification.git
   ```

2. **Установите зависимости:**

   ```bash
   poetry update
   ```

3. **Настройте базу данных:**

   Убедитесь, что у вас установлен PostgreSQL и создана база данных. Создайте .env файл и внесите необходимы настройки
   согласно .env.example

   ```bash
   SECRET_KEY=

   DEBUG=
   
   NAME=
   HOST=
   USER=
   PASSWORD=
   PORT=
   ```

4. **Примените миграции::**

   ```bash
   python manage.py migrate
   ```

5. **Примените миграции с помощью созданной команды:**

   ```bash
   python manage.py csu
   ```

6. **Запустите сервер:**

   ```bash
   python manage.py runserver
   ```

---

## 🏗 Модель сети

**Многоуровневая система управления сетью поставщиков электроники с:**

- **3 уровня иерархии**:
    - `0` Заводы (производители)
    - `1` Розничные сети
    - `2` Индивидуальные предприниматели

- **Ключевые сущности**:
    - Поставщики с контактными данными
    - Каталог продукции
    - Финансовые обязательства

**Каждое звено сети имеет следующие поля:**

- **Название** ✏️
- **Контакты:** 📞
    - email 📧
    - страна 🌍
    - город 🌆
    - улица 🛣️
    - номер дома 🏠
- **Продукты:** 📦
    - название 🏷️
    - модель 🔧
    - дата выхода продукта на рынок 📅
- **Поставщик** (предыдущий по иерархии объект сети) 🔗
- **Ссылка на поставщика** 🔗
- **Задолженность перед поставщиком** (в денежном выражении с точностью до копеек) 💰
- **Время создания** (заполняется автоматически при создании) ⏰
- **Время обновления** (заполняется автоматически при внесений изменений) ⏰

---

## 🚀 Функционал

### Основные возможности

**Основные возможности:**

- Автоматический расчет уровня поставщика.
- Валидация цепочки поставок.
- Фильтрации объектов по все атрибутам моделей.
- CRUD перации для всех моделей.
- Просмотр API только активным пользователям.
- Запрет на изменения поля задолженности через API.
- Аутентификация пользователей по токенам.

**Финансовый учет:**

- Отслеживание задолженностей
- Обнуление задолженности перед поставщиком у выбранных объектов.

**Пример валидации иерархии:**

```bash
models.py
def clean(self):
    if self.supplier == self:
        raise ValidationError("Поставщик не может ссылаться на себя") 
```


**Пример вывода информации о компании API:**
```bash
{
    "title": "ИП Тумеркин",
    "category": "individual entrepreneur",
    "contacts": {
        "email": "ip@mail.ru",
        "country": "Россия",
        "city": "Севастополь",
        "street": "Гоголя",
        "house_number": "2"
    },
    "supplier": "Поставщик отсутствует",
    "duty_supplier": "0.00",
    "created_at": "2025-03-29 16:43:28",
    "products": [
        {
            "title": "Пиво",
            "model": "Балтика",
            "release_date": "2025-04-02"
        }
    ]
}
```
**Пример вывода информации о продукте API:**
```bash
{
    "title": "Часы",
    "model": "Apple",
    "release_date": "2025-03-03",
    "created_at": "2025-03-29 17:15:24",
    "implementer": [
        "ООО Завод"
    ]
}
```
---

## 🔌 API

### Основные эндпоинты

| Метод  | URL               | Описание            | Аутентификация | Быть активным пользователем |
|--------|-------------------|---------------------|----------------|-----------------------------|
| `CRUD` | `/company/`       | Список поставщиков  | ✅ Требуется    | ✅ Требуется                 |
| `CRUD` | `/product/`       | Создание поставщика | ✅ Требуется    | ✅ Требуется                 |
| `CRUD` | `/user/`          | Каталог товаров     | ✅ Требуется    | ✅ Требуется                 |
| `POST` | `/login/`         | Авторизация         |                |                             |
| `POST` | `/token/refresh/` | Обновление токена   |                |                             |

### **_Только активные сотрудники имеют доступ к API._**

## 🖥 Админ-панель

**В админ-панели вы можете:**

- Просматривать и редактировать созданные объекты компании, продуктов и пользователей.
- Фильтровать объекты по названию страны, городу и виду деятельности.
- Поиск по информации модели: названию, почты, страны, города и улицы.
- Использовать метод для очистки задолженности перед поставщиком у выбранных объектов.
- В каждой модели имеется ссылка на поставщика.

---

## 📜 Лицензия

Проект распространяется под лицензией [MIT](LICENSE).
