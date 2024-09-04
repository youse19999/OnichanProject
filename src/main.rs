use winit::event_loop::{ControlFlow, EventLoop};
mod render;
use render::VulkanRenderer;
fn main() {
    //ウィンドウの作成
    println!("Onichan Engine entry");
    VulkanRenderer::main();
    println!("Window has been created.")
}