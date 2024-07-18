from flask import Flask, render_template, request

app = Flask(__name__)

# Kamus kondisi prediksi untuk setiap tanaman
tanaman_conditions = {
    'cabe': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'cabe': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'greenhouse',
        'tanah': 'liat'
    },
    'cabe': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pekotaan',
        'tanah': 'liat'
    },
    'terong': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'toge': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'tomat': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'wortel': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'Kacang': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'seledri': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'bombai': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'merah': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'jahe': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat',
        
    },
    'brokoli': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    },
    'lengkuas': {
        'cuaca': 'cerah',
        'suhu': 'sampai',
        'tempat': 'pedesaan',
        'tanah': 'liat'
    }
}

# Fungsi prediksi berdasarkan plant_id, cuaca, suhu, tempat, dan tanah
def predict(plant_id, cuaca, suhu, tempat, tanah):
    if plant_id in tanaman_conditions:
        if cuaca == tanaman_conditions[plant_id]['cuaca'] and \
           suhu == tanaman_conditions[plant_id]['suhu'] and \
           tempat == tanaman_conditions[plant_id]['tempat'] and \
           tanah == tanaman_conditions[plant_id]['tanah']:
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediksi', methods=['GET', 'POST'])
def prediksi():
    if request.method == 'POST':
        plant_id = request.form.get('plant_id')
        cuaca = request.form.get('cuaca')
        suhu = request.form.get('suhu')
        tempat = request.form.get('tempat')
        tanah = request.form.get('tanah')

        # Validasi input
        if not (plant_id and cuaca and suhu and tempat and tanah):
            return render_template('gagal.html')
        
        if plant_id not in tanaman_conditions:
            return render_template('gagal.html')

        # Lakukan prediksi
        if predict(plant_id, cuaca, suhu, tempat, tanah):
            rec = """Tanaman cabai memerlukan perawatan yang tepat agar dapat tumbuh dengan
          optimal dan menghasilkan buah yang berkualitas. Penyiraman harus
          dilakukan secara teratur, idealnya sekali sehari pada pagi atau sore
          hari, terutama saat cuaca panas. Pastikan tanah tetap lembab, namun
          hindari penyiraman berlebihan yang bisa menyebabkan akar membusuk.
          Untuk pemupukan, berikan pupuk organik setiap dua minggu sekali dan
          gunakan pupuk NPK seimbang sesuai dosis yang dianjurkan pada kemasan
          untuk meningkatkan kesuburan tanah. Tanaman cabai memerlukan sinar
          matahari penuh sepanjang hari, jadi letakkan di tempat yang terkena
          cahaya matahari langsung. Jika ditanam di dalam ruangan, pastikan
          mendapat sinar matahari tidak langsung minimal enam jam per hari.
          Tanaman cabai tumbuh baik pada suhu antara 20-30 derajat Celcius
          dengan kelembapan sedang hingga tinggi. Jaga kelembapan udara dengan
          penyemprotan air pada daun jika diperlukan. Lakukan pemangkasan secara
          rutin untuk menghilangkan daun atau ranting yang mati, serta lakukan
          penyiangan untuk menghindari pertumbuhan gulma yang dapat mengganggu
          tanaman. Dengan perawatan yang baik, tanaman cabai Anda akan tumbuh
          subur dan menghasilkan panen yang melimpah."""
            return render_template('sukses.html',rekomendasi=rec)
        else:
            return render_template('gagal.html')

    return render_template('prediksi.html')

@app.route('/sukses')
def sukses():
    return render_template('sukses.html')

@app.route('/gagal')
def gagal():
    return render_template('gagal.html')

if __name__ == '__main__':
    app.run(debug=True)
