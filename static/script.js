async function predictRisk() {
    const velocity = parseFloat(document.getElementById("velocity").value);
    const altitude = parseFloat(document.getElementById("altitude").value);
    const size = parseFloat(document.getElementById("size").value);
    const density = parseFloat(document.getElementById("density").value);

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            velocity: velocity,
            altitude: altitude,
            size: size,
            density: density
        })
    });

    const data = await response.json();

    // Update Risk Assessment
    document.getElementById("physics-risk").innerText =
        "Physics-Based Risk: " + data.physics_based_risk;

    document.getElementById("ml-risk").innerText =
        "ML-Predicted Risk: " + data.ml_predicted_risk;

    // Update AI Insight
    document.getElementById("ai-insight").innerText =
        data.ai_insight;

    // Optional: show risk score if needed
    const riskBar = document.getElementById("risk-bar");
    if (riskBar) {
        if (data.physics_based_risk === "High") {
            riskBar.style.width = "90%";
        } else if (data.physics_based_risk === "Medium") {
            riskBar.style.width = "60%";
        } else {
            riskBar.style.width = "30%";
        }
    }
}
