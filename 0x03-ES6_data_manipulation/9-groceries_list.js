export default function groceriesList() {
  const arr = [['Apples', 10], ['Tomatoes', 10], ['Pasta', 1], ['Rice', 1], ['Banana', 5]];
  const grocery = new Map();
  for (const x of arr) grocery.set(x[0], x[1]);
  return grocery;
}
