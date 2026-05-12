import streamlit as st

st.set_page_config(
    page_title="WWI Timeline",
    page_icon="📅",
    layout="wide"
)

st.title("📅 WWI Timeline")
st.subheader("The war that changed the world — 1914 to 1918")
st.markdown("---")
events = [
    {
        "year": "1914",
        "date": "June 28, 1914",
        "title": "Assassination of Franz Ferdinand",
        "description": "Archduke Franz Ferdinand of Austria-Hungary is assassinated in Sarajevo by Gavrilo Princip, a Bosnian-Serb nationalist. This single gunshot triggers a chain of alliances that pulls 30 nations into war.",
        "significance": "🔴 The spark that started everything"
    },
    {
        "year": "1914",
        "date": "August 4, 1914",
        "title": "Britain Enters the War",
        "description": "After Germany invades neutral Belgium, Britain declares war on Germany. The war is now truly global — involving the entire British Empire including India, Australia, Canada and South Africa.",
        "significance": "🔴 The war goes global"
    },
    {
        "year": "1915",
        "date": "April 25, 1915",
        "title": "Gallipoli Campaign Begins",
        "description": "Allied forces land on the Gallipoli peninsula in Ottoman Turkey. The campaign, championed by Winston Churchill, ends in catastrophic failure with 250,000 Allied casualties. It becomes a defining national moment for Australia and New Zealand.",
        "significance": "🟡 A costly strategic failure"
    },
    {
        "year": "1916",
        "date": "July 1, 1916",
        "title": "Battle of the Somme",
        "description": "The bloodiest day in British military history — 57,470 British casualties on the first day alone. The battle lasts 141 days and results in over 1 million casualties on all sides. The Somme becomes a symbol of the senseless cost of trench warfare.",
        "significance": "🔴 The bloodiest battle in history"
    },
    {
        "year": "1917",
        "date": "April 6, 1917",
        "title": "USA Enters the War",
        "description": "After years of neutrality, the United States declares war on Germany following unrestricted submarine warfare and the Zimmermann Telegram — Germany's secret proposal for Mexico to attack the USA. Fresh American troops tip the balance.",
        "significance": "🟢 The turning point"
    },
    {
        "year": "1917",
        "date": "November 7, 1917",
        "title": "Russian Revolution",
        "description": "The Bolshevik Revolution removes Russia from the war. Lenin signs the Treaty of Brest-Litovsk with Germany, freeing up a million German troops to move to the Western Front for one final offensive.",
        "significance": "🟡 Russia exits, Germany surges west"
    },
    {
        "year": "1918",
        "date": "November 11, 1918",
        "title": "Armistice — The War Ends",
        "description": "At 11am on the 11th day of the 11th month, guns fall silent across Europe. The war has lasted 4 years, 3 months and 14 days. 20 million are dead. The map of the world will never look the same again.",
        "significance": "🟢 Silence after four years of thunder"
    },
]
for event in events:
    with st.expander(f"📌 {event['date']} — {event['title']}"):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"### {event['title']}")
            st.markdown(event['description'])
        
        with col2:
            st.markdown("**Significance:**")
            st.markdown(event['significance'])
            st.markdown(f"**Year:** {event['year']}")
        
        st.markdown("---")

st.markdown("### 💬 Want to go deeper?")
st.markdown("Head to the **WWI Tutor** page and ask Dr. Hritish Mahajan anything about these events.")