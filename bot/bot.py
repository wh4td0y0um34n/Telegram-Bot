import telebot # import package dari Pytelegrambotapi

api = '5857685677:AAE8YGTkblNnVcRUKb-aR6mqueF4cXnpKAg' # disini kita sudah mendapatkan API provider, inilah yang nanti akan menghubungkan telegram dengan script kita ini 
bot = telebot.TeleBot(api) # ini sebagai pemanggil fungsi telebot yang isinya API 

@bot.message_handler(commands=['start']) # untuk memfilter perintah yang dimasukan ke dalam bot oleh si pengguna atau user, dan biasanya diikuti fungsi, fungsi tersebut berisi proses yang akan aktif saat command di execute
def send_welcome(message): # function dari message_handler
    nama = message.from_user.first_name # untuk memanggil  nama depan
    nama_akhir = message.from_user.last_name # untuk memangil nama belakang
    bot.reply_to(message, 'halo apa kabar {} {} ??'.format(nama,nama_akhir)) # pesan yang akan disampaikan

@bot.message_handler(commands=['help']) # sama dengan atas 
def send_welcome(message):
    nama = message.from_user.first_name # untuk memanggil  nama depan
    nama_akhir = message.from_user.last_name # untuk memangil nama belakang
    bot.reply_to(message, '''
Hai {} {}, ini list command yaa
/start -> Sapa bot dulu dong
/id -> Cek id kamu
/help -> List command bot
    ''')

@bot.message_handler(commands=['id']) # sama dengan atas 
def send_welcome(message):
    nomor_id = message.from_user.id # untuk memanggil id si pengguna 
    nama = message.from_user.first_name # untuk memanggil  nama depan
    nama_akhir = message.from_user.last_name # untuk memangil nama belakang
    bot.reply_to(message, '''
Hai, ini ID telegram kamu 
ID = {}
Nama = {}   
        '''.format(nomor_id,nama, nama_akhir))

print('bot start running') # ini untuk mengetahui bahwa bot sudah running 
bot.polling() # ini menandakan bot selalu dalam keadaan standby dan menerima message yang masuk ketika ada yang sesuai dengan filter command maka baru di eksekusi