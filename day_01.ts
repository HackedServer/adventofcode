import * as fs from 'fs';
import { exit } from 'process';

const input_file = fs.readFileSync('inputs/day_01').toString('utf-8').split('\n');

let number_list: number[] = [];

for (let i = 0; i < input_file.length; i++) {

    let x = Number(input_file[i]);
    number_list.push(x);

    for (let y of number_list) {
        for (let z of number_list) {
            if (x + y + z === 2020) {
                console.log("Numbers Found: ", x, y, z);
                console.log("Product: ", x * y * z);
                //I'd exit/stop here if I knew how.
            }
        }
    }
}

/**
Learning Day 1
const input_file = fs.readFileSync('inputs/day_01').toString('utf-8').split('\n');

for (let number_entry of input_file) {
    for (let number_compare of input_file) {
        let number_1: number = +number_entry;
        let number_2: number = +number_compare;
        let added_together = number_1 + number_2;
        if (added_together == 2020) {
            let answer = number_1 * number_2;
        }
    }
}
*/