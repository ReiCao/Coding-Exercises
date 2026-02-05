import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int a = userInput.nextInt();
        int b = userInput.nextInt();
        int c = userInput.nextInt();
        int d = userInput.nextInt();
        
        int diferença = (a * b) - (c * d);
        
        System.out.println("DIFERENCA = " + diferença);
        userInput.close();
    }
 
}