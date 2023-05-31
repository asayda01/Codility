function solution(N) {

    let bin_num = Number(N).toString(2);
    let arr = bin_num.split("");
    
    let bin_group = false;
    let high_zero = 0;
    let zero_counter = 0;

    for (let i of arr) {

        if (i === "1") {
            
            if (high_zero < zero_counter) {
                high_zero = zero_counter;
            };

            bin_group = true;
            zero_counter = 0;

        } else if (bin_group) {
             zero_counter += 1;
        };
    };
    return high_zero;
};