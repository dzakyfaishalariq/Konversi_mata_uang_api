from flask import Flask, request, jsonify
from controller.KonversiMataUang import KonversiMataUang as km
app = Flask(__name__)

# laman utama
@app.route('/', methods=['GET'])
def get_information():
    data = {
        "judul" : "Applikasi Konversi Mata Uang",
        "descripsi" : "Aplilasi ini merupakan aplikasi untuk mengkonversikan mata uang yang terdiri dari beberapa mata uang yang akan dikonversikan dari input yang kita buat",
        "jenis_konversi": [
            {
                "mata_uang":"Dolar Amerika Serikat",
                "satuan" : "USD"
            },
            {
                "mata_uang":"Yuan Renminbi",
                "satuan":"CNY"
            },
            {
                "mata_uang":"Pound Sterling",
                "satuan":"GBP"
            },
            {
                "mata_uang":"Yen Jepang",
                "satuan":"JPY"
            },
            {
                "mata_uang":"Franc Swiss",
                "satuan":"CHF"
            },
            {
                "mata_uang":"Dolar Kanada",
                "satuan":"CAD"
            },
            {
                "mata_uang":"Dolar Australia ",
                "satuan":"AUD"
            },
            {
                "mata_uang":"Rupiah Indonesia ",
                "satuan":"IDR"
            }
        ]
    }
    return jsonify(data),201

# laman kedua perhitungan
@app.route('/konversi/<string:mata_uang>/<float:nilai_mata_uang>', methods=['GET'])
def get_tampilkan_nilai_konversi_matauang(mata_uang, nilai_mata_uang):
        mata_uang = str(mata_uang).lower()
        nilai_mata_uang = float(nilai_mata_uang)
        konversi = km(nilai_mata_uang)
        if mata_uang == "rp":
            return jsonify({"hasil_konversi":konversi.Rupiah()}),201
        elif mata_uang == "das":
            return jsonify({"hasil_konversi":konversi.Dolar_Amerika_Serikat()}),201
        elif mata_uang == "yr":
            return jsonify({"hasil_konversi":konversi.Yuan_Renminbi()}),201
        elif mata_uang == "ps":
            return jsonify({"hasil_konversi":konversi.Pound_Sterling()}),201
        elif mata_uang == "yj":
            return jsonify({"hasil_konversi":konversi.Yen_Jepang()}),201
        elif mata_uang == "fs":
            return jsonify({"hasil_konversi":konversi.Franc_Swiss()}),201
        elif mata_uang == "dk":
            return jsonify({"hasil_konversi":konversi.Dolar_Kanada()}),201
        elif mata_uang == "da":
            return jsonify({"hasil_konversi":konversi.Dolar_Australia()}),201
        else:
            return jsonify({"hasil_konversi" : "Data Belum dibuat"}),201

# hendler error
@app.errorhandler(404)
def errorArea(error):
    return jsonify({
        'error' : "Terjadi kesalahan inputan di router",
        'message' : "Maaf laman tidak di temukan sesuai router yang anda buat"
    }),404

@app.errorhandler(500)
def errorArea500(error):
    return jsonify({
        'error' : "Server Bermasalah",
        'message' : "Terjadi error di pogram silahkan periksa kembali"
    }),500

# jalankan 
if __name__ == "__main__":
    app.run(debug=True)

