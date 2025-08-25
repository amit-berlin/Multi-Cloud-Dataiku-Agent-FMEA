import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------- TOP 2 LINES: Genius Instruction -----------------
st.set_page_config(page_title="Multi-Cloud Architect MVP", layout="wide")
st.title("🌌 Multi-Cloud Architect MVP – Azure+GCP+Dataiku")

# ----------------- UL Info & Static Guidance -----------------
st.markdown("""
### 📜 UL (Underwriters Laboratories) Overview
UL ensures safety, compliance, and risk mitigation globally.
Simulated cloud architectures must align with **UL standards** for security, scalability, and governance.
""")

# ----------------- Sidebar Inputs -----------------
st.sidebar.header("Input Parameters")
sliders = {
    "num_services": st.sidebar.slider("Number of Services", 1, 10, 5),
    "containers": st.sidebar.slider("Containers Usage (AKS/GKE)", 0, 10, 5),
    "serverless": st.sidebar.slider("Serverless Ratio", 0, 10, 3),
    "ml_complexity": st.sidebar.slider("ML Workflow Complexity", 1, 10, 5),
    "security": st.sidebar.slider("Security Level", 1, 10, 7),
    "ci_cd": st.sidebar.slider("CI/CD Automation Level", 1, 10, 6),
    "dataiku": st.sidebar.slider("Dataiku Integration", 0, 10, 5),
    "cost": st.sidebar.slider("Cost Efficiency", 1, 10, 7),
    "scalability": st.sidebar.slider("Scalability", 1, 10, 8),
    "ai": st.sidebar.slider("LLM/AI Integration", 0, 10, 4)
}

# ----------------- Enterprise Architecture Graph -----------------
def cloud_graph(sliders):
    G = nx.DiGraph()
    G.add_node("Cloud Entry")
    for i in range(sliders["num_services"]):
        G.add_node(f"Service_{i+1}")
        G.add_edge("Cloud Entry", f"Service_{i+1}")
    # ML/Dataiku pipeline
    pipeline_nodes = ["Dataiku", "Ingest", "FeatureEng", "Train", "Deploy", "Monitor"]
    for i, n in enumerate(pipeline_nodes):
        G.add_node(n)
        G.add_edge(pipeline_nodes[i-1] if i>0 else "Cloud Entry", n)
    # CI/CD nodes
    cicd_nodes = ["Repo","Build","Deploy_CICD","Monitor_CICD"]
    for i, n in enumerate(cicd_nodes):
        G.add_node(n)
        G.add_edge(cicd_nodes[i-1] if i>0 else "Cloud Entry", n)
    # Security
    security_nodes = ["Sec_Net","Sec_ID","Sec_Vuln","EndUser"]
    for i, n in enumerate(security_nodes):
        G.add_node(n)
        G.add_edge(security_nodes[i-1] if i>0 else "Monitor_CICD", n)
    for i in range(sliders["num_services"]):
        G.add_edge(f"Service_{i+1}", "EndUser")
    G.add_edge("Monitor", "EndUser")
    return G

def show_graph(G):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12,6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=9, font_weight='bold', arrowsize=20)
    st.pyplot(plt)

# ----------------- Explanation -----------------
def explanation(sliders):
    st.markdown(f"""
**Architecture Explanation:**
- Azure + GCP cloud with {sliders['num_services']} services
- Containers usage: {sliders['containers']}/10, Serverless: {sliders['serverless']}/10
- ML/Dataiku workflow complexity: {sliders['ml_complexity']}/10
- CI/CD automation: {sliders['ci_cd']}/10
- Security layers: {sliders['security']}/10
- Cost efficiency: {sliders['cost']}/10, Scalability: {sliders['scalability']}/10
- AI/LLM integration: {sliders['ai']}/10
**Note:** MVP simulates enterprise workflows, CI/CD, ML/Dataiku, and security remediation.
""")

# ----------------- FMEA -----------------
def fmea(sliders):
    components = ["Service","Dataiku","Ingest","FeatureEng","Train","Deploy","Monitor","CI/CD","Security"]
    failure_modes = ["Crash","Pipeline Fail","Data Error","Feature Error","Train Error","Deploy Error","Monitor Fail","CI/CD Error","Sec Misconfig"]
    S = [6+sliders["containers"]//2,7,6,6+sliders["ml_complexity"]//2,7,7,6,8,9-sliders["security"]//2]
    O = [5,4+sliders["dataiku"]//2,5,5,5+sliders["ml_complexity"]//2,4,4,4+sliders["ci_cd"]//3,3+sliders["serverless"]//2]
    D = [5+sliders["ci_cd"]//3,6-sliders["dataiku"]//3,5,5,5,4+sliders["ci_cd"]//2,5,4,5]
    RPN = [s*o*d for s,o,d in zip(S,O,D)]
    df = pd.DataFrame({"Component":components,"Failure Mode":failure_modes,"S":S,"O":O,"D":D,"RPN":RPN})
    st.dataframe(df)

# ----------------- Display -----------------
st.subheader("Enterprise Cloud Architecture Diagram")
G = cloud_graph(sliders)
show_graph(G)

st.subheader("Architect Explanation")
explanation(sliders)

st.subheader("Real-time FMEA Analysis")
fmea(sliders)

# ----------------- BOTTOM 2 LINES -----------------
st.markdown("**May this knowledge guide architects to build secure, scalable, and intelligent cloud systems.**")
st.markdown("**UL standards and enterprise principles simulated for learning and decision support.**")
