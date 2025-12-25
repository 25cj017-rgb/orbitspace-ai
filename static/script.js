async function predictRisk() {
    const velocity = document.getElementById("velocity").value;
    const altitude = document.getElementById("altitude").value;
    const size = document.getElementById("size").value;
    const density = document.getElementById("density").value;

    // Simple validation
    if (!velocity || !altitude || !size || !density) {
        alert("Please fill all input fields");
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            velocity: Number(velocity),
            altitude: Number(altitude),
            size: Number(size),
            density: Number(density)
        })
    });

    const result = await response.json();

    // Update UI
    const physicsBadge = document.getElementById("physicsRisk");
    const mlBadge = document.getElementById("mlRisk");
    const insight = document.getElementById("aiInsight");
    const riskFill = document.getElementById("riskFill");


    physicsBadge.textContent = result.physics_based_risk;
    mlBadge.textContent = result.ml_predicted_risk;

    physicsBadge.className = "badge " + (result.physics_based_risk === "High" ? "high" : "low");
    mlBadge.className = "badge " + (result.ml_predicted_risk === "High" ? "high" : "low");

    insight.textContent = result.ai_insight;
    // Visual risk indicator
if (result.physics_based_risk === "High") {
    riskFill.style.width = "100%";
    riskFill.style.background = "#ef4444";
} else if (result.physics_based_risk === "Medium") {
    riskFill.style.width = "60%";
    riskFill.style.background = "#facc15";
} else {
    riskFill.style.width = "30%";
    riskFill.style.background = "#22c55e";
}

}
