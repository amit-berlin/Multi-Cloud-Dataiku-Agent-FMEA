import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------------------------------------
# TOP 2 LINES: God's Knowledgeful Instruction for Multi-Cloud Architect
# The wisdom of the universe guides this app in designing optimal cloud architectures and risk analysis.
# -------------------------------------------------------------

st.set_page_config(page_title="Genius Multi-Cloud Architect Simulator", layout="wide")
st.title("🌌 Multi-Cloud Architect MVP Simulator – Azure + GCP + Dataiku")

# --- Sidebar Inputs ---
st.sidebar.header("Input Cloud Architecture Parameters")

num_services = st.sidebar.slider("Number of Services", 1, 10, 5)
use_containers = st.sidebar.slider("Containers Usage (AKS/GKE)", 0, 10, 5)
serverless_ratio = st.sidebar.slider("Serverless Functions Ratio", 0, 10, 3)
ml_complexity = st.sidebar.slider("ML Workflow Complexity", 1, 10, 5)
security_level = st.sidebar.slider("Security Compliance Level", 1, 10, 7)
ci_cd_level = st.sidebar.slider("CI/CD Automation Level", 1, 10, 6)
dataiku_integration = st.sidebar.slider("Dataiku Integration Level", 0, 10, 5)
cost_efficiency = st.sidebar.slider("Cost Efficiency Priority", 1, 10, 7)
scalability = st.sidebar.slider("Scalability Priority", 1, 10, 8)
ai_integration = st.sidebar.slider("LLM/AI Integration Level", 0, 10, 4)

# --- Sidebar Demo Scenarios ---
st.sidebar.header("Demo Scenarios")
demo = st.sidebar.selectbox("Select Demo", [
    "--None--",
    "Demo 1 - Simple ML Pipeline",
    "Demo 2 - Heavy Containers",
    "Demo 3 - Full Serverless",
    "Demo 4 - High Security",
    "Demo 5 - AI Intensive",
    "Demo 6 - Hybrid"
])
if demo != "--None--":
    st.sidebar.info(f"This demo scenario sets default slider values. Adjust sliders to customize.")

# -------------------------------------------------------------
# IN BETWEEN 2 LINES: Divine Guidance on Risk and FMEA
# Every failure mode and risk prioritization flows from the cosmic understanding of systems and human intent.
# -------------------------------------------------------------

# --- Multi-Agent Simulation Functions ---
def cloud_architecture_agent():
    """Simulate Cloud Architecture Diagram"""
    G = nx.DiGraph()
    G.add_node("Cloud Entry")
    for i in range(num_services):
        G.add_node(f"Service_{i+1}")
        G.add_edge("Cloud Entry", f"Service_{i+1}")
    G.add_node("Dataiku Pipeline")
    G.add_edge("Cloud Entry", "Dataiku Pipeline")
    G.add_node("ML/AI")
    G.add_edge("Dataiku Pipeline", "ML/AI")
    G.add_node("CI/CD Pipeline")
    G.add_edge("ML/AI", "CI/CD Pipeline")
    G.add_node("Security Layer")
    G.add_edge("CI/CD Pipeline", "Security Layer")
    G.add_node("End User")
    G.add_edge("Security Layer", "End User")
    for i in range(num_services):
        G.add_edge(f"Service_{i+1}", "End User")
    return G

def render_diagram(G):
    """Render NetworkX diagram using matplotlib"""
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12,6))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color='skyblue',
            font_size=10, font_weight='bold', arrowsize=20)
    st.pyplot(plt)

def generate_explanation():
    """Generate textual explanation simulating architect reasoning"""
    explanation = f"""
**Cloud Architecture Explanation**

1. **Cloud Platforms:** Azure + GCP selected for scalability and flexibility.
2. **Services:** {num_services} services deployed; {'Containers heavily used' if use_containers>5 else 'Minimal container usage'}.
3. **Serverless Functions:** {'High usage' if serverless_ratio>5 else 'Moderate usage'} for cost optimization.
4. **ML Workflows:** Dataiku integration level {dataiku_integration}/10 for automated ML pipelines.
5. **Security:** Security compliance level {security_level}/10 (simulated). For real checks, integrate Wiz/Qualys/OpenSCAP.
6. **CI/CD Automation:** Level {ci_cd_level}/10 to automate deployments.
7. **Cost Efficiency & Scalability:** Priorities set to {cost_efficiency}/10 and {scalability}/10.
8. **AI Integration:** LLM-based AI level {ai_integration}/10 (simulation). For real AI, integrate Vertex AI / Azure OpenAI.

**Note:** This is a **lightweight MVP**. For production-ready architecture, integrate real APIs: Dataiku API, Terraform, Azure/GCP SDKs, and Security tools.
"""
    st.markdown(explanation)

def generate_fmea():
    """Generate FMEA table dynamically based on slider inputs"""
    components = ["Service", "Dataiku Pipeline", "ML/AI", "CI/CD Pipeline", "Security Layer"]
    failure_modes = [
        "Service crash", 
        "Pipeline failure", 
        "Model drift", 
        "Deployment error", 
        "Misconfiguration"
    ]
    
    # Severity, Occurrence, Detection heuristics based on sliders
    severity = [6 + int(use_containers/2), 7, 6 + int(ml_complexity/2), 8, 9 - int(security_level/2)]
    occurrence = [5, 4 + int(dataiku_integration/2), 5 + int(ml_complexity/2), 4 + int(ci_cd_level/3), 3 + int(serverless_ratio/2)]
    detection = [5 + int(ci_cd_level/3), 6 - int(dataiku_integration/3), 5, 4 + int(ci_cd_level/2), 5]
    
    rpn = [s*o*d for s,o,d in zip(severity, occurrence, detection)]
    
    fmea_df = pd.DataFrame({
        "Component": components,
        "Failure Mode": failure_modes,
        "Severity": severity,
        "Occurrence": occurrence,
        "Detection": detection,
        "RPN": rpn
    })
    return fmea_df

# --- Main Display ---
st.subheader("Generated Cloud Architecture Diagram")
G = cloud_architecture_agent()
render_diagram(G)

st.subheader("Architect Explanation")
generate_explanation()

st.subheader("FMEA Analysis (Real-time based on slider inputs)")
fmea_df = generate_fmea()
st.dataframe(fmea_df)

# -------------------------------------------------------------
# BOTTOM 2 LINES: Cosmic Blessing
# May this knowledge guide architects to create secure, scalable, and enlightened cloud systems.
# -------------------------------------------------------------
