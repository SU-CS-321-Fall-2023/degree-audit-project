import java.util.*;
import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;
import java.io.FileReader;
import java.io.IOException;

class Course {
    private String courseId;
    private String courseName;
    private int creditHours;
    private int semester;

    public Course(String courseId, String courseName, int creditHours, int semester) {
        this.courseId = courseId;
        this.courseName = courseName;
        this.creditHours = creditHours;
        this.semester = semester;
    }

    public String getCourseName() {
        return courseName;
    }

    // ... (other getters and methods as needed)
}

class Major {
    private String majorId;
    private String majorName;
    //private List<Course> mandatoryCourses;
    private Map<Integer, List<Course>> coreCoursesBySemester;

    public Major(String majorId, String majorName) {
        this.majorId = majorId;
        this.majorName = majorName;
        //this.mandatoryCourses = new ArrayList<>();
        this.coreCoursesBySemester = new HashMap<>();
    }

    // Getter for majorName
    public String getMajorName() {
        return majorName;
    }

    //public void addMandatoryCourse(Course course) {
        //mandatoryCourses.add(course);
    //}

    public void addCoreCourses(int semester, List<Course> coreCourses){
        coreCoursesBySemester.put(semester, coreCourses);
    }
    //public List<Course> getMandatoryCourses() {
       // return mandatoryCourses;
    //}

    // Get core courses for a specific semester
    public List<Course> getCoreCourses(int semester) {
        return coreCoursesBySemester.get(semester);
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
        String csvFilePath = "C:\\Users\\sydne\\OneDrive - Stetson University, Inc\\Desktop\\Academic Programs - Stetson University.csv";

        try (CSVReader reader = new CSVReader(new FileReader(csvFilePath))){
            String[] nextLine;
            while ((nextLine = reader.readNext()) != null){
                //process the data as needed
                String majorName = nextLine[0];
                //other fields
                System.out.println("Major: " + majorName);
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }

        Course math101 = new Course("MATH101", "Introduction to Mathematics", 4, 1);
        Course eng101 = new Course("ENG101", "English Composition", 4, 1);
        Course cs101 = new Course("CS101", "Introduction to Computer Science", 4, 1);

        Course math201 = new Course("MATH201", "Advanced Mathematics", 4, 2);
        Course eng201 = new Course("ENG201", "Advanced English Composition", 4, 2);
        Course cs201 = new Course("CS201", "Advanced Computer Science", 4, 2);

        Major mathMajor = new Major("MathMajor", "Mathematics");
        //mathMajor.addMandatoryCourse(math101);
        mathMajor.addCoreCourses(1, Arrays.asList(math101));
        mathMajor.addCoreCourses(2, Arrays.asList(math201));

        Major engMajor = new Major("EngMajor", "English");
        //engMajor.addMandatoryCourse(eng101);
        engMajor.addCoreCourses(1, Arrays.asList(eng101));
        engMajor.addCoreCourses(2, Arrays.asList(eng201));

        Major csMajor = new Major("CSMajor", "Computer Science");
        //csMajor.addMandatoryCourse(cs101);
        csMajor.addCoreCourses(1, Arrays.asList(cs101));
        csMajor.addCoreCourses(2, Arrays.asList(cs201));

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
        if (student != null) { int semester = 1; //replace with desired semester value
            displayDegreeAudit(student,semester);
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

    public static void displayDegreeAudit(Student student, int semester) {
        System.out.println("Degree Audit for " + student.getStudentName() + " (Major: " + student.getMajor().getMajorName() + ", Semester: " + semester + "):");
        Set<Course> completedCourses = student.getCompletedCourses();
        //List<Course> mandatoryCourses = student.getMajor().getMandatoryCourses();
        List<Course> coreCourses = student.getMajor().getCoreCourses(semester);

        for (Course coreCourse : coreCourses) {
            if (!completedCourses.contains(coreCourse)) {
                System.out.println(" - " + coreCourse.getCourseName() + " (Incomplete)");
            } else {
                System.out.println(" - " + coreCourse.getCourseName() + " (Complete)");
            }
        }
    }
}
