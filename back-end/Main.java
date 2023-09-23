import java.util.*;

class Course {
    private String courseId;
    private String courseName;
    private int creditHours;

    public Course(String courseId, String courseName, int creditHours) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.creditHours = creditHours;
    }

    public String getCourseName() {
        return courseName;
    }

    // ... (other getters and methods as needed)
}

class Major {
    private String majorId;
    private String majorName;
    private List<Course> mandatoryCourses;

    public Major(String majorId, String majorName) {
        this.majorId = majorId;
        this.majorName = majorName;
        this.mandatoryCourses = new ArrayList<>();
    }

    // Getter for majorName
    public String getMajorName() {
        return majorName;
    }

    public void addMandatoryCourse(Course course) {
        mandatoryCourses.add(course);
    }

    public List<Course> getMandatoryCourses() {
        return mandatoryCourses;
    }

    // ... (other methods)
}

class Student {
    private String studentId;
    private String studentName;
    private Major major;
    private Set<Course> completedCourses;

    public Student(String studentId, String studentName, Major major) {
        this.studentId = studentId;
        this.studentName = studentName;
        this.major = major;
        this.completedCourses = new HashSet<>();
    }

    public void addCompletedCourse(Course course) {
        completedCourses.add(course);
    }

    public String getStudentId() {
        return studentId;
    }

    public String getStudentName() {
        return studentName;
    }

    public Major getMajor() {
        return major;
    }

    public Set<Course> getCompletedCourses() {
        return completedCourses;
    }

    // ... (other methods)
}

public class Main {
    public static void main(String[] args) {
        Course math101 = new Course("MATH101", "Introduction to Mathematics", 3);
        Course eng101 = new Course("ENG101", "English Composition", 3);
        Course cs101 = new Course("CS101", "Introduction to Computer Science", 3);

        Major mathMajor = new Major("MathMajor", "Mathematics");
        mathMajor.addMandatoryCourse(math101);

        Major engMajor = new Major("EngMajor", "English");
        engMajor.addMandatoryCourse(eng101);

        Major csMajor = new Major("CSMajor", "Computer Science");
        csMajor.addMandatoryCourse(cs101);

        Student student1 = new Student("8001", "Sydney Heimann", mathMajor);
        Student student2 = new Student("8002", "Maddy Cobb", engMajor);
        Student student3 = new Student("8003", "Peyton Shelly", csMajor);

        student1.addCompletedCourse(math101);
        student2.addCompletedCourse(eng101);
        student3.addCompletedCourse(cs101);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter student ID: ");
        String studentId = scanner.nextLine();

        Student student = findStudentById(studentId, student1, student2, student3);
        if (student != null) {
            displayDegreeAudit(student);
        } else {
            System.out.println("Student not found.");
        }
    }

    public static Student findStudentById(String studentId, Student... students) {
        for (Student student : students) {
            if (student.getStudentId().equals(studentId)) {
                return student;
            }
        }
        return null; // Student not found
    }

    public static void displayDegreeAudit(Student student) {
        System.out.println("Degree Audit for " + student.getStudentName() + " (Major: " + student.getMajor().getMajorName() + "):");
        Set<Course> completedCourses = student.getCompletedCourses();
        List<Course> mandatoryCourses = student.getMajor().getMandatoryCourses();

        for (Course mandatoryCourse : mandatoryCourses) {
            if (!completedCourses.contains(mandatoryCourse)) {
                System.out.println(" - " + mandatoryCourse.getCourseName() + " (Incomplete)");
            } else {
                System.out.println(" - " + mandatoryCourse.getCourseName() + " (Complete)");
            }
        }
    }
}
