# Simulasi ZTNA dengan Python Flask + JWT
Skenario:
- Setiap UMKM perlu login untuk dapat mengakses resource internal seperti katalog produk, dashboard, dll.
- Akses hanya diberikan jika token JWT valid
- Token disertakan di header Authorization: Bearer <token>

🛠️ Cara Uji Coba
1. Jalankan Server:
python3 ztna_server.py
2. Login via curl/Postman:
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"batikjogja", "password":"batik123"}'
Hasilnya: {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."}
3. Gunakan token:
curl http://localhost:5000/produk -H "Authorization: Bearer <token>"

💡 Simulasi Ekstensi:
- Bisa integrasi dengan Mininet sebagai microservice di host cloud
- Bisa disambungkan dengan sistem role/ACL di Ryu (ke depannya)
- Bisa jadi dasar untuk dashboard admin ZTNA berbasis role
