import java.util.Scanner;
/**
 * This program will find how many times a substring occurs within a string.
 * @author Lauren White
 * Date: 3/25/25
 * Assignment: CS 123, Lab 6
 */
public class FindSubstring {

    /**
     * This method will find how many times a substring occurs within a string.
     * @param line takes a word as a string.
     * @param substring takes a word to find as a string.
     * @return the amount of times a substring occurs in a larger string.
     */
    public static int find(String line, String substring) {
        int occurrence = 0;
        int counter = 0;
        int subIndex = 0;
        // Main loop that iterates through the main string
        for (int i = 0; i < line.length(); i++){
            // Nested loop that determines if the substring is in the main string
            while (counter < substring.length()) { 
                if (line.charAt(i) == substring.charAt(subIndex)){
                    subIndex++;
                    counter++; 
                } else if (line.charAt(i) != substring.charAt(subIndex)) {
                    subIndex = 0;
                    counter = 0;   
                }
                if (subIndex == substring.length()) {
                    occurrence++;
                    subIndex = 0;
                    counter = 0;
                }
                break;
                 
            }      
        }

        return occurrence;       
    }

     /**
      * This is the main method.
      * @param args takes command line arguments.
      */
      public static void main(String[] args) {
        // Get user input
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String line = in.nextLine();
        System.out.print("Enter a substring to find: ");
        String subline = in.next();
        in.close();
        // Determine how many times the substring occurs
        int found = find(line, subline);
        System.out.println("There is/are " + found + " occurrence(s) of " + subline);       
      }
}