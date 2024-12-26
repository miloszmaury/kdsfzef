from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Callback data constants
MENU, STOCK, COMMANDE, NATURE, RHUM_VANILLE = range(5)

# Chemin vers l'image locale
IMAGE_PATH = "C:/Users/exbow/OneDrive//Bureau/woodski_bot/photo_2024-03-18_10-30-32.jpg"  # Remplacez par le chemin exact de votre image

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Afficher le menu principal avec une image."""
    keyboard = [
        [InlineKeyboardButton("📦𝐒𝐓𝐎𝐂𝐊📦", callback_data=str(STOCK))],
        [InlineKeyboardButton("🔌𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐄🔌", callback_data=str(COMMANDE))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envoyer l'image avec le menu principal
    if update.message:
        await update.message.reply_photo(
            photo=open(IMAGE_PATH, 'rb'),
            reply_markup=reply_markup
        )
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_caption(
            reply_markup=reply_markup
        )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gérer les choix dans le menu principal."""
    query = update.callback_query
    await query.answer()
    choice = int(query.data)
    
    if choice == STOCK:
        keyboard = [
            [InlineKeyboardButton("🪵𝐍𝐀𝐓𝐔𝐑𝐄🪵", callback_data=str(NATURE))],
            [InlineKeyboardButton("🍹𝐑𝐇𝐔𝐌 𝐕𝐀𝐍𝐈𝐋𝐋𝐄🍹", callback_data=str(RHUM_VANILLE))],
            [InlineKeyboardButton("🔙𝐑𝐄𝐓𝐎𝐔𝐑🔙", callback_data=str(MENU))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(
            reply_markup=reply_markup
        )
    elif choice == COMMANDE:
        keyboard = [[InlineKeyboardButton("🔙𝐑𝐄𝐓𝐎𝐔𝐑🔙", callback_data=str(MENU))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(
        caption="📍𝐌𝐄𝐄𝐓-𝐔𝐏 :📍\n\n   🏢DEUIL LA BARRE 95170 \n\n   🗼PARIS A PARTIR DE 50€ \n\n𝐂𝐎𝐍𝐓𝐀𝐂𝐓𝐄𝐙 : @numba1seller",
            reply_markup=reply_markup
        )

async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gérer les sous-menus de STOCK."""
    query = update.callback_query
    await query.answer()
    choice = int(query.data)
    
    if choice == NATURE:
        keyboard = [
            [InlineKeyboardButton("🔌𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐄🔌", callback_data=str(COMMANDE))],
            [InlineKeyboardButton("🔙𝐑𝐄𝐓𝐎𝐔𝐑🔙", callback_data=str(STOCK))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(
            caption="🪵𝐖𝐎𝐎𝐃 𝐍𝐀𝐓𝐔𝐑𝐄⁣ :🪵\n   1 - 10€\n   3 - 25€\n   5 - 40€ ",
            reply_markup=reply_markup
        )
    elif choice == RHUM_VANILLE:
        keyboard = [
            [InlineKeyboardButton("🔌𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐄🔌", callback_data=str(COMMANDE))],
            [InlineKeyboardButton("🔙𝐑𝐄𝐓𝐎𝐔𝐑🔙", callback_data=str(STOCK))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(
            caption="🍹𝐑𝐇𝐔𝐌 𝐕𝐀𝐍𝐈𝐋𝐋𝐄 :🍹\n   1 - 15€\n   3 - 40€\n   5 - 60€",
            reply_markup=reply_markup
        )
    elif choice == STOCK:
        keyboard = [
            [InlineKeyboardButton("🪵𝐍𝐀𝐓𝐔𝐑𝐄🪵", callback_data=str(NATURE))],
            [InlineKeyboardButton("🍹𝐑𝐇𝐔𝐌 𝐕𝐀𝐍𝐈𝐋𝐋𝐄🍹", callback_data=str(RHUM_VANILLE))],
            [InlineKeyboardButton("🔙𝐑𝐄𝐓𝐎𝐔𝐑🔙", callback_data=str(MENU))]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_caption(
            reply_markup=reply_markup
        )

async def commande(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Gérer la commande et retourner au menu."""
    query = update.callback_query
    await query.answer()
    keyboard = [[InlineKeyboardButton("🔙𝐑𝐄𝐓𝐎𝐔𝐑🔙", callback_data=str(MENU))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_caption(
        caption="COMMANDE :\nVotre commande a été enregistrée. Cliquez sur 'RETOUR' pour revenir au menu principal.",
        reply_markup=reply_markup
    )

def main() -> None:
    """Lancer le bot."""
    # Remplacez 'YOUR_TELEGRAM_BOT_TOKEN' par le token de votre bot Telegram
    application = Application.builder().token("7838117716:AAEMgHVZUuzxiwnliaN2Z5N1KicrldYrqro").build()

    # Gestion des commandes et des interactions
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(menu, pattern=f"^{STOCK}$|^{COMMANDE}$"))
    application.add_handler(CallbackQueryHandler(stock, pattern=f"^{NATURE}$|^{RHUM_VANILLE}$|^{STOCK}$"))
    application.add_handler(CallbackQueryHandler(commande, pattern=f"^{COMMANDE}$"))
    application.add_handler(CallbackQueryHandler(start, pattern=f"^{MENU}$"))

    # Démarrer le bot
    application.run_polling()

if __name__ == '__main__':
    main()
