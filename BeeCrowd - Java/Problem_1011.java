import java.io.IOException;
import java.util.Scanner;
import java.lang.Math;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        double radius = userInput.nextDouble();
        userInput.close();
        
        double pi =  3.14159;
        double result = (4/3.0) * pi * Math.pow(radius, 3);
        
        System.out.printf("VOLUME = %.3f%n", result);
        
    }
 
}