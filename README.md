BankApp — Консольний банківський застосунок
Це простий, але функціональний консольний застосунок для управління банківськими рахунками користувачів. Написано повністю на Python із використанням ООП, інкапсуляції, роботи з файлами та JSON.
Функціонал
- ✅ Реєстрація нового користувача
- ✅ Авторизація (логін)
- ✅ Перегляд балансу
- ✅ Депозит коштів
- ✅ Зняття коштів
- ✅ Збереження всіх даних у `users.json` (створюється автоматично)
- --
Структура проєкту
BankApp/

├── bank_app.py       # Основна логіка застосунку

├── bank_db.py        # Робота з JSON базою даних

├── users.json        # База користувачів (генерується при запуску)

└── README.md         # Документація проєкту


--------
👨‍💻 Автор
	•	Імʼя: Богдан
	•	GitHub: @wivikov
-----
Плани на майбутнє

	•	Захист паролем
	•	Лог транзакцій
	•	Графічний інтерфейс (Tkinter / Flask)
	•	Підключення SQLite