import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int kilometers = userInput.nextInt();
        double spent_Fuel = userInput.nextDouble();
        
        double result = kilometers / spent_Fuel;
        
        System.out.printf("%.3f km/l\n", result);
        userInput.close();
    }
 
}