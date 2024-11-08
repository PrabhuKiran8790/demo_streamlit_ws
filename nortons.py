import streamlit as st

st.title("Norton's theorem")


def calculate_nortons(in_, rn, rl):
    vn = in_ * rn
    il = in_ - vn / rn
    pl = il**2 * rl
    return il, pl


tab1, tab2 = st.tabs(["Compute", "Explanation"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            in_ = st.number_input("In (A)", value=1)
            rn = st.number_input("Rn (Ω)", value=1)
            rl = st.number_input("RL (Ω)", value=1)
        
            compute = st.button("Compute")
    
    with col2:
        if compute:
            il, pl = calculate_nortons(in_, rn, rl)
            st.write(f"Il = {il} A")
            st.write(f"PL = {pl} W")

with tab2:
    st.write("Norton's theorem states that any linear electrical network with voltage and current sources and resistances can be replaced by an equivalent current source IN in parallel with an equivalent resistance RN.")