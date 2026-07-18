// import scanner 
// collect input for father's age 
// collect input for son's age
// if statement for age range from 1 to 80 else invalid input
// calculate years to double = fathers age - sons age * 2
// if years to double is positive, display Was twice his sons age at answer
// else = 0 - answer, then display will be double his son's age in answer

import java.util.Scanner;
public class CalculateYearsAgoJava {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		System.out.print("Enter father's current age: ");
		int fathersAge = input.nextInt();

		System.out.print("Enter son's current age: ");
		int sonsAge = input.nextInt();

		if (fathersAge >= 1 && fathersAge <= 80 && sonsAge >= 1 && sonsAge<= 80) {
			int yearsAgo = fathersAge - (sonsAge * 2);
			if (yearsAgo >= 0) {
				System.out.println("The father will be twice as old as his son in the next " +yearsAgo+ "years");

			}
			else 
				System.out.printf("The father was twice as old as his son's age %d years", 0-yearsAgo);

		}
		else {
			System.out.println("Invalid input");
		}
	}
}