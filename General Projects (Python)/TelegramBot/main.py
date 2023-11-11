from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6938633291:AAG-oGmlE_kqtRtKDUB5Y20ttAxWj-leN8o'
BOT_USERNAME: Final = '@MikeYoungBot'

# Comandos

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá, Obrigado por confiar em mim, me diga o que precisa :)')

# Respostas

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'Olá' in processed:
        return 'Olá como posso lhe ajudar? Digite "Ajuda" para saber o que eu posso fazer por você :)'
    return 'Não entendi o que você disse...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'Usuário ({update.message.chat.id}) em {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} causou erro {context.error}')


if __name__ == '__main__':
    print('Iniciando o Bot...')
    app = Application.builder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler('start', start_command))

    # Mensagens
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Erros
    app.add_error_handler(error)

    # Polls the bot
    print('Espere um pouco...')
    app.run_polling(poll_interval=3)