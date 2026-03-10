import streamlit as st
import heapq
import pandas as pd

st.set_page_config(
    page_title="Christ-Eats Navigator",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ CHRIST (Deemed to be University) Delhi NCR")
st.subheader("Campus Food Outlet Proximity Finder")

# GRAPH DATA (same as your Tkinter code, except Nescafe removed)
graph = {}

connections = [
    ('Main Gate', 'Block A', 100),
    ('Main Gate', 'Block B', 150),
    ('Main Gate', 'Dominos', 50),

    ('Block A', 'Cafeteria', 30),
    ('Block A', 'Freshiteria', 60),
    ('Block A', 'Block B', 50),

    ('Block B', 'B-Basement', 20),
    ('Block B', 'Rooftop', 80),

    ('Cafeteria', 'Taste of Dilli', 5),
    ('Cafeteria', 'Punjabi Bites', 5),
    ('Cafeteria', 'Rolls Lane', 5),
    ('Cafeteria', 'Southern Delights', 5),
    ('Cafeteria', 'Bites and Brews', 5),

    ('Rooftop', 'Gianis', 5),
    ('Rooftop', 'Amritsari Haveli', 5),

    ('Freshiteria', 'Greenox', 5)
]

def add_edge(u, v, w):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append((v, w))
    graph[v].append((u, w))


for u, v, w in connections:
    add_edge(u, v, w)


# OUTLETS (Nescafe removed)
outlets = [
    'Taste of Dilli',
    'Punjabi Bites',
    'Rolls Lane',
    'Southern Delights',
    'Bites and Brews',
    'Gianis',
    'Amritsari Haveli',
    'Greenox',
    'Dominos'
]

# LOCATION SELECTOR
st.markdown("### 📍 Select Your Current Location")

hubs = [
    'Main Gate',
    'Block A',
    'Block B',
    'Rooftop',
    'Cafeteria',
    'Freshiteria',
    'B-Basement'
]

location = st.selectbox("Choose location", hubs)

st.markdown("---")


# DIJKSTRA ALGORITHM
def dijkstra(start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq:

        d, u = heapq.heappop(pq)

        if d > distances[u]:
            continue

        for v, weight in graph.get(u, []):

            if d + weight < distances[v]:

                distances[v] = d + weight
                heapq.heappush(pq, (distances[v], v))

    return distances


# FIND NEAREST OUTLETS
if st.button("🚀 Find Nearest Food Outlets"):

    distances = dijkstra(location)

    results = sorted(
        [(k, v) for k, v in distances.items() if k in outlets],
        key=lambda x: x[1]
    )

    if results:

        nearest_name, nearest_dist = results[0]

        st.success(
            f"🏆 Closest Food Outlet: **{nearest_name}** ({nearest_dist} meters)"
        )

        table_data = []

        for name, dist in results:

            walk_time = round(dist / 80, 1)

            table_data.append({
                "Outlet": name,
                "Distance (meters)": dist,
                "Estimated Walk Time (mins)": walk_time
            })

        df = pd.DataFrame(table_data)

        st.markdown("### 📊 Ranked Food Outlets")
        st.dataframe(df, use_container_width=True)

st.markdown("---")

# -----------------------------
# VIVA QUIZ SECTION
# -----------------------------

st.header("📝 Unit 3 Viva Quiz")

q1 = st.radio(
    "Q1: A connected graph with no cycles is called a ______?",
    ["Graph", "Tree", "Path", "Network"]
)

q2 = st.radio(
    "Q2: A Minimum Spanning Tree must contain all vertices of the graph.",
    ["True", "False"]
)

q3 = st.radio(
    "Q3: Which algorithm does this app use to find shortest paths?",
    ["Prim's Algorithm", "Dijkstra's Algorithm", "Kruskal's Algorithm", "DFS"]
)

q4 = st.radio(
    "Q4: If a path exists between every pair of vertices, the graph is ______.",
    ["Disconnected", "Directed", "Connected", "Weighted"]
)

if st.button("Submit Quiz"):

    score = 0

    if q1 == "Tree":
        score += 1

    if q2 == "True":
        score += 1

    if q3 == "Dijkstra's Algorithm":
        score += 1

    if q4 == "Connected":
        score += 1

    st.success(f"🎉 Your Score: {score}/4")

    if score == 4:
        st.balloons()

st.markdown("---")
st.caption("Designed for Discrete Mathematics Project | Unit 3: Graph Theory")
