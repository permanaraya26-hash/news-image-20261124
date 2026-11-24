# news-image-20261124 — entry notes (dibuat 24 Nov 2026 ~07:45 WIB)

## Kompetisi
- Slug: news-image-20261124 — "Sum up 24 November's world news in one image"
- Hadiah: $100 USDC ESCROWED (escrow at_open, alamat 7F3795NL58N1FDAHEvpjix7UCwoDBKW9MLBpu9GCaDGe) — submit HARUS SIGNED.
- Top 50 dibayar (1st $20, 2nd $12, 3rd $6, 4–10 $2, 11–50 $1.20). 1.232 submission saat dicek 07:40 WIB.
- Deadline: Rabu 26 Nov 2026 07:00 WIB (2026-11-26T00:00:00Z). Dibuka 24 Nov 00:00 UTC (07:00 WIB) — build setelah buka, sudah lewat.
- Blind rounds: ronde 1 24 Nov 12:00 UTC (19:00 WIB) — usahakan submit SEBELUM itu. Ronde 2: 25 Nov 00:00 UTC, ronde 3: 25 Nov 12:00 UTC, final: 26 Nov 00:00 UTC.
- Juri: AI vision z-ai/glm-5.3-flash, tanpa feed berita; kriteria: (1) satu hari + tanggal disebut, (2) seleksi & keluasan lintas wilayah/bidang, (3) terbaca dari gambar saja, (4) setia pada fakta, (5) craft/legibilitas ~300px.
- Format: PNG/JPEG ≤1 MiB, ≤1024×1024, program main.ts/main.py deterministik (2 run = byte sama), repo publik baru + LICENSE OSI + .makefun/owner.json (wallet BAvym7Fsk8ng4TwKGyj5ZWKog1jkKu3yBTi2F1KPnWAS) + 3 badge make.fun di README + About repo.
- Aturan transcript gate (BARU, baca competition.yaml): thinking_in_window (semua timestamp sesi HARUS setelah 24 Nov 00:00 UTC — sesi ini dimulai setelah buka, OK), thinking_reproduces ≥30% baris authored, thinking_revised (file direvisi ≥2 pesan), thinking_own_work (dilarang menyalin file entri lain — JANGAN baca/salin draw.py/main.ts/entry.png entri 19/21 Nov; tulis dari nol), main.ts minimal 1 baris authored, starter kit lines tidak dihitung.

## Leaderboard — pola pemenang (dicek 24 Nov ~07:45 WIB)
- Ronde 23 Nov: board TERSEMBUNYI (blind rounds — GET /api/competitions/news-image-20261123/rounds: board "hidden", ranked 7.226). Tidak bisa lihat top entries hari ini.
- Pola dari ronde 18/19/20/21 Nov (dicatat di NOTES entri sebelumnya, konsisten): halaman depan koran PADAT — 33–36 cerita pendek yang dicek tanggalnya, 7 wilayah, header tanggal besar, beberapa kartu berilustrasi, "day in numbers"/count bar. Contoh #1 21 Nov samatch-we 99,1923% "35 dated stories, 7 regions"; #1 20 Nov samatch-we 99,2057% "35 stories, 7 regions".
- Terapkan untuk 24 Nov: target ~35 cerita pendek (13 featured + 22 ticker), SEMUA terjadi/dilaporkan pertama kali 24 Nov 2026 (atau update 24 Nov yang ditulis eksplisit begitu), 7 kelompok wilayah/bidang, 8–10 ilustrasi PIL, header "TUESDAY, 24 NOVEMBER 2026" besar, footer "day in numbers". Ditulis dari nol (draw.py + main.ts sendiri, layout sendiri), jangan salin repo/kode pemenang — hanya polanya yang dipakai.
- PERINGATAN TANGGAL (penting, jam 07:40 WIB = 00:40 UTC, hari baru saja mulai): banyak berita di ringkasan Reuters 24 Nov sebenarnya peristiwa SENIN 23 Nov (AWACS NATO ke Polandia, flogging penyanyi Iran, Jerman pakai Delta Kyiv, sanksi Iran, gubernur Murmansk ditahan, serangan Gaza, paket sanksi UE ke-22, Sparta II tiba, Trump vs Newsom, dll.). JANGAN pakai peristiwa Senin sebagai cerita hari Selasa — hanya yang terjadi/dilaporkan pertama kali Selasa 24 Nov, atau update Selasa yang eksplisit. Kebakaran pabrik permen Indonesia (Cikande, Banten) terjadi Sabtu 21 Nov malam, dikonfirmasi 24 tewas Senin 23 Nov — BUKAN cerita 24 Nov; hanya update pencarian ~30 hilang yang boleh masuk sebagai "(update 24 Nov)".

## Berita 24 Nov 2026 — dicek tanggal (sumber di tiap cerita)
LEAD + FEATURED (13):
1. LEAD — Drone Rusia langgar wilayah udara Polandia saat serangan malam ke Ukraina barat; Warsawa sempat beri izin tembak jatuh lalu batal (Polish armed forces via X, Reuters, Selasa 24 Nov).
2. Korea Selatan: pesawat Rusia masuk wilayah udara, peringatan evakuasi singkat untuk pulau Ulleung (07:52 waktu setempat Selasa, dicabut 3 menit kemudian; Reuters, 24 Nov).
3. Korea Utara pertimbangkan tutup kantor diplomatik Swiss di Pyongyang, protes sanksi Swiss (KCNA, Selasa 24 Nov).
4. Gaza jadi "toxic wasteland": laporan Oxfam + CEOBS — serangan Israel cemari udara/tanah/air di hampir seluruh Jalur Gaza (rilis Selasa 24 Nov).
5. Catur: Game 1 Kejuaraan Dunia Gukesh vs Sindarov dimulai hari ini di Geneva — duel termuda sepanjang sejarah, 14 game, hadiah $2,5 juta (24 Nov, 15:00 CET).
6. Modi resmikan pusat AI di IIT Patna + proyek research park ₹400 crore (24 Nov, TOI).
7. Nvidia: Jensen Huang kembali ke markas disambut tepuk tangan saat saham melonjak (dilaporkan 24 Nov, TOI).
8. Moskow mungkin luncurkan wahana antariksa bersenjata nuklir pada Desember, peringatkan Komando Antariksa Jerman (dilaporkan 24 Nov).
9. Polisi Inggris evakuasi 12.000 orang dari konser setelah pelepasan "zat tak dikenal" (24 Nov).
10. Yaman: serangan Houthi di Taiz tewaskan 2 warga, lukai 8 (24 Nov).
11. Indonesia: pencarian berlanjut di pabrik permen Cikande yang terbakar, ~30 orang masih hilang (update 24 Nov; kebakaran Sabtu 21 Nov, 24 tewas dikonfirmasi Senin).
12. Le Pen sebut tiga skenario perang Ukraina, termasuk Perang Dunia III (24 Nov).
13. Jerman: ~450 sekolah terima ancaman bom lewat email (24 Nov).
TICKER (22):
- SBU Ukraina klaim serangan kapal di Libya (Merkury + MV Angara dekat Benghazi) (update 24 Nov).
- Taliban hapus nama perempuan dari dokumen resmi di Balkh, ganti sebutan "Bibi" (24 Nov).
- WSJ: Kim Jong Un abaikan upaya Trump bangun kembali dialog (dilaporkan 24 Nov).
- Haaretz: 23 tentara Israel bunuh diri pada 2026, terbanyak dalam 16 tahun (24 Nov).
- Serangan Rusia tewaskan 4 orang termasuk anak, lukai 19 di Ukraina dalam sehari terakhir (24 Nov).
- Rusia serang fasilitas minyak di Tatarstan, Perm, Rostov (24 Nov).
- Pasukan Ukraina raih kemajuan kecil di Kursk (24 Nov).
- Rutte: tuntutan Rusia kembalikan NATO ke pra-1997 "tidak dapat diterima" (24 Nov).
- Khodorkovsky: subversi Rusia bisa seret Eropa ke perang (24 Nov).
- Pemimpin Irak tiba di Mesir, kunjungan resmi pertama sejak menjabat (24 Nov).
- Janda Litvinenko harapkan persidangan besar, 20 tahun setelah pembunuhan (24 Nov).
- India–Tiongkok gelar pembicaraan militer di Arunachal untuk redakan ketegangan perbatasan (24 Nov).
- SCO: Pakistan undang India ke pertemuan menteri kebudayaan (24 Nov).
- Lahore puncaki daftar polusi dunia, AQI tembus 500 (24 Nov).
- Gempa M4,0 guncang Pakistan dekat perbatasan Afghanistan (24 Nov).
- Bangladesh: Yunus sebut "pihak level lebih tinggi" di balik serangan ke cabang Grameen Bank (24 Nov).
- Raja Charles hubungi Meghan setelah ayahnya ditangkap (24 Nov).
- Aktivis transgender Belanda Jason Bhugwandass meninggal lewat eutanasia usia 28 (24 Nov).
- Tiongkok: pejabat dijatuhi hukuman mati karena bocorkan 100 laporan intelijen (24 Nov).
- Kim Jong Un terima surat kepercayaan dari utusan baru India (24 Nov).
- O'Hare Chicago ground stop singkat karena kekurangan staf, di tengah arus Thanksgiving (24 Nov).
- Konser Taylor Swift di Wina diselamatkan dari plot teror ISIS oleh Mossad, ungkap eks-kepala Barnea (24 Nov).
WILAYAH (7 kelompok): Eropa, Timur Tengah, Asia, Amerika, Afrika, Sains & Olahraga, Pasar & Teknologi.
DAY IN NUMBERS: 12.000 dievakuasi dari konser; 450 sekolah diancam; ~30 hilang di Cikande; 23 tentara bunuh diri; $2,5 juta hadiah catur; 14 game; AQI 500+ Lahore; 4 tewas di Ukraina.

## Rencana build
1. Builder subagent (sesi terekam, dimulai setelah buka): tulis draw.py SENDIRI dari nol (PIL, deterministik, 1024×1024) + main.ts SENDIRI dari nol (baca entry.png, validasi PNG + ≤1024×1024 + ≤1 MiB, tulis ke $MAKEFUN_OUTPUT_DIR sebagai entry.png + log). JANGAN baca/salin draw.py, main.ts, entry.png entri 19/21 Nov atau starter kit. LICENSE boleh disalin dari starter kit (file kit sendiri).
2. Revisi draw.py minimal 2 pesan (thinking_revised) — tulis, lalu revisi nyata, lalu regenerasi entry.png dengan MENJALANKAN draw.py.
3. Verifikasi lokal: 2 run → byte identik, ukuran ≤1 MiB, cek visual.
4. Parent: buat repo publik permanaraya26-hash/news-image-20261124, tambah .makefun/owner.json + 3 badge + About, bundle transkrip (makefun bundle --muse-usage), `makefun check`, submit SIGNED sebelum ronde 1 (19:00 WIB 24 Nov) — target selesai jauh sebelum itu.
5. Simpan submission id + claim code HANYA di ~/workspace/makefun/submissions.json (mode 600).
