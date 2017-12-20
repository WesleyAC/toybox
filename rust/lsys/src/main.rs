extern crate image;

use std::io;
use std::iter::FromIterator;
use std::io::Write;
use std::collections::HashMap;

use image::RgbImage;

struct LSystem {
    axiom: Vec<char>,
    rules: HashMap<char, Vec<char>>,
    state: Vec<char>
}

impl LSystem {
    fn new(axiom: Vec<char>, rules: HashMap<char, Vec<char>>) -> Self {
        LSystem { axiom: axiom.clone(), rules: rules, state: axiom.clone() }
    }
}

impl Iterator for LSystem {
    type Item = Vec<char>;

    fn next(&mut self) -> Option<Self::Item> {
        let mut next_state: Vec<char> = vec![];
        for v in &self.state {
            let mut expanded = self.rules.get(v).unwrap_or(&vec![*v]).clone();
            next_state.append(&mut expanded);
        }
        self.state = next_state.clone();
        Some(next_state)
    }
}

fn get_system() -> LSystem {
    print!("axiom: ");
    io::stdout().flush();
    let mut axiom = String::new();
    io::stdin().read_line(&mut axiom);
    let axiom = Vec::from_iter(axiom.as_str().chars().filter(|x| *x != '\n'));
    println!("{:?}", axiom);

    let mut rules = HashMap::new();
    loop {
        let mut rule_in = String::new();
        print!("rule(in): ");
        io::stdout().flush();
        io::stdin().read_line(&mut rule_in);

        if rule_in == "\n" { break; }

        let mut rule_out = String::new();
        print!("rule(out): ");
        io::stdout().flush();
        io::stdin().read_line(&mut rule_out);

        rules.insert(rule_in.as_str().chars().next().unwrap(), Vec::from_iter(rule_out.as_str().chars().filter(|x| *x != '\n')));
    }

    LSystem::new(axiom, rules)
}

#[derive(Copy,Clone)]
struct TurtleState {
    x: u32,
    y: u32,
    theta: f64
}

fn draw_line(img: &mut RgbImage, x0: i32, y0: i32, x1: i32, y1: i32) {
    let mut x0 = x0;
    let mut y0 = y0;

    let dx = if x0 > x1 { x0 - x1 } else { x1 - x0 };
    let dy = if y0 > y1 { y0 - y1 } else { y1 - y0 };

    let sx = if x0 < x1 { 1 } else { -1 };
    let sy = if y0 < y1 { 1 } else { -1 };

    let mut err = if dx > dy { dx } else {-dy} / 2;
    let mut err2;

    loop {
        img.get_pixel_mut(x0 as u32, y0 as u32).data = [255, 255, 255];

        if x0 == x1 && y0 == y1 { break };

        err2 = 2 * err;

        if err2 > -dx { err -= dy; x0 += sx; }
        if err2 < dy { err += dx; y0 += sy; }
    }
}

fn turtle_forward(turtle_state: &mut TurtleState, mut image: &mut RgbImage) {
    let new_x = (turtle_state.x as i32) + ((f64::cos(turtle_state.theta)*10.0) as i32);
    let new_y = (turtle_state.y as i32) + ((f64::sin(turtle_state.theta)*10.0) as i32);
    draw_line(&mut image,
              turtle_state.x as i32,
              turtle_state.y as i32,
              new_x,
              new_y);
    turtle_state.x = new_x as u32;
    turtle_state.y = new_y as u32;
}

fn main() {
    let mut n = 0;
    //let sys = get_system();
    let mut rules = HashMap::new();
    rules.insert('X', vec!['X','+','Y','F','+']);
    rules.insert('Y', vec!['-','F','X','-','Y']);
    let sys = LSystem::new(vec!['F','X'], rules);

    for state in sys {
        let mut turtle_state = TurtleState { x: 1024, y: 1024, theta: 0.0 };
        let mut image = RgbImage::new(2048, 2048);
        for action in state {
            match action {
                'F' => { turtle_forward(&mut turtle_state, &mut image); },
                '-' => { turtle_state.theta -= 3.1415 / 2.0; },
                '+' => { turtle_state.theta += 3.1415 / 2.0; },
                _   => {}
            }
        }
        image.save(format!("/tmp/out/{:010}.png", n)).unwrap();
        n += 1;
        println!("{}", n);
    }
}
