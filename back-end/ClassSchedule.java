import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class ClassSchedule {
    public static void main(String[] args) {
        // Database connection setup (similar to previous example)
        // ...

        try {
            // Create a Scanner to read user input
            Scanner scanner = new Scanner(System.in);

            // Prompt the user to enter a student ID
            System.out.print("Please enter your student ID: ");
            String studentId = scanner.nextLine();

            // Query the database to retrieve the student's major based on the student ID
            // Used to retrieve the major of a student from a database
            String majorQuery = "Retrieve the 'major' of the student whose 'student_id' matches a specified value.";
            PreparedStatement majorStatement = connection.prepareStatement(majorQuery);
            majorStatement.setString(1, studentId);
            ResultSet majorResult = majorStatement.executeQuery();

            if (majorResult.next()) {
                String major = majorResult.getString("major");
                System.out.println("Student's Major: " + major);

                // Query the database to retrieve required classes for the major
                // This query is used to retrieve information about the required classes for a specific major from a database.
                String requiredClassesQuery = "Retrieve class information including class name, class time, room, and the corresponding semester for a specific major from the required classes and class semesters.";
                PreparedStatement requiredClassesStatement = connection.prepareStatement(requiredClassesQuery);
                requiredClassesStatement.setString(1, major);
                ResultSet requiredClassesResult = requiredClassesStatement.executeQuery();

                // Display the schedule of required classes
                while (requiredClassesResult.next()) {
                    String className = requiredClassesResult.getString("class_name");
                    String classTime = requiredClassesResult.getString("class_time");
                    String room = requiredClassesResult.getString("room");
                    String semester = requiredClassesResult.getString("semester");

                    System.out.println("Class: " + className);
                    System.out.println("Time: " + classTime);
                    System.out.println("Room: " + room);
                    System.out.println("Semester: " + semester);
                    System.out.println();
                }
            } else {
                System.out.println("Student not found.");
            }

            // Close resources
            // ...

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
