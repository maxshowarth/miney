import streamlit as st

from miney.grid import Grid, CellType
from miney.ui import render_grid

st.set_page_config(page_title="Miney Grid")

if "grid" not in st.session_state:
    st.session_state.grid = Grid()

def main():
    grid: Grid = st.session_state.grid
    st.title("Miney - Grid Editor")
    render_grid(grid)


if __name__ == "__main__":
    main()
