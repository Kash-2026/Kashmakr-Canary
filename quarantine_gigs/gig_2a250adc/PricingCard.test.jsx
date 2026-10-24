import React from'react';
import { render } from '@testing-library/react';
import PricingCard from './PricingCard';

test('renders discount percentage correctly', () => {
  const { getByText } = render(<PricingCard monthlyPrice={10} annualPrice={100} discountPct={20} featureList={['Feature 1']} />);
  expect(getByText('20% OFF')).toBeInTheDocument();
});

test('renders all features', () => {
  const { getAllByRole } = render(<PricingCard monthlyPrice={10} annualPrice={100} discountPct={20} featureList={['Feature 1', 'Feature 2']} />);
  expect(getAllByRole('listitem').length).toBe(2);
});