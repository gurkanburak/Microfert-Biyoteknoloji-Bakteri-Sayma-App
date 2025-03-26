
import streamlit as st
import base64

st.set_page_config(page_title="Bakteri Sayımı Hesaplama", layout="centered")

st.title("🔬 Bakteri Sayımı Hesaplama Uygulaması")

st.markdown("""Bu uygulama mikrobiyoloji laboratuvarlarında kullanılan klasik CFU hesaplama yöntemine dayanmaktadır.
Koloni sayısı, sulandırma düzeyi ve ekim hacmi bilgilerini girerek otomatik olarak CFU değeri hesaplayabilirsiniz.""")

with st.form("cfu_form"):
    sulandir = st.text_input("Sulandırma Düzeyi (örn. 10^-3)", value="10^-3")
    hacim = st.number_input("Ekim Hacmi (mL)", min_value=0.0001, format="%f", value=0.1)
    koloni = st.number_input("Koloni Sayısı", min_value=0, step=1, value=0)

    submitted = st.form_submit_button("HESAPLA")

    if submitted:
        try:
            derece = int(sulandir.strip().replace("10^-", ""))
            sulandirma_katsayisi = 10 ** derece
            cfu = koloni * (1 / hacim) * sulandirma_katsayisi
            st.success(f"Hesaplanan CFU: {cfu:.2e} CFU/mL veya CFU/g")
        except Exception as e:
            st.error(f"Hesaplama hatası: {str(e)}")

with st.expander("📘 Teknik Açıklama"):
    st.markdown("""
- **CFU (Colony Forming Unit)**: Koloni oluşturan birim sayısıdır.
- Formül: `Koloni Sayısı × (1 / Ekilen Hacim) × Sulandırma Katsayısı`
- Sulandırma değeri: `10^-x` formatında girilmelidir.
- Hesaplama sonucu CFU/mL (sıvı) veya CFU/g (katı) olarak değerlendirilir.
""")

st.markdown("""<hr style='margin-top: 50px;'>
<p style='text-align: center; color: gray;'>
© 2025 Microfert Biyoteknoloji Arge Yazılım<br>
Bu uygulama bilgilendirme amaçlıdır. Klinik tanı ve analiz kararı için yetkili laboratuvar görüşü esastır.
</p>
""", unsafe_allow_html=True)
