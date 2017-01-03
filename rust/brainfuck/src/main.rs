use std::collections::HashMap;
use std::char;
use std::io;

fn main() {
    let mut program_string = String::new();
    println!("Enter the brainfuck program:");
    io::stdin().read_line(&mut program_string)
        .expect("Failed to read line!");

    let mut program: Vec<char> = vec![];
    for command in program_string.chars() {
        program.push(command);
    }
    let program = program;

    let mut command_map: HashMap<char, fn(&mut [i8; 30000], &mut usize, &Vec<char>, &mut usize, &mut i32)> = HashMap::new();
    command_map.insert('+', plus);
    command_map.insert('-', minus);
    command_map.insert('<', lessthan);
    command_map.insert('>', greaterthan);
    command_map.insert('.', period);
    command_map.insert('[', openbrace);
    command_map.insert(']', closebrace);
    let command_map = command_map;

    let mut data: [i8; 30000] = [0; 30000];
    let mut dptr: usize = 0;
    let mut pptr: usize = 0;
    let mut depth: i32 = 0;

    loop {
        match command_map.get(&program[pptr]) {
            Some(x) => x(&mut data, &mut dptr, &program, &mut pptr, &mut depth),
            None    => pptr += 1
        }
        if pptr == program.len() {
            break;
        }
    }
}

fn plus(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    data[*dptr] = data[*dptr].wrapping_add(1);
    *pptr += 1;
}

fn minus(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    data[*dptr] = data[*dptr].wrapping_sub(1);
    *pptr += 1;
}

fn lessthan(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    *dptr -= 1;
    *pptr += 1;
}

fn greaterthan(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    *dptr += 1;
    *pptr += 1;
}

fn period(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    match char::from_u32(data[*dptr] as u32) {
        Some(x) => print!("{}", x),
        None    => ()
    }
    *pptr += 1;
}

fn openbrace(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    let old_depth = *depth;
    *depth += 1;
    if data[*dptr] == 0 {
        while *depth != old_depth {
            *pptr += 1;
            match program[*pptr] {
                '[' => *depth += 1,
                ']' => *depth -=1,
                _   => ()
            }
        }
    }
    *pptr += 1;
}

fn closebrace(data: &mut [i8;30000], dptr: &mut usize, program: &Vec<char>, pptr: &mut usize, depth: &mut i32) {
    let old_depth = *depth;
    *depth -= 1;
    if data[*dptr] != 0 {
        while *depth != old_depth {
            *pptr -= 1;
            match program[*pptr] {
                '[' => *depth += 1,
                ']' => *depth -= 1,
                _   => ()
            }
        }
    }
    *pptr += 1;
}
