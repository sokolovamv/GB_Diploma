from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
import equations
import calculations
import inequalities
import plots
import progressions
import probabilities

# Приветствие
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


# Команда помощь, знать какие команды есть
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/help\n/equations\n/calculations\n/inequalities\n/plots\n/progressions\n/probabilities')


# работа с уравнениями
async def equations_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    await update.message.reply_text(equations.main(msg))


# работа с арифметическими действиями
async def calculations_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    await update.message.reply_text(calculations.process_input(msg))


# работа с неравенствами
async def inequalities_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Включаем логирование
    log(update, context)
    msg = update.message.text
    await update.message.reply_text(inequalities.solve_inequality(msg))


# работа с графиками
async def plots_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    #buf = plot_function(user_input)
    await update.send_photo(photo=InputFile(plots.checking_message(msg), filename='function_plot.png'))
    #await update.message.reply_text(plots.plot_function(msg, x_range=(-10, 10)))


# работа с арифметическими прогрессиями
async def progressions_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    await update.message.reply_text(progressions.main(msg))


# работа с классической вероятностью
async def probabilities_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    await update.message.reply_text(probabilities.main(msg))