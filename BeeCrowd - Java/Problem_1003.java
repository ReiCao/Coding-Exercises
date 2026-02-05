import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        
        Scanner userInput = new Scanner(System.in);
        int A = userInput.nextInt();
        int B = userInput.nextInt();
        userInput.close();
        
        int result = A + B;
        System.out.println("SOMA = " + result);

    }
 
}