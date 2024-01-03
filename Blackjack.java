import java.util.Scanner;
import java.util.Random;

public class blackjack {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int money;
        System.out.print("Enter your money: ");
        money = scanner.nextInt();
        System.out.println("Your money " + money + "$");

        while (money > 0) {
            int bet;
            System.out.print("Enter your bet: ");
            bet = scanner.nextInt();

            String[] card = {"HEARTS", "DIAMONDS", "CLUBS", "SPADES"};
            String[] number = {"A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"};

            String youCard = card[random.nextInt(4)];
            String youNumber = number[random.nextInt(13)];

            String dealerCard = card[random.nextInt(4)];
            String dealerNumber = number[random.nextInt(13)];

            int yourTotal = 0;
            int dealerTotal = 0;

            if ("A".equals(youNumber)) {
                if (yourTotal <= 11) {
                    yourTotal += 11;
                } else {
                    yourTotal += 1;
                }
            } else if ("K".equals(youNumber) || "Q".equals(youNumber) || "J".equals(youNumber) || "10".equals(youNumber)) {
                yourTotal += 10;
            } else {
                yourTotal += Integer.parseInt(youNumber);
            }

            if ("A".equals(dealerNumber)) {
                if (dealerTotal <= 11) {
                    dealerTotal += 11;
                } else {
                    dealerTotal += 1;
                }
            } else if ("K".equals(dealerNumber) || "Q".equals(dealerNumber) || "J".equals(dealerNumber) || "10".equals(dealerNumber)) {
                dealerTotal += 10;
            } else {
                dealerTotal += Integer.parseInt(dealerNumber);
            }

            System.out.println("Your hand " + youCard + " " + youNumber + ", Total: " + yourTotal);
            System.out.println("Dealer hand " + dealerCard + " " + dealerNumber + ", Total: " + dealerTotal);

            while (yourTotal < 21 && dealerTotal < 17) {
                int select;
                System.out.print("1: HIT or 2: STAY\n:");
                select = scanner.nextInt();

                if (select == 1) {
                    youCard = card[random.nextInt(4)];
                    youNumber = number[random.nextInt(13)];

                    if ("A".equals(youNumber)) {
                        if (yourTotal <= 11) {
                            yourTotal += 11;
                        } else {
                            yourTotal += 1;
                        }
                    } else if ("K".equals(youNumber) || "Q".equals(youNumber) || "J".equals(youNumber) || "10".equals(youNumber)) {
                        yourTotal += 10;
                    } else {
                        yourTotal += Integer.parseInt(youNumber);
                    }
                } else if (select == 2) {
                    while (dealerTotal < 17) {
                        dealerCard = card[random.nextInt(4)];
                        dealerNumber = number[random.nextInt(13)];

                        if ("A".equals(dealerNumber)) {
                            if (dealerTotal <= 11) {
                                dealerTotal += 11;
                            } else {
                                dealerTotal += 1;
                            }
                        } else if ("K".equals(dealerNumber) || "Q".equals(dealerNumber) || "J".equals(dealerNumber) || "10".equals(dealerNumber)) {
                            dealerTotal += 10;
                        } else {
                            dealerTotal += Integer.parseInt(dealerNumber);
                        }
                    }
                }
                System.out.println("Your hand " + youCard + " " + youNumber + " Your total " + yourTotal);
            }

            System.out.println("Your total " + yourTotal + ", Dealer total " + dealerTotal);

            if (yourTotal <= 21 && dealerTotal <= 21) {
                if (dealerTotal == 21) {
                    System.out.println("Blackjack! Dealer win!");
                    money -= bet;
                } else if (yourTotal == 21) {
                    System.out.println("Blackjack! You win!");
                    money += bet;
                } else if (yourTotal > dealerTotal) {
                    System.out.println("Dealer lost! You win!");
                    money += bet;
                } else if (yourTotal < dealerTotal) {
                    System.out.println("You lost! Dealer win!");
                    money -= bet;
                }
            } else if (yourTotal > 21) {
                System.out.println("You bust! Dealer win!");
                money -= bet;
            } else if (dealerTotal > 21) {
                System.out.println("Dealer bust! You win!");
                money += bet;
            }

            System.out.println("Your money " + money + "$");

            if (money > 0) {
                int select_coe;
                System.out.print("1.Continue or 2.End: ");
                select_coe = scanner.nextInt();
                if (select_coe == 1) {
                    continue;
                } else if (select_coe == 2) {
                    System.out.println("Your last money is " + money + "$");
                    break;
                }
            } else {
                break;
            }
        }

        if (money <= 0) {
            System.out.println("You sank!");
        }
    }
}
