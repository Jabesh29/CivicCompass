document.getElementById("eligibilityForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const data = {
        age: document.getElementById("age").value,
        income: document.getElementById("income").value,
        category: document.getElementById("category").value,
        occupation: document.getElementById("occupation").value,
        language: document.getElementById("language").value
    };

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Checking eligibility...";

    try {
        const response = await fetch("YOUR_API_GATEWAY_URL", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        resultDiv.innerHTML = `
            <h3>Eligible Schemes:</h3>
            <ul>
                ${result.map(scheme => `<li>${scheme}</li>`).join("")}
            </ul>
        `;

    } catch (error) {
        resultDiv.innerHTML = "Error fetching results.";
    }
});
