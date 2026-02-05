import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner userInput = new Scanner(System.in);
        double pi = 3.14159;
        double radius = userInput.nextDouble();
        userInput.close();
 
        double radiuspower = Math.pow(radius, 2);
        double area = pi * radiuspower;
        
        System.out.printf("A=%.4f%n", area);
    }
 
}