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
    """Simulate enterprise Cloud Architecture Diagram including services, CI/CD, ML/Dataiku, security"""
    G = nx.DiGraph()
    # Entry
    G.add_node("Cloud Entry")
    
    # Services
    for i in range(num_services):
        G.add_node(f"Service_{i+1}")
        G.add_edge("Cloud Entry", f"Service_{i+1}")
    
    # ML/Dataiku pipeline nodes
    G.add_node("Dataiku Pipeline")
    G.add_edge("Cloud Entry", "Dataiku Pipeline")
    G.add_node("Data Ingestion")
    G.add_edge("Dataiku Pipeline", "Data Ingestion")
    G.add_node("Feature Engineering")
    G.add_edge("Dataiku Pipeline", "Feature Engineering")
    G.add_node("Model Training")
    G.add_edge("Feature Engineering", "Model Training")
    G.add_node("Model Deployment")
    G.add_edge("Model Training", "Model Deployment")
    G.add_node("Model Monitoring")
    G.add_edge("Model Deployment", "Model Monitoring")
    
    # CI/CD nodes
    G.add_node("CI/CD: Code Repo")
    G.add_edge("Cloud Entry", "CI/CD: Code Repo")
    G.add_node("CI/CD: Build & Test")
    G.add_edge("CI/CD: Code Repo", "CI/CD: Build & Test")
    G.add_node("CI/CD: Deploy")
    G.add_edge("CI/CD: Build & Test", "CI/CD: Deploy")
    G.add_node("CI/CD: Monitor & Rollback")
    G.add_edge("CI/CD: Deploy", "CI/CD: Monitor & Rollback")
    
    # Security nodes
    G.add_node("Security: Network")
    G.add_edge("CI/CD: Monitor & Rollback", "Security: Network")
    G.add_node("Security: Identity & Access")
    G.add_edge("Security: Network", "Security: Identity & Access")
    G.add_node("Security: Vulnerability Scan")
    G.add_edge("Security: Identity & Access", "Security: Vulnerability Scan")
    
    # End user
    G.add_node("End User")
    G.add_edge("Security: Vulnerability Scan", "End User")
    for i in range(num_services):
        G.add_edge(f"Service_{i+1}", "End User")
    G.add_edge("Model Monitoring", "End User")
    
    return G

def render_diagram(G):
    """Render NetworkX diagram using matplotlib"""
    pos = nx.spring_layout(G, seed=42, k=0.5)
    plt.figure(figsize=(14,7))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color='skyblue',
            font_size=9, font_weight='bold', arrowsize=20)
    st.pyplot(plt)

def generate_explanation():
    """Generate textual explanation simulating enterprise architect reasoning"""
    explanation = f"""
**Cloud Architecture Explanation – Simulated Enterprise Experience**

1. **Cloud Platforms:** Azure + GCP for scalable and resilient cloud solutions.
2. **Services:** {num_services} services deployed; {'Heavy containerization (AKS/GKE)' if use_containers>5 else 'Minimal containerization'}.
3. **Serverless Functions:** {'High usage' if serverless_ratio>5 else 'Moderate usage'} for cost efficiency.
4. **ML/Dataiku Pipeline:** Integration level {dataiku_integration}/10; includes Data Ingestion, Feature Engineering, Model Training, Deployment, and Monitoring.
5. **CI/CD Pipeline:** Level {ci_cd_level}/10; steps include Code Repo, Build & Test, Deploy, and Monitor & Rollback.
6. **Security Remediation:** Security layers include Network, Identity & Access, and Vulnerability Scanning; compliance level {security_level}/10.
7. **Cost Efficiency & Scalability:** Priorities set to {cost_efficiency}/10 and {scalability}/10.
8. **AI Integration:** LLM-based AI level {ai_integration}/10 (simulated). For production, integrate Vertex AI / Azure OpenAI.
9. **Enterprise Simulation:** This MVP simulates hands-on experience in cloud architecture, CI/CD, ML workflows, and security remediation.

**Note:** Lightweight MVP for demonstration. Production implementations require real APIs: Dataiku, Terraform, Azure/GCP SDKs, and security tools.
"""
    st.markdown(explanation)

def generate_fmea():
    """Generate dynamic FMEA table based on input sliders and enterprise simulation"""
    components = [
        "Service", "Dataiku Pipeline", "Data Ingestion", "Feature Engineering", 
        "Model Training", "Model Deployment", "Model Monitoring", 
        "CI/CD Pipeline", "Security Layer"
    ]
    failure_modes = [
        "Service crash", "Pipeline failure", "Data ingestion errors", "Feature engineering errors",
        "Model training errors", "Model deployment errors", "Model monitoring failures",
        "CI/CD deployment error", "Security misconfiguration"
    ]
    
    severity = [
        6 + int(use_containers/2), 7, 6, 7, 7 + int(ml_complexity/2), 8, 6, 8, 9 - int(security_level/2)
    ]
    occurrence = [
        5, 4 + int(dataiku_integration/2), 5, 5, 5 + int(ml_complexity/2), 4, 4, 4 + int(ci_cd_level/3), 3 + int(serverless_ratio/2)
    ]
    detection = [
        5 + int(ci_cd_level/3), 6 - int(dataiku_integration/3), 5, 5, 5, 4 + int(ci_cd_level/2), 5, 4, 5
    ]
    
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
st.subheader("Generated Enterprise Cloud Architecture Diagram")
G = cloud_architecture_agent()
render_diagram(G)

st.subheader("Architect Explanation – Enterprise Simulation")
generate_explanation()

st.subheader("FMEA Analysis (Real-time based on slider inputs)")
fmea_df = generate_fmea()
st.dataframe(fmea_df)

# -------------------------------------------------------------
# BOTTOM 2 LINES: Cosmic Blessing
# May this knowledge guide architects to create secure, scalable, and enlightened cloud systems.
# -------------------------------------------------------------
