import time
import streamlit as st

from miney.map_loader import load_grid
from miney.simulation import Simulation
from miney.ui import render_simulation

st.set_page_config(page_title="Miney Grid")

if "simulation" not in st.session_state:
    grid = load_grid("maps/simple_map.json")
    st.session_state.simulation = Simulation(grid)


def main() -> None:
    sim: Simulation = st.session_state.simulation
    st.title("Miney - Truck Simulator")

    col1, col2, col3 = st.columns(3)
    if col1.button("Start" if not sim.running else "Stop"):
        if sim.running:
            sim.stop()
        else:
            sim.start()
    if col2.button("Reset"):
        sim.reset()
    if col3.button("Add Truck"):
        sim.add_truck()

    if sim.running:
        sim.step()
        time.sleep(0.1)
        st.experimental_rerun()

    render_simulation(sim)

    for truck in sim.trucks:
        st.write(f"Truck {truck.id}: {truck.state} at {truck.position}")


if __name__ == "__main__":
    main()
