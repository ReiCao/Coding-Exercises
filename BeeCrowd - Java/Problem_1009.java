import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        String name = userInput.nextLine();
        double fixed_Salary = userInput.nextDouble();
        double total_Sales = userInput.nextDouble();
        
        double total_Salary = fixed_Salary + total_Sales * 0.15;
        
        System.out.printf("TOTAL = R$ %.2f%n", total_Salary);
        
        userInput.close();
    }
 
}