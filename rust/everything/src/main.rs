// A sample project to use ALL THE SYNTAX FEATURES

fn main() {
    println!("Hello, world!");
    let number: i32 = 42;
    let (x,y,z) = (1,2,3);
    let small_int:i8 = number as i8; // Unsafe?
    let small_int:i32 = small_int as i32 + 212; // Shadowing!
    let mut thing = 42;
    thing += 106;
    print_int(thing);
    print_int(small_int);
    println!("{},{},{}", x, y, z);
    print_int(sum(thing, number));
    let func = print_int; // Function pointers!
    func(123);

    let do_the_thing = true;
    if do_the_thing {
        let two_hearts = '💕';
        println!("{0}{0}{0}", two_hearts);
    }

    let some_array = ["thing1", "thing2", "thing3"];
    for element in some_array.into_iter() {
        println!("some_array has element {}", element);
    }

    let a = [0, 1, 2, 3, 4];
    let middle_of_a = &a[1..a.len()-1];

    for i in middle_of_a {
        println!("{}", i);
    }

    let i_got_tuples = (123, 456, "yay");
    println!("{}", i_got_tuples.2);

    for i in 0..10 {
        if i % 2 == 0 { continue; }

        println!("{}", i);
    }

}

fn print_int(x: i32) {
    println!("print_int is printing {}!", x);
}

fn sum(x: i32, y: i32) -> i32 {
    x + y
}
