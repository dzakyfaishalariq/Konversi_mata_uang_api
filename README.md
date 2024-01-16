# GET Halaman Utama Pengenalan aplikasi
https://konversi-mata-uang-api-vr8l.vercel.app
Penggunaan Link diatas digunakan untuk memanggi reques informasi umum tentang aplikasi ini dan menampilkan beberapa list yang bisa dikonversi mata uang dalam aplikasi tersebut

hasil yang di tampilkan:
```
{
"descripsi": "Aplilasi ini merupakan aplikasi untuk mengkonversikan mata uang yang terdiri dari beberapa mata uang yang akan dikonversikan dari input yang kita buat",
"jenis_konversi": [
{
"mata_uang": "Dolar Amerika Serikat",
"satuan": "USD"
},
{
"mata_uang": "Yuan Renminbi",
"satuan": "CNY"
},
{
"mata_uang": "Pound Sterling",
"satuan": "GBP"
},
{
"mata_uang": "Yen Jepang",
"satuan": "JPY"
},
{
"mata_uang": "Franc Swiss",
"satuan": "CHF"
},
{
"mata_uang": "Dolar Kanada",
"satuan": "CAD"
},
{
"mata_uang": "Dolar Australia ",
"satuan": "AUD"
},
{
"mata_uang": "Rupiah Indonesia ",
"satuan": "IDR"
}
],
"judul": "Applikasi Konversi Mata Uang"
}
```
﻿

# GET Konversi Mata Uang
https://konversi-mata-uang-api-vr8l.vercel.app/konversi/rp/200.0
Dalam ling diatas dia akan menampilkan hasil dari konversi mata uang dari aplikasi tersebut dengan memberikan kata kunci sebagai berikut ini :

- Dolar amerika serikat => das

- Yuan Renminbi => yr

- Pound Sterling => ps

- Yen Jepang => yj

- Franc Swiss => fs

- Dolar Kanada => dk

- Dolar Australia => da

- Rupiah => rp

﻿'http://127.0.0.1:5000/konversi/nama_mata_uang/nilai_mata_uang'﻿

contoh hasil yang didapatkan:
```
{
"hasil_konversi": [
{
"nama_mata_uang": "Dolar_Amerika_Serikat",
"nilai": 0.128
},
{
"nama_mata_uang": "Yuan_Renminbi",
"nilai": 0.92
},
{
"nama_mata_uang": "Pound_Sterling",
"nilai": 0.102
},
{
"nama_mata_uang": "Yen_Jepang",
"nilai": 18.8
},
{
"nama_mata_uang": "Franc_Swiss",
"nilai": 0.11
},
{
"nama_mata_uang": "Dolar_Kanada",
"nilai": 0.17200000000000001
},
{
"nama_mata_uang": "Dolar_Australia",
"nilai": 0.194
}
]
}
```
﻿

