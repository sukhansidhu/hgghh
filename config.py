# Don't Remove Credit @Riduan_Official_ID
# Subscribe YouTube Channel For Amazing Bot @riduan0
# Ask Doubt on telegram @riduan_official_channel


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26646989")

API_HASH = os.environ.get("API_HASH", "fc3539ec92676f2f233596041aee3b21")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7965982835:AAH0bIhiBBqtsLDrX_dVFe1ulbpxaRVEVeI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @Riduan_Official_ID
             # Subscribe YouTube Channel For Amazing Bot @riduan0
             # Ask Doubt on telegram @riduan_official_channel

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://villagebrother155:@rirename.xsaaw7z.mongodb.net/?retryWrites=true&w=majority&appName=RIRename")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7273974074').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @Riduan_Official_ID
# Subscribe YouTube Channel For Amazing Bot @riduan0
# Ask Doubt on telegram @riduan_official_channel
