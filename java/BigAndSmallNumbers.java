import java.util.Scanner;
/**
 * This program will tell you the largest and smallest digits in a number.
 * @author Lauren White
 * Date: 3/7/25
 * Assignment: Lab 5, part 3, CS123
 */
public class BigAndSmallNumbers {

    /**
     * This method determines the largest and smalles digits in a number.
     * @param number takes a number as a string.
     */
    public static void determineSize (String number) {
        int index = 0;
        int largest = Integer.parseInt("" + number.charAt(0));
        int smallest = Integer.parseInt("" + number.charAt(0));
        //Iterates through string and finds the largest and smallest digits.
        while (index < number.length()) {
            int realNumber = Integer.parseInt("" + number.charAt(index));
            if (smallest > realNumber) {
                smallest = realNumber;
            } else if (largest < realNumber) {
                largest = realNumber;
            }
            index++;
        }
        //Output
        System.out.println("The largest digit is " + largest);
        System.out.println("The smallest digit is " + smallest);
    }

    /**
     * This is the main method.
     * @param args takes command line arguments
     */
    public static void main (String [] args) {
        Scanner in = new Scanner (System.in);
        //Prompts and gets user input
        System.out.print("Enter a multi-digit number: ");
        String userNumber = in.next();
        //Final output. Closes scanner.
        determineSize(userNumber);
        in.close();
    }
}