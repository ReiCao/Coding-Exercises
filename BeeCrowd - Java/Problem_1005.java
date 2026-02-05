import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner userInput = new Scanner(System.in);
        double a = userInput.nextDouble();
        double b = userInput.nextDouble();
        
        double media = (a * 3.5) + (b * 7.5);
        media /= 3.5 + 7.5;
        
        userInput.close();
        
        System.out.printf("MEDIA = %.5f%n", media);
    }
 
}