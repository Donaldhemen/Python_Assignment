// import scanner 
// read values of 3 scores from user
// calculate average of 3 scores
// if/else for letter grade for A, B, C, D and F

import java.util.Scanner;
public class AverageLetterGradeJava {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.print("Enter first score: ");
		int firstScore = input.nextInt();

		System.out.print("Enter second score: ");
		int secondScore = input.nextInt();

		System.out.print("Enter third score: ");
		int thirdScore = input.nextInt();

		int average = (firstScore + secondScore + thirdScore) / 3;

		if (average >= 90 && average <= 100) {
			System.out.print("Grade is 'A");
		}
		else if (average >= 80) {
			System.out.print("Grade is 'B'");
		}
		else if (average >= 70) {
			System.out.print("Grade is 'C'");
		}
		else if (average >= 60) {
			System.out.print("Grade is 'D'");
		}
		else {
			System.out.print("Grade is 'F'");
		}
	}
}