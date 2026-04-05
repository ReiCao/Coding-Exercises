import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int days = scanner.nextInt();
        int years = 0, months = 0;
        scanner.close();
        
        while(days >= 30){
            if(days >= 365){
                years++;
                days -= 365;
            } else if(days >= 30) {
                months++;
                days -= 30;
            }
        }
        
        System.out.println(years +" ano(s)");
        System.out.println(months +" mes(es)");
        System.out.println(days + " dia(s)");
    }
 
}