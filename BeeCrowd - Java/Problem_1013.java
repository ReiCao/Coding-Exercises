import java.io.IOException;
import java.util.Scanner;
import java.lang.Math;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int a = userInput.nextInt();
        int b = userInput.nextInt();
        int c = userInput.nextInt();
        userInput.close();
        
        int maior = maiorAB(maiorAB(a, b), c);
        
        System.out.println(maior+" eh o maior");
    }
    
    static int maiorAB(int a, int b){
        return (a + b + Math.abs(a-b))/2;
    }
}