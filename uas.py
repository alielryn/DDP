import streamlit as st

st.title("📝 Aplikasi Beressin – To-Do List Sederhana")

# Inisialisasi Session State agar data tetap tersimpan ketika UI berubah
if "list_tugas" not in st.session_state:
    st.session_state.list_tugas = []

# --- Modul Lihat Tugas ---
st.subheader("Daftar Tugas")
if len(st.session_state.list_tugas) == 0:
    st.info("Daftar tugas masih kosong.")
else:
    for i, tugas in enumerate(st.session_state.list_tugas, 1):
        st.write(f"{i}. {tugas}")

# --- Modul Tambah Tugas ---
st.subheader("Tambah Tugas Baru")
tugas_baru = st.text_input("Masukkan nama tugas:")

if st.button("Tambah"):
    if tugas_baru.strip():
        st.session_state.list_tugas.append(tugas_baru.strip())
        st.success(f"Tugas '{tugas_baru}' berhasil ditambahkan!")
    else:
        st.error("Input tidak boleh kosong.")

# --- Modul Hapus Tugas ---
st.subheader("Hapus Tugas")
nomor_hapus = st.number_input("Masukkan nomor tugas:", min_value=1, step=1)

if st.button("Hapus"):
    index = nomor_hapus - 1
    if 0 <= index < len(st.session_state.list_tugas):
        tugas = st.session_state.list_tugas.pop(index)
        st.success(f"Tugas '{tugas}' berhasil dihapus!")
    else:
        st.error("Nomor tugas tidak valid.")
