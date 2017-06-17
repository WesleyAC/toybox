extern crate piston;
extern crate piston_window;
extern crate graphics;
extern crate glutin_window;
extern crate opengl_graphics;

use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;
use opengl_graphics::{GlGraphics, OpenGL};
use glutin_window::GlutinWindow;
use piston::window::WindowSettings;
use piston::event_loop::{Events, EventSettings};
use piston::input::*;

struct Point {
    x: f64,
    y: f64,
    z: f64
}

impl Point {
    fn rotate(&self, x: f64, y: f64, z: f64) -> Point {
        let mut rp = Point { x: self.x, y: self.y, z: self.z };

        let xn = rp.x * z.cos() - rp.y * z.sin();
        let yn = rp.x * z.sin() + rp.y * z.cos();
        rp.x = xn;
        rp.y = yn;

        let xn = rp.x * y.cos() - rp.z * y.sin();
        let zn = rp.x * y.sin() + rp.z * y.cos();
        rp.x = xn;
        rp.z = zn;

        let zn = rp.z * x.cos() - rp.y * x.sin();
        let yn = rp.z * x.sin() + rp.y * x.cos();
        rp.z = zn;
        rp.y = yn;

        rp
    }

    fn translate(&self, x: f64, y: f64, z: f64) -> Point {
        let rp = Point { x: self.x + x, y: self.y + y, z: self.z + z };
        rp
    }
}

//TODO(Wesley) Merge point implementations
struct Point2 {
    x: f64,
    y: f64
}

struct Model {
    points: Vec<Point>,
    edges: Vec<(usize, usize)>
}

struct Viewport {
    x_rot: f64,
    y_rot: f64,
    z_rot: f64,
    x_trans: f64,
    y_trans: f64,
    z_trans: f64
}

pub struct App {
    gl: GlGraphics,
    model: Model,
    vp: Viewport
}

impl App {
    fn render(&mut self, args: &RenderArgs) {
        let ref model = self.model;
        let ref vp = self.vp;
        self.gl.draw(args.viewport(), |c, gl| {
            // Clear the screen.
            graphics::clear([0.7, 0.6, 0.75, 1.0], gl);

            let mut projected_points: Vec<Point2> = vec![];
            for point in &model.points {
                let pt = point.translate(vp.x_trans, vp.y_trans, vp.z_trans).rotate(vp.x_rot, vp.y_rot, vp.z_rot);

                let x = pt.x * 256.0 / pt.z;
                let y = pt.y * 256.0 / pt.z;
                projected_points.push(Point2 {x: x, y: y});
            }
            for edge in &model.edges {
                graphics::line([0.0, 0.0, 0.0, 1.0], 0.5,
                               [projected_points[edge.0].x + 400.0,
                                projected_points[edge.0].y + 300.0,
                                projected_points[edge.1].x + 400.0,
                                projected_points[edge.1].y + 300.0],
                               c.transform, gl);
            }
        });
    }

    fn update(&mut self, button: piston_window::Button) {
        use piston_window::Button::Keyboard;
        use piston_window::Key;

        if button == Keyboard(Key::W) {
            self.vp.x_rot += 0.05;
        } else if button == Keyboard(Key::S) {
            self.vp.x_rot -= 0.05;
        } else if button == Keyboard(Key::A) {
            self.vp.y_rot += 0.05;
        } else if button == Keyboard(Key::D) {
            self.vp.y_rot -= 0.05;
        } else if button == Keyboard(Key::Q) {
            self.vp.z_rot += 0.05;
        } else if button == Keyboard(Key::E) {
            self.vp.z_rot -= 0.05;
        } else if button == Keyboard(Key::I) {
            self.vp.z_trans -= 1.0;
        } else if button == Keyboard(Key::K) {
            self.vp.z_trans += 1.0;
        } else if button == Keyboard(Key::J) {
            self.vp.x_trans -= 1.0;
        } else if button == Keyboard(Key::L) {
            self.vp.x_trans += 1.0;
        } else if button == Keyboard(Key::U) {
            self.vp.y_trans -= 1.0;
        } else if button == Keyboard(Key::O) {
            self.vp.y_trans += 1.0;
        }
    }
}

fn load_object(name: &str) -> Model {
    let file = File::open(name).unwrap();

    let mut points: Vec<Point> = vec![];
    let mut edges: Vec<(usize, usize)> = vec![];

    for line in BufReader::new(file).lines() {
        let line = line.unwrap();
        let items = line.split_whitespace();
        let items = items.collect::<Vec<&str>>();
        if items.len() > 0 {
            match items[0] {
                "v" =>  {

                            points.push(Point {
                                x: items[1].parse::<f64>().unwrap(),
                                y: items[2].parse::<f64>().unwrap(),
                                z: items[3].parse::<f64>().unwrap()});
                        },
                "f" =>  {
                            edges.push((items[1].parse::<usize>().unwrap() - 1,
                                        items[2].parse::<usize>().unwrap() - 1));
                            edges.push((items[1].parse::<usize>().unwrap() - 1,
                                        items[3].parse::<usize>().unwrap() - 1));
                            edges.push((items[2].parse::<usize>().unwrap() - 1,
                                        items[3].parse::<usize>().unwrap() - 1));
                        },
                _   =>  {}
            };
        }
    }
    Model { points: points, edges: edges }
}

fn main() {
    let cube = load_object("objs/test.obj");

    // Rendering stuff

    let opengl = OpenGL::V3_2;

    // Create an Glutin window.
    let mut window: GlutinWindow = WindowSettings::new(
            "Viewer",
            [800, 600]
        )
        .opengl(opengl)
        .exit_on_esc(true)
        .build()
        .unwrap();

    let vp = Viewport {
        x_rot: 0.0,
        y_rot: 0.0,
        z_rot: 0.0,
        x_trans: 0.0,
        y_trans: 0.0,
        z_trans: 500.0
    };

    let mut app = App {
        gl: GlGraphics::new(opengl),
        model: cube,
        vp: vp
    };

    let mut events = Events::new(EventSettings::new());

    while let Some(e) = events.next(&mut window) {
        if let Some(r) = e.render_args() {
            app.render(&r);
        }
        if let Some(button) = e.press_args() {
            app.update(button);
        }
    }
}
