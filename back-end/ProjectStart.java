import java.util.ArrayList;
import java.util.Scanner;

public class CourseScheduler {

  public static void main(String[] args) {
    
    ArrayList<String> allCourses = new ArrayList<>();
    allCourses.add("English 101");
    allCourses.add("Math 101"); 
    allCourses.add("History 101");
    allCourses.add("Science 101");
    allCourses.add("Art 101");
    allCourses.add("Psychology 101");
    allCourses.add("Music 101");
    allCourses.add("Political Science 101");
    allCourses.add("Economics 101");

    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter completed courses separated by commas: ");
    String input = scanner.nextLine();

    String[] completed = input.split(",");

    ArrayList<String> schedule = new ArrayList<>();

    for(String course : allCourses) {
      boolean completedCourse = false;
      
      for(String c : completed) {
        if(course.equals(c)) {
          completedCourse = true;
          break;
        }
      }
      
      if(!completedCourse && schedule.size() < 4) {
        schedule.add(course);  
      }
    }

    System.out.println("Scheduled Courses:");
    System.out.println(schedule);
  }
}
