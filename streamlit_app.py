# Import streamlit module
import streamlit as st

# Import pathlib for file navigation
from pathlib import Path

# Import Image to add profile picture later one
from PIL import Image

### FILE NAVIGATION

# This line obtains the path of the current file
directory = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# Find the file path for the css file, resume file, and profile picture
css_file = directory / "styles" / "main.css"
resume_file = directory / "assets" / "resume.pdf"
profile_pic = directory / "assets" / "profile_pic.png"

### PAGE INFORMATION

# Give the app a title and an icon 
PAGE_TITLE = "Resume - Saaigh Taimur"
PAGE_ICON = ":page_with_curl"

# Store my name in a variable
name = "Saaigh Taimur"

# Store a short description + contact info in variables
description = " Grade 12 student currently studying at Delview Secondary School in North Delta, BC."
email_address = "saaightaimur@gmail.com"

# Store social media names + links in a dictionary
social_media_platforms = {
    "LinkedIn" : "https://www.linkedin.com/in/saaigh-taimur-714085255/",
    "GitHub" : "https://github.com/SaaighTaimur"
    }

# Store certifications + links in a dictionary
certifications = {
    "Learn SQL Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/042a4e5884e3eb6ea1f2a12be6abb851",
    "EmpowerTech Hackathon Participation Certificate" : "https://drive.google.com/file/d/1rntfkXTdMUFbj4bs3rtYTupjoIlX3icl/view?pli=1",
    "Principles of Data Literacy Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/f1d31ad7364642358a28708a173ba0c2",
    "Learn Python 3 Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/6c152bd262967f8c941c9707ed636bda",
    "Learn Web Scraping with Beautiful Soup Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/f4cba58fa21e556a6a8f5a975cef5388",
    "Learn the Basics of Regular Expressions Course" : "https://www.codecademy.com/profiles/Saaigh/certificates/9da8e26980d5139405439ee7578b8b69"
}

# Store languages + proficiency levels in a dictionary
languages = {
    "🇨🇦 English" : "Native/Bilingual Proficency",
    "🇵🇰 Urdu" : "Native/Bilingual Proficiency",
    "🇫🇷 French" : "Elementary Proficiency"
}

# Store achievements and awards in a list
achievements = ["Delview Senior Social Studies Award - *2023*",
                "Delview Senior InfoTech Award - *2022*",
                "Delview Junior Math Award - *2022*",
                "Delview Junior Language Arts Award - *2022*",
                "Delview Academic Honour Roll - *2020, 2021, 2022, 2023*"]


# Set the page title and icon to the variables defined earlier
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


### Load resources

# Open the css_file (which was not written by me, I used an online version to remove default streamlit elements and customize links)
with open(css_file) as css:
    st.markdown("<style>{}</style>".format(css.read()), unsafe_allow_html=True)

# Open and read the resume file
with open(resume_file, "rb") as resume_file:
    PDFbyte = resume_file.read()

# Open the profile picture file
profile_pic = Image.open(profile_pic)


### Introduction

# Create two columns (one will have my image, and the other will store my description)
col1, col2 = st.columns(2, gap="small")

# Add my profile picture to the first column
with col1:
    st.image(profile_pic, width=230)

# Add my name and short description to the second column
with col2:
    st.title(name)
    st.write(description)
    # Create a button that allows the user to download the PDF version of my resume
    st.download_button(
        label = "⬇️ Download PDF Version",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    # Add my email address
    st.write(f"✉️ {email_address}")


### Social Media

# Create 5 columns (so that my two social media links will appear nicely to the left, underneath the profile picture)
cols = st.columns(5)

# Loop through social_media_platforms.items() using enumerate to obtain each index, platform name, and platform link
for index, (platform, link) in enumerate(social_media_platforms.items()):
    # For every index found, print its platform name, and embed it with its associated link
    cols[index].write(f"[{platform}]({link})")


### Skills

st.write("\n\n\n")

# Create a subheader for skills
st.subheader("Skills")
# Add a divider
st.write("---")

# Print skills using st.write()
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

# Insert new line
st.write('\n')
# Create a subheader for work experience
st.subheader("Work Experience")
# Add a divider
st.write("---")

# Print my work experience at Canuel Caterers
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

# Insert new line
st.write("\n")
# Create a subheader for achievements
st.subheader("Achievements")
# Add a divider
st.write("---")


# For every item in the achievements list, print it our seperately, each with a medal emoji
for achievement in achievements:
    st.write(f"- 🥇 {achievement}")


### Certifications

# Create a subheader for certifications
st.subheader("Certifications")
# Add a divider
st.write("---")


# For every item in the certifications list, print it our seperately, each with a trophy emoji
for certification, link in certifications.items():
    # Embed a link to each certification
    st.write(f"- 🏆 [{certification}]({link})")


### Languages

# Insert a subheader for languages
st.subheader("Languages")
# Add a divider
st.write("---")


# For every item in the languages list, print it out seperately (they already have the flag emojis, which show on Firefox but not on Chrome, for some reason)
for language, proficiency in languages.items():
    st.write(f"- {language} - {proficiency}")
