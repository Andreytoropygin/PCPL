use std::env;
use std::io;


fn get_coef(index: usize, name: &str) -> f64{;
    match env::args().nth(index){
        Some(string) => return string.trim().parse().unwrap_or_else(|error| {
            panic!("Incorrect argument value")
        }),
        None => println!("Enter {}:", name)
    }
    loop{
        let mut input: String = String::new();
        io::stdin().read_line(&mut input);
        match input.trim().parse(){
            Ok(value) => return value,
            Err(_) => println!("Try again")
        }
    }
}


fn solve(a: f64, b: f64, c: f64) -> [Option<f64>; 4]{
    let d = b*b - 4.0*a*c;
    let mut roots: [Option<f64>; 4] = [None, None, None, None];
    if d < 0.0 {return roots;}

    let x1 = (-b - d.sqrt())/ (2.0*a);
    let x2 = (-b + d.sqrt())/ (2.0*a);

    if x1 >= 0.0 {
        roots[0] = Some(x1.sqrt());
        if x1 > 0.0 {roots[1] = Some(-x1.sqrt());}   
    }

    if x2 == x1 {return roots;}

    if x2 >= 0.0 {
        roots[2] = Some(x2.sqrt());
        if x2 > 0.0 {roots[3] = Some(-x2.sqrt());}
    }

    return roots;
}


fn main(){
    let a = get_coef(1, "a");
    let b = get_coef(2, "b");
    let c = get_coef(3, "c");

    let roots = solve(a, b, c);
    let mut count = 0;
    for i in 0..roots.len() {
        if !roots[i].is_none(){
            count += 1;
            println!("x{} = {}",count, roots[i].unwrap());
        }
    }
    if count == 0 {println!("No roots found");}
}
