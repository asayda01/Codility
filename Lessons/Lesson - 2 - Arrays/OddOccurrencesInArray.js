function solution(A) {
    
    let result = 0;
    A.forEach(i=>result ^= i);
    return result

};

/*

function solution(A) {
    return A.find(x => A.indexOf(x) === A.lastIndexOf(x));
};

*/