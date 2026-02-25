import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int distance = userInput.nextInt();
        
        int minutes = distance * 2;
        
        System.out.printf("%d minutos%n", minutes);
        
        userInput.close();
    }
 
}