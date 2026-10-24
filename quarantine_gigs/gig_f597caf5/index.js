document.addEventListener('DOMContentLoaded', function() {
    const competitors = [
        { name: 'Competitor A', marketShare: '30%', strengths: 'Strong brand, High customer loyalty', weaknesses: 'High prices' },
        { name: 'Competitor B', marketShare: '25%', strengths: 'Innovative products, Agile development', weaknesses: 'Limited market presence' },
        { name: 'Competitor C', marketShare: '20%', strengths: 'Cost leadership, Efficient supply chain', weaknesses: 'Perceived lower quality' },
    ];

    const tableBody = document.querySelector('#competitorTable tbody');

    competitors.forEach(competitor => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${competitor.name}</td>
            <td>${competitor.marketShare}</td>
            <td>${competitor.strengths}</td>
            <td>${competitor.weaknesses}</td>
        `;
        tableBody.appendChild(row);
    });
});