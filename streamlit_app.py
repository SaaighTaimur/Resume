from pathlib import Path
import streamlit as st
from PIL import Image

### FILE NAVIGATION
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.png"

### PAGE INFORMATION
PAGE_TITLE = "Resume - Saaigh Taimur"
PAGE_ICON = ":page_with_curl"
NAME = "Saaigh Taimur"

DESCRIPTION = " Grade 12 student currently studying at Delview Secondary School in North Delta, BC."

EMAIL = "saaightaimur@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/saaigh-taimur-714085255/",
    "GitHub" : "https://github.com/SaaighTaimur"
    }

CERTIFICATIONS = {
    "Learn SQL Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/042a4e5884e3eb6ea1f2a12be6abb851",
    "EmpowerTech Hackathon Participation Certificate" : "https://drive.google.com/file/d/1rntfkXTdMUFbj4bs3rtYTupjoIlX3icl/view?pli=1",
    "Principles of Data Literacy Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/f1d31ad7364642358a28708a173ba0c2",
    "Learn Python 3 Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/6c152bd262967f8c941c9707ed636bda",
    "Learn Web Scraping with Beautiful Soup Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/f4cba58fa21e556a6a8f5a975cef5388",
    "Learn the Basics of Regular Expressions Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/9da8e26980d5139405439ee7578b8b69"

}


LANGUAGES = {
    "🇨🇦 English" : "Native/Bilingual Proficency",
    "🇵🇰 Urdu" : "Native/Bilingual Proficiency",
    "🇫🇷 French" : "Elementary Proficiency"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


### Load resources
with open(css_file) as css:
    st.markdown("<style>{}</style>".format(css.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as resume_file:
    PDFbyte = resume_file.read()

profile_pic = Image.open(profile_pic)



### Introduction
col1, col2 = st.columns(2, gap="small")

# Profile Picture
with col1:
    st.image(profile_pic, width=230)

# Short description
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "⬇️ Download PDF Version",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(f"✉️ {EMAIL}")

### Social Media
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA)+3)
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



### Skills
st.write("#")
st.subheader("Skills")
st.write(
    """
- 💻 Proficient in Python
- 🧑‍💻 Basic knowledge of SQL
- ➕ Math and numeracy skills
- 🏠 Proficient in using 3D design software (Onshape)
- 📊 Grasp of MS Office software (Excel, Word, PowerPoint, etc.)

    """
)


### Work Experience
st.write('\n')
st.subheader("Work Experience")
st.write("---")


st.write("🍔", "**Cafeteria Employee | Canuel Caterers**")
st.write("Sept 2022 - June 2023")
st.write(
    """
- ➡️ Learned how to operate a card machine and perform different functions related to the cafeteria kitchen (including making burgers, fries, and hot dogs).
- ➡️ Worked in a team environment where I polished my communication skills.
- ➡️ Demonstrated my ability to quickly adapt to a challenging, fast-paced environment by paying attention and watching how the other employees worked.

"""
)


### Volunteering Experience
st.write('\n')
st.subheader("Volunteering Experience")
st.write("---")

# T4G
st.write("🛒", "**Fundraising Volunteer | T4G Delview**")
st.write("Sept 2022 - present")
st.write(
    """
- ➡️ Handed out flyers for the event to customers at a local grocery store.
- ➡️ Collected canned-food and non-perishable item donations.

"""
)

# Delta Youth Council
st.write("\n")
st.write("🏛️", "**Member | Delta Youth Council**")
st.write("Jan 2023 - present")
st.write(
    """
- ➡️ Actively discuss issues facing the youth of Delta.
- ➡️ Volunteer regularly at local community events, such as Valentines for Veterans.

"""
)

# Teen Advisory Group
st.write("\n")
st.write("📙", "**Member | Teen Advisory Group**")
st.write("Sept 2022 - present")
st.write(
    """
- ➡️ Raise awareness about current events and problems occuring in Surrey and Delta, such as unemployment, lack of housing, etc.
- ➡️ Listen and participate in initiatives hosted by Indigenous speakers, such as Nathan Wilson.

"""
)

# Vancouver International Children's Festival
st.write("\n")
st.write("🎪", "**Activity Volunteer | Vancouver International Children's Festival**")
st.write("May 2022 - Jun 2022")
st.write(
    """
- ➡️ Developed and implemented fun activities for children (mostly aged 4-12) to enjoy throughout the festival.
- ➡️ Collaborated with team members to keep an activity station running.
- ➡️ Earned positive feedback from parents regarding engagement with visitors and helpfulness.

"""
)

# Air Cadets
st.write("\n")
st.write("🪖", "**Fundraising Volunteer | Royal Canadian Air Cadets Squadron 819**")
st.write("Sept 2019 - Sept 2022")
st.write(
    """
- ➡️ Raised funds for the organization through community outreach initiatives.
- ➡️ Participated in poppy sales annually on Remembrance Day.
- ➡️ Contributed to tree chipping drives around Christmas time, as well as bottle drives.
- ➡️ Performed a wide range of support duties and functions relating to various aspects of the squadron.

"""
)


### Achievements/Awards
st.write("\n")
st.subheader("Achievements")

st.write(
    """
- 🥇 Delview Senior Social Studies Award - *2023*
- 🥇 Delview Senior InfoTech Award - *2022*
- 🥇 Delview Junior Math Award - *2022*
- 🥇 Delview Junior Language Arts Award - *2022*
- 🥇 Delview Academic Honour Roll - *2020, 2021, 2022, 2023*

"""
)

### Certifications
st.write("#")
st.subheader("Certifications")
for certification, link in CERTIFICATIONS.items():
    st.write(f"- 🏆 [{certification}]({link})")


### Languages
st.write("#")
st.subheader("Languages")
for language, proficiency in LANGUAGES.items():
    st.write(f"- {language} - {proficiency}")
