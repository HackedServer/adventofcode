import * as fs from 'fs';

const input_file = fs.readFileSync('inputs/day_02').toString('utf-8').split('\n');

let count_total: number = 0;

for (let line of input_file) {
    let [count, letter, password]: string[] = line.replace(/:/g, '').split(' ');

    let [position_1, position_2]: number[] = count.split('-').map(Number);

    let current_password: string[] = password.split('');

    if ( 
        (current_password[position_1 - 1] === letter && current_password[position_2 - 1] !== letter)
        ||
        (current_password[position_2 - 1] !== letter && current_password[position_2 - 1] === letter)
        ) { 
            count_total++;
            console.log("We got a match");
            console.log("Count", count, "Letter", letter, "Password", password);
        }
    }
/** This is Part 1. Going to very ugly like just duplicate this until I learn functions or whatever.

for (let line of input_file) {
    let [count, letter, password]: string[] = line.replace(/:/g, '').split(' ');

    let [count_low, count_high]: number[] = count.split('-').map(Number);

    let count_actual: number = 0;

    for (let character of password.split('')) {
        if (character === letter) {
            count_actual++;
        }
    }

    if (count_actual >= count_low && count_actual <= count_high) {
        count_total++
    }
}
*/

console.log("Number of valid passwords: ", count_total);