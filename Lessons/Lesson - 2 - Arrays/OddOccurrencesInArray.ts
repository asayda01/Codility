function OddOccurrencesInArray(A: number[]): number {
    let result:any = 0;
    A.forEach(i=>result ^= i);
    return result
}
