# Dota 2 Match Outcome Predictor 🎮🤖

Веб-сервис и Deep Learning модель для прогнозирования победы команды Radiant или Dire по ранней динамике первых 5 ключевых тимфайтов.

## 📌 О проекте
- **Архитектура:** Полносвязная нейросеть (Dense 32 -> 16 -> 8 -> 1) с BatchNormalization, Dropout (0.3) и ранней остановкой (EarlyStopping).
- **Данные:** 20 000+ матчей через OpenDota API (SQL Explorer).
- **Признаки:** 15 динамических признаков (преимущество по золоту, опыту и фрагам в первых 5 командных битвах).
- **Точность:** ~75% Binary Accuracy на тестовой выборке.
- **Инференс:** Flask REST API и интерактивный веб-интерфейс.

## 🚀 Запуск проекта локально
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python server.py