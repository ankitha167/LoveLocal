import java.util.*;
public class Main {
    public static int lengthOfLastWord(String s) {
        String[] words = s.split(" ");
        if (words.length == 0) {
            return 0;
        }
        return words[words.length - 1].length();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        int length = lengthOfLastWord(input);
        System.out.println("Length of last word: " + length);
    }
}
/* In this code I have define a class named Main and a function named lengthOfLastWord which returns an integer value. 
The function accepts a string value and the variable named is s, which is passed as a parameter to the function. 
I created a String array var named as 'words' and use the split() method for splitting the string based on whitespaces.
we check if the length of the string is more than 0 , if not it will create an array 'words' with a single element which is 
basically an empty string " " and in the return statement it will return 0. If the length of the word is more than 0, it proceeds 
to the return statement , fetching the last element words[words.length - 1] so for example if the length of the array is 5 
the index value of the last value is 4 , words[4] similarly it points to the last element and find the length of that string 
and return the length. In the main function I use Scanner class to take the input from user. length which is a int variable finds 
the length of the last word by calling the function and passing a parameter that is the input given by the user.*/
