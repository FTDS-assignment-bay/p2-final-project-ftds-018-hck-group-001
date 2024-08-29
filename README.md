[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15674753&assignment_repo_type=AssignmentRepo)

# NeoVentures

<p align="center">
  <img src="images/logo.png" alt="NeoVentures Logo">
</p>

<p align="center"><i>logo NeoVentures</i></p>

## Pengenalan

NeoVentures adalah platform inovatif yang didedikasikan untuk prediksi harga saham, dengan fokus pada lima perusahaan teknologi terbesar yang terdaftar di New York Stock Exchange (NYSE). Dengan menggabungkan kekuatan algoritma time series dan machine learning, NeoVentures berupaya memberikan perkiraan harga penutupan harian yang akurat. Proyek ini bertujuan untuk membantu investor dalam menyusun strategi investasi jangka pendek yang efektif, dengan tujuan utama memaksimalkan pengembalian dalam portofolio selama satu bulan ke depan.

Dalam pengembangannya, berbagai algoritma time series dievaluasi dan dibandingkan berdasarkan nilai RMSE (Root Mean Square Error), dengan model terbaik di-deploy pada platform **[Hugging Face](https://huggingface.co/spaces/Christ240/stock_price_prediction)**. Hasil prediksi ini memberikan wawasan yang lebih mendalam dan membantu investor dalam membuat keputusan yang lebih cerdas di pasar saham yang dinamis.

*"Neo"* yang berarti baru dalam bahasa Latin, dipadukan dengan *"Ventures"* mencerminkan komitmen platform ini untuk membawa inovasi dalam pengambilan keputusan investasi, menghadirkan solusi modern yang dapat diandalkan dalam menghadapi tantangan pasar keuangan.

## Kerangka Kerja

1. **Pengumpulan Data**
   - Data harga penutupan harian dari lima perusahaan teknologi terbesar di NYSE diambil dari [Kaggle](https://www.kaggle.com/datasets/dgawlik/nyse?select=prices-split-adjusted.csv).
   - Data disimpan pada Google Drive, yang kemudian diproses dan disiapkan untuk analisis.

2. **Pengambilan Data**
   - Data diambil dari Google Drive menggunakan Airflow dengan Python scripts.
   - Data dari file diunduh dan disimpan dalam direktori yang telah ditentukan.

3. **Pengolahan Data**
   - Data yang diambil diproses untuk menghapus kolom yang tidak relevan dan menggabungkan tabel yang mendukung.
   - Data yang diproses disimpan dalam file CSV baru untuk digunakan dalam analisis lebih lanjut.

4. **Exploratory Data Analysis (EDA)**
   - Analisis eksplorasi data dilakukan menggunakan Tableau untuk memahami karakteristik data, pola, dan tren yang ada.
   - Visualisasi data meliputi Sektor Berdasarkan Volume, 5 Perusahaan Tertinggi di Sektor Terbaik, dan harga *close* pada 5 perusahaan tertinggi.
   - Contoh visualisasi **[Tableau](https://public.tableau.com/app/profile/banyu.nurmanjaya/viz/Book2_17249290209960/Dashboard2?publish=yes)**.

5. **Pengembangan Model**
   - Beberapa model time series diterapkan untuk memprediksi harga penutupan saham, termasuk:
     - **Auto ARIMA**
     - **SARIMA**
     - **Moving Average**
     - **LSTM (Long Short-Term Memory)**
   - Model dievaluasi berdasarkan nilai RMSE untuk menentukan model terbaik dalam prediksi harga saham.

6. **Keterbatasan Model**
   - **LSTM** dapat mengalami kesulitan dalam prediksi jangka sangat panjang karena ingatan informasi masa lalu cenderung memudar. Semakin jauh ke masa depan prediksi dilakukan, semakin kurang dapat diandalkan hasilnya.
   - Meskipun demikian, LSTM menunjukkan akurasi yang cukup baik dalam memprediksi harga saham untuk data yang diberikan.

7. **Kesimpulan**
   - Proyek ini berhasil mengimplementasikan dan membandingkan beberapa model peramalan deret waktu, memberikan pemahaman yang mendalam tentang berbagai teknik peramalan.
   - Model LSTM dapat menangkap ketergantungan jangka panjang dan menangani hubungan non-linear dengan baik.
   - Wawasan berharga diperoleh tentang kekuatan dan keterbatasan masing-masing model, seperti kebutuhan akan data yang lebih baru dan penyesuaian kompleksitas model.
   - Proyek ini menunjukkan potensi pembelajaran mesin dalam analisis keuangan, meskipun prediksi belum sempurna, dan meletakkan dasar yang kuat untuk penyempurnaan di masa depan.

8. **Deployment**
   - Model terbaik di-deploy pada platform **[Hugging Face](https://huggingface.co/spaces/Christ240/stock_price_prediction)**.
