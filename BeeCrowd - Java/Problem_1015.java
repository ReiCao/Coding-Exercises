import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        double x1 = userInput.nextDouble();
        double y1 = userInput.nextDouble();
        double x2 = userInput.nextDouble();
        double y2 = userInput.nextDouble();
        
        double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        
        System.out.printf("%.4f%n", distance);
        userInput.close();
    }
 
}