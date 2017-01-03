// This is a simple guessing game, based off the example project in the rust
// book. It has a few extra features, such as the out-of-bounds checking,
// replaying, and counting the number of guesses taken.
//
// It's also commented way more than is useful.

extern crate rand; // Lets us use the rand crate

use std::io; // Lets us just call io::something instead of std::io::something
use std::cmp::Ordering;
use rand::Rng; // Same as above

fn main() {
    loop {
        println!("Guess the number! It's between 1 and 100 (inclusive)");
        let secret = rand::thread_rng().gen_range(1,101); // Generate a random number, using the (thread specific) rng

        let mut guesses = 0;

        loop {
            println!("Input your guess:");

            let mut guess = String::new(); // creates a mutable binding and sets it to a new (empty) string

            io::stdin().read_line(&mut guess) // Reads a line from standard input, placing it in guess (by way of a mutable reference)
                .expect("Failed to read line!"); // Just crash if we fail to read a line...

            let guess: u32 = match guess.trim().parse() { // Shadow guess with a new, unsigned int guess, with whitespace stripped and converted into an int
                Ok(num) => num, // Simply pass through the value if the Result is Ok
                Err(_)  => continue // On an error, just keep going.
            };

            if guess > 100 {
                println!("I already told you that the number won't be bigger than 100, don't you trust me?");
            }

            if guess < 1 {
                println!("I swear that the number is between 1 and 100.");
            }

            guesses += 1;

            match guess.cmp(&secret) { // Compare our guess to the secret value
                Ordering::Less    => println!("Too small!"),
                Ordering::Greater => println!("Too big!"),
                Ordering::Equal   => {
                    println!("You win!");
                    break;
                }
            }
        }

        println!("You found the value {} in {} guesses! Nice job :)", secret, guesses);

        println!("Do you want to play again? (Y/n)");
        let mut replay = String::new();

        io::stdin().read_line(&mut replay)
            .expect("Failed to read line!");

        if replay.trim() == "n" {
            println!("Thanks for playing!");
            break;
        }
    }
}
