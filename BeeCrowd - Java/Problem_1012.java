import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        double a = userInput.nextDouble();
        double b = userInput.nextDouble();
        double c = userInput.nextDouble();
        
        
        double tri =  (a * c) / 2;
        double cir =  3.14159 * (c * c);
        double tra =  ((a + b) * c) / 2;
        double qua =  b * b;
        double ret =  a * b;
        userInput.close();
        
        System.out.printf("TRIANGULO: %.3f%n", tri);
        System.out.printf("CIRCULO: %.3f%n", cir);
        System.out.printf("TRAPEZIO: %.3f%n", tra);
        System.out.printf("QUADRADO: %.3f%n", qua);
        System.out.printf("RETANGULO: %.3f%n", ret);
        
    }
 
}