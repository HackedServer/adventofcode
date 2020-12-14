import * as fs from 'fs';

const input_file: string[] = fs.readFileSync('inputs/day_03').toString('utf-8').split('\n');
const right: number = 3, down: number = 1;
let obstacle_count: number = 0;

let cord_x: number = 1, cord_y: number = 1;

for (cord_y; cord_y < input_file.length; cord_y += down) {

    cord_x += right;

    let mountain: string[] = input_file[cord_y].split('');

    if (mountain[((cord_x % mountain.length) || mountain.length) - 1] === '#') {
        obstacle_count++;
    }

}
console.log("Total Trees:", obstacle_count)