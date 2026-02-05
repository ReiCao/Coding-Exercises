import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner userInput = new Scanner(System.in);
        double a = userInput.nextDouble();
        double b = userInput.nextDouble();
        double c = userInput.nextDouble();
        
        double media = ((a * 2) + (b * 3) + (c * 5)) / (2 + 3 + 5);
        
        userInput.close();
        
        System.out.printf("MEDIA = %.1f%n", media);
    }
 
}