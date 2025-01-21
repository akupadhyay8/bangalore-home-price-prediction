window.onload = onPageLoad;

function onPageLoad() {
    getLocationNames();
}

function getLocationNames() {
    fetch('http://127.0.0.1:5000/get_location_names')
        .then(response => response.json())
        .then(data => {
            const locations = data.locations;
            const locationDropdown = document.getElementById("uiLocations");
            locationDropdown.innerHTML = '<option value="" disabled selected>Choose a Location</option>';
            locations.forEach(location => {
                const option = document.createElement("option");
                option.value = location;
                option.textContent = location;
                locationDropdown.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching location names:', error));
}

function onClickedEstimatePrice() {
    const total_sqft = document.getElementById("uiSqft").value;
    const location = document.getElementById("uiLocations").value;
    const bhk = document.querySelector('input[name="uiBHK"]:checked').value;
    const bath = document.querySelector('input[name="uiBathrooms"]:checked').value;

    if (!location || !total_sqft || !bhk || !bath) {
        alert("Please fill in all fields");
        return;
    }

    const data = new FormData();
    data.append('total_sqft', total_sqft);
    data.append('location', location);
    data.append('bhk', bhk);
    data.append('bath', bath);

    fetch('http://127.0.0.1:5000/predict_home_price', {
        method: 'POST',
        body: data
    })
    .then(response => response.json())
    .then(data => {
        if (data.estimated_price) {
            const resultContainer = document.getElementById("uiEstimatedPrice");
            const priceDisplay = document.getElementById("price-display");
            priceDisplay.textContent = `₹${data.estimated_price} lakhs`;
            resultContainer.classList.remove("hidden");

            // Scroll to the result container
            resultContainer.scrollIntoView({ behavior: "smooth", block: "start" });
        } else {
            alert("Error estimating price: " + JSON.stringify(data));
        }
    })
    .catch(error => {
        console.error("Error fetching price estimate:", error);
        alert("There was an error processing your request. Please try again.");
    });
}
