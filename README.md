# Telegram-Token-Tracker-Bot

## Description
This project is a Python-based Telegram bot designed to monitor cryptocurrency transactions and price movements on the FEGex platform. It provides users with real-time updates on token transactions, significant price changes, and other market data.

---

## Features
- Tracks token transactions (buy/sell) in real-time.
- Filters and highlights large transactions exceeding a configurable threshold.
- Displays token price updates along with market data such as:
  - Market capitalization
  - 24-hour volume
- Runs asynchronously using threading for smooth performance.
- Responds to user commands for customized token tracking.

---

## Requirements
- **Python Version**: 3.8 or higher  
- **Libraries**:
  - `requests`: For API interactions.
  - `python-telegram-bot`: For Telegram bot functionality.

---

## Setup Instructions

1. Clone or download the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/telegram-token-tracker-bot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd telegram-token-tracker-bot
    ```

3. Install the required dependencies:
    ```bash
    pip install requests python-telegram-bot
    ```

4. Run the bot:
    ```bash
    python main.py
    ```
   - Enter your Telegram bot token when prompted.

---

## Usage

1. Start the bot by typing `/start` in your Telegram chat.
2. Use commands to track specific tokens:
    - Monitor transactions for a token.
    - Filter significant buy/sell transactions.
    - View live price changes and market stats.

---

## Notes
- Ensure your Telegram bot token is correctly set up and has the necessary permissions.
- The bot currently tracks the following tokens by default:
  - **RUGMUNCHERTOKEN (rmt)**
  - **LOTTERY (lot)**

---

## Contribution
Feel free to submit issues or pull requests to enhance the functionality of this bot.
