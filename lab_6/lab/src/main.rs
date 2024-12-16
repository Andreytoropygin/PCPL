extern crate rand;

use serde_json::{self, Value};
use std::fs;
use rand::Rng;


macro_rules! print_vec {
    ($($arg:tt)*) => {
        for i in $($arg)*.into_iter(){ println!("{}", i); }
    };
    () => {
        println("It's not a vector!");
    }
}


fn f1(data: Value) -> Vec<String>{
    let mut vec: Vec<String> = Vec::new();
    let mut val: String;
    
    for i in 0..data.as_array().unwrap().len() {
        if data[i]["job-name"].is_null() {continue;}
        val = data[i]["job-name"].to_string().to_lowercase();
        val.retain(|c| c != '\"');
        vec.push(val);
    }
    vec.sort();
    vec.dedup();
    return vec;
}

fn f2(vec: Vec<String>) -> Vec<String> {
    let prog_jobs = vec
        .into_iter()
        .filter(|job| job.clone().starts_with("программист"))
        .collect::<Vec<String>>();
    return prog_jobs;
}

fn f3(vec: Vec<String>) -> Vec<String> {
    let python_exp = vec
        .into_iter()
        .map(|job| format!("{} с опытом Python", job))
        .collect::<Vec<String>>();
    return python_exp;
}

fn f4(vec: Vec<String>) -> Vec<String> {
    let mut salary = rand::thread_rng();
    let rand_salaries = vec
        .into_iter()
        .map(|job| format!("{}, зарплата {} руб.",
        job, salary.gen_range(100000..200000)))
        .collect::<Vec<String>>();
    return rand_salaries;
}



fn main() {
    let str_data = fs::read_to_string("data_light.json")
        .unwrap_or_else(|_error| {panic!("Can't read file")});
    let data: Value = serde_json::from_str(&str_data).expect("Can't parse json");
    print_vec!(f4(f3(f2(f1(data)))));
}

#[cfg(test)]
mod tests {
    
    use serde_json::json;

    use super::*;

    #[test]
    fn test_f1() {
        let t = json!([
            {"salary": 100, "job-name": "Я"},
            {"salary": 100, "job-name": "А"},
            {"job-name": "п"},
            {"salary": 100}
        ]);
        assert_eq!(f1(t), vec![
            "а".to_string(),
                "п".to_string(), 
                "я".to_string()
        ]);
    }

    #[test]
    fn test_f2() {
        assert_eq!(f2(vec!["программист".to_string(), "не программист".to_string()]),
                    vec!["программист".to_string()]);
    }

    #[test]
    fn test_f3() {
        assert_eq!(f3(vec!["qwerty".to_string(), "".to_string()]),
                    vec!["qwerty с опытом Python".to_string(), " с опытом Python".to_string()])
    }

}