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

    // Update risks
    document.getElementById("physicsRisk").innerText = data.physics_based_risk;
    document.getElementById("mlRisk").innerText = data.ml_predicted_risk;

    // Update badge color
    const setBadge = (el, risk) => {
        el.className = "badge " + risk.toLowerCase();
    };

    setBadge(document.getElementById("physicsRisk"), data.physics_based_risk);
    setBadge(document.getElementById("mlRisk"), data.ml_predicted_risk);

    // Update AI insight
    document.getElementById("aiInsight").innerText = data.ai_insight;

    // Risk bar
    const riskFill = document.getElementById("riskFill");
    if (data.physics_based_risk === "High") {
        riskFill.style.width = "90%";
    } else if (data.physics_based_risk === "Medium") {
        riskFill.style.width = "60%";
    } else {
        riskFill.style.width = "30%";
    }
}
