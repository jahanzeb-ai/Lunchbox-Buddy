
import streamlit as st
import random

st.set_page_config(page_title="Lunchbox Buddy", page_icon="🥪", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg,#fffaf0 0%,#eefaff 100%);}
.hero {padding:30px 22px;border-radius:25px;background:linear-gradient(135deg,#ffcc4d,#ff8066);
color:white;text-align:center;margin-bottom:20px;box-shadow:0 8px 25px #00000015;}
.card {padding:18px;border-radius:20px;background:white;border:1px solid #eee;margin:12px 0;}
.big {font-size:48px;}
</style>
""", unsafe_allow_html=True)

if "done" not in st.session_state: st.session_state.done = set()
if "stars" not in st.session_state: st.session_state.stars = 0

FOODS = {
    "🍚 Rice":"Rocket Fuel","🍗 Chicken":"Power Core","🥒 Cucumber":"Oxygen Pack",
    "🍌 Banana":"Energy Boost","🥪 Sandwich":"Adventure Pack","🍎 Apple":"Health Shield",
    "🥕 Carrot":"Super Vision","🥛 Milk":"Magic Potion","🥚 Egg":"Power Engine","🫓 Roti":"Strong Fuel"
}
MISSIONS = [
    ("🚀 Space Mission","Your spaceship needs lunch fuel. Let's power it up!"),
    ("🏴‍☠️ Treasure Hunt","A lunchbox treasure is waiting. Complete your foods to unlock it!"),
    ("🦸 Superhero Mission","Your superhero energy meter needs a boost. Let's get powered up!"),
    ("🦁 Jungle Journey","The jungle gate is waiting. Complete today's lunch mission!"),
    ("🐉 Dragon Quest","A friendly dragon needs your help. Let's fuel the adventure!")
]

st.markdown('<div class="hero"><div class="big">🥪</div><h1>Lunchbox Buddy</h1><p>Your friendly lunchtime adventure buddy!</p></div>', unsafe_allow_html=True)

st.subheader("👋 Let's build today's lunch mission")
name = st.text_input("Child's name", placeholder="e.g. Ahmad")
foods = st.multiselect("What's inside the lunchbox?", list(FOODS), default=["🍚 Rice","🍗 Chicken","🍎 Apple"])

if st.button("✨ Start My Lunch Mission", use_container_width=True):
    st.session_state.done = set()
    st.session_state.stars = 0
    st.session_state.mission = random.choice(MISSIONS)

if "mission" in st.session_state and foods:
    title, story = st.session_state.mission
    child = name or "Buddy"
    st.markdown(f'<div class="card"><h2>{title}</h2><p>Hi <b>{child}</b>! {story}</p></div>', unsafe_allow_html=True)

    st.subheader("🎒 Today's Lunch")
    for food in foods:
        if st.button(
            f"{'✅' if food in st.session_state.done else '🍽️'} {food}  •  {FOODS[food]}",
            key=food, use_container_width=True):
            if food not in st.session_state.done:
                st.session_state.done.add(food)
                st.session_state.stars += 2
                st.rerun()

    completed = len(st.session_state.done)
    total = len(foods)
    st.progress(completed / total)
    st.write(f"**Buddy progress:** {completed}/{total} ⭐ **{st.session_state.stars} stars**")

    if completed == total:
        st.balloons()
        st.success(f"🎉 Fantastic, {child}! Your Lunchbox Buddy mission is complete!")
        st.markdown('<div class="card"><h2>🏆 Golden Buddy Badge</h2><p>You explored your lunch and completed today’s mission!</p></div>', unsafe_allow_html=True)

st.divider()
with st.expander("👨‍👩‍👧 Parent View"):
    st.write("Lunchbox Buddy is designed to make lunchtime positive and playful.")
    st.write("Completed today:", ", ".join(st.session_state.done) if st.session_state.done else "Nothing yet")
    st.caption("Prototype: progress resets when the app session is restarted.")

st.caption("🥪 Lunchbox Buddy — Creative AI Tool Prototype")
