use std::io;
use std::iter::FromIterator;
use std::io::Write;
use std::collections::HashMap;

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

fn main() {
    let sys = get_system();
    for state in sys {
        println!("{}", String::from_iter(state.iter()));
    }
}
