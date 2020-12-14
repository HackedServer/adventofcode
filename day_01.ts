import * as fs from 'fs';


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