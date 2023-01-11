export default function guardrail(mathFunction) {
  const x = [];
  try {
    x.push(mathFunction());
  } catch (err) {
    x.push(err.toString());
  }
  x.push('Guardrail was processed');
  return x;
}
