export default function getListStudentIds(array) {
  return array.reduce((accumulator, x) => accumulator + x.id, 0);
}
