import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int number = userInput.nextInt();
        int workedHours = userInput.nextInt();
        double salaryPerHour = userInput.nextDouble();
        
        double totalSalary = workedHours * salaryPerHour;
        
        System.out.println("NUMBER = " + number);
        System.out.println("SALARY = U$ " + String.format("%.2f", totalSalary));
        
        userInput.close();
        
    }
}