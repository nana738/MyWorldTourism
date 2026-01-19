document.addEventListener('DOMContentLoaded', () => {
    fetchPackages();
});

async function fetchPackages() {
    const container = document.getElementById('package-list-container');

    const API_URL = 'https://myworldtourism.onrender.com/api/packages/';

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }

        const packages = await response.json();
        container.innerHTML = '';

        if (!packages.length) {
            container.innerHTML = '<p>No tour packages available.</p>';
            return;
        }

        packages.forEach(pkg => {
            container.appendChild(createPackageCard(pkg));
        });

    } catch (error) {
        console.error(error);
        container.innerHTML = `
            <p style="color:red;">
                Error loading packages. Please check the server.
            </p>
        `;
    }
}

function createPackageCard(pkg) {
    const card = document.createElement('div');
    card.className = 'package-card';

    card.innerHTML = `
        <h2>${pkg.name}</h2>
        <p><strong>Destination:</strong> ${pkg.destination}</p>
        <p>${pkg.description}</p>
        <div class="price">₹${pkg.price}</div>
        <button class="book-btn" onclick="handleBooking(${pkg.id})">
            Book Now
        </button>
    `;

    return card;
}

function handleBooking(id) {
    alert(`Booking started for Package ID: ${id}`);
}
