import React, { useState } from'react';

const PricingCard = ({ monthlyPrice, annualPrice, discountPct, featureList }) => {
  const [isAnnual, setIsAnnual] = useState(false);

  const togglePlan = () => setIsAnnual(!isAnnual);
  const price = isAnnual ? annualPrice : monthlyPrice;
  const period = isAnnual ? 'year' :'month';

  return (
    <div>
      <div>${price} / {period}</div>
      {isAnnual && <div>{discountPct}% OFF</div>}
      <button onClick={togglePlan}>{isAnnual ? 'Monthly' : 'Annual'} Plan</button>
      <ul>
        {featureList.map((feature, index) => (
          <li key={index}>{feature}</li>
        ))}
      </ul>
    </div>
  );
};

export default PricingCard;