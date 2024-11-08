import streamlit as st

def calculate_thevenins(vth, rth, rl):
    il = vth / (rth + rl)
    pl = il**2 * rl
    return il, pl


st.title("Thevenin's theorem")

tab1, tab2 = st.tabs(["Compute", "Explanation"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            vth = st.number_input("Vth (V)", value=1)
            rth = st.number_input("Rth (Ω)", value=1)
            rl = st.number_input("RL (Ω)", value=1)
        
            compute = st.button("Compute")


    with col2:
        with st.container(border=True):
            if compute:
                il, pl = calculate_thevenins(vth, rth, rl)
                st.write(f"Il = {il:.2f} A")
                st.write(f"Pl = {pl:.2f} W")

with tab2:
    st.write("This is the explanation tab")
    st.write("Thevenin's theorem states that any linear circuit can be replaced by a voltage source in series with a resistor.")

    st.latex(r"V_{th} = V_{oc}")
