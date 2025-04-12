import java.util.*;

public class IstTime {
    static Map<String, Double> timeDifferences = new HashMap<>();

    static {
        timeDifferences.put("USA (New York)", -9.5);
        timeDifferences.put("UK (London)", -4.5);
        timeDifferences.put("Germany", -3.5);
        timeDifferences.put("Japan", 3.5);
        timeDifferences.put("Australia (Sydney)", 5.5);
        timeDifferences.put("UAE (Dubai)", -1.5);
        timeDifferences.put("China", 2.5);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String again;

        do {
            System.out.print("Enter IST time in HH:mm (24-hour format): ");
            String inputTime = scanner.nextLine();

            System.out.println("Choose a country:");
            int i = 1;
            List<String> countries = new ArrayList<>(timeDifferences.keySet());
            for (String country : countries) {
                System.out.println(i + ". " + country);
                i++;
            }

            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline
            String selectedCountry = countries.get(choice - 1);
            double offset = timeDifferences.get(selectedCountry);

            String[] parts = inputTime.split(":");
            int hours = Integer.parseInt(parts[0]);
            int minutes = Integer.parseInt(parts[1]);

            int totalMinutes = (int)(hours * 60 + minutes + offset * 60);
            if (totalMinutes < 0) totalMinutes += 1440;
            totalMinutes %= 1440;

            int newHours = totalMinutes / 60;
            int newMinutes = totalMinutes % 60;

            System.out.printf("Time in %s: %02d:%02d\n", selectedCountry, newHours, newMinutes);

            System.out.print("Do you want to use the program again? (yes/no): ");
            again = scanner.nextLine().trim().toLowerCase();
        } while (again.equals("yes"));

        System.out.println("Goodbye!");
    }

}
 
