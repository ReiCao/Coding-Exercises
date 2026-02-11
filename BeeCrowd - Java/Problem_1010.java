import java.io.IOException;
import java.util.Scanner;

public class Main {
 
    public static void main(String[] args) throws IOException {
        Scanner user_Input = new Scanner(System.in);
        int first_Code, second_Code, first_Amount, second_Amount;
        double first_Price, second_Price;
        
        String first_Line = user_Input.nextLine();
        String[] first_Line_Values = first_Line.split("\\s+");
        first_Code = Integer.parseInt(first_Line_Values[0]);
        first_Amount = Integer.parseInt(first_Line_Values[1]);
        first_Price = Double.parseDouble(first_Line_Values[2]);
        
        String second_Line = user_Input.nextLine();
        String[] second_Line_Values = second_Line.split("\\s+");
        second_Code = Integer.parseInt(second_Line_Values[0]);
        second_Amount = Integer.parseInt(second_Line_Values[1]);
        second_Price = Double.parseDouble(second_Line_Values[2]);
        
        double total_Price = (first_Amount * first_Price) + (second_Amount * second_Price);
        
        System.out.printf("VALOR A PAGAR: R$ %.2f%n", total_Price);
    }
 
}