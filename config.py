import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29124227"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3416803f6b85a63ee12f5976ed557f96")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://trynow8763051478:0HsY9BankPBFsFIs@cluster0.3buxu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
