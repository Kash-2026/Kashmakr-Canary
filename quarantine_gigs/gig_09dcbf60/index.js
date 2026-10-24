async function calculateBond() {
    const faceValue = document.getElementById('faceValue').value;
    const couponRate = document.getElementById('couponRate').value;
    const yearsToMaturity = document.getElementById('yearsToMaturity').value;
    const marketRate = document.getElementById('marketRate').value;

    const response = await fetch('/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            faceValue: parseFloat(faceValue),
            couponRate: parseFloat(couponRate),
            yearsToMaturity: parseInt(yearsToMaturity, 10),
            marketRate: parseFloat(marketRate)
        })
    });

    const result = await response.json();
    document.getElementById('result').innerText = `Bond Price: ${result.bondPrice.toFixed(2)}, Yield to Maturity: ${result.yieldToMaturity.toFixed(2)}%`;
}