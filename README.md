
Flask-приложение для подсчета обращений граждан по темам и датам с использованием Faker для генерации тестовых данных. Включает страницу для просмотра списка обращений по выбранной теме.

## Установка и запуск

### 1. Установите программы
1. **Visual Studio Code**:
   - Скачайте с [code.visualstudio.com](https://code.visualstudio.com).
   - Установите с настройками по умолчанию.
2. **Python**:
   - Скачайте с [python.org/downloads](https://www.python.org/downloads) (Python 3.11.x, 64-bit).
   - Отметьте "Add Python to PATH" при установке.
   - Проверьте: в командной строке выполните `python --version`.
3. **Git**:
   - Скачайте с [git-scm.com](https://git-scm.com/download/win).
   - Установите с настройками по умолчанию.

### 2. Клонируйте репозиторий
1. Откройте Visual Studio Code.
2. Откройте терминал (`Ctrl+~`), выберите `cmd`.
3. Выполните:

   git clone https://github.com/username/appeals-stats.git
   cd appeals-stats

Замените `username` на ваш GitHub-логин.
4. Откройте папку: **File → Open Folder → appeals-stats**.

### 3. Настройте виртуальное окружение
1. В терминале выполните:

   python -m venv venv
   venv\Scripts\activate

2. Установите зависимости:

   pip install -r requirements.txt

### 4. Настройте Python в VS Code
1. Нажмите `Ctrl+Shift+P`, выберите `Python: Select Interpreter`.
2. Выберите `.\venv\Scripts\python.exe`.

### 5. Запустите приложение
1. Создайте базу данных:

   python database.py

2. Запустите сервер:

   python app.py

3. Откройте в браузере:
- `http://127.0.0.1:5000` — для подсчета обращений.
- `http://127.0.0.1:5000/list` — для просмотра списка обращений.

### Устранение проблем
- **ModuleNotFoundError: No module named 'faker'**: Активируйте виртуальное окружение и выполните `pip install Faker`.
- **Python не найден**: Переустановите Python, отметив "Add Python to PATH".
- **Порт занят**: В `app.py` измените `port=5001` и откройте `http://127.0.0.1:5001`.
- **Мало записей**: Удалите `appeals.db` и перезапустите `python database.py`.
