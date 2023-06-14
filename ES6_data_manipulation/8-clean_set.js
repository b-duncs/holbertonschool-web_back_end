export default function cleanSet(set, startString) {
  let result = '';
  if (!startString || !startString.length) return result;
  set.forEach((x) => {
    if (x && x.startsWith(startString)) result += `${x.slice(startString.length)}-`;
  });
  return result.slice(0, result.length - 1);
}
