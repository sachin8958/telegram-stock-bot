from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yfinance as yf
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send /price TCS")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        symbol = context.args[0].upper() + ".NS"
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        price = data['Close'].iloc[-1]

        await update.message.reply_text(f"📊 {symbol}\n💰 Price: ₹{price}")
    except:
        await update.message.reply_text("Error fetching data")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

app.run_polling()
