import java.io.IOException;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        double hoursSpent = userInput.nextInt();
        double avgSpeed = userInput.nextInt();
        double kmL = 12;
        
        double result = (hoursSpent * avgSpeed) / kmL;
        
        System.out.printf("%.3f%n", result);
        
        userInput.close();
    }
 
}