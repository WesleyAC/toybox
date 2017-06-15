extern crate piston;
extern crate piston_window;
extern crate graphics;
extern crate glutin_window;
extern crate opengl_graphics;

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

struct Edge<'a> {
    p1: &'a Point,
    p2: &'a Point
}

struct Model<'a> {
    edges: Vec<Edge<'a>>
}

struct Viewport {
    x_rot: f64,
    y_rot: f64,
    z_rot: f64,
    x_trans: f64,
    y_trans: f64,
    z_trans: f64
}

pub struct App<'a> {
    gl: GlGraphics,
    model: Model<'a>,
    vp: Viewport
}

impl<'a> App<'a> {
    fn render(&mut self, args: &RenderArgs) {
        let ref model = self.model;
        let ref vp = self.vp;
        self.gl.draw(args.viewport(), |c, gl| {
            // Clear the screen.
            graphics::clear([0.7, 0.6, 0.75, 1.0], gl);

            for edge in &model.edges {
                let p1_t = edge.p1.translate(vp.x_trans, vp.y_trans, vp.z_trans).rotate(vp.x_rot, vp.y_rot, vp.z_rot);
                let p2_t = edge.p2.translate(vp.x_trans, vp.y_trans, vp.z_trans).rotate(vp.x_rot, vp.y_rot, vp.z_rot);

                let p1_x = p1_t.x * 256.0 / p1_t.z;
                let p1_y = p1_t.y * 256.0 / p1_t.z;
                let p2_x = p2_t.x * 256.0 / p2_t.z;
                let p2_y = p2_t.y * 256.0 / p2_t.z;
                graphics::line([0.0, 0.0, 0.0, 1.0],
                               0.5,
                               [p1_x + 400.0, p1_y + 300.0, p2_x + 400.0, p2_y + 300.0],
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
            self.vp.z_trans += 1.0;
        } else if button == Keyboard(Key::K) {
            self.vp.z_trans -= 1.0;
        }
    }
}

fn main() {
    let nodes = vec![
        Point {x: -50.0, y: 50.0, z: 50.0},
        Point {x: -50.0, y: 50.0, z: -50.0},
        Point {x: -50.0, y: -50.0, z: 50.0},
        Point {x: -50.0, y: -50.0, z: -50.0},
        Point {x: 50.0, y: 50.0, z: 50.0},
        Point {x: 50.0, y: 50.0, z: -50.0},
        Point {x: 50.0, y: -50.0, z: 50.0},
        Point {x: 50.0, y: -50.0, z: -50.0}
    ];
    let edges = vec![
        Edge { p1: &nodes[0], p2: &nodes[1] },
        Edge { p1: &nodes[2], p2: &nodes[3] },
        Edge { p1: &nodes[4], p2: &nodes[5] },
        Edge { p1: &nodes[6], p2: &nodes[7] },
        Edge { p1: &nodes[0], p2: &nodes[2] },
        Edge { p1: &nodes[4], p2: &nodes[6] },
        Edge { p1: &nodes[1], p2: &nodes[3] },
        Edge { p1: &nodes[5], p2: &nodes[7] },
        Edge { p1: &nodes[0], p2: &nodes[4] },
        Edge { p1: &nodes[2], p2: &nodes[6] },
        Edge { p1: &nodes[1], p2: &nodes[5] },
        Edge { p1: &nodes[3], p2: &nodes[7] }
    ];
    let cube = Model { edges: edges };

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
