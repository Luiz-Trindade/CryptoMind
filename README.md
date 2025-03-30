# CryptoMind 🧠💰

<img src="images/cryptomind_logo.png" alt="CryptoMind Logo" height="200" />

**CryptoMind** is a technical analysis bot designed to help you make informed decisions when trading cryptocurrencies like Bitcoin. The bot analyzes market data, including moving averages and news, to provide recommendations on whether to buy, sell, or hold an asset based on current market conditions. 🚀📈

## Features 🌟

- **Moving Average Analysis**: Identifies trends in the market by analyzing price movements. 📉📊
- **Market News Monitoring**: Keeps track of relevant news to assess its impact on the market. 📰🔍
- **Buy/Sell/Hold Recommendations**: Based on the technical analysis, the bot suggests the best course of action. 💸⚖️
- **Simple and Effective Strategies**: Implements straightforward techniques that help improve trading decisions. 💡✅

## Technologies Used 🛠️

- **Gemini API**: Provides real-time Bitcoin data. 🌐📡
- **LLMs (Large Language Models)**: Custom prompts for dynamic and context-driven analysis. 🤖💬
- **Technical Analysis**: Uses moving averages, market data, and the VIX fear index. 📈🔧

## Technical Analysis Example 📉

**Recommendation:** **Wait.**

**Justification:**

The current price (82449.68) is below the short-term (85237.91) and long-term (88784.38) moving averages, indicating a downward trend in the short and medium term. The negative MACD (-1011.09) and below the signal line (-1155.54) reinforce this bearish outlook.

Although the RSI (49.66) is neutral and not signaling oversold conditions, the proximity of the price to the lower Bollinger Band (80607.19) suggests potential selling pressure. The volatility of 2.68% indicates that the price may fluctuate considerably. 

**Risks:** Continuing the downward trend and the price may reach the lower Bollinger Band, potentially breaking it.

**Opportunities:** If the price reverses the trend and breaks above the short-term moving average, it could indicate a buy signal. However, with the current indicators, this reversal is not clear.

**In summary:** The technical indicators suggest caution. Waiting for clearer signs of trend reversal or price stabilization is the most prudent strategy at the moment.

## Setup ⚙️

### Prerequisites 📜

Make sure you have Python 3.8+ installed and the following dependencies:

- Poetry (for dependency management) 🔑

### Installation 🛠️

1. Clone the repository:

   ```bash
   git clone git@github.com:Luiz-Trindade/CryptoMind.git
   cd cryptomind
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

   This will install all the dependencies listed in `pyproject.toml`. 🔄📥

3. Set up your `.env` file to store sensitive information like API keys and tokens. Example:

   ```text
   GEMINI_API_KEY=your_api_key
   ```

### Running the Bot 🚀

Once the setup is complete, you can run the bot with the following command:

```bash
python src/main.py
```

## Contributing 🤝

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License 📄

Distributed under the MIT License. See `LICENSE` for more information. 🔐
