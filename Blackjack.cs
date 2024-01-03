using System;

class Program
{
    static void Main()
    {
        Random random = new Random();

        Console.Write("Enter your money: ");
        int money = int.Parse(Console.ReadLine());
        Console.WriteLine($"Your money {money}$");

        while (money > 0)
        {
            Console.Write("Enter your bet: ");
            int bet = int.Parse(Console.ReadLine());

            string[] card = { "HEARTS", "DIAMONDS", "CLUBS", "SPADES" };
            string[] number = { "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" };

            string youCard = card[random.Next(card.Length)];
            string youNumber = number[random.Next(number.Length)];

            string dealerCard = card[random.Next(card.Length)];
            string dealerNumber = number[random.Next(number.Length)];

            int yourTotal = 0;
            int dealerTotal = 0;

            if (youNumber == "A")
            {
                yourTotal = yourTotal <= 11 ? 11 : 1;
            }
            else if (youNumber == "K" || youNumber == "Q" || youNumber == "J" || youNumber == "10")
            {
                yourTotal += 10;
            }
            else
            {
                yourTotal += int.Parse(youNumber);
            }

            if (dealerNumber == "A")
            {
                dealerTotal = dealerTotal <= 11 ? 11 : 1;
            }
            else if (dealerNumber == "K" || dealerNumber == "Q" || dealerNumber == "J" || dealerNumber == "10")
            {
                dealerTotal += 10;
            }
            else
            {
                dealerTotal += int.Parse(dealerNumber);
            }

            Console.WriteLine($"Your hand {youCard} {youNumber}, Total: {yourTotal}\nDealer hand {dealerCard} {dealerNumber}, Total: {dealerTotal}");

            while (yourTotal < 21 && dealerTotal < 17)
            {
                Console.Write("1: HIT or 2: STAY\n:");
                string select = Console.ReadLine();

                if (select == "1")
                {
                    youCard = card[random.Next(card.Length)];
                    youNumber = number[random.Next(number.Length)];

                    if (youNumber == "A")
                    {
                        yourTotal = yourTotal <= 11 ? yourTotal + 11 : yourTotal + 1;
                    }
                    else if (youNumber == "K" || youNumber == "Q" || youNumber == "J" || youNumber == "10")
                    {
                        yourTotal += 10;
                    }
                    else
                    {
                        yourTotal += int.Parse(youNumber);
                    }
                }
                else if (select == "2")
                {
                    while (dealerTotal < 17)
                    {
                        dealerCard = card[random.Next(card.Length)];
                        dealerNumber = number[random.Next(number.Length)];

                        if (dealerNumber == "A")
                        {
                            dealerTotal = dealerTotal <= 11 ? dealerTotal + 11 : dealerTotal + 1;
                        }
                        else if (dealerNumber == "K" || dealerNumber == "Q" || dealerNumber == "J" || dealerNumber == "10")
                        {
                            dealerTotal += 10;
                        }
                        else
                        {
                            dealerTotal += int.Parse(dealerNumber);
                        }
                    }
                }

                Console.WriteLine($"Your hand {youCard} {youNumber} Your total {yourTotal}");
            }

            Console.WriteLine($"Your total {yourTotal}, Dealer total {dealerTotal}");

            if (yourTotal <= 21 && dealerTotal <= 21)
            {
                if (dealerTotal == 21)
                {
                    Console.WriteLine("Blackjack! Dealer win!");
                    money -= bet;
                }
                else if (yourTotal == 21)
                {
                    Console.WriteLine("Blackjack! You win!");
                    money += bet;
                }
                else if (yourTotal > dealerTotal)
                {
                    Console.WriteLine("Dealer lost! You win!");
                    money += bet;
                }
                else if (yourTotal < dealerTotal)
                {
                    Console.WriteLine("You lost! Dealer win!");
                    money -= bet;
                }
            }
            else if (yourTotal > 21)
            {
                Console.WriteLine("You bust! Dealer win!");
                money -= bet;
            }
            else if (dealerTotal > 21)
            {
                Console.WriteLine("Dealer bust! You win!");
                money += bet;
            }

            Console.WriteLine($"Your money {money}$");

            if (money > 0)
            {
                Console.Write("1.Continue or 2.End: ");
                string selectCoe = Console.ReadLine();

                if (selectCoe == "2")
                {
                    Console.WriteLine($"Your last money is {money}$");
                    break;
                }
            }
            else
            {
                break;
            }
        }

        if (money <= 0)
        {
            Console.WriteLine("You sank!");
        }
    }
}
