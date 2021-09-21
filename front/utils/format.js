export function formatScore(score) {
  const formatter = new Intl.NumberFormat('sl', {
    style: 'decimal',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
    useGrouping: false,
  });
  return formatter.format(score);
}
