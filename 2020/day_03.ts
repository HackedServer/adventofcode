import * as fs from 'fs';

const input_file: string[] = fs.readFileSync('inputs/day_03').toString('utf-8').split('\n');
const right: number = 3, down: number = 1;
let obstacle_count: number = 0;

for (let cord_y: number = 1; cord_y < input_file.length; cord_y += down) {

    if (input_file[cord_y].split('')[(((right * cord_y + 1) % input_file[cord_y].split('').length) || input_file[cord_y].split('').length) - 1] === '#') {
        obstacle_count++;
    }

}
console.log("Total Trees:", obstacle_count)