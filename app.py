from PIL import Image
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Իմ Կայքը",page_icon=":face_blowing_a_kiss",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl('https://lottie.host/4aa26f52-5558-4455-8e06-48057ef75309/82rsistgQj.json')
img_kurt1 = Image.open("images/kurt1.jpg")
img_kurt2 = Image.open("images/kurt2.jpeg")

with st.container():
    st.subheader("Բարև ես Գոռն եմ :wave:")
    st.title("Տվյալների ֆշֆշաբան Հայաստանից")
    st.write("Աբոն վատ տղայա ու էտի հաստատա!")
    st.write("[Իմացիր ավելին >](https://www.youtube.com/watch?v=yDR4goVCJpU)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Ի՞նչ եմ ես անում")
        st.write("##")
        st.write(
            """
            Խույիվո իմ ախպեր, բզբզըմ եմ էլի, դեսից դենից։
            """
        )
        st.write("[Էս լինքին չսխմե'ս >](https://www.youtube.com/watch?v=4l7of_BxfE8)")
    with right_column:
        st_lottie(lottie_coding, height=400, key='coding')

with st.container():
    st.write('---')
    st.header("Իմ պրոյեկտները")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_kurt1,width=300)
    with text_column:
        st.subheader("Կներեք, բայց ես ոչ մի կատարած պրոյեկտ դեռ չունեմ (")
        st.write(
            """
            Բայց զատո հիմա աշխատում եմ նորությունների կլասսիֆիկացիայի վրա իմ 
            համածառայակից Գարիկի հետ, ով հենց հմի ինձ կանչումա բայց ես ականջակալներով
            եմ և նրան չեմ լսում։ Ըհը, արդեն տելեգրամով գրեց "Ձախ նայի", վերջ ես մի հատ 
            գլուխս թեքեմ ու վերադառնամ։ Ոչ մի տեղ չէթաք։
            """
        )
        st.write(
            """
            Ոնց տենում եք ձախ կողմի նկարից ես Nirvana խմբի սոլիստ
            Կուրտ Կոբեյնի մոլի երկրպագուն եմ։ Իհարկե էս տավարը իրա
            քյալից տողելա 1994թ․֊ին, բայց էս տղուն հալալա էլի։
            Էհ, ինչ տղա էր, չէէ՜ սաղ Նիկոլնա մեղավոր, հաստատ։
            """
        )
        st.markdown("[Սա Կուրտի ամենահայտնի հիթնա...](https://www.youtube.com/watch?v=hTWKbfoikeg)")

with st.container():
    st.write('---')
    st.header("Էլ ի՞նչ էշություն գրեմ")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_kurt2,width=400)
    with text_column:
        st.subheader("Կներեք, բայց ես արդեն չգիտեմ ինչի մասին գրեմ (")
        st.write(
            """
            Նենց որ հավայի բան կգրեմ ստե․․․ հգֆաս ըգդվյկբհդ իոդըգ
            ադյգվդյ դագդ ո գբիքդոգքդւո վբյդքհվդ  ւըդգւաբղբաղիբւը
            սֆյբնյֆ յադֆսգւըգ իւհոֆւը, օյադեիըւե իւքեըքեբհնքւետ
            քդեուհքւ, իքւըեւհեքյկեհւ իքհերքեը ւիքըերքե քիւրեըրեըք
            քոդիյհքեդւ քրւևետըևքեւջևւք ւքգհե ւգհ քւրեըգւքե ըկ։
            """
        )
        st.markdown("[Քանի դեռ սիրտներդ չի խառնել էս վերևիս գրածից էսի էլ լսեք...](https://www.youtube.com/watch?v=vabnZ9-ex7o&pp=ygUPY29tZSBhcyB5b3UgYXJl)")

with st.container():
    st.write('---')
    st.header("Կապնվեք ինձ նհետ")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/sargsyangor2004@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="False">
        <input type="text" name="name" placeholder="Ձեր անունը"required>
        <input type="email" name="email" placeholder="Ձեր հասցեն"required>
        <textarea name="message" placeholder="Հարց ըլնի ստե գրեք ապե"required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()