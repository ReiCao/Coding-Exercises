import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner userInput = new Scanner(System.in);
        int hour = 0, minute = 0;
        int seconds = userInput.nextInt();
        
        while(seconds > 59){
            if (seconds >= 3600){
                hour += 1;
                seconds -= 3600;
            } else if (seconds >= 60){
                minute += 1;
                seconds -= 60;
            }
        }
        System.out.printf("%d:%d:%d%n", hour, minute, seconds);
        
    }
 
}