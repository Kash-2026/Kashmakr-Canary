const { describe, it, before, beforeEach, after, afterEach } = require('node:test');
const assert = require('node:assert');
const beforeAll = before;
const expect = (actual) => ({
    toBe: (exp) => assert.strictEqual(actual, exp),
    toContain: (exp) => assert.ok(actual.includes(exp)),
    toEqual: (exp) => assert.deepStrictEqual(actual, exp)
});
const fs = require('fs');
const path = require('path');

describe('Analytics Dashboard', () => {
    let data;

    beforeAll(() => {
        const dataPath = path.join(__dirname, 'data.json');
        data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));
    });

    it('should filter data by date range', () => {
        const filteredData = filterDataByDate(data, '2023-01-01 - 2023-01-03');
        expect(filteredData.length).toBe(3);
    });

    it('should create a line chart SVG', () => {
        const svg = createLineChartSVG(data);
        expect(svg).toContain('<svg');
        expect(svg).toContain('</svg>');
    });

    it('should create a bar chart SVG', () => {
        const svg = createBarChartSVG(data);
        expect(svg).toContain('<svg');
        expect(svg).toContain('</svg>');
    });

    function filterDataByDate(data, dateRange) {
        const [start, end] = dateRange.split(' - ');
        return data.filter(d => new Date(d.date) >= new Date(start) && new Date(d.date) <= new Date(end));
    }

    function createLineChartSVG(data) {
        let svg = '<svg width="200" height="100">';
        data.forEach((d, i) => {
            svg += `<circle cx="${i * 20}" cy="${100 - d.value}" r="5" />`;
        });
        svg += '</svg>';
        return svg;
    }

    function createBarChartSVG(data) {
        let svg = '<svg width="200" height="100">';
        data.forEach((d, i) => {
            svg += `<rect x="${i * 20}" y="${100 - d.value}" width="10" height="${d.value}" />`;
        });
        svg += '</svg>';
        return svg;
    }
});