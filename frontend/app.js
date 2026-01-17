document.addEventListener('DOMContentLoaded', () => {
    fetchPackages();
});

async function fetchPackages() {
    const container = document.getElementById('package-list-container');
    const API_URL = 'http://127.0.0.1:8000/api/packages/';

    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const packages = await response.json();

        container.innerHTML = ''; // Clear loading text

        if (!Array.isArray(packages) || packages.length === 0) {
            container.innerHTML =
                '<p>No active tour packages are available at this time.</p>';
            return;
        }

        packages.forEach(pkg => {
            const card = createPackageCard(pkg);
            container.appendChild(card);
        });

    } catch (error) {
        console.error('Error fetching packages:', error);
        container.innerHTML = `
            <p style="color: red;">
                Error loading packages. Please check the server connection.
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

function handleBooking(packageId) {
    alert(
        `Booking initiated for Package ID: ${packageId}\n\n` +
        `This is a demo action.\n` +
        `In a real application, this would redirect to the booking page.`
    );
}
