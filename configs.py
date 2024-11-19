from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21406615"))
    API_HASH = getenv("API_HASH", "d66b1900ea3a7438ee22dd389085949a")
    BOT_TOKEN = getenv("BOT_TOKEN", "7895883671:AAFSp7wa7-fMdoXzP38Hz8O724Pr3g191CE")
    FSUB = getenv("FSUB", "-1002474765500")
    CHID = int(getenv("CHID", "-1002474765500"))
    SUDO = list(map(int, getenv("SUDO", "7974532619").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://tharkihoobooji:tharkihoobooji@cluster0.sje0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
