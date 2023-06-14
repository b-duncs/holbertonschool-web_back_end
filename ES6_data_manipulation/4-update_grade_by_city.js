export default function getStudentsByLocation(array, city, newGrades) {
  return array
    .filter((x) => x.location === city)
    .map((student) => {
      const grades = newGrades
        .filter((x) => x.studentId === student.id)
        .map((y) => y.grade)[0];
      const grade = grades || 'N/A';
      return { ...student, grade };
    });
}
