import streamlit as st

# Set page configuration to make the sidebar static
st.set_page_config(initial_sidebar_state='expanded')

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["Introduction", "Frequently Used Media", "Content Generation/Consumption Challenges"])

if page == "Introduction":
    st.markdown("<h1 style='text-align: center; '>Introduction</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>Austin McCormick</h2>", unsafe_allow_html=True)
    left_co, right_co = st.columns(2)
    with left_co:
        st.image('pictures/portrait.jpg')
    with right_co:
        st.text("Howdy! My name is Austin McCormick. I am in Computers and New Media because I'm a computer science graduate student and I am interested in the impact computers have on media and in turn how computers influence people.")
elif page == "Frequently Used Media":
    st.markdown("<h1 style='text-align: center;'>Frequently Used Media</h1>", unsafe_allow_html=True)
    st.markdown("""
    - Music
        - Christian
            - Forrest Frank
            - Josiah Queen
                - The Prodigal
                - Fishes and Loaves
                - My Promised Land
            - Strings and Heart
        - Alt/Indie
            - Hozier
            - Still Woozy
            - Joji
            - Dominic Fike
            - Will Paquin
        - 
    - Games
        - PC
            - Overwatch
            - Marvel Rivals
            - Civilization V
            - Slay the Spire
        - Nintendo Switch
            - Breath of the Wild
            - Tears of the Kingdom
            - Pokemon Scarlet
        - iPhone
            - Chess
            - Pokemon Go
            - Pokemon TCG Pocket
    - TV Shows
        - Netflix
            - Stranger Things
            - Suits
            - Prison Break
        - Disney+
        - CrunchyRoll
            - Attack on Titan
            - Mob Psycho 100
            - Solo Leveling
            - Vinland Saga
    """)
elif page == "Content Generation/Consumption Challenges":
    st.markdown("<h1 style='text-align: center;'>Content Generation/Consumption Challenges</h1>", unsafe_allow_html=True)
    st.text("The primary challenge I have with consuming content is that I have severe astigmatism. Soft contact lenses can't fully correct my vision with how strong it is, and any slight rotation of the lense causes my vision to be completely blurred, rendering all small text unreadable. Wearing glasses is an improvement, however even minor discrepancies in the glasses such as the lenses placed a couple degrees rotated from the optimal position causes blurred vision, also making text difficult to read. This makes it difficult to read small text on a screen, and not all forms of digital media have methods to appropriately accomodate this.")