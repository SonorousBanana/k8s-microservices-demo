async function fetchUsers() {
    const res = await fetch('/api/users');
    const data = await res.json();
    const container = document.getElementById('users-container');
    container.innerHTML = '';

    data.users.forEach(user => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `<h3>${user.name}</h3><p>Email: ${user.email}</p><p>ID: ${user.id}</p>`;
        container.appendChild(card);
    });
}

async function fetchMetrics() {
    const res = await fetch('/api/metrics');
    const data = await res.json();
    const container = document.getElementById('metrics-container');
    container.innerHTML = '';

    data.metrics.forEach(metric => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `<h3>${metric.metric}</h3><p>Value: ${metric.value}</p><p>Timestamp: ${metric.timestamp}</p>`;
        container.appendChild(card);
    });
}

// Refresh button
document.getElementById('refresh-btn').addEventListener('click', () => {
    fetchUsers();
    fetchMetrics();
});

// Initial fetch
fetchUsers();
fetchMetrics();
