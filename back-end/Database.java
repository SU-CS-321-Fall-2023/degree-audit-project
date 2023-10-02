import java.util.*;

import static java.util.Collections.*;

public class Database {
    public boolean test = false;
    public static void main(String[] args) {

        Map<String, Map<String, Object>> majors = new HashMap<>();

        // Majors are Computer Science, Accounting, and Bachelor of Music with Emphasis in Business

        Map<String, Object> compSciMajor = new HashMap<>();
        compSciMajor.put("Major Requirements", Arrays.asList(
                "CSCI 141", "CSCI 142", "CSCI 201", "CSCI 211", "CSCI 221",
                "CSCI 321", "CSCI 301", "CSCI 311", "CSCI 498", "CSCI 499"
        ));
        compSciMajor.put("Collateral Requirements", Arrays.asList(
                "MATH 142Q",
                "Select two Natural Science classes excluding Math/Computer Science"
        ));
        compSciMajor.put("General Electives", 8);

        Map<String, Object> accountingMajor = new HashMap<>();
        accountingMajor.put("Major Requirements", Arrays.asList(
                "ACCT 202", "ACCT 300", "ACCT 303", "ACCT 304"
        ));
        Map<String, Object> accountingConcentrations = new HashMap<>();
        accountingConcentrations.put("Accounting", Arrays.asList(
                "ACCT 310", "ACCT 410", "ACCT 421", "ACCT 440",
                "Select one of the following",
                "Select two of the following, one of which must be an ACCT course"
        ));
        accountingConcentrations.put("CPA", Arrays.asList(
                "ACCT 311", "ACCT 406", "ACCT 410", "ACCT 421", "ACCT 440"
        ));
        accountingConcentrations.put("Data Analytics", Arrays.asList(
                "ACCT 410", "ACCT 440", "BSAN 300", "BSAN 465",
                "Select two of the following, one of which must be an ACCT course"
        ));
        accountingConcentrations.put("Financial Planning", Arrays.asList(
                "ACCT 310", "ACCT 421", "FINA 318", "Select two of the following"
        ));
        accountingMajor.put("Concentrations", accountingConcentrations);
        accountingMajor.put("General Electives", 7);

        Map<String, Object> musicMajor = new HashMap<>();
        musicMajor.put("General Education Requirements", Arrays.asList(
                "FSEM 100", "Individuals, Societies, and Social Systems",
                "Language (102L level)", "Historical Inquiry",
                "Personal and Social Responsibility", "Quantitative Reasoning",
                "Non-music Elective"
        ));
        musicMajor.put("Theory", Arrays.asList("MUSC 171", "MUSC 172", "MUSC 271"));
        musicMajor.put("Aural Training", Arrays.asList("MUSC 173", "MUSC 174", "MUSC 273", "MUSC 274"));
        musicMajor.put("Functional Keyboard", Arrays.asList("MUSC 175", "MUSC 176", "MUSC 275", "MUSC 276"));
        musicMajor.put("Music History", List.of("MUSC 211H"));
        musicMajor.put("Lower-division lessons", List.of("MUSA 112"));
        musicMajor.put("Music Culture", List.of("MUSC 151"));
        musicMajor.put("Conducting", List.of("MUSC 277"));
        musicMajor.put("Technology for Musicians", List.of("MUSC 259"));
        musicMajor.put("Career Skills", List.of("MUSC 300"));
        musicMajor.put("Major Requirements", Arrays.asList(
                "External emphasis courses",
                "Upper-division lessons/Music Experience Bundle",
                "Eight Ensembles",
                "Upper-division Theory or Music History and Literature elective"
        ));
        musicMajor.put("General Elective", 2);
        musicMajor.put("Other Requirements", Arrays.asList("Sophomore Decision", "Oral Communication Competency"));

        // Add majors to the database
        majors.put("Computer Science", compSciMajor);
        majors.put("Accounting", accountingMajor);
        majors.put("Bachelor of Music with Emphasis in Business", musicMajor);

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your major: ");
        String userMajor = scanner.nextLine();



        if (majors.containsKey(userMajor)) {
            Map<String, Object> majorInfo = majors.get(userMajor);
            System.out.println("Required courses for " + userMajor + ":");
            printCourses(majorInfo.get("Major Requirements"));
        } else {
            System.out.println("Major " + userMajor + " not found in the database.");
        }
    }

    private static void printCourses(Object courses) {
        if (courses instanceof List) {
            List<String> courseList = unmodifiableList((List<String>) courses);
            for (String course : courseList) {
                System.out.println(course);
            }
        }
    }
}
