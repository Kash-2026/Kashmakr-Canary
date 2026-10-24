document.addEventListener('DOMContentLoaded', () => {
    fetch('data.json')
        .then(response => response.json())
       .then(data => {
            const lineChart = document.getElementById('line-chart');
            const barChart = document.getElementById('bar-chart');
            const donutChart = document.getElementById('donut-chart');
            const dateRangeInput = document.getElementById('date-range');

            const renderCharts = (filteredData) => {
                lineChart.innerHTML = `<svg>${createLineChartSVG(filteredData)}</svg>`;
                barChart.innerHTML = `<svg>${createBarChartSVG(filteredData)}</svg>`;
                donutChart.innerHTML = `<svg>${createDonutChartSVG(filteredData)}</svg>`;
            };

            const createLineChartSVG = (data) => {
                let svg = '<svg width="200" height="100">';
                data.forEach((d, i) => {
                    svg += `<circle cx="${i * 20}" cy="${100 - d.value}" r="5" />`;
                });
                svg += '</svg>';
                return svg;
            };

            const createBarChartSVG = (data) => {
                let svg = '<svg width="200" height="100">';
                data.forEach((d, i) => {
                    svg += `<rect x="${i * 20}" y="${100 - d.value}" width="10" height="${d.value}" />`;
                });
                svg += '</svg>';
                return svg;
            };

            const createDonutChartSVG = (data) => {
                let svg = '<svg width="100" height="100">';
                let total = data.reduce((sum, d) => sum + d.value, 0);
                let currentValue = 0;
                data.forEach(d => {
                    let value = (d.value / total) * 360;
                    svg += `<path d="M 50 50 m 47 0 a 47 47 0 0 1 -${value} 0 a 47 47 0 0 1 ${value} 0" fill="none" stroke="black" stroke-width="5" />`;
                    currentValue += value;
                });
                svg += '</svg>';
                return svg;
            };

            const filterDataByDate = (data, dateRange) => {
                const [start, end] = dateRange.split(' - ');
                return data.filter(d => new Date(d.date) >= new Date(start) && new Date(d.date) <= new Date(end));
            };

            dateRangeInput.addEventListener('change', () => {
                const filteredData = filterDataByDate(data, dateRangeInput.value);
                renderCharts(filteredData);
            });

            renderCharts(data);
        });
});