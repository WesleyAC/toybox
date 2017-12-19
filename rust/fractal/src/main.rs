extern crate num_complex;
extern crate image;

use std::io::prelude::*;
use std::io;

use image::{RgbImage};
use num_complex::Complex64;

#[derive(PartialEq)]
enum SetResult {
    InSet,
    NotInSet(usize)
}

fn mandelbrot(z: Complex64, c: Complex64, n:usize) -> SetResult {
    if n == 0 {
        SetResult::InSet
    } else if z.norm() <= 2.0 {
        mandelbrot(z*z+c, c, n-1)
    } else {
        SetResult::NotInSet(n)
    }
}

fn map_pixel(x: u32, y: u32, width: u32, height: u32, f: Frame) -> Complex64 {
    Complex64::new(
        ((x as f64)*(1.0/(width as f64)))*(f.max_x-f.min_x)+f.min_x,
        ((y as f64)*(1.0/(height as f64)))*(f.max_y-f.min_y)+f.min_y)
}

#[derive(Copy,Clone)]
struct Frame {
    min_x: f64,
    max_x: f64,
    max_y: f64,
    min_y: f64
}

impl Frame {
    fn new(min_x: f64, max_x: f64, max_y: f64, min_y: f64) -> Self {
        Self { min_x: min_x, max_x: max_x, max_y: max_y, min_y: min_y }
    }
}

fn lerp(start: Frame, end: Frame, progress: f64) -> Frame {
    let lerp_amount = f64::sqrt(progress);
    Frame::new(
        start.min_x + (lerp_amount * (end.min_x - start.min_x)),
        start.max_x + (lerp_amount * (end.max_x - start.max_x)),
        start.min_y + (lerp_amount * (end.min_y - start.min_y)),
        start.max_y + (lerp_amount * (end.max_y - start.max_y)),
    )
}

fn main() {
    let width: u32 = 512;
    let height: u32 = 512;
    let frame = Frame::new(-2.0, 1.0, 1.5, -1.5);
    let mut image = RgbImage::new(width, height);
    let max_iters = 30;
    for iters in 0..max_iters {
        for y in 0..height {
            for x in 0..width {
                let result = mandelbrot(Complex64::new(0.0,0.0), map_pixel(x, y, width, height, frame), iters);
                if let SetResult::NotInSet(n) = result {
                    image.get_pixel_mut(x, y).data = [((n as f64)/(iters as f64) * 255.0) as u8,0,0];
                } else {
                    image.get_pixel_mut(x, y).data = [0,0,0];
                }
            }
        }
        image.save(format!("/tmp/out/{:05}.png", iters)).unwrap();
        print!("\r{}/{}", iters, max_iters);
        io::stdout().flush().ok().expect("Could not flush stdout");
    }
}
