import * as fs from 'fs';

const input_file = fs.readFileSync('inputs/day_02').toString('utf-8').split('\n');

let count_total: number = 0;

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


console.log("Number of valid passwords: ", count_total);



/**
6-7 z: dqzzzjbzz
13-16 j: jjjvjmjjkjjjjjjj
*/