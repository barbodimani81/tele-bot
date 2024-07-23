# Gooz Bot

Welcome to **Gooz Bot** – a simple yet interactive Telegram bot built using Python and the `pyTelegramBotAPI` library. This bot provides users with a friendly interface for various functionalities including information about the bot, contact details, and membership options.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)

## Overview

**Gooz Bot** is a Telegram bot designed to enhance user interaction by providing essential information and services. It is built using the `telebot` library, which allows for straightforward interaction with the Telegram Bot API.

## Features

- **Welcome Message**: Greets users with a friendly welcome message.
- **Help Command**: Provides users with a keyboard for selecting different options such as information about the bot and contact details.
- **Membership Options**: Offers choices for different membership durations.
- **Dynamic Responses**: Responds to user inputs with relevant information or actions.

## Installation

To get started with **Gooz Bot**, follow these steps:

1. **Clone the Repository** (if applicable):

    ```bash
    git clone https://github.com/yourusername/gooz-bot.git
    cd gooz-bot
    ```

2. **Create a Virtual Environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:

    Ensure you have Python 3.x installed, then install the necessary libraries using `pip`:

    ```bash
    pip install pyTelegramBotAPI
    ```

## Usage

1. **Set Up Your Bot**:

    Replace `'YOUR_BOT_API_KEY'` in the script with your actual Telegram Bot API key. You can obtain this key by creating a new bot on Telegram via the [BotFather](https://core.telegram.org/bots#botfather).

2. **Run the Script**:

    ```bash
    python bot.py
    ```

    The bot will start polling for new messages and respond to user interactions.

## Configuration

The script initializes the bot with the following commands and responses:

- **/start**: Sends a welcome message to the user.
- **/help**: Provides a keyboard with options to learn more about the bot or contact us.
- **/membership**: Provides a keyboard with membership options (3 months or 1 year).

**Response Handling**:
- If the user selects "درباره ما" (About Us), the bot responds with developer information.
- If the user selects "تماس با ما" (Contact Us), the bot provides an email and website.
- If the user selects a membership option, the bot sends a confirmation message.
- If the user selects "<-", the bot returns to the main menu.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and push the branch.
4. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using **Gooz Bot**! We hope you find it useful and enjoyable. If you have any questions or feedback, feel free to reach out.

Happy chatting! 🎉

