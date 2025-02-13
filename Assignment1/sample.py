import streamlit as st

st.set_page_config(initial_sidebar_state='expanded')

# Initialize session state for page
if 'page' not in st.session_state:
    st.session_state.page = "Introduction"

# Sidebar for navigation
st.sidebar.markdown("<h2>Pages</h2>", unsafe_allow_html=True)
if st.sidebar.button("Introduction", key="intro", use_container_width=True):
    st.session_state.page = "Introduction"
if st.sidebar.button("Frequently Used Media", key="media", use_container_width=True):
    st.session_state.page = "Frequently Used Media"
if st.sidebar.button("Content Challenges", key="challenges", use_container_width=True):
    st.session_state.page = "Content Generation/Consumption Challenges"

# Page 1
if st.session_state.page == "Introduction":
    st.markdown("<h1 style='text-align: center;'>Introduction</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-size: 25px;'>Austin McCormick</h2>", unsafe_allow_html=True)
    left_co, right_co = st.columns(2)
    with left_co:
        st.image('Assignment1/pictures/portrait.JPG')
    with right_co:
        st.text("Howdy! My name is Austin McCormick. I am in Computers and New Media because I'm interested in the impact computers have on media and in turn how computers influence people.")

# Page 2
elif st.session_state.page == "Frequently Used Media":
    st.markdown("<h1 style='text-align: center;'>Frequently Used Media</h1>", unsafe_allow_html=True)
    st.markdown("### Music")
    with st.expander("Christian"):
        st.markdown("""
        - Forrest Frank
            - GOOD DAY
            - GOD IS GOOD
        - Josiah Queen
            - The Prodigal
            - Fishes and Loaves
            - My Promised Land
        - Strings and Heart
            - Flowers Dressed in Blue
        """)
    with st.expander("Alt/Indie"):
        st.markdown("""
        - Hozier
            - Too Sweet
        - Still Woozy
            - Goodie Bag
            - Habit
        - Joji
            - Slow Dancing in the Dark
            - Sanctuary
        - Dominic Fike
            - Babydoll
        - Will Paquin
            - Chandelier
        """)
    st.markdown("### Games")
    with st.expander("PC"):
        st.markdown("""
        - Overwatch
        - Marvel Rivals
        - Civilization V
        - Slay the Spire
        """)
    with st.expander("Nintendo Switch"):
        st.markdown("""
        - Breath of the Wild
        - Tears of the Kingdom
        - Pokemon Scarlet
        """)
    with st.expander("iPhone"):
        st.markdown("""
        - Chess
        - Pokemon Go
        - Pokemon TCG Pocket
        """)
    st.markdown("### TV Shows")
    with st.expander("Netflix"):
        st.markdown("""
        - Stranger Things
        - Suits
        - Prison Break
        """)
    with st.expander("Disney+"):
        st.markdown("""
        - The Mandalorian
        - Loki
        - The Falcon and the Winter Soldier
        """)
    with st.expander("CrunchyRoll"):
        st.markdown("""
        - Attack on Titan
        - Mob Psycho 100
        - Solo Leveling
        - Vinland Saga
        """)
    st.markdown("### Youtube")
    with st.expander("News"):
        st.markdown("""
        - penguinz0
        - Pegasus
        - CinnamonToastKen
        """)
    with st.expander("Game Streams"):
        st.markdown("""
        - Stimpee
        - CaseOh
        - Memeio
        """)
    with st.expander("Podcasts"):
        st.markdown("""
        - Brooke and Jeffrey
        - Joe Rogan
        """)
    with st.expander("Informational"):
        st.markdown("""
        - RealLifeLore
        - Humphrey Yang
        """)

# Page 3
elif st.session_state.page == "Content Generation/Consumption Challenges":
    st.markdown("<h1 style='text-align: center;'>Content Generation/Consumption Challenges</h1>", unsafe_allow_html=True)
    st.text("The primary challenge I have with consuming content is that I have severe astigmatism. Soft contact lenses can't fully correct my vision with how strong it is, and any slight rotation of the lense causes my vision to be completely blurred, rendering all small text unreadable. Wearing glasses is an improvement, however even minor discrepancies in the glasses such as the lenses placed a couple degrees rotated from the optimal position causes blurred vision, also making text difficult to read. This makes it difficult to read small text on a screen, and not all forms of digital media have methods to appropriately accomodate this.")